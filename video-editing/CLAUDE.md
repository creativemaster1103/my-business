# Working in video-editing/

Ad creative editing for Hoolest. Read `README.md` and `specs/meta-export.md` in this folder
first. Paths below are relative to `video-editing/`.

- **Never commit media.** Video, audio and NLE caches stay on the shared drive; `.gitignore`
  enforces this. Don't weaken it to get a file in.
- **File names come from the brief, verbatim.** The Video Brief's *File naming* table is
  produced by the naming sheet. Copy those strings into the cut list; never rebuild a name
  from its parts, even when one looks wrong. If it is wrong, the brief's inputs need fixing
  upstream (`.claude/skills/competitor-ad-swipe/references/naming-generator.md`). The Winner
  Crawl matches live ads back to briefs by these names, so a hand-built one can make a winning
  cut invisible.
- **Four hooks per brief.** One concept means four cuts: same body and CTA, different opening.
  A cut list for a brief has four rows unless the brief says otherwise.
- **Run `scripts/qc.py` on every export before calling it done**, and report its output as-is.
- Scripts are standard-library Python plus ffmpeg. Keep them that way; editors run them on
  their own machines without installing anything.
