# 附录 C · 延伸阅读

书里的判断都建立在前人的工作上。这一页列出真正值得花时间的资料，按“先读什么”排序。

## 官方文档

工业软件的文档普遍不好读，但这几份是例外，值得从头翻一遍。

- **Qt**：[doc.qt.io](https://doc.qt.io/)。重点看 Model/View、元对象系统、`QOpenGLWidget`、插件与部署章节。Qt 的示例代码质量很高，比大多数教程可靠。
- **OpenCASCADE**：[dev.opencascade.org/doc](https://dev.opencascade.org/doc/overview/html/)。先读 “Modeling Data” 和 “Modeling Algorithms” 两章，理解 `TopoDS_Shape` 和布尔运算的用法，再去看 Visualization。
- **VTK**：[vtk.org](https://vtk.org/documentation/)。《VTK Textbook》和《VTK User's Guide》都有免费在线版，管线模型那几章是理解一切后处理软件的基础。
- **ITK**：[itk.org/ItkSoftwareGuide](https://itk.org/ItkSoftwareGuide/html/)。软件指南里的管线与流式处理章节，讲清楚了“按需计算”怎么实现。
- **ParaView**：[paraview.org/paraview-guide](https://www.paraview.org/paraview-guide/)。除了操作，重点看 Python 脚本和 Catalyst 的部分。
- **QGIS**：[docs.qgis.org](https://docs.qgis.org/)。开发者文档里的架构说明和 PyQGIS Cookbook 都值得读。
- **KiCad**：[docs.kicad.org](https://docs.kicad.org/)。除了使用手册，它的文件格式文档写得很细，是理解 EDA 数据模型的好材料。
- **FreeCAD**：[wiki.freecad.org](https://wiki.freecad.org/)。Power users hub 和 Scripting 章节比源码更容易入门。

## 书

- **《Design Patterns》**（GoF）。命令、观察者、组合、工厂，这四个模式在工业软件里出现的频率远高于其他。不必通读，把这四个看透就够。
- **《The Architecture of Open Source Applications》**（[aosabook.org](https://aosabook.org/)）。免费在线，讲的是真实项目怎么做架构决策，包括构建系统、插件、性能取舍。
- **《Real-Time Rendering》**。如果要做三维视口，这本书解释了 GPU 管线的每一个阶段，以及为什么某些写法会慢。
- **《Fundamentals of Computer Graphics》**。几何变换、投影、光照的数学基础，查漏补缺用。

## 代码

读书不如读代码，但要有选择。

- **Mayo**：一万行以内的 OCCT + Qt 完整应用，适合精读。
- **GPXSee**：一个人维护的专业工具，看它怎么控制范围、怎么组织模块。
- **LibrePCB**：现代 C++ 的领域建模，强类型和事务的用法可以直接借鉴。
- **QCAD 的脚本示例**：理解“脚本即 API”能做到什么程度。
- **Slicer 的模块示例**：看 CLI、Loadable、Scripted 三档扩展怎么落地。

## 社区

- **Qt Forum**（forum.qt.io）：问具体 API 问题，回复质量比 Stack Overflow 稳定。
- **FreeCAD Forum**：老牌社区，很多 CAD 架构的讨论在里面。
- **KiCad Forum**：EDA 领域的实战经验。
- **OSGeo**：GIS 开源项目的聚集地。
- **KDE**：LabPlot、Krita 等大型 Qt 应用的家，能学到很多工程细节。

## 怎么参与

如果你读到这里，说明你对这些项目有兴趣。参与的方式不止写代码：

- **报 bug**，并且给出可复现的最小步骤。这是最有价值的贡献。
- **补文档**，尤其是把“怎么开始”写清楚。新人的第一小时决定他会不会留下来。
- **翻译**，中文文档的缺口很大。
- **写示例**，一个能跑起来的最小例子，比十页 API 说明有用。

工业软件的开源生态比 Web 领域小得多，任何一个认真的贡献者都会被看见。
