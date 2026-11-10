#!/usr/bin/env python3
"""Check exported cuts before upload: file name, frame size, codec, audio, file size.

    python3 scripts/qc.py exports/HPT085

Checks every .mp4 and .mov under the given folders (or the given files), whether it came
from assemble.py or straight out of Premiere/CapCut. Exits non-zero if any cut fails, so
nothing gets uploaded with a wrong name or a 1080x1080 export where a 9:16 belonged.

Standard library only. Needs ffprobe on PATH.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

FRAMES = {(1080, 1920): "9x16", (1080, 1350): "4x5", (1080, 1080): "1x1"}
MAX_BYTES = 4 * 1024**3  # Meta's upload limit for a video ad file
EXTENSIONS = {".mp4", ".mov"}


def check_name(stem):
    """Return (failures, warnings) for a file name. The naming sheet's current form is

    <CreativeID>_VID_<Concept>_<Var><Self><TEEP>-<Zone>_<Product>_<ContentType>_<Avatar>_<Offer>_<Category>_<Strategist>_<Editor>_<MMDDYY>

    The first four fields are hard requirements: the Winner Crawl matches live Meta ads to
    their Notion brief on Creative ID, VID and variant, so a cut that gets them wrong can never
    be tagged a winner. Older briefs carry a short variant token (`1B`) and fewer fields;
    those pass with a warning rather than failing.
    """
    parts = stem.split("_")
    if len(parts) < 4:
        return ["name is not the '_'-separated name from the brief"], []
    if any(not p.strip() for p in parts):
        return ["name has an empty field (two '_' in a row)"], []

    fails = []
    cid, fmt, _concept, token = parts[:4]
    if not re.fullmatch(r"[A-Z]+\d+", cid):
        fails.append(f"creative ID '{cid}' should look like HPT085")
    if fmt != "VID":
        fails.append(f"format field is '{fmt}', expected 'VID'")
    if not re.fullmatch(r"\d+[A-Za-z]{1,2}(-Z\d+)?", token):
        fails.append(f"variant token '{token}' should look like 1Ab-Z3 (variation, self, TEEP, zone)")

    date = parts[-1]
    if re.fullmatch(r"\d{5}", date):
        fails.append(f"date '{date}' lost its leading zero (should be '0{date}')")
    elif re.fullmatch(r"\d{6}", date) and not re.fullmatch(
            r"(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{2}", date):
        fails.append(f"date '{date}' is not MMDDYY")

    warns = []
    current = len(parts) == 12 and "-Z" in token and re.fullmatch(r"\d{6}", date)
    if not fails and not current:
        warns.append("not the naming sheet's current 12-field form; fine for an older brief, "
                     "otherwise re-copy the name from the brief")
    return fails, warns


def probe(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)


def check(path, max_seconds):
    """Return (summary, failures, warnings) for one file."""
    fails, warns = check_name(path.stem)

    info = probe(path)
    if info is None:
        return "unreadable", fails + ["ffprobe cannot read the file"], warns
    streams = info.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    if video is None:
        return "no video", fails + ["no video stream"], warns

    w, h = video.get("width"), video.get("height")
    rotation = next((abs(int(d.get("rotation", 0))) for d in video.get("side_data_list", [])
                     if "rotation" in d), 0)
    if rotation in (90, 270):
        w, h = h, w
    frame = FRAMES.get((w, h))
    if frame is None:
        fails.append(f"frame is {w}x{h}; export 1080x1920, 1080x1350 or 1080x1080")

    codec = video.get("codec_name")
    if codec != "h264":
        fails.append(f"video codec is {codec}; export H.264")
    if video.get("pix_fmt") != "yuv420p":
        fails.append(f"pixel format is {video.get('pix_fmt')}; export 8-bit 4:2:0 (yuv420p)")

    try:
        num, den = (int(x) for x in video.get("avg_frame_rate", "0/1").split("/"))
        fps = num / den if den else 0
    except ValueError:
        fps = 0
    if fps and not 23 <= fps <= 60:
        warns.append(f"frame rate is {fps:.2f} fps; 24-60 is safe")

    if not any(s.get("codec_type") == "audio" for s in streams):
        fails.append("no audio track")

    size = path.stat().st_size
    if size > MAX_BYTES:
        fails.append(f"file is {size / 1024**3:.1f} GB; Meta's limit is 4 GB")

    duration = float(info.get("format", {}).get("duration") or 0)
    if max_seconds and duration > max_seconds:
        fails.append(f"runs {duration:.1f}s, over the {max_seconds:g}s limit")

    summary = f"{frame or f'{w}x{h}'}  {duration:5.1f}s  {size / 1024**2:6.1f} MB"
    return summary, fails, warns


def main():
    ap = argparse.ArgumentParser(description="Check exported cuts before upload.")
    ap.add_argument("paths", nargs="+", type=Path, help="folders and/or video files")
    ap.add_argument("--max-seconds", type=float, help="fail cuts longer than this")
    args = ap.parse_args()

    if shutil.which("ffprobe") is None:
        sys.exit("error: ffprobe not found on PATH")

    files = []
    for p in args.paths:
        if p.is_dir():
            files += sorted(f for f in p.rglob("*")
                            if f.suffix.lower() in EXTENSIONS and not f.name.endswith(".partial.mp4"))
        elif p.is_file():
            files.append(p)
        else:
            sys.exit(f"error: {p} does not exist")
    if not files:
        sys.exit("error: no .mp4 or .mov files found")

    failed = 0
    for f in files:
        summary, fails, warns = check(f, args.max_seconds)
        failed += bool(fails)
        print(f"{'FAIL' if fails else 'PASS'}  {summary}  {f}")
        for msg in fails:
            print(f"        x {msg}")
        for msg in warns:
            print(f"        ! {msg}")

    print(f"\n{len(files) - failed} passed, {failed} failed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
