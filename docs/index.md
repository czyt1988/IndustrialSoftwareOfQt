---
hide:
  - toc
  - footer
---

<div class="book-cover" markdown>
<p class="cover-eyebrow">电子书 · 第一版</p>
<h1 class="cover-title">Qt 工业软件工程实践</h1>
<p class="cover-subtitle">架构、交付与 AI 协作</p>
<div class="cover-rule"></div>
<p class="cover-meta"><strong>尘中远</strong> 著 <span>2026 · 第一版</span> <span>持续修订</span></p>
</div>

[从前言开始](preface.md){ .book-cta }

## 这本书讲什么

工业软件的界面看起来都差不多：一个主窗口，左侧是模型树或图层树，中间是视口，右侧是属性面板，下面是一条日志。真正把这些软件区分开的，是窗口背后那条数据链——几何模型怎么表达，编辑操作怎么撤销，计算结果怎么和视图对齐，插件怎么在不重新编译主程序的前提下接进来。这条链断了，界面再漂亮也只是个昂贵的查看器。

Qt 在这条链里承担的是“人机接口”那一段。它提供窗口、输入、模型视图、元对象和插件加载，但不提供几何内核、网格算法和求解器。本书讨论的全部工程问题，都发生在这段边界上：怎么把内核接进来，怎么把界面切开，怎么让几十个人的团队在同一个代码库里改代码而不互相踩踏，怎么把构建、测试、文档和发布串成一条可靠的流水线。

书里的案例分两类。一类是别人已经做成的开源项目：FreeCAD、ParaView、QGIS、KiCad、3D Slicer、Gmsh、LibreCAD、Mayo，以及它们背后的 OCCT、VTK、GDAL、ITK。这些项目解决过的问题，大多数团队也会遇到，只是规模小一点。另一类是作者自己维护的库和平台：SARibbon、QWT 分支、QIm、DAWidgets、QtPropertyBrowser、SAColorWidgets、qwindowkit 和 data-workbench。它们在书里不是“推荐清单”，而是被拆开看的工程样本：哪一块补了什么缺口，代价是什么，什么情况下不该用。

## 适合谁读

**正在做工业客户端的 Qt 工程师。** 你可能已经能写窗口和控件，但卡在“功能一多就乱”的阶段。本书第二、三部分讲的就是从单窗口程序到可维护产品的这段路。

**要为团队做技术选型的人。** 第 2、3 章讨论框架、版本与许可证，第 10、11 章讨论交付和第三方库。这些内容可以直接拿去开会，但书里不替你做决定，只把决策所需的约束摆出来。

**刚开始接触工业软件的学生和转岗工程师。** 第 1 章用半小时建立行业地图，后面的章节可以按兴趣跳读。每章末尾给的项目和资料，足够顺藤摸瓜。

## 怎么读

全书按“先看别人怎么做，再定自己的工程基础，最后处理架构、性能和交付”的顺序组织。第一次读建议按顺序，因为后面的章节会引用前面的判断。已经做过大型项目的读者可以从第 5 章开始，把第 1、2 章当作背景。

书中的代码大多是可编译的最小片段，少数长示例标注了“结构示意”。Mermaid 图解释机制，截图说明界面形态，两者都不能替代源码阅读；每章给出的仓库地址，才是最终的验证入口。

## 全书结构

<div class="book-toc" markdown>

**第一部 · 应用与选型背景**

1. [用 Qt 写成的工业软件版图](chapters/01-industrial-map.md)
2. [桌面框架选型：Qt、Electron、Python 与 Web](chapters/02-framework-selection.md)

**第二部 · 工程基础**

3. [Qt 版本与许可证](chapters/03-versions-licenses.md)
4. [开发环境与技术栈](chapters/04-dev-environment.md)
5. [大型项目工程结构管理](chapters/05-project-structure.md)

**第三部 · 架构与工程经验**

6. [架构：模块化与插件化](chapters/06-architecture.md)
7. [文档、质量测试及自动化](chapters/07-docs-quality.md)
8. [性能工程](chapters/08-performance.md)
9. [稳定性与可维护性](chapters/09-stability.md)
10. [交付与部署](chapters/10-delivery.md)

**第四部 · 参考**

11. [常见第三方库推荐](chapters/11-libraries.md)

**第五部 · AI**

12. [AI 驱动开发](chapters/12-ai-development.md)

**附录**

- [A 工业软件项目索引](appendix/a-project-index.md)
- [B 工具与资源清单](appendix/b-tools-resources.md)
- [C 术语表](appendix/c-glossary.md)
- [D 截图与示例仓库来源](appendix/d-sources.md)

</div>

## 关于本书

书稿用 Markdown 写成，MkDocs 构建，发布在 GitHub Pages 上，源码在[仓库](https://github.com/czyt1988/IndustrialSoftwareOfQt)公开。文字与作者自己的代码示例以 MIT 协议发布；文中提到的开源项目，版权与许可证归各自作者所有，引用仅用于技术讨论。

书里的截图来自项目官网、公开仓库和作者本机的实际运行界面，来源逐张列在附录 D。软件会更新，界面会变，章节里的版本号和许可信息以文中标注的核对时间为准。发现错误、过期链接或更好的案例，欢迎在仓库提 issue。
