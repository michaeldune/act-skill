#!/usr/bin/env python3
"""Search emotion knowledge-base files (.docx/.md/.txt) with simple deterministic scoring."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Iterable

def read_docx(path: Path) -> list[str]:
    try:
        from docx import Document
        from docx.oxml.ns import qn
        from docx.table import Table
        from docx.text.paragraph import Paragraph
    except ImportError as exc:
        raise RuntimeError(
            "Reading .docx files requires python-docx. Install it with: pip install python-docx"
        ) from exc
    doc = Document(path)
    lines: list[str] = []
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            text = Paragraph(child, doc).text.strip()
            if text:
                lines.append(text)
        elif child.tag == qn("w:tbl"):
            table = Table(child, doc)
            for row in table.rows:
                text = " | ".join(cell.text.strip() for cell in row.cells if cell.text.strip())
                if text:
                    lines.append(text)
    return lines


def read_lines(path: Path) -> list[str]:
    if path.suffix.lower() == ".docx":
        return read_docx(path)
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def chunks(lines: Iterable[str]) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    heading = "Untitled entry"
    buffer: list[str] = []
    for line in lines:
        markdown_heading = re.match(r"^##\s+(.+)$", line)
        normalized_heading = markdown_heading.group(1).strip() if markdown_heading else line
        # English headings run longer than the original Chinese ones, so the limit is 80 characters.
        # The \u escapes still recognise headings in a Chinese knowledge base (chapter numbers and
        # the "emotion:" prefix), so both languages can be searched.
        is_heading = len(normalized_heading) <= 80 and (
            re.match(
                r"^(\u7b2c[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]+\u7ae0"
                r"|\d+[.\u3001]|[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]+[\u3001.])",
                line,
            )
            or line.startswith("\u60c5\u7eea\uff1a")
            or line.lower().startswith("emotion:")
            or bool(markdown_heading)
        )
        if is_heading:
            if buffer:
                result.append((heading, "\n".join(buffer)))
            heading, buffer = normalized_heading, [line]
        else:
            buffer.append(line)
        if sum(len(x) for x in buffer) >= 900:
            result.append((heading, "\n".join(buffer)))
            buffer = []
    if buffer:
        result.append((heading, "\n".join(buffer)))
    return result


def terms(query: str) -> list[str]:
    raw = re.findall(r"[\u4e00-\u9fff]{1,8}|[A-Za-z0-9_-]+", query.lower())
    # Very short English words ("a", "of", "to") match almost every entry and drown the ranking.
    raw = [t for t in raw if not (t.isascii() and len(t) < 3)]
    return list(dict.fromkeys(raw))


def score(heading: str, text: str, query_terms: list[str]) -> int:
    low = text.lower()
    heading_low = heading.lower()
    total = 0
    for term in query_terms:
        count = low.count(term)
        if count:
            total += 6 + min(count, 5) * 2 + min(len(term), 4)
        if term in heading_low:
            total += 24
    matched = sum(1 for t in query_terms if t in low)
    if query_terms and matched == len(query_terms):
        total += 12
    return total


def discover_library(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit
    env_path = os.environ.get("ACT_SKILL_KB")
    candidates = []
    if env_path:
        candidates.append(Path(env_path))
    script_path = Path(__file__).resolve()
    candidates.extend([
        script_path.parents[3] / "knowledge-base" / "emotion",
    ])
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        "Emotion knowledge base not found. Pass its path with --library, or set the ACT_SKILL_KB environment variable."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--library", type=Path)
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    library = discover_library(args.library)
    if library.is_file():
        files = [library]
    else:
        discovered = sorted(
            p for p in library.rglob("*") if p.suffix.lower() in {".docx", ".md", ".txt"}
        )
        # A Markdown mirror and Word source often share the same stem. Search one
        # representation only so the same knowledge entry does not crowd out other results.
        preferred: dict[tuple[Path, str], Path] = {}
        rank = {".md": 3, ".docx": 2, ".txt": 1}
        for path in discovered:
            key = (path.parent, path.stem)
            current = preferred.get(key)
            if current is None or rank[path.suffix.lower()] > rank[current.suffix.lower()]:
                preferred[key] = path
        files = sorted(preferred.values())
    query_terms = terms(args.query)
    results = []
    for path in files:
        for heading, text in chunks(read_lines(path)):
            value = score(heading, text, query_terms)
            if value > 0:
                results.append({
                    "score": value,
                    "source": str(path),
                    "section": heading,
                    "text": text[:1200],
                })
    results.sort(key=lambda item: (-item["score"], item["source"], item["section"]))
    results = results[: max(0, args.top_k)]
    if args.json:
        print(json.dumps({"query": args.query, "results": results}, ensure_ascii=False, indent=2))
    else:
        for index, item in enumerate(results, 1):
            print(f"[{index}] score={item['score']} {item['section']}\n{item['source']}\n{item['text']}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
