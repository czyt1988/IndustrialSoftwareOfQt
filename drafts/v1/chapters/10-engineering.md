---
title: 构建、许可与选型
chapter: 10
part: 第三部 · 工程
---

# 构建、许可与选型

!!! abstract "本章要点"
    一个工业软件项目的成败，很多时候在写第一行代码之前就定了：依赖怎么管、Qt 用哪个版本、许可证能不能闭源、装到客户机器上要多大。这一章给出一套可以直接拿去开会的判断方法，以及一张把功能、许可、维护成本放在一起看的选型表。

## 10.1 构建：CMake 是唯一答案

Qt 6 之后，CMake 是官方构建系统，`qmake` 退居维护模式。工业软件几乎必然要用 CMake，因为它的依赖（OCCT、VTK、ITK）都只提供 CMake 配置。

一个最小可用的骨架：

```cmake
cmake_minimum_required(VERSION 3.21)
project(MyCad LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets OpenGLWidgets)
find_package(OpenCASCADE REQUIRED)

add_executable(mycad
    src/main.cpp
    src/mainwindow.cpp
)
target_link_libraries(mycad PRIVATE
    Qt6::Widgets
    Qt6::OpenGLWidgets
    TKernel TKMath TKBRep TKTopAlgo TKSTEP
)
```

三个实践建议。

**用 target，不要用全局变量。** `target_link_libraries`、`target_include_directories` 是现在的标准，`include_directories` 会让依赖关系变成一团。

**用 CMake Presets。** `CMakePresets.json` 把编译器、构建类型、依赖路径固化下来，新同事克隆仓库后一条命令就能构建。工业软件的依赖配置是最容易劝退新人的部分。

**把第三方依赖当二进制。** OCCT 和 VTK 从源码编译要几个小时。用 vcpkg、Conan 或者公司内部的二进制包，CI 里只编译自己的代码。

## 10.2 Qt 版本：5 还是 6

2026 年的现实是：新项目用 Qt 6，存量项目大多还在 Qt 5.15。

Qt 6 的变化不小：C++17 起步、`QRegExp` 移除、高 DPI 默认开启、部分模块拆分（`QtOpenGLWidgets` 独立）、图形栈重写（`QRhi`）。迁移一个中型项目通常要几周到几个月，工作量集中在自定义绘制、旧式 `QGLWidget`、以及依赖 Qt 5 私有 API 的代码。

策略上分三种：

- **全新项目**：直接 Qt 6，别犹豫。
- **存量项目**：先把第三方依赖升到支持 Qt 6 的版本，再逐模块迁移，用 `QT_VERSION_CHECK` 隔离差异。
- **要支持老系统**（Windows 7、旧版 Linux）：Qt 5.15 是唯一选择，要接受它不再更新的现实。

许可证也要一起考虑：Qt 6 开源版是 LGPLv3，闭源商用必须动态链接，并且允许用户替换 Qt 库。静态链接要么买商业许可，要么提供目标文件，实务上很少走通。

## 10.3 部署：最后一公里

工业软件的客户常常在内网，安装包必须离线可用。

- **Windows**：`windeployqt` 收集 DLL 和插件，Inno Setup 或 WiX 做安装器，注意 VC 运行库和 OpenGL 驱动检测。
- **Linux**：AppImage 最省事，或者用 Flatpak 做沙箱。要注意 glibc 版本和目标发行版的兼容。
- **macOS**：`macdeployqt` 打包，签名 + 公证（notarization）是必须的，否则用户打不开。

体积是个现实问题。一个带 OCCT + VTK 的 Qt 应用，安装包轻松超过 300 MB。能裁的模块要裁（VTK 只编需要的模块），能用动态库就别静态链接。

## 10.4 许可：先把红线画出来

工业软件选开源组件，许可证是第一道筛子。下面这张表覆盖了书里提到的主要项目。

