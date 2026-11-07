"""书稿一致性检查：front matter、字数、图号、图片链接、Mermaid、禁用词。

用法：
    python tools/check_book.py
返回码非零表示有需要修的问题；构建检查仍以 mkdocs build --strict 为准。
"""

from __future__ import annotations

import re
import sys
import pathlib
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CHAPTERS = DOCS / "chapters"
APPENDIX = DOCS / "appendix"

CJK = re.compile(r"[\u3400-\u9fff]")
LATIN = re.compile(r"[A-Za-z0-9][A-Za-z0-9+#./_-]*")
FIG = re.compile(r'<span class="fig-no">图 (\d+)-(\d+)</span>')
IMG = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
MERMAID_FENCE = re.compile(r"^```mermaid\s*$", re.MULTILINE)
BANNED = [
    "众所周知",
    "总而言之",
    "综上所述",
    "值得注意的是",
    "需要指出的是",
    "不难发现",
    "深入探讨",
    "赋能",
    "抓手",
    "颗粒度",
    "让我们",
    "接下来，我们将",
    "本章将带你",
]
BANNED_PATTERNS = [
    re.compile(r"随着.{0,12}(发展|进步|普及|演进|成熟)"),
]
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def front_matter(text: str) -> dict[str, str]:
    m = FRONT.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def check_file(path: pathlib.Path, expect_chapter: int | None) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8")
    meta = front_matter(text)
    name = path.relative_to(ROOT).as_posix()

    if expect_chapter is not None:
        if str(expect_chapter) not in meta.get("chapter", ""):
            problems.append(f"{name}: front matter chapter 不是 {expect_chapter}")
        if not meta.get("part"):
            problems.append(f"{name}: front matter 缺 part")
        title = meta.get("title", "")
        first = text.split("\n", 1)[1] if "\n" in text else ""
        if f"# {title}" not in text:
            problems.append(f"{name}: 一级标题与 title 不一致")

    cjk = len(CJK.findall(text))
    latin = len(LATIN.findall(text))
    figs = [(int(a), int(b)) for a, b in FIG.findall(text)]
    if expect_chapter is not None and figs:
        expected = 1
        for chapter, number in figs:
            if chapter != expect_chapter:
                problems.append(f"{name}: 图号 {chapter}-{number} 不属于本章")
            if number != expected:
                problems.append(f"{name}: 图号不连续，期望 {expected}，实际 {number}")
            expected += 1

    for target in IMG.findall(text):
        if target.startswith(("http://", "https://")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            problems.append(f"{name}: 图片不存在 {target}")

    for phrase in BANNED:
        if phrase in text:
            problems.append(f"{name}: 出现禁用表达“{phrase}”")
    for pattern in BANNED_PATTERNS:
        match = pattern.search(text)
        if match:
            problems.append(f"{name}: 出现禁用句式“{match.group(0)}”")

    in_fence = False
    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith(("!!!", "<", "|", ">")):
            continue
        bare = re.sub(r"`[^`]*`", "", line)
        if '"' in bare and CJK.search(bare):
            problems.append(f"{name}:{line_no}: 中文行里出现 ASCII 引号")

    return problems, cjk, latin, len(figs), len(MERMAID_FENCE.findall(text))


def main() -> int:
    all_problems: list[str] = []
    rows = []
    for path in sorted(CHAPTERS.glob("*.md")):
        m = re.match(r"(\d+)-", path.name)
        chapter = int(m.group(1)) if m else None
        result = check_file(path, chapter)
        if result is None:
            continue
        problems, cjk, latin, figs, mermaids = result
        rows.append((path.name, cjk, latin, figs, mermaids))
        all_problems.extend(problems)
    for path in sorted(APPENDIX.glob("*.md")):
        result = check_file(path, None)
        if result is None:
            continue
        problems, cjk, latin, figs, mermaids = result
        rows.append((path.name, cjk, latin, figs, mermaids))
        all_problems.extend(problems)

    print(f"{'文件':34} {'中文字符':>6} {'英文词':>6} {'图':>3} {'Mermaid':>7}")
    for name, cjk, latin, figs, mermaids in rows:
        print(f"{name:34} {cjk:>6} {latin:>6} {figs:>3} {mermaids:>7}")
    print(f"\n合计中文字符 {sum(r[1] for r in rows):,}，英文词 {sum(r[2] for r in rows):,}")

    if all_problems:
        print("\n问题：")
        for problem in all_problems:
            print("  -", problem)
        return 1
    print("\n未发现结构性问题。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
