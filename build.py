#!/usr/bin/env python3
"""
Build distributables for every skill in skills/.

For each skills/<name>/ containing a SKILL.md, this produces:

  dist/<name>.skill              zip archive — installs in Claude
  dist/<Name>-single-file.md     self-contained markdown — paste into
                                 ChatGPT / Gemini / anything else

The single-file build inlines everything under references/ as lettered
appendices and rewrites the pointers in the body, so nothing needs to be
fetched at runtime. Run it after editing any source file.

    python3 build.py
"""

import os
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"

SINGLE_FILE_HEADER = """# {title}
{tagline}

**How to use this file.** Paste the whole thing into a new chat with ChatGPT,
Claude, Gemini, or any capable AI, then say what you want it to do.

It works better as project instructions or a Custom GPT than as a pasted
message, because it stays loaded. If your tool supports saved instructions or
a project knowledge file, put it there.

The appendices at the bottom are referenced throughout. They're part of this
file — the AI already has them, nothing needs to be fetched.

---

"""

# Separates the human-facing onboarding from the instructions for the AI, so a
# model reading the whole pasted file doesn't mistake the first section for its
# own brief.
ONBOARDING_DIVIDER = """
> **Everything above this line is for the person running this — a plain-language
> orientation, written for someone who has never used an AI skill before.
> Everything below is the working instruction set. If you're an AI reading this
> file: the section above tells you what the coach has been told to expect, which
> is useful context. Your actual instructions start here.**

---

"""


def title_case(slug: str) -> str:
    return " ".join(w.capitalize() for w in slug.split("-"))


def file_stem(slug: str) -> str:
    """Capitalised but hyphenated, so filenames stay shell- and URL-friendly."""
    return "-".join(w.capitalize() for w in slug.split("-"))


def read_frontmatter(text: str):
    """Return (frontmatter_dict, body_without_frontmatter)."""
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        return {}, text
    meta = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
    return meta, text[match.end():]


def build_skill_archive(skill_dir: Path) -> Path:
    """Zip the skill folder into dist/<name>.skill."""
    out = DIST / f"{skill_dir.name}.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_dir() or path.name == ".DS_Store":
                continue
            zf.write(path, path.relative_to(skill_dir.parent))
    return out


def build_single_file(skill_dir: Path) -> Path:
    """Inline references/ into one self-contained markdown file."""
    meta, body = read_frontmatter((skill_dir / "SKILL.md").read_text())

    refs_dir = skill_dir / "references"
    refs = sorted(refs_dir.glob("*.md")) if refs_dir.is_dir() else []

    # Order appendices so the ones the body points at first come first.
    order = {name: body.find(name) for name in (r.name for r in refs)}
    refs.sort(key=lambda r: (order.get(r.name, 10**9), r.name))

    letters = {r.name: chr(ord("A") + i) for i, r in enumerate(refs)}

    def repoint(text: str) -> str:
        for name, letter in letters.items():
            for pattern in (f"`references/{name}`", f"references/{name}", f"`{name}`"):
                text = text.replace(pattern, f"**Appendix {letter}**")
        return text

    # First heading of a reference file becomes its appendix title.
    def ref_title(text: str, fallback: str) -> str:
        m = re.search(r"^#\s+(.*)$", text, flags=re.M)
        return m.group(1).strip() if m else title_case(fallback)

    title = title_case(skill_dir.name).upper()
    tagline = ""
    m = re.search(r"^\*\*(.+?)\*\*\s*$", body, flags=re.M)
    if m:
        tagline = f"### {m.group(1)} — single-file edition"

    # A coach-facing orientation, if one exists, leads the file. It lives outside
    # the skill folder so it never burns context in the Claude-installed version,
    # where the coach reads it in the repo instead of in the prompt.
    onboarding = ROOT / "docs" / f"{skill_dir.name}-start-here.md"
    if onboarding.is_file():
        parts = [onboarding.read_text(), ONBOARDING_DIVIDER]
    else:
        parts = [SINGLE_FILE_HEADER.format(title=title, tagline=tagline)]

    parts.append(repoint(body))

    for ref in refs:
        raw = ref.read_text()
        heading = ref_title(raw, ref.stem)
        content = repoint(re.sub(r"^#\s+.*\n", "", raw, count=1))
        parts.append(
            f"\n\n---\n\n# APPENDIX {letters[ref.name]} · {heading}\n{content}"
        )

    out = DIST / f"{file_stem(skill_dir.name)}-single-file.md"
    out.write_text("".join(parts))
    return out


def main() -> None:
    DIST.mkdir(exist_ok=True)
    skill_dirs = sorted(d for d in SKILLS.iterdir() if (d / "SKILL.md").is_file())

    if not skill_dirs:
        print(f"no skills found in {SKILLS}")
        return

    for skill_dir in skill_dirs:
        archive = build_skill_archive(skill_dir)
        single = build_single_file(skill_dir)
        print(f"{skill_dir.name}")
        print(f"  → {archive.relative_to(ROOT)}  ({archive.stat().st_size:,} bytes)")
        print(f"  → {single.relative_to(ROOT)}  ({single.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
