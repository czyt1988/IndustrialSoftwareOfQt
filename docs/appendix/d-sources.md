# 附录 D · 截图与示例仓库来源

书中的图片分三类：项目界面截图、作者维护的库的界面截图、以及用 Mermaid 绘制的示意图。前两类来自公开官网或公开仓库，第三类是为本书原创，随书稿以 MIT 协议发布。

## D.1 第 1 章的项目截图

第 1 章的截图由仓库维护者从各项目官网、官方文档或公开仓库收集，原始文件保存在仓库根目录的 `screenshot/` 下，构建时由 `tools/build_images.py` 统一转成 WebP。下表列出每个项目对应的公开入口；截图的具体页面可能随项目改版而变化。

| 图号 | 项目 | 公开入口 | 许可证 |
| --- | --- | --- | --- |
| 图 1-2 | FreeCAD | <https://www.freecad.org/> | LGPL-2.1 |
| 图 1-3 | Mayo | <https://github.com/fougue/mayo> | BSD-2 |
| 图 1-4 | QCAD | <https://qcad.org/> | GPLv3 / 商业 |
| 图 1-5 | LibreCAD | <https://librecad.org/> | GPL-2.0 |
| 图 1-6 | KiCad | <https://www.kicad.org/> | GPL-3.0 |
| 图 1-7 | LibrePCB | <https://librepcb.org/> | GPL-3.0 |
| 图 1-8 | ParaView | <https://www.paraview.org/> | BSD-3 |
| 图 1-9 | Gmsh | <https://gmsh.info/> | GPL-2.0 |
| 图 1-10 | FastCAE | <https://github.com/DISOGitHub/FastCAE> | BSD-3 |
| 图 1-11 | 3D Slicer | <https://www.slicer.org/> | BSD 风格 |
| 图 1-12 | Inviwo | <https://www.inviwo.org/> | BSD-2 |
| 图 1-13 | QGIS | <https://qgis.org/> | GPL-2.0 |

截图仅用于说明界面形态和架构判断，不构成对项目功能的完整展示。界面元素、图标和商标的版权归各自项目所有。

## D.2 第 11 章的库截图

第 11 章使用的库截图，来自以下公开仓库或项目官网，构建时统一转成 WebP：

| 图号 | 文件 | 来源 |
| --- | --- | --- |
| 图 11-2 | `libraries/qim-3d.webp` | <https://github.com/czyt1988/QIm>（`docs/qim/readme_3d_example.png`） |
| 图 11-3 | `libraries/qwt-7-simpleplot.webp` | <https://github.com/czyt1988/QWT>（`docs/assets/screenshots/simpleplot.png`） |
| 图 11-4 | `libraries/qwt-waterfall3d.webp` | <https://github.com/czyt1988/QWT>（`docs/assets/screenshots-3D/waterfall3D.png`） |
| 图 11-5 | `libraries/qim-2d.webp` | <https://github.com/czyt1988/QIm>（`docs/qim/readme_2d_example.png`） |
| 图 11-6 | `charts/qcustomplot.webp` | <https://www.qcustomplot.com/> |
| 图 11-7 | `charts/jkqtplotter.webp` | <https://github.com/jkriege2/JKQtPlotter> |
| 图 11-8 | `charts/kd-chart.webp` | <https://github.com/KDAB/KDChart> |
| 图 11-9 | `libraries/saribbon.webp` | <https://github.com/czyt1988/SARibbon>（`docs/assets/screenshot/SARibbonBar-gallery.png`） |
| 图 11-10 | `libraries/qtpropertybrowser.webp` | <https://github.com/czyt1988/QtPropertyBrowser>（`doc/images/qtpropertybrowser.png`） |
| 图 11-11 | `libraries/sacolorwidgets.webp` | <https://github.com/czyt1988/SAColorWidgets>（`doc/screenshot/screenshot1.gif`） |
| 图 11-12 | `libraries/qwindowkit.webp` | <https://github.com/czyt1988/qwindowkit>（`docs/images/win11.png`） |

图 11-1 是原创 Mermaid 选型链路图，图 11-13 是 data-workbench 的工作流截图（来源见 D.3）。第 11 章未逐张列出 `charts/` 原图的原始文件名，原始素材保存在 `screenshot-visualization2D/`。

## D.3 data-workbench 截图

第 5、8、11、12 章使用的 data-workbench 截图来自其公开仓库的 `docs/assets/screenshot/` 目录：

| 文件 | 原图 | 用途 |
| --- | --- | --- |
| `workbench/table.webp` | `01.png` | 数据表格案例 |
| `workbench/chart.webp` | `03.png` | 统计绘图案例 |
| `workbench/workflow.webp` | `04.png` | 工作流案例 |
| `workbench/agent.webp` | `02.png` | Agent 对话界面 |
| `workbench/agent-chart.webp` | `agent-create-chart.png` | Agent 自动绘图 |

data-workbench 以 LGPL-3.0 发布，仓库地址为 <https://github.com/czyt1988/data-workbench>。截图中的界面、图表和图标版权归项目作者所有，本书引用仅用于技术讨论。

## D.4 Mermaid 图

第 1 章至第 12 章中的流程图、时序图、类图、状态图和时间线，均为本书原创，使用 Mermaid 11 语法编写，渲染脚本在 `docs/assets/js/mermaid-init.js`，Mermaid 运行时本地存放在 `docs/assets/js/vendor/mermaid.min.js`。这些图随书稿以 MIT 协议发布，转载时请保留出处。

## D.5 示例与文档仓库

除上述项目外，书中还引用了以下仓库和文档作为事实来源。许可证以仓库 LICENSE 原文为准，核对时间为 2026 年 11 月。

| 项目 | 用途 | 许可证 |
| --- | --- | --- |
| Qt | 框架、版本、许可证 | LGPLv3 / GPLv3 / 商业 |
| OpenCASCADE Technology | 几何内核案例 | LGPL-2.1（含例外） |
| VTK | 可视化管线案例 | BSD-3 |
| GDAL / PROJ / GEOS | QGIS 依赖 | MIT / X11 等 |
| Qt-Advanced-Docking-System | 停靠窗口案例 | LGPL-2.1 |
| spdlog | 日志库案例 | MIT |
| pybind11 | Python 绑定案例 | BSD-3 |
| Catch2 | 测试框架案例 | BSL-1.0 |
| GoogleTest | 测试框架案例 | BSD-3 |
| clang-format / clang-tidy | 格式化与静态分析 | Apache-2.0 with LLVM exception |
| MkDocs / Material for MkDocs | 文档站案例 | BSD / MIT |
| CMake / CPack | 构建与打包 | BSD-3 |
| Inno Setup | Windows 安装器 | 自有许可（见官网） |

如果图片或引文的权利人认为本书的使用方式不妥，请通过仓库 issue 联系，我们会在下一次修订时替换或移除。
