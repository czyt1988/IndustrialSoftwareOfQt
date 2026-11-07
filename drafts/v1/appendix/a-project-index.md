# 附录 A · 项目索引

下表是全书涉及的项目，按领域分组。“界面”一列写的是图形界面所用的框架，“无”表示该项目不提供图形界面。“许可”以仓库的 LICENSE 文件为准；GitHub 自动识别经常给出 `NOASSERTION`，这类情况标注为“见仓库”。

!!! note "数据说明"
    项目状态与许可是在 2026 年 11 月核对的。开源项目变化很快，使用前请以仓库当前状态为准。标注为“双许可”的项目同时提供 GPL 版本与商业授权，闭源使用需要购买商业许可。

## 设计与制造

| 项目 | 领域 | 界面 | 许可 | 仓库 |
| --- | --- | --- | --- | --- |
| FreeCAD | 参数化建模 | Qt | LGPL-2.1 | [GitHub](https://github.com/FreeCAD/FreeCAD) |
| OpenCASCADE | 几何内核 | 无 | LGPL-2.1 | [opencascade.org](https://dev.opencascade.org/) |
| Mayo | 查看/转换 | Qt | BSD-2 | [GitHub](https://github.com/fougue/mayo) |
| QCAD | 二维制图 | Qt | 双许可 | [qcad.org](https://qcad.org/) |
| LibreCAD | 二维制图 | Qt | GPL-2.0 | [GitHub](https://github.com/LibreCAD/LibreCAD) |
| Analysis Situs | 算法 SDK | Qt/VTK | 见仓库 | [GitLab](https://gitlab.com/ssv/AnalysisSitus) |
| TiGL | 飞机几何 | Qt | Apache-2.0 | [GitHub](https://github.com/DLR-SC/tigl) |
| Klampt | 机器人 | Qt/OpenGL | BSD-3 | [GitHub](https://github.com/krishauser/Klampt) |
| OpenNURBS | 几何交换 | 无 | 见仓库 | [GitHub](https://github.com/OpenNURBS/OpenNURBS) |
| rhioCAD | 参数化建模 | Qt | 见仓库 | [GitHub](https://github.com/mikowiec/rhioCAD) |
| Topologic | 空间拓扑 | 无 | AGPL-3.0 | [GitHub](https://github.com/wassimj/Topologic) |

## 电子设计

| 项目 | 领域 | 界面 | 许可 | 仓库 |
| --- | --- | --- | --- | --- |
| KiCad | PCB/原理图 | wxWidgets | GPL-3.0 | [kicad.org](https://www.kicad.org/) |
| LibrePCB | PCB/原理图 | Qt | GPL-3.0 | [GitHub](https://github.com/LibrePCB/LibrePCB) |

## 仿真与网格

| 项目 | 领域 | 界面 | 许可 | 仓库 |
| --- | --- | --- | --- | --- |
| ParaView | 后处理 | Qt/VTK | BSD-3 | [paraview.org](https://www.paraview.org/) |
| FastCAE | CAE 平台 | Qt/VTK | BSD-3 | [GitHub](https://github.com/DISOGitHub/FastCAE) |
| Gmsh | 网格 | FLTK | GPL-2.0 | [gmsh.info](https://gmsh.info/) |
| OpenFOAM | CFD | 无 | GPL-3.0 | [openfoam.org](https://openfoam.org/) |

## 科学可视化

| 项目 | 领域 | 界面 | 许可 | 仓库 |
| --- | --- | --- | --- | --- |
| VTK | 可视化库 | 无 | BSD-3 | [vtk.org](https://vtk.org/) |
| ITK | 图像库 | 无 | Apache-2.0 | [itk.org](https://itk.org/) |
| CTK | 影像框架 | Qt | Apache-2.0 | [commontk.org](https://commontk.org/) |
| 3D Slicer | 医学影像 | Qt/VTK | BSD | [slicer.org](https://www.slicer.org/) |
| Inviwo | 原型工具 | Qt/OpenGL | BSD-2 | [inviwo.org](https://www.inviwo.org/) |
| VisIt | 大规模可视化 | Qt/VTK | BSD-3 | [visit.llnl.gov](https://visit.llnl.gov/) |
| LabPlot | 数据分析 | Qt/KDE | GPL-2.0 | [labplot.kde.org](https://labplot.kde.org/) |

## 图表与地理信息

| 项目 | 领域 | 界面 | 许可 | 仓库 |
| --- | --- | --- | --- | --- |
| QCustomPlot | 图表 | Qt | 双许可 | [qcustomplot.com](https://www.qcustomplot.com/) |
| QWT | 技术图表 | Qt | LGPL-2.1 | [sourceforge](https://qwt.sourceforge.io/) |
| KD Chart | 报表图表 | Qt | MIT | [GitHub](https://github.com/KDAB/KDChart) |
| JKQtPlotter | 科学绘图 | Qt | LGPL-2.1 | [GitHub](https://github.com/jkriege2/JKQtPlotter) |
| QGIS | 地理信息 | Qt | GPL-2.0 | [qgis.org](https://qgis.org/) |
| GPXSee | GPS 轨迹 | Qt | GPL-3.0 | [GitHub](https://github.com/tumic0/GPXSee) |

## 按许可证快速筛选

| 你的情况 | 可以看 | 需要避开 |
| --- | --- | --- |
| 闭源商业产品 | BSD、Apache-2.0、LGPL（动态链接） | GPL、AGPL |
| 开源且允许衍生开源 | GPL-3.0 系列 | 无 |
| 内部工具，不对外分发 | 几乎都可以 | AGPL 的网络条款 |
| 要静态链接 | BSD、Apache-2.0 | LGPL（除非有例外或商业许可） |
