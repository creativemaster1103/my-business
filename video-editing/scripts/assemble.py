#!/usr/bin/env python3
"""Build ad cuts from a cut list: one row per deliverable, clips joined in column order.

    python3 scripts/assemble.py jobs/HPT085.csv --media media/HPT085 --out exports/HPT085

The cut list is a CSV whose first column is `filename`, pasted verbatim from the brief's
File naming table, and whose remaining columns are that cut's clips, in order:

    filename,hook,body,cta
    HPT085_VID_..._1Bd-Z3_..._082726,hook1.mp4,body.mp4,cta.mp4

Every clip is scaled to the target frame and conformed to 30 fps and 48 kHz stereo, then
all of them are joined in one encode, so footage from different sources (AI VO renders,
Higgsfield generations, phone clips) mixes without pre-processing. A clip with no audio
gets silence, so a silent b-roll hook does not break the join.

Standard library only. Needs ffmpeg and ffprobe on PATH.
"""

import argparse
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path

FORMATS = {
    "9x16": (1080, 1920),  # Reels, Stories
    "4x5": (1080, 1350),   # Feed
    "1x1": (1080, 1080),   # Feed, right column
}
FPS = 30


def probe(path):
    """Return (duration of the video stream in seconds, whether the file has audio)."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.exit(f"error: ffprobe cannot read {path}: {result.stderr.strip()}")
    info = json.loads(result.stdout)
    streams = info.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    if video is None:
        sys.exit(f"error: no video stream in {path}")
    duration = video.get("duration") or info.get("format", {}).get("duration")
    if duration in (None, "N/A"):
        sys.exit(f"error: cannot read the duration of {path} (still images are not supported)")
    has_audio = any(s.get("codec_type") == "audio" for s in streams)
    return float(duration), has_audio


def ffmpeg_command(clips, size, fit, dest):
    w, h = size
    if fit == "crop":
        frame = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}"
    else:
        frame = f"scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2"

    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    graph = []
    for i, (path, duration, has_audio) in enumerate(clips):
        cmd += ["-i", str(path)]
        graph.append(
            f"[{i}:v:0]{frame},setsar=1,fps={FPS},format=yuv420p,"
            f"trim=duration={duration:.3f},setpts=PTS-STARTPTS[v{i}]"
        )
        # Pad or cut each clip's audio to its own picture length, so VO never drifts
        # across a join and a silent clip still contributes a track to the concat.
        source = (
            f"[{i}:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,apad"
            if has_audio else "anullsrc=r=48000:cl=stereo"
        )
        graph.append(f"{source},atrim=duration={duration:.3f},asetpts=PTS-STARTPTS[a{i}]")
    pairs = "".join(f"[v{i}][a{i}]" for i in range(len(clips)))
    graph.append(f"{pairs}concat=n={len(clips)}:v=1:a=1[v][a]")

    cmd += [
        "-filter_complex", ";".join(graph),
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-profile:v", "high",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(dest),
    ]
    return cmd


def read_cutlist(path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows or not rows[0] or rows[0][0].strip().lower() != "filename":
        sys.exit(f"error: {path} must start with a header row whose first column is 'filename'")
    cuts = []
    for n, row in enumerate(rows[1:], start=2):
        if not row or not row[0].strip():
            continue
        name = row[0].strip()
        if name.lower().endswith(".mp4"):
            name = name[:-4]
        if "/" in name or "\\" in name:
            sys.exit(f"error: {path} line {n}: filename contains a slash: {name}")
        clips = [c.strip() for c in row[1:] if c.strip()]
        if not clips:
            sys.exit(f"error: {path} line {n}: no clips listed for {name}")
        cuts.append((name, clips))
    if not cuts:
        sys.exit(f"error: {path} has no cuts")
    names = [name for name, _ in cuts]
    dupes = sorted({x for x in names if names.count(x) > 1})
    if dupes:
        sys.exit(f"error: {path} lists the same filename more than once: {', '.join(dupes)}")
    return cuts


def main():
    ap = argparse.ArgumentParser(
        description="Build ad cuts (hook + body + CTA, or any clip sequence) from a CSV cut list.",
    )
    ap.add_argument("cutlist", type=Path, help="CSV: filename, then one column per clip in order")
    ap.add_argument("--media", type=Path,
                    help="folder the clip paths are relative to (default: the cut list's folder)")
    ap.add_argument("--out", type=Path, default=Path("exports"),
                    help="output folder; each format gets a subfolder (default: exports)")
    ap.add_argument("--format", default="9x16",
                    help=f"comma-separated, from: {', '.join(FORMATS)} (default: 9x16)")
    ap.add_argument("--fit", choices=["crop", "pad"], default="crop",
                    help="crop fills the frame (default); pad letterboxes so nothing is cut off")
    ap.add_argument("--force", action="store_true", help="re-render cuts that already exist")
    ap.add_argument("--dry-run", action="store_true", help="print the ffmpeg commands only")
    args = ap.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if shutil.which(tool) is None:
            sys.exit(f"error: {tool} not found on PATH")

    formats = [f.strip() for f in args.format.split(",") if f.strip()]
    unknown = [f for f in formats if f not in FORMATS]
    if unknown or not formats:
        sys.exit(f"error: unknown format {', '.join(unknown) or '(none)'}; use {', '.join(FORMATS)}")

    cuts = read_cutlist(args.cutlist)
    media = args.media or args.cutlist.parent

    # Check every clip before rendering anything, so a typo fails in a second, not
    # after ten minutes of encodes.
    missing = sorted({c for _, clips in cuts for c in clips if not (media / c).is_file()})
    if missing:
        sys.exit(f"error: missing clips in {media}:\n  " + "\n  ".join(missing))
    probed = {c: probe(media / c) for c in sorted({c for _, clips in cuts for c in clips})}

    jobs = [(fmt, name, clips) for fmt in formats for name, clips in cuts]
    built = skipped = 0
    for i, (fmt, name, clips) in enumerate(jobs, start=1):
        dest = args.out / fmt / f"{name}.mp4"
        length = sum(probed[c][0] for c in clips)
        label = f"[{i}/{len(jobs)}] {fmt}/{name}.mp4 ({length:.1f}s)"
        if dest.exists() and not args.force:
            print(f"{label} exists, skipped (use --force to re-render)")
            skipped += 1
            continue
        cmd = ffmpeg_command(
            [(media / c, *probed[c]) for c in clips], FORMATS[fmt], args.fit, dest,
        )
        if args.dry_run:
            print(label)
            print("  " + subprocess.list2cmdline(cmd))
            continue
        print(label, flush=True)
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_name(dest.stem + ".partial.mp4")
        cmd[-1] = str(tmp)
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            tmp.unlink(missing_ok=True)
            sys.exit(f"error: ffmpeg failed on {name}:\n{result.stderr.strip()}")
        tmp.replace(dest)
        built += 1

    if not args.dry_run:
        print(f"done: {built} built, {skipped} skipped, in {args.out}")


if __name__ == "__main__":
    main()
