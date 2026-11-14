#!/usr/bin/env python3
"""Copy the skill's runtime files into a clean directory.

The release tree is what an install fetches from `main`: the skill's
SKILL.md, references, and scripts, plus the license and README. Tests,
fixtures, and evidence stay on `dev`. The output directory is created fresh;
an existing directory is rebuilt only when it carries this builder's marker.
"""

import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MARKER = ".skill-review-pr-release"
ALLOW = ["LICENSE", "README.md", "CHANGELOG.md", "review-pr/SKILL.md"]
SKILL_SUBTREES = ["review-pr/references", "review-pr/scripts"]


def prepare_output(out: Path) -> None:
    if out.exists():
        if not (out / MARKER).is_file():
            sys.exit(f"refusing to replace {out}: it exists and was not built by this script")
        shutil.rmtree(out)
    out.mkdir(parents=True)
    (out / MARKER).write_text("built by scripts/build-release-tree.py; safe to delete\n")


def build(out: Path) -> None:
    prepare_output(out)
    for rel in ALLOW:
        dst = out / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / rel, dst)
    for rel in SKILL_SUBTREES:
        shutil.copytree(
            REPO / rel, out / rel, ignore=shutil.ignore_patterns("__pycache__", "*.pyc")
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:  # noqa: PLR2004
        sys.exit("usage: build-release-tree.py OUTPUT_DIR")
    build(Path(sys.argv[1]).resolve())
