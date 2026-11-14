# review-pr

An agent skill that reviews a GitHub pull request from any directory through a tested runner adapter (Claude Code or Codex), with pinned evidence, a fixed four-lens contract, and no posted comments or applied fixes.

See [`review-pr/SKILL.md`](review-pr/SKILL.md) for how it works.

## Installation

```bash
# GitHub CLI v2.90+
gh skill install briandconnelly/skill-review-pr --agent claude-code --scope user

# Vercel Labs skills CLI
npx skills add briandconnelly/skill-review-pr
```

## Development

`main` holds only the files an install needs and is published automatically from `dev`.
Tests, fixtures, and evidence live on [`dev`](https://github.com/briandconnelly/skill-review-pr/tree/dev); open pull requests against it.
Run the checks with `prek run --all-files`.

## License

MIT
