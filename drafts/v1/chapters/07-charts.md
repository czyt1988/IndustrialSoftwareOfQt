---
title: 图表与数据：实时曲线的工程学
chapter: 7
part: 第二部 · 领域
---

# 图表与数据：实时曲线的工程学

!!! abstract "本章要点"
    工业图表和商业图表是两种东西。前者要在 60 帧的预算里画完十万个点，要能跟随采集卡刷新，还要能导出成能贴进报告的图。Qt 生态里四个主力库各有取舍，选错一个，后面要么重写渲染，要么忍受卡顿。

<figure markdown>
  ![QCustomPlot](../assets/images/charts/qcustomplot.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 7-1</span>QCustomPlot 的示例图。坐标轴、图例、游标、选区这些“看起来简单”的东西，是工业图表八成的工作量。</figcaption>
</figure>

## 7.1 工业图表要什么

监控界面上的曲线，需求和 Excel 完全不同。

- **刷新率**：采集卡 1 kHz，界面至少 10 Hz 刷新，不能掉帧。
- **数据量**：一次试验几十万到几百万点，全画会卡死。
- **交互**：缩放、平移、框选、游标读数、区间统计，都要跟手。
- **导出**：矢量图给报告，位图给邮件，坐标轴和字体要能改。
- **稳定**：连续跑三个月不崩、不漏点、不涨内存。

这五条决定了架构：数据层和绘图层必须分开，绘制必须能抽稀，更新必须是增量的。

## 7.2 四个主力库

**QCustomPlot** 是单文件库，一个 `.h` 加一个 `.cpp`，直接拖进项目就能用。它基于 `QPainter`，API 设计得像 Qt 原生控件：`addGraph()`、`graph()->setData()`、`replot()`。交互功能（缩放、拖拽、图例、游标）开箱即用，导出 PNG/PDF/SVG 也很完整。

它的优点是**成本极低**：没有构建系统负担，没有依赖，源码可读可改。缺点是许可证：GPLv3 或商业许可，闭源产品必须买授权。另外，纯 `QPainter` 的绘制在百万点级别会吃力。

**QWT** 是 Qt 世界里最老的图表库之一，LGPL 加例外条款，可以用于闭源产品。它的 API 更“正统”：`QwtPlot`、`QwtPlotCurve`、`QwtScaleDiv`，扩展点设计得比较细，适合做定制化的仪表和示波器界面。

缺点是代码风格偏老，文档一般，部分功能需要自己补。它更适合“我要一个稳定的基础，然后自己往上搭”的场景。

**KD Chart** 来自 KDAB，仓库标注 MIT 许可。它的定位偏商业报表：柱状图、饼图、甘特图、极坐标图，支持模型/视图，适合做统计和报表界面，而不是高频刷新的实时曲线。

**JKQtPlotter** 是近年比较活跃的一个，LGPL-2.1，功能覆盖面很广：2D 折线、柱状、统计图、图像、LaTeX 公式渲染，Qt5/Qt6 都支持。它的作者维护得很勤，示例齐全，适合“功能要多、预算要低”的项目。

<figure markdown>
  ![QWT](../assets/images/charts/qwt.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 7-2</span>QWT 的典型外观。它的风格和 Qt 原生控件一致，扩展点多，适合做仪表盘而不是“漂亮图表”。</figcaption>
</figure>

<figure markdown>
  ![KD Chart](../assets/images/charts/kd-chart-2.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 7-3</span>KD Chart 的图表类型。它更像报表工具，强项是图表种类和排版，而不是高频绘制。</figcaption>
</figure>

## 7.3 百万点怎么画

无论选哪个库，性能问题的解法是同一套。

**抽稀，而不是全画。** 屏幕宽 1920 像素，一行最多显示 1920 个点。把数据按像素列聚合，每列取最小值和最大值，画一条竖线。一百万点抽稀到几千条线段，视觉上几乎无损，速度提升两个数量级。这在信号处理里叫 min/max decimation，是所有示波器软件的标配。

**增量更新。** 新数据到来时，不要 `setData()` 整个数组。维护一个环形缓冲，只把新增的区段标记为脏，只重绘脏区。

**分层的绘制。** 网格、坐标轴、曲线、游标分成不同的图层。缩放时只有坐标轴和曲线需要重画，背景网格可以缓存成 pixmap。

**避开 QPainter 的陷阱。** 每个点设置一次 `QPen` 是灾难；用 `drawPolyline` 一次画完；抗锯齿在高频刷新时关掉；能用整数坐标就别用浮点。

**必要时上 OpenGL。** 如果点数超过百万且必须实时，`QOpenGLWidget` 加顶点缓冲是唯一出路。但要注意：GPU 上传也有带宽成本，动态数据每帧全量上传反而更慢，要用环形缓冲和 `glBufferSubData` 做增量。

## 7.4 LabPlot：产品级的样子

LabPlot 是 KDE 的数据分析软件，GPL，功能接近 Origin 的开源替代：导入数据、画图、拟合、统计分析、导出。

它不适合直接当库用（代码和 KDE 框架耦合较深），但适合看“一个完整的分析软件长什么样”：项目管理、工作表、图表、拟合对话框、批量导出，这些模块怎么组织，怎么和 Qt 的 Model/View 配合。

<figure markdown>
  ![LabPlot](../assets/images/viz/labplot.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 7-4</span>LabPlot 的工作区。它把“数据表、图表、分析结果”放在同一个项目里，是科学绘图软件的典型信息架构。</figcaption>
</figure>

## 7.5 选型表

| 需求 | 推荐 | 注意 |
| --- | --- | --- |
| 闭源商业产品，预算有限 | QWT 或 JKQtPlotter | 确认 LGPL 的动态链接方式 |
| 快速出原型，可以开源 | QCustomPlot | 单文件，改起来最省事 |
| 报表、统计图为主 | KD Chart | 图表种类多，实时性一般 |
| 数据分析全流程 | LabPlot（参考） | 不适合作为嵌入式库 |
| 百万点实时 | 自研 OpenGL 或 QCustomPlot + 抽稀 | 先做 min/max 抽稀，再考虑重写 |

一个常被忽略的点：图表的**导出质量**往往比屏幕效果更重要。客户最终要的是能贴进 Word 的图，矢量导出、字体嵌入、线宽控制在 0.5 pt 以上，这些细节决定专业感。
