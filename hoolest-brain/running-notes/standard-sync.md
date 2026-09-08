# Standard sync — the update ledger

## Where this brain stands

- **Factory remote:** https://github.com/real-simple-labs/parker-brain
- **Posture:** `follow`
- **Pinned release:** v15 (commit `b55c441` — v14 and v15 are the same commit; v15 is the highest tag)
- **Migrations applied through:** v14 (newest migration note in the factory; no v15 migration exists)
- **Last compared:** 2026-09-08 against v15

## Sync deviation — read this first

This brain is **self-managed**, not Parker Desktop-synced. The Parker Desktop app is not
installable in the environment this build ran in, so the runner's Desktop path did not apply.

- The brand repo `parker-brain/hoolest-hoolest-performance-technologies` was provisioned by
  `setup_parker_brain` but could **not** be pushed to from the build session: GitHub access was
  scoped to `creativemaster1103/my-business` and both the token clone and repo-attach were denied.
- The brain therefore lives at `hoolest-brain/` inside `creativemaster1103/my-business`, on branch
  `claude/parker-mcp-brands-l3s0t9`, and is version-controlled by that repo's own git.
- `parker-system/` is a real submodule of `my-business`, pinned to v15 — the mount behaves exactly
  as the runner intends.
- **To move this brain to its own repo:** copy `hoolest-brain/` into a clone of
  `parker-brain/hoolest-hoolest-performance-technologies`, re-add the submodule there, and push.
  `/save-brain` and the git-guard hook assume Desktop sync — read them before relying on them here.

## Offer history

No offers yet — the first `/update-brain` run fills this in.