| 许可证 | 闭源商用 | 主要义务 | 书中项目 |
| --- | --- | --- | --- |
| MIT / BSD | 可以 | 保留版权声明 | Mayo、VTK、VisIt、Inviwo、FastCAE、Klampt、Slicer |
| Apache-2.0 | 可以 | 保留声明与变更说明，含专利授权 | ITK、CTK、TiGL |
| LGPL-2.1/3.0 | 可以（动态链接） | 允许用户替换库，公开对库的修改 | Qt、OCCT、FreeCAD、QWT、JKQtPlotter |
| GPL-2.0/3.0 | 不可以 | 衍生作品必须开源 | QGIS、LibreCAD、KiCad、LibrePCB、OpenFOAM、GPXSee |
| AGPL-3.0 | 不可以（含网络服务） | 网络提供服务也算分发 | Topologic |
| 双许可 | 看买的哪一边 | 商业许可可闭源 | QCAD、QCustomPlot、Qt |

读表要注意三件事。

**LGPL 的“动态链接”不是口号。** 你要让用户能替换 Qt/OCCT 的 DLL，意味着不能把库静态编进去，也不能阻止用户替换。很多团队栽在“为了发布方便改成静态链接”上。

**GPL 的传染范围是“衍生作品”。** 通过进程边界调用（命令行、socket）通常不算衍生，链接进同一个进程通常算。这也是为什么 OpenFOAM 可以没有界面：界面是独立进程，许可互不影响。

**双许可要看清版本。** QCustomPlot 的 GPLv3 版本可以免费用，商业版本要买；QCAD 的社区版是 GPLv3，专业版是商业许可。用错版本，法务问题会在融资尽调时才爆出来。

## 10.5 怎么选：一张打分表

选型不是比功能列表，是把约束量化。给自己列五个维度，每个 1 到 5 分，加权求和。

| 维度 | 权重 | 判断依据 |
| --- | --- | --- |
| 许可证匹配 | 30% | 能不能闭源、有没有静态链接需求 |
| 集成成本 | 25% | 依赖数量、构建难度、ABI 稳定性 |
| 维护活跃度 | 20% | 最近提交、issue 响应、版本节奏 |
| 性能与规模 | 15% | 你的数据量下能不能达标 |
| 文档与社区 | 10% | 出问题能不能搜到答案 |

拿“闭源产品的实时曲线库”做一次示范：

| 候选 | 许可 | 集成 | 活跃 | 性能 | 文档 | 加权 |
| --- | --- | --- | --- | --- | --- | --- |
| QWT | 5 | 4 | 3 | 4 | 3 | 4.0 |
| JKQtPlotter | 5 | 4 | 4 | 4 | 4 | 4.2 |
| QCustomPlot | 2 | 5 | 3 | 3 | 4 | 3.3 |
| KD Chart | 5 | 4 | 3 | 3 | 3 | 3.7 |

分数不重要，重要的是这个过程逼你把“我觉得它好用”翻译成“它在哪个维度上赢”。开会时，这张表比十页 PPT 有用。

## 10.6 从零到一的路线

如果今天要启动一个工业软件产品，我会这样排：

1. **定数据模型**：根对象、节点类型、ID、序列化格式。这一步错了，后面全错。
2. **定内核**：几何用 OCCT，可视化用 VTK，图像用 ITK，不要自研。
3. **搭壳**：Qt 主窗口、文档、撤销栈、属性面板，先把“打开 → 改 → 保存 → 撤销”跑通。
4. **接视口**：把内核的渲染接进来，处理高 DPI 和事件。
5. **开扩展点**：插件接口 + 脚本入口，哪怕一开始只有一个空插件。
6. **补工程**：CMake Presets、CI、安装包、许可声明。

前三步决定这个产品能不能活，后三步决定它能不能长大。

## 10.7 最后

这本书拆了三十个项目，最后能落成一句话：**工业软件的难度不在写代码，在约束里做选择。** 几何内核选谁、界面框架选谁、许可证怎么走、数据模型怎么定，这些选择的代价会在三年后显现。

希望这本书能让你在选的时候，少踩几个别人踩过的坑。
