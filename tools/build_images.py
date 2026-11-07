"""把 screenshot/ 下的原始截图转换成站点使用的 WebP。

原图保留在仓库根部，作为可追溯的素材来源；docs/assets/images/ 下的文件
全部由本脚本生成，不要手工替换（否则下次构建会被覆盖）。

用法：
    python tools/build_images.py
"""

from __future__ import annotations

import pathlib
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "images"

# 源文件 -> (目标分组, 目标文件名)
ASSETS: dict[str, tuple[str, str]] = {
    # CAD
    "freecad.jpg": ("cad", "freecad.webp"),
    "freecad2.png": ("cad", "freecad-2.webp"),
    "mayo.gif": ("cad", "mayo.webp"),
    "mayo2.png": ("cad", "mayo-2.webp"),
    "qcad3_windows.png": ("cad", "qcad.webp"),
    "librecad_screenshot_2.1.3.png": ("cad", "librecad.webp"),
    "rhiocad.jpg": ("cad", "rhiocad.webp"),
    "AnalysisSitus.gif": ("cad", "analysis-situs.webp"),
    "tiglviewer.jpg": ("cad", "tigl.webp"),
    "Topologic.png": ("cad", "topologic.webp"),
    # EDA
    "kicad.png": ("eda", "kicad.webp"),
    "kicad2.png": ("eda", "kicad-2.webp"),
    "LibrePCB.png": ("eda", "librepcb.webp"),
    # CAE
    "paraView.png": ("cae", "paraview.webp"),
    "paraView2.png": ("cae", "paraview-2.webp"),
    "fastcae.png": ("cae", "fastcae.webp"),
    "gmsh.png": ("cae", "gmsh.webp"),
    "gmsh1.png": ("cae", "gmsh-2.webp"),
    # 可视化
    "ctk.png": ("viz", "ctk.webp"),
    "3DSlicerSegmentEditor.png": ("viz", "slicer.webp"),
    "LabPlot2.png": ("viz", "labplot.webp"),
    "Inviwo.png": ("viz", "inviwo.webp"),
    "Vislt.png": ("viz", "visit.webp"),
    # GIS
    "qgis.png": ("gis", "qgis.webp"),
    "qgis2.png": ("gis", "qgis-2.webp"),
    "GPXSee.png": ("gis", "gpxsee.webp"),
    # 2D 图表
    "qcustomplot.png": ("charts", "qcustomplot.webp"),
    "qcustomplot2.png": ("charts", "qcustomplot-2.webp"),
    "qwt.png": ("charts", "qwt.webp"),
    "kdchart.png": ("charts", "kd-chart.webp"),
    "kdchart2.png": ("charts", "kd-chart-2.webp"),
    "JKQtPlotter.png": ("charts", "jkqtplotter.webp"),
    "JKQtPlotter2.png": ("charts", "jkqtplotter-2.webp"),
    # 第 11 章：作者维护的库与 data-workbench
    "saribbon-gallery.png": ("libraries", "saribbon.webp"),
    "qwt-simpleplot.png": ("libraries", "qwt-7-simpleplot.webp"),
    "qwt-waterfall3d.png": ("libraries", "qwt-waterfall3d.webp"),
    "qim-2d.png": ("libraries", "qim-2d.webp"),
    "qim-3d.png": ("libraries", "qim-3d.webp"),
    "qtpropertybrowser.png": ("libraries", "qtpropertybrowser.webp"),
    "screenshot1.gif": ("libraries", "sacolorwidgets.webp"),
    "color-palette-grid.png": ("libraries", "sacolor-palette.webp"),
    "qwindowkit.png": ("libraries", "qwindowkit.webp"),
    "table.png": ("workbench", "table.webp"),
    "chart.png": ("workbench", "chart.webp"),
    "workflow.png": ("workbench", "workflow.webp"),
    "agent.png": ("workbench", "agent.webp"),
    "agent-chart.png": ("workbench", "agent-chart.webp"),
}

MAX_WIDTH = 1680


def save(src: pathlib.Path, dst: pathlib.Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        animated = getattr(im, "is_animated", False)
        if not animated and im.width > MAX_WIDTH:
            height = round(im.height * MAX_WIDTH / im.width)
            im = im.resize((MAX_WIDTH, height), Image.LANCZOS)
        elif animated and im.width > MAX_WIDTH:
            height = round(im.height * MAX_WIDTH / im.width)
            im = im.resize((MAX_WIDTH, height), Image.LANCZOS)

        params: dict[str, object] = {"quality": 88 if animated else 84, "method": 6}
        if animated:
            params.update(
                {
                    "save_all": True,
                    "duration": im.info.get("duration", 120),
                    "loop": 0,
                    "format": "WEBP",
                }
            )
        im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB").save(dst, **params)


def main() -> int:
    sources: dict[str, pathlib.Path] = {}
    for root in (ROOT / "screenshot", ROOT / "screenshot-visualization2D"):
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if path.name in sources:
                print(f"源文件名重复：{path} 与 {sources[path.name]}", file=sys.stderr)
                return 1
            sources[path.name] = path

    missing = [name for name in ASSETS if name not in sources]
    if missing:
        print("缺少源文件：" + ", ".join(missing), file=sys.stderr)
        return 1

    before = after = 0
    for name, (group, target) in ASSETS.items():
        src = sources[name]
        dst = OUT / group / target
        save(src, dst)
        before += src.stat().st_size
        after += dst.stat().st_size
        print(f"{src.name:32} -> {group}/{target:26} {dst.stat().st_size / 1024:8.0f} KB")

    print(f"\n合计 {before / 1024 / 1024:.1f} MB -> {after / 1024 / 1024:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
