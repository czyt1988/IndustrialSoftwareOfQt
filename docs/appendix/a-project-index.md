# 附录 A · 工业软件项目索引

这份索引把书中提到的项目和同类代表放在一起，按领域分组。每一行给出项目、领域、界面框架、内核或主要依赖、许可证和一句判断。许可证以仓库 LICENSE 原文或项目官网为准，核对时间为 2026 年 11 月；开源项目变化很快，实际使用前请再看一眼仓库当前状态。

标注“见仓库”的项目，是指仓库没有附标准许可证文件，或自动识别结果不可靠。真正做商业决策时，请以许可证原文为准，必要时咨询法务。

## A.1 设计与制造

| 项目 | 领域 | 界面 | 内核 / 依赖 | 许可证 | 一句话判断 |
| --- | --- | --- | --- | --- | --- |
| [FreeCAD](https://github.com/FreeCAD/FreeCAD) | 参数化 CAD | Qt | OCCT、Coin3D | LGPL-2.1 | 文档对象、属性系统和工作台机制是自研 CAD 的教科书 |
| [OpenCASCADE](https://dev.opencascade.org/) | 几何内核 | 无 | 自研 | LGPL-2.1（含例外） | 开源世界唯一的重型 B-Rep 内核，前端生态的底座 |
| [Mayo](https://github.com/fougue/mayo) | CAD 查看 / 转换 | Qt | OCCT | BSD-2 | 几千行代码把“读入、显示、选中、导出”讲清楚 |
| [QCAD](https://qcad.org/) | 二维制图 | Qt | 自研 | GPL-3.0 + 例外 / 商业 | 脚本接口是“能力即 API”的典型案例 |
| [LibreCAD](https://github.com/LibreCAD/LibreCAD) | 二维制图 | Qt | 自研 | GPL-2.0 | DXF 兼容性和图纸语义的实战样本 |
| [Analysis Situs](https://gitlab.com/ssv/AnalysisSitus) | 几何算法平台 | Qt / VTK | OCCT | 见仓库 | 适合看几何算法如何被验证，不适合直接做产品 |
| [TiGL](https://github.com/DLR-SC/tigl) | 飞机几何 | Qt | OCCT、CPACS | Apache-2.0 | 行业数据标准 + 通用内核的组合示范 |
| [Topologic](https://github.com/wassimj/Topologic) | 空间拓扑 | Qt / 无 | 自研 | AGPL-3.0 | 非流形拓扑适合空间分析，闭源产品要避开 AGPL |
| [OpenNURBS](https://github.com/OpenNURBS/OpenNURBS) | 几何交换 | 无 | 自研 | GPL-2.0 | 3DM 读写库，常作为 Rhino 互通的第二内核 |
| [rhioCAD](https://github.com/mikowiec/rhioCAD) | 参数化建模 | Qt | 自研 | 见仓库 | 失败案例：内核没解决就先做界面，最终停更 |

## A.2 电子设计

| 项目 | 领域 | 界面 | 内核 / 依赖 | 许可证 | 一句话判断 |
| --- | --- | --- | --- | --- | --- |
| [KiCad](https://www.kicad.org/) | EDA | wxWidgets | 自研 | GPL-3.0 | 不用 Qt 也能做成完整 EDA，工程结构比界面框架重要 |
| [LibrePCB](https://librepcb.org/) | EDA | Qt | 自研 | GPL-3.0 | 数据模型更干净，但生态规模输给 KiCad |

## A.3 仿真与网格

| 项目 | 领域 | 界面 | 内核 / 依赖 | 许可证 | 一句话判断 |
| --- | --- | --- | --- | --- | --- |
| [ParaView](https://www.paraview.org/) | 后处理 | Qt | VTK | BSD-3 | 管线与界面分离、状态可序列化，值得每个后处理软件借鉴 |
| [Gmsh](https://gmsh.info/) | 网格 | FLTK | 自研 | GPL-2.0 或更高 | `.geo` 文本接口让自动化流程不依赖界面 |
| [FastCAE](https://github.com/DISOGitHub/FastCAE) | CAE 平台 | Qt | VTK、求解器接口 | BSD-3 | 国产 CAE 平台化集成的样本，接口稳定性是关键 |
| [OpenFOAM](https://openfoam.org/) | CFD | 无 | 自研 | GPL-3.0 | 去界面化，把求解和呈现彻底解耦 |

## A.4 科学可视化

| 项目 | 领域 | 界面 | 内核 / 依赖 | 许可证 | 一句话判断 |
| --- | --- | --- | --- | --- | --- |
| [VTK](https://vtk.org/) | 可视化库 | 无 | 自研 | BSD-3 | 科学可视化的事实标准，体量大、需要按需裁剪 |
| [ITK](https://itk.org/) | 图像处理库 | 无 | 自研 | Apache-2.0 | 分割、配准、滤波的算法基础 |
| [CTK](https://commontk.org/) | 医学影像框架 | Qt | Qt、DCMTK | Apache-2.0 | 把 Qt 与模块系统、服务注册结合起来 |
| [3D Slicer](https://www.slicer.org/) | 医学影像 | Qt / VTK | VTK、ITK、CTK | BSD 风格 | 库、框架、应用三层结构完整，医学影像的标杆 |
| [Inviwo](https://www.inviwo.org/) | 可视化原型 | Qt / OpenGL | 自研 | BSD-2 | 节点式可视化管线，适合算法原型 |
| [VisIt](https://visit.llnl.gov/) | 大规模可视化 | Qt / VTK | VTK | BSD-3 | 面向 TB 级数据与远程并行渲染 |
| [MITK](https://www.mitk.org/) | 医学影像 | Qt | VTK、ITK | BSD-3 | 医学影像工作站常用的应用框架 |
| [LabPlot](https://labplot.kde.org/) | 数据分析 | Qt / KDE | 自研 | GPL-2.0 或更高 | 实验数据分析与绘图，轻量、交互完整 |

## A.5 地理信息

| 项目 | 领域 | 界面 | 内核 / 依赖 | 许可证 | 一句话判断 |
| --- | --- | --- | --- | --- | --- |
| [QGIS](https://qgis.org/) | GIS | Qt | GDAL、PROJ、GEOS | GPL-2.0 | 坐标参考系贯穿全流程，处理框架支撑插件生态 |
| [GPXSee](https://github.com/tumic0/GPXSee) | GPS 轨迹 | Qt | 自研 | GPL-3.0 | 小项目也能把“解析、配准、渲染、导出”做完整 |
| [CloudCompare](https://www.cloudcompare.org/) | 点云处理 | Qt | 自研、CCCoreLib | GPL-2.0 | 点云查看、配准、比较的开源样本 |

## A.6 其他与通用平台

| 项目 | 领域 | 界面 | 内核 / 依赖 | 许可证 | 一句话判断 |
| --- | --- | --- | --- | --- | --- |
| [MeshLab](https://www.meshlab.net/) | 网格处理 | Qt | VCGLib | GPL-3.0 | 网格清理、修复、简化的工具集 |
| [OpenSCAD](https://openscad.org/) | 程序化建模 | Qt | CGAL、OpenCSG | GPL-2.0 | “代码即模型”的另一种 CAD 路线 |
| [SALOME](https://www.salome-platform.org/) | CAE 集成平台 | Qt | OCCT、VTK | LGPL-2.1 | 几何、网格、求解集成的老牌平台 |

## A.7 按需求快速定位

| 你要做的事 | 先看 | 再看 |
| --- | --- | --- |
| 自研参数化 CAD | FreeCAD 的 App/Gui 分层、OCCT | Mayo 的 OCCT + Qt 接入 |
| 二维图纸编辑 | QCAD 的 RDocument、LibreCAD 的 DXF 处理 | 图纸语义与打印样式 |
| 电子设计 | KiCad 的文档模型、LibrePCB 的库模型 | 元件库与格式兼容 |
| 后处理与可视化 | ParaView 的管线、VTK | VisIt 的大规模数据 |
| 医学影像 | 3D Slicer、CTK、MITK | ITK 的算法 |
| GIS | QGIS 的 CRS 与 Processing 框架 | GDAL/PROJ/GEOS |
| 点云 / 网格 | CloudCompare、MeshLab | Open3D、PCL |

索引只能帮你找到入口，不能替代源码阅读。每个项目真正值得看的部分，通常只有几个文件：文档对象、插件接口、命令栈、渲染循环。找到它们，比通读整个仓库有效。
