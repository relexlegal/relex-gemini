#!/usr/bin/env python3
"""Mirror plugin/skills and plugin/references to the extension root.

Gemini CLI loads an extension from the directory that holds
gemini-extension.json (the repo root) and discovers Agent Skills only under
<extension root>/skills/<name>/SKILL.md. The canonical skill pack lives in
plugin/ (shared with the other Relex plugin repos), so this script copies it
to the root. Run it after editing plugin/skills or plugin/references.

  python3 scripts/sync_gemini_extension.py          # write the mirror
  python3 scripts/sync_gemini_extension.py --check  # exit 1 if it is stale
"""
from __future__ import annotations

import filecmp
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAIRS = (("plugin/skills", "skills"), ("plugin/references", "references"))


def _files(base: pathlib.Path) -> set[str]:
    return {str(p.relative_to(base)) for p in base.rglob("*") if p.is_file() and p.name != ".DS_Store"}


def stale() -> list[str]:
    out: list[str] = []
    for src_rel, dst_rel in PAIRS:
        src, dst = ROOT / src_rel, ROOT / dst_rel
        if not dst.exists():
            out.append(f"{dst_rel}/ missing")
            continue
        a, b = _files(src), _files(dst)
        out += [f"{dst_rel}/{f} missing" for f in sorted(a - b)]
        out += [f"{dst_rel}/{f} extra" for f in sorted(b - a)]
        out += [f"{dst_rel}/{f} differs" for f in sorted(a & b)
                if not filecmp.cmp(src / f, dst / f, shallow=False)]
    return out


def main() -> int:
    if "--check" in sys.argv:
        problems = stale()
        for p in problems:
            print(p)
        print("OK — extension mirror is current" if not problems else "STALE — run scripts/sync_gemini_extension.py")
        return 1 if problems else 0
    for src_rel, dst_rel in PAIRS:
        dst = ROOT / dst_rel
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(ROOT / src_rel, dst, ignore=shutil.ignore_patterns(".DS_Store"))
    print("synced", ", ".join(d for _, d in PAIRS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
