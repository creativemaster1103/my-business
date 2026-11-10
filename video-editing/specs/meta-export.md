# Meta export spec

Export every cut to this spec. `scripts/qc.py` checks the parts marked ✓.

## Frame

| Format | Size | Use |
|---|---|---|
| **9:16** | 1080 × 1920 ✓ | Reels, Stories (default; build this first) |
| 4:5 | 1080 × 1350 ✓ | Feed |
| 1:1 | 1080 × 1080 ✓ | Feed, right column |

Edit in 9:16. Build 4:5 or 1:1 only when the brief or the campaign asks for them. Reframe
those by hand when on-screen text would be cropped. `assemble.py --fit pad` is the fallback.

## Encode

| | |
|---|---|
| Container | `.mp4` |
| Video | H.264 ✓, High profile, 8-bit 4:2:0 / yuv420p ✓ |
| Frame rate | 30 fps (24–60 accepted) |
| Quality | CRF 18, or 15–20 Mbps VBR for 1080×1920 |
| Audio | AAC ✓ (required), 48 kHz stereo, 192 kbps |
| Size | Under 4 GB ✓ |
| Fast start | On (`-movflags +faststart` / "Optimize for web") |

Don't upload ProRes, HEVC or 10-bit masters. Meta re-encodes everything anyway, and those
formats are where color shifts and failed uploads come from.

## Safe zones (9:16)

Meta's interface sits on top of the video. Keep captions, the product, the logo and the CTA
out of these areas:

| Placement | Top | Bottom | Sides |
|---|---|---|---|
| Reels | 14% (~270 px) | 35% (~670 px) | 6% (~65 px) |
| Stories | 14% (~250 px) | 14% (~250 px) | — |

A cut that is safe for Reels is also safe for Stories. These are Meta's figures at the time of
writing; when in doubt, check the current Meta Ads Guide.

## Naming

The file name is the one in the brief's **File naming** table, copied exactly, plus `.mp4`:

```
HPT085_VID_Test Zap_1Bd-Z3_VeRelief Prime_AI VO_Multi_NA_New_Mark_JM_082726.mp4
```

`1Bd-Z3` is four fields: variation `1`, self-targeting `B`, TEEP stage `d`, valence zone `Z3`.
The date is `MMDDYY` with its leading zero.
