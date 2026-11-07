"""把正文中的 ASCII 双引号换成中文引号。

只处理代码块之外的散文部分：跳过围栏代码、行内代码、HTML 标签，
以及 Material 的 admonition 标题语法（`!!! note "标题"` 必须保留 ASCII 引号）。
"""

from __future__ import annotations

import pathlib
import re

TAG = re.compile(r"<[^>]+>")
CODE = re.compile(r"`[^`]*`")


def convert_line(line: str) -> str:
    if line.lstrip().startswith(("!!!", "???", "```")):
        return line

    # 先切出 HTML 标签与行内代码，这些片段原样保留
    parts = re.split(r"(<[^>]+>|`[^`]*`)", line)
    open_quote = True
    for i, part in enumerate(parts):
        if part.startswith("<") or part.startswith("`"):
            continue
        if '"' not in part:
            continue
        out = []
        for ch in part:
            if ch == '"':
                out.append("“" if open_quote else "”")
                open_quote = not open_quote
            else:
                out.append(ch)
        parts[i] = "".join(out)
    return "".join(parts)


def main() -> None:
    changed = 0
    for path in sorted(pathlib.Path("docs").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        in_code = False
        out_lines = []
        for line in lines:
            if line.strip().startswith("```"):
                in_code = not in_code
                out_lines.append(line)
                continue
            if in_code:
                out_lines.append(line)
                continue
            new = convert_line(line)
            if new != line:
                changed += 1
            out_lines.append(new)
        new_text = "\n".join(out_lines)
        if text.endswith("\n"):
            new_text += "\n"
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(f"updated {path}")
    print(f"{changed} lines changed")


if __name__ == "__main__":
    main()
