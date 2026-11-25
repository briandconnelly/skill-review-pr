# Changelog

## [Unreleased]

## [0.1.0] - 2026-11-25

### Added

- The reviewer now reads the issues a pull request closes and reports requirements the change implements wrongly or only in part.
  `REVIEW_PR_MAX_ISSUES` caps how many are fetched.
- `CONTRIBUTING.md` and `CODING_STANDARDS.md` at the repository root, in `.github/`, or in `docs/` are now reviewer policy, read from the base branch.

### Changed

- Moved from [briandconnelly/skills](https://github.com/briandconnelly/skills) into its own repository, with history.
  Install from this repository's `main` branch, which carries only the runtime files.
- A pull request with an empty diff now fails at checkout instead of starting a review.

### Fixed

- A review that could not read the pinned diff no longer claims lens coverage: its summary now opens with `Lenses not checked: pinned diff unavailable.` instead of the lenses-checked line, and the result validator rejects either line when it contradicts the `DIFF-UNAVAILABLE` sentinel.
- A runner that trapped the watchdog's TERM on timeout and exited 0 no longer reports a completed review: the envelope `exit` is forced to a nonzero value, so the relay treats the run as did not complete.
- A failed `git diff` while listing a pull request's changed policy files now fails checkout instead of reporting an empty list, which silently dropped the notice that the PR modifies reviewer policy.
- Checkout no longer aborts on Linux when the base branch's skill index is large but within its documented limits: skill metadata now passes to `jq` through a file instead of a single command-line argument, which Linux caps at 128 KiB.

[Unreleased]: https://github.com/briandconnelly/skill-review-pr/compare/v0.1.0...dev
[0.1.0]: https://github.com/briandconnelly/skill-review-pr/releases/tag/v0.1.0
