#!/usr/bin/env python3
"""Collect review context from a LaTeX paper project.

This script is read-only unless --out is supplied.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from collections import Counter


SECTION_RE = re.compile(r"\\(part|chapter|section|subsection|subsubsection)\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", re.S)
INPUT_RE = re.compile(r"\\(?:input|include)\{([^{}]+)\}")
CITE_RE = re.compile(r"\\cite[a-zA-Z*]*?(?:\[[^\]]*\]){0,2}\{([^{}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
CAPTION_RE = re.compile(r"\\caption(?:\[[^\]]*\])?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", re.S)


def read_text(path: pathlib.Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "gbk", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace")


def strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        cut = None
        escaped = False
        for i, ch in enumerate(line):
            if ch == "\\":
                escaped = not escaped
                continue
            if ch == "%" and not escaped:
                cut = i
                break
            escaped = False
        out.append(line[:cut] if cut is not None else line)
    return "\n".join(out)


def normalize_tex_path(base: pathlib.Path, name: str) -> pathlib.Path:
    candidate = (base / name).expanduser()
    if candidate.suffix == "":
        candidate = candidate.with_suffix(".tex")
    return candidate.resolve()


def find_main(path: pathlib.Path) -> pathlib.Path:
    path = path.resolve()
    if path.is_file():
        return path
    preferred = ["main.tex", "paper.tex", "manuscript.tex", "submission.tex"]
    for name in preferred:
        candidate = path / name
        if candidate.exists():
            return candidate.resolve()
    tex_files = sorted(path.rglob("*.tex"))
    for tex in tex_files:
        if "\\documentclass" in read_text(tex):
            return tex.resolve()
    if tex_files:
        return max(tex_files, key=lambda p: p.stat().st_size).resolve()
    raise FileNotFoundError(f"No .tex files found under {path}")


def collect_sources(main: pathlib.Path) -> list[pathlib.Path]:
    seen: set[pathlib.Path] = set()
    ordered: list[pathlib.Path] = []

    def visit(path: pathlib.Path) -> None:
        path = path.resolve()
        if path in seen or not path.exists():
            return
        seen.add(path)
        ordered.append(path)
        text = strip_comments(read_text(path))
        for match in INPUT_RE.finditer(text):
            child = normalize_tex_path(path.parent, match.group(1))
            visit(child)

    visit(main)
    return ordered


def clean_inline(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", "", text)
    text = text.replace("{", "").replace("}", "")
    return text.strip()


def extract_environment(text: str, name: str) -> str:
    m = re.search(rf"\\begin\{{{name}\}}(.*?)\\end\{{{name}\}}", text, re.S)
    return clean_inline(m.group(1)) if m else ""


def extract_title(text: str) -> str:
    m = re.search(r"\\title(?:\[[^\]]*\])?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", text, re.S)
    return clean_inline(m.group(1)) if m else ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect LaTeX context for manuscript review.")
    parser.add_argument("path", help="LaTeX source directory or main .tex file")
    parser.add_argument("--main", help="Override main .tex file")
    parser.add_argument("--max-chars", type=int, default=80000, help="Maximum source text chars to include")
    parser.add_argument("--out", help="Optional output markdown path")
    args = parser.parse_args()

    input_path = pathlib.Path(args.main) if args.main else pathlib.Path(args.path)
    main_tex = find_main(input_path)
    sources = collect_sources(main_tex)
    source_texts = []
    for src in sources:
        source_texts.append(f"% ===== {src} =====\n" + strip_comments(read_text(src)))
    combined = "\n\n".join(source_texts)

    sections = [(kind, clean_inline(title)) for kind, title in SECTION_RE.findall(combined)]
    citations = []
    for group in CITE_RE.findall(combined):
        citations.extend([x.strip() for x in group.split(",") if x.strip()])
    labels = LABEL_RE.findall(combined)
    captions = [clean_inline(x) for x in CAPTION_RE.findall(combined)]

    title = extract_title(combined)
    abstract = extract_environment(combined, "abstract")
    body_excerpt = clean_inline(combined[: args.max_chars])

    lines = []
    lines.append("# LaTeX Manuscript Context")
    lines.append("")
    lines.append(f"Main file: `{main_tex}`")
    lines.append("")
    lines.append("## Included Files")
    for src in sources:
        lines.append(f"- `{src}`")
    lines.append("")
    lines.append("## Title")
    lines.append(title or "(not found)")
    lines.append("")
    lines.append("## Abstract")
    lines.append(abstract or "(not found)")
    lines.append("")
    lines.append("## Section Outline")
    for kind, heading in sections:
        lines.append(f"- {kind}: {heading}")
    if not sections:
        lines.append("(no section commands found)")
    lines.append("")
    lines.append("## Figures and Tables")
    for caption in captions[:40]:
        lines.append(f"- {caption}")
    if not captions:
        lines.append("(no captions found)")
    lines.append("")
    lines.append("## Labels")
    for label, count in Counter(labels).most_common(80):
        lines.append(f"- {label} ({count})")
    if not labels:
        lines.append("(no labels found)")
    lines.append("")
    lines.append("## Citation Keys")
    for key, count in Counter(citations).most_common(120):
        lines.append(f"- {key} ({count})")
    if not citations:
        lines.append("(no citations found)")
    lines.append("")
    lines.append("## Source Excerpt")
    lines.append(body_excerpt)
    lines.append("")

    output = "\n".join(lines)
    if args.out:
        pathlib.Path(args.out).write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

