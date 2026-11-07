---
title: 几何与设计：从内核到制图
chapter: 3
part: 第二部 · 领域
---

# 几何与设计：从内核到制图

!!! abstract "本章要点"
    CAD 的成本几乎全部压在三件事上：几何内核、参数化重算、交互精度。内核决定了你能不能做布尔和倒角，重算图决定了改动能不能传播，交互精度决定了用户信不信你的数字。开源世界里，前三件事都有成熟答案，第四件事（行业数据与工艺知识）没有。

<figure markdown>
  ![FreeCAD 主界面](../assets/images/cad/freecad.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 3-1</span>FreeCAD 的主界面。左侧模型树、右侧三维视口、下方 Python 控制台，是典型的“文档 + 视图 + 脚本”三件套布局。</figcaption>
</figure>

## 3.1 内核为什么是护城河

做一个能画立方体的 CAD，一个周末够了。做一个能对两个复杂曲面做布尔运算、再倒角、再抽壳、最后导出 STEP 别人还能打开的 CAD，需要十年。

差距全在内核里。

**表示方式决定了能力上限。** 网格（mesh）只能表达近似形状，布尔运算会产生自交和碎片；边界表示（B-Rep）用面、边、顶点的拓扑关系描述实体，能精确表达圆柱、NURBS 曲面，也能做真正的求交。工业设计要的是后者。

**布尔运算的鲁棒性是玄学。** 两个面共面、两条边几乎重合、一个顶点落在面上，这些退化情况在数学上都有定义，在浮点数里全是坑。商业内核花了几十年积累这些特殊情况，开源内核的差距主要在这里，而不在算法论文。

**格式交换是第二道墙。** STEP、IGES、JT、Parasolid、ACIS，每一种背后都是一套语义。能把别人的模型读进来、不改形状、再原样写出去，本身就是产品能力。

所以当有人问“我自己写一个 CAD 内核行不行”，答案通常是：写一个能用的要五年，写一个能商用的要十五年，而且每年都在修上一年的 bug。

## 3.2 OpenCASCADE：开源世界唯一的重型内核

OCCT（Open CASCADE Technology）是这个领域里唯一一个全尺寸的开源内核。它不年轻，代码风格停留在 2000 年代，文档也不友好，但它是唯一能支撑工业级 CAD 的开源选择。

它的模块划分值得了解，因为它决定了一个 CAD 的代码结构：

| 模块 | 职责 | 代表类 |
| --- | --- | --- |
| Foundation | 基础类型、数学、异常 | `Standard_Real`、`gp_Pnt`、`gp_Trsf` |
| Modeling Data | 几何与拓扑数据 | `Geom_BSplineSurface`、`TopoDS_Shape` |
| Modeling Algorithms | 求交、布尔、倒角、抽壳 | `BRepAlgoAPI_Fuse`、`BRepFilletAPI_MakeFillet` |
| Data Exchange | STEP/IGES/STL 读写 | `STEPControl_Reader`、`IGESControl_Writer` |
| Visualization | OpenGL 视口 | `AIS_InteractiveContext`、`V3d_Viewer` |
| Mesh | 三角化 | `BRepMesh_IncrementalMesh` |

理解 `TopoDS_Shape` 是理解 OCCT 的关键。它是一个句柄，内部指向共享的拓扑结构，所以复制一个 shape 很便宜，修改它则需要用 `BRep_Builder` 或算法类产生新 shape。这种“不可变 + 共享”的设计让大装配的内存占用可控，但也让初学者经常困惑于“为什么我改了这个 shape，那个 shape 也变了”。

OCCT 的许可是 LGPL-2.1 加例外条款，允许以动态链接方式用于闭源软件。这对商业产品是友好的，但仍然要求你遵守 LGPL 的替换义务。第 10 章会细说。

## 3.3 FreeCAD：文档-对象模型的教科书

FreeCAD 是理解“参数化 CAD 怎么组织代码”的最好样本。它有一百多万行代码，但你只需要看三个地方。

**第一，`App` 与 `Gui` 的分离。** `App` 里有 `Document`、`DocumentObject`、`Property`，完全不知道界面的存在；`Gui` 里有 `ViewProvider`、`Command`、`View3DInventor`，负责显示和交互。这种分离让 FreeCAD 可以无界面运行脚本，也让 Python 绑定变得自然。

**第二，属性系统。** `App::Property` 不只是数据容器，它同时承担了序列化、撤销、属性编辑器生成、依赖追踪四件事。新增一种属性类型，编辑器会自动出现对应的控件，保存和撤销也自动工作。这是整个项目最值得抄的设计。

**第三，重算图。** 每个 `DocumentObject` 有 `execute()`，输入是它的属性，输出也是它的属性。修改一个参数会把依赖它的对象标记为“需要重算”，`Document::recompute()` 按拓扑序执行。这就是参数化的本质：不是“记录操作历史”，而是“记录一张可以重新求值的图”。

```cpp
// 结构示意，非 FreeCAD 源码
class Feature : public App::DocumentObject {
public:
    App::PropertyLength Radius;
    App::PropertyLink   Base;

    App::DocumentObjectExecReturn *execute() override {
        auto shape = Base->Shape.getValue();
        Shape.setValue(makeCylinder(shape, Radius.getValue()));
        return App::DocumentObject::StdReturn;
    }
};
```

工作台（workbench）是 FreeCAD 的插件单位。它本质上是一个 Python 包，注册一组命令和界面，按需加载。Part、PartDesign、Sketcher、Draft、FEM 都是工作台。这种“插件即工作台”的设计让社区可以独立扩展，代价是启动时加载的东西越来越多，各个工作台之间的概念也不完全统一。

<figure markdown>
  ![FreeCAD 草图与约束](../assets/images/cad/freecad-2.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 3-2</span>FreeCAD 的 Sketcher：几何元素加上约束，求解器负责把约束网络解成一个确定的形状。约束求解是参数化 CAD 的第二个内核。</figcaption>
</figure>

FreeCAD 的弱点同样值得记住：渲染基于 Coin3D（OpenInventor 的继承者），在处理超大装配时不如现代 OpenGL 管线；工作台之间的 API 稳定性一般；Python 绑定让启动变慢。这些都是“历史选择 + 社区规模”的结果，不是能力问题。

## 3.4 Mayo：最小可用的 OCCT + Qt 参考

如果你只想学“怎么把 OCCT 接进 Qt”，不要从 FreeCAD 开始，从 [Mayo](https://github.com/fougue/mayo) 开始。

Mayo 是一个 CAD 查看器和格式转换器，两千多行核心代码，BSD-2 许可。它做的事很聚焦：读 STEP/IGES/BREP/STL/OBJ 等格式，显示，导出。代码分成 `app`、`gui`、`io`、`occ` 四层，每一层职责单一，CMake 写得干净，用的是现代 C++。

它最有价值的地方是**边界处理**：OCCT 的 `TopoDS_Shape` 怎么变成 Qt 场景里的可绘制对象，选中怎么映射回 shape，XDE 文档的装配层级怎么显示成树。这些问题是每个 CAD 前端都要解决的，Mayo 给了一份不到一万行的参考答案。

<figure markdown>
  ![Mayo](../assets/images/cad/mayo-2.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 3-3</span>Mayo 的界面。功能克制，但把“读入、显示、选中、导出”这条最小闭环做完整了，适合作为自研 CAD 的起点。</figcaption>
</figure>

## 3.5 二维：QCAD 与 LibreCAD

三维很热闹，但工业现场大量交付物仍然是二维图纸。DXF 是这个领域的事实标准，围绕它的开源软件也有两个值得读的项目。

**QCAD** 是商业公司 RibbonSoft 的产品，GPLv3 加商业双许可。它的架构比 LibreCAD 现代：`RDocument` 持有实体，`REntity` 是几何基元，渲染与命中有独立抽象。最有意思的是它的 **ECMAScript 脚本接口**：几乎所有功能都能用脚本调用，社区用它写插件、做批量处理。这是“脚本即 API”的典型案例，比 C++ 插件轻得多。

**LibreCAD** 是 QCAD 社区版分叉出来的项目，GPLv2，代码更老，`RS_*` 前缀的类遍布全局，但功能完整、用户基数大。它的价值在于“一个纯 Qt 的二维 CAD 能做成什么样”，以及大量 DXF 兼容性的实战经验。

二维 CAD 的技术难点和三维不同：不在几何内核，而在**图纸语义**。图层、线型、标注、图块、打印样式，这些东西构成了工程制图的规则，比几何更难标准化。

<figure markdown>
  ![QCAD](../assets/images/cad/qcad.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 3-4</span>QCAD 的界面。二维 CAD 的重心是图层、捕捉和标注，而不是三维视口。</figcaption>
</figure>

<figure markdown>
  ![LibreCAD](../assets/images/cad/librecad.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 3-5</span>LibreCAD 的绘图区与图层列表。命令行、图层、捕捉三件套，是二维 CAD 交互的全部骨架。</figcaption>
</figure>

## 3.6 几个专业方向

除了通用 CAD，这个领域还有几类“垂直内核”，它们的存在说明工业软件的另一个规律：**通用能力之上，行业知识才是壁垒。**

**Analysis Situs** 是一个 CAD/CAM/CAE 算法的实验平台，Qt + VTK + Tcl，基于 OCCT。它提供特征识别、曲面分析、网格修复等算法，界面更像一个算法调试器。适合学习“几何算法怎么被验证”，不适合直接做产品。

**TiGL** 处理飞机几何。它读 CPACS（一种基于 XML 的飞机参数描述格式），用 NURBS 生成机翼、机身、尾翼的曲面，再导出 STEP/IGES。这个项目的价值在于示范了“行业数据标准 + 几何库”的组合方式：CPACS 定义语义，OCCT 提供运算。

<figure markdown>
  ![TiGL Viewer](../assets/images/cad/tigl.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 3-6</span>TiGL Viewer 显示的机翼外形。参数化在这里不是“拉伸一个草图”，而是“用一组工程参数生成整架飞机的外形”。</figcaption>
</figure>

**Klampt** 是机器人运动规划工具箱，Qt 只负责界面，核心是运动学、动力学和规划算法。它提醒我们：工业软件不等于 CAD，机器人、测量、检测都有各自的“内核”，Qt 在其中的角色始终是同一件事——把内核的能力变成人能操作的东西。

**OpenNURBS** 是 Rhino 的 3DM 格式读写库，专注几何交换，不做界面。它常常作为“第二内核”出现在需要和 Rhino 互通的产品里。

**Topologic** 走的是另一条路：它不关心 CAD 的边界面，而是用非流形拓扑描述建筑空间之间的邻接关系，适合做空间分析而不是出图。它的许可证是 AGPL-3.0，闭源产品基本不能碰，这一点在选择之前就要想清楚。

**rhioCAD** 是 NaroCAD 的分支，试图用 C# 做参数化建模，2016 年之后基本停更。把它列进来不是为了推荐，而是为了说明：**开源 CAD 的失败案例比成功案例多得多**，原因几乎总是同一个——内核没解决，先去解决界面。

## 3.7 如果今天要做一个 CAD

给一张按需求走的路线表。

| 你的目标 | 建议起点 | 理由 |
| --- | --- | --- |
| 查看、转换、批处理 | Mayo | 代码小，BSD 许可，改起来没有负担 |
| 参数化零件设计 | FreeCAD 的 `App` + OCCT | 属性系统与重算图可以直接借鉴 |
| 二维图纸编辑 | QCAD 的脚本层或 LibreCAD | DXF 兼容性与图纸语义的现成经验 |
| 行业专用建模（飞机、船舶、建筑） | OCCT + 自研参数层 | 行业语义必须自己定义，内核用现成的 |
| 几何算法研究 | Analysis Situs | 有完整的算法验证框架 |

最后一句提醒：不要从“做一个通用 CAD”开始。这个赛道已经没有空位了。找一个行业，把它的数据标准和几何需求吃透，用 OCCT 做内核、Qt 做界面，胜算大得多。
