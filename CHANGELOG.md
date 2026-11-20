# Changelog

## [Unreleased]

### Added

- The reviewer now reads the issues a pull request closes and reports requirements the change implements wrongly or only in part.
  `REVIEW_PR_MAX_ISSUES` caps how many are fetched.
- `CONTRIBUTING.md` and `CODING_STANDARDS.md` at the repository root, in `.github/`, or in `docs/` are now reviewer policy, read from the base branch.

### Changed

- A pull request with an empty diff now fails at checkout instead of starting a review.

### Changed

- Moved from [briandconnelly/skills](https://github.com/briandconnelly/skills) into its own repository, with history.
  Install from this repository's `main` branch, which carries only the runtime files.
