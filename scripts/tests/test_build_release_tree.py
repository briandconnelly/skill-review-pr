from __future__ import annotations

import importlib.util
import os
import re
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "build-release-tree.py"
_spec = importlib.util.spec_from_file_location("build_release_tree", SCRIPT)
assert _spec is not None
assert _spec.loader is not None
builder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(builder)

SKILL = builder.REPO / "review-pr"


def _files(root: Path) -> set[str]:
    return {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}


@pytest.fixture
def tree(tmp_path: Path) -> Path:
    out = tmp_path / "release"
    builder.build(out)
    return out


def test_ships_every_runtime_file(tree: Path) -> None:
    shipped = _files(tree)
    for sub in ("references", "scripts"):
        for rel in _files(SKILL / sub):
            if "__pycache__" not in rel:
                assert f"review-pr/{sub}/{rel}" in shipped
    assert "review-pr/SKILL.md" in shipped


def test_ships_no_tests(tree: Path) -> None:
    assert not (tree / "review-pr" / "tests").exists()
    assert not (tree / "scripts").exists()


def test_scripts_keep_their_mode(tree: Path) -> None:
    executable = 0
    for src in (SKILL / "scripts").rglob("*"):
        if src.is_file():
            shipped = tree / "review-pr" / src.relative_to(SKILL)
            assert shipped.stat().st_mode == src.stat().st_mode, shipped
            executable += os.access(src, os.X_OK)
    assert executable > 0


def test_shipped_relative_links_resolve(tree: Path) -> None:
    link = re.compile(r"\]\((?!https?://|#|mailto:)([^)#\s]+)")
    for md in tree.rglob("*.md"):
        for target in link.findall(md.read_text(encoding="utf-8")):
            assert (md.parent / target).exists(), f"{md.relative_to(tree)} -> {target}"


def test_refuses_to_replace_unmarked_directory(tmp_path: Path) -> None:
    out = tmp_path / "precious"
    out.mkdir()
    with pytest.raises(SystemExit):
        builder.build(out)


def test_rebuilds_its_own_output(tree: Path) -> None:
    (tree / "stale").write_text("x")
    builder.build(tree)
    assert not (tree / "stale").exists()


def test_ships_dependabot_config_but_no_workflows(tree: Path) -> None:
    # Dependabot reads its config only from the default branch, `main`; the
    # publish job's GITHUB_TOKEN cannot push `.github/workflows/`.
    shipped = _files(tree)
    assert ".github/dependabot.yml" in shipped
    assert not any(rel.startswith(".github/workflows/") for rel in shipped)
