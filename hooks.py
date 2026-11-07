"""构建期钩子：给章节页补上「部 / 章 / 字数 / 阅读时间」这些书籍元素。

页面在自己的 front matter 里声明：

    ---
    chapter: 3
    part: 第二部 · 领域
    ---

钩子会把章号与所属部插到一级标题之前，把字数与阅读时长插到标题之后。
这样正文仍然是干净的 Markdown，排版信息集中在一处。
"""

from __future__ import annotations

import re

CJK = re.compile(r"[\u3400-\u9fff]")
LATIN = re.compile(r"[A-Za-z0-9][A-Za-z0-9+#./_-]*")
H1 = re.compile(r"^#\s+.+$", re.MULTILINE)

# 中文阅读速度取 400 字/分钟，英文取 200 词/分钟
CJK_PER_MINUTE = 400
LATIN_PER_MINUTE = 200


def _count(text: str) -> tuple[int, int]:
    return len(CJK.findall(text)), len(LATIN.findall(text))


def on_page_markdown(markdown: str, page, config, files):  # noqa: ANN001
    chapter = page.meta.get("chapter")
    if chapter is None:
        return markdown

    match = H1.search(markdown)
    if not match:
        return markdown

    part = page.meta.get("part", "").strip()
    cjk, latin = _count(markdown)
    minutes = max(1, round(cjk / CJK_PER_MINUTE + latin / LATIN_PER_MINUTE))
    words = f"{cjk + latin:,}"

    kicker = [
        '<p class="chapter-kicker">',
        f'<span class="chapter-part">{part}</span>' if part else "",
        '<span class="chapter-rule" aria-hidden="true"></span>',
        f'<span class="chapter-no">第 {chapter} 章</span>',
        "</p>",
    ]
    meta = (
        f'<p class="chapter-meta">{words} 字 · 约 {minutes} 分钟</p>'
    )

    markdown = (
        markdown[: match.start()]
        + "".join(kicker)
        + "\n\n"
        + match.group(0)
        + "\n\n"
        + meta
        + "\n"
        + markdown[match.end() :]
    )
    return markdown
