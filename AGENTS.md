- When writing markdown, use one sentence per line for easy diffs
- Commit messages follow conventional commits
- Branch from `dev` and open pull requests against `dev` (`gh pr create --base dev`).
  `main` is the runtime tree that `.github/workflows/publish-runtime.yml` builds from `dev` with `scripts/build-release-tree.py`; never commit to it or target it.
  GitHub closes issues from `Fixes #N` only on merges into the default branch, which is `main`, so close an issue by hand once its fix merges into `dev`
- A link in a shipped file (`review-pr/SKILL.md`, `review-pr/references/`) must not point into `review-pr/tests/`, which `main` does not carry; link to `https://github.com/briandconnelly/skill-review-pr/blob/dev/...` instead
- `CHANGELOG.md` records every user-visible change under `## [Unreleased]`, in the pull request that makes it; dev-only changes (tests, scripts, evidence) stay out of it
- Run every check with `prek run --all-files`
