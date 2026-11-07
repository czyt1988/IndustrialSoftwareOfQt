# 《Qt 工业软件工程实践》写作规范

这份规范约束全书正文的语气、结构和图文格式。写作前先读一遍，写完再对照检查。

## 一、全书结构

书名：**《Qt 工业软件工程实践：架构、交付与 AI 协作》**

五部十二章，附录四篇：

| 部 | 章 | 文件 |
| --- | --- | --- |
| 第一部 应用与选型背景 | 1 用 Qt 写成的工业软件版图 | `docs/chapters/01-industrial-map.md` |
| | 2 桌面框架选型：Qt、Electron、Python 与 Web | `docs/chapters/02-framework-selection.md` |
| 第二部 工程基础 | 3 Qt 版本与许可证 | `docs/chapters/03-versions-licenses.md` |
| | 4 开发环境与技术栈 | `docs/chapters/04-dev-environment.md` |
| | 5 大型项目工程结构管理 | `docs/chapters/05-project-structure.md` |
| 第三部 架构与工程经验 | 6 架构：模块化与插件化 | `docs/chapters/06-architecture.md` |
| | 7 文档、质量测试及自动化 | `docs/chapters/07-docs-quality.md` |
| | 8 性能工程 | `docs/chapters/08-performance.md` |
| | 9 稳定性与可维护性 | `docs/chapters/09-stability.md` |
| | 10 交付与部署 | `docs/chapters/10-delivery.md` |
| 第四部 参考 | 11 常见第三方库推荐 | `docs/chapters/11-libraries.md` |
| 第五部 AI | 12 AI 驱动开发 | `docs/chapters/12-ai-development.md` |
| 附录 | A 工业软件项目索引 | `docs/appendix/a-project-index.md` |
| | B 工具与资源清单 | `docs/appendix/b-tools-resources.md` |
| | C 术语表 | `docs/appendix/c-glossary.md` |
| | D 截图与示例仓库来源 | `docs/appendix/d-sources.md` |

## 二、声音

目标读者是已经会用 Qt、正在做或准备做工业软件客户端的工程师。写作姿态是“一个做过十年工业软件的工程师，在白板前把判断、证据和代价讲给同事听”，不是产品文案，也不是教程朗读。

具体要求：

1. **完整段落承载论证。** 一个自然段 2–6 句，段与段之间有推进关系。不要一句一段，不要把段落写成 bullet。
2. **先判断，再证据，最后代价。** 每节开头用一个明确的判断句立论，例如“大型工程必须用 CMake，原因不在语法，而在依赖传递”，然后给项目、代码或数据作证据，最后写清楚这个选择的代价和适用边界。
3. **列表只用于并列项。** 步骤、参数、检查项可以用列表；论证必须用段落。一节里列表不超过两组。
4. **具体到名词。** 写“`QUndoStack::mergeWith()` 决定拖动操作的合并粒度”，不写“良好的撤销机制很重要”。提到项目就写它的模块名、类名、目录名。
5. **承认不确定。** 没有公开证据的项目内部实现，写“从公开仓库结构看”；许可证以仓库原文为准；时效性强的数据标注核对时间。
6. **术语首次出现给中英文**，例如“边界表示（B-Rep）”，之后只用中文。中文与英文、数字与单位之间留空格。

### 禁用与慎用的表达

以下句式是 AI 腔的重灾区，出现即改：

- “随着……的发展”“在当今……的背景下”“众所周知”“总而言之”“综上所述”
- “值得注意的是”“需要指出的是”“不难发现”“可以看到”
- “不仅……而且……”“不是……而是……”（每章最多一次，且要有真正的对照关系）
- “让我们……”“接下来，我们将……”“本章将带你……”“深入探讨”“赋能”“闭环”“抓手”“颗粒度”
- “首先、其次、最后”三段式（改成有逻辑关系的完整句子）
- 空洞的形容词：“强大”“优雅”“高效”“灵活”“无缝”“极致”
- 每段开头都用“在……方面”“对于……而言”

### 语气样例

差：

> 随着工业软件的发展，Qt 变得越来越重要。它不仅提供了丰富的界面组件，而且拥有良好的跨平台能力。值得注意的是，选择合适的框架非常关键。首先，要考虑性能；其次，要考虑生态；最后，要考虑团队。

好：

> Qt 在工业软件里的位置，不是“界面库”三个字能概括的。它同时提供了窗口系统、模型视图、元对象和插件加载四套基础设施，这四样东西恰好对应工业客户端最耗时间的四块工作。代价是它把领域能力全部留给了你：几何内核、网格算法、求解器，一行都没有。理解这条边界，比记住多少个 Qt 类更重要。

## 三、章节模板

每个章节文件以 front matter 开头，一级标题与 `title` 一致，正文第一块是摘要：

```markdown
---
title: 章节标题
chapter: 6
part: 第三部 · 架构与工程经验
---

# 章节标题

!!! abstract "本章要点"
    一段 150–250 字的判断，说清本章的结论和它成立的边界。不要复述目录，不要写“本章将介绍……”。

## 6.1 节标题

正文……

## 6.2 节标题

正文……

!!! note "小结"
    可选的收束段，三到五句，把本章的判断收回到全书主线。
```

节标题编号用 `6.1`、`6.2`，不要用“一、”“（一）”。每章 5–9 个二级标题；每节至少有一个具体支撑：项目案例、代码片段、对比表、截图或图。

## 四、图

### 截图

图片一律使用 `docs/assets/images/` 下已经生成的 WebP，不直接引用 `screenshot/` 原图。图注格式固定：

```html
<figure markdown>
  ![替代文本](../assets/images/cad/freecad.webp){ loading=lazy }
  <figcaption><span class="fig-no">图 1-1</span>图注文字，说明这张图证明了什么，而不是“FreeCAD 界面”。</figcaption>
</figure>
```

图号按“章-序”手写，章内从 1 连续编号。新增图先在 `tools/build_images.py` 注册源文件映射，运行 `python tools/build_images.py`。

### Mermaid 图

流程图、时序图、类图、状态图、时间线一律用 Mermaid，不用外链图片。图必须包在 `figure.book-diagram` 里，才能和截图共用边框与图注样式：

```html
<figure class="book-diagram" markdown>
```mermaid
flowchart LR
  A[输入] --> B[处理] --> C[输出]
```
<figcaption><span class="fig-no">图 6-1</span>图注文字。</figcaption>
</figure>
```

Mermaid 写作约束：

- 单图节点不超过 14 个，超过就拆成两张图。
- 节点文字用中文短语，不超过 12 个字；箭头标签不超过 8 个字。
- 线性流程优先用 `flowchart TB`，横向对比或分层用 `LR`；全章方向不要混用。
- 类图、时序图、状态图优先用 Mermaid 原生语法，不要用截图代替。
- 图内不要写 `style` 自定义颜色，配色由站点脚本按日间/夜间模式统一注入。
- 图注写清“这张图在解释什么机制”，不要只写“架构图”。
- 行内写 ` ```mermaid ` 即可，构建时自动转成 `book-mermaid`，不要手写 HTML 类名。

### 可用图片

图片全部在 `docs/assets/images/` 下，引用路径相对章节文件：

| 分组 | 文件 | 适合的章节 |
| --- | --- | --- |
| `cad/` | freecad、freecad-2、mayo-2、qcad、librecad、analysis-situs、tigl、topologic、rhiocad | 第 1 章 |
| `eda/` | kicad、librepcb | 第 1 章 |
| `cae/` | paraview、paraview-2、gmsh、gmsh-2、fastcae | 第 1 章 |
| `viz/` | slicer、inviwo、visit、labplot、ctk | 第 1 章 |
| `gis/` | qgis、qgis-2、gpxsee | 第 1 章 |
| `charts/` | qwt、qcustomplot、qcustomplot-2、jkqtplotter、jkqtplotter-2、kd-chart、kd-chart-2 | 第 11 章 |
| `libraries/` | saribbon、qwt-7-simpleplot、qwt-waterfall3d、qim-2d、qim-3d、qtpropertybrowser、sacolorwidgets、sacolor-palette、qwindowkit | 第 11 章 |
| `workbench/` | table、chart、workflow、agent、agent-chart | 第 5、6、10、11、12 章 |

第 1 章已经用完 12 张截图，不要重复引用。第 11 章按库分配图片，避免同一个库出现两张同类截图。

### 图的数量

每章 3–6 张图，其中至少一张 Mermaid 图。第 1 章和第 11 章以截图为主，第 2–10 章以 Mermaid 图为主。图片总量控制在 5 MB 以内。

## 五、表

对比、选型、检查清单用表格。表头用中文，第一列通常是判断维度。表格前后要有正文解释，不能只放一张表就结束一节。表格宽度超过正文时，优先删列，不要压缩字号。

## 六、代码

- C++ 代码用 `cpp`，CMake 用 `cmake`，shell 用 `bash`，YAML 用 `yaml`。
- 示例要么能编译，要么在代码块上方注明“结构示意，非完整实现”。
- 代码块内注释用中文，但标识符保持英文。
- 不贴超过 40 行的代码；需要长示例时，只保留关键片段并用 `// ...` 省略。

## 七、篇幅

按大纲的目标字数写，允许 ±20%：

| 章 | 目标字数 | 章 | 目标字数 |
| --- | --- | --- | --- |
| 1 | 10,000 | 7 | 10,000 |
| 2 | 8,000 | 8 | 12,000 |
| 3 | 8,000 | 9 | 8,000 |
| 4 | 10,000 | 10 | 12,000 |
| 5 | 12,000 | 11 | 18,000 |
| 6 | 14,000 | 12 | 14,000 |

字数按中文字符计，`hooks.py` 会在页面顶部显示。宁可把一个问题写透，不要每节都浅尝辄止。

## 八、事实与引用

- 项目地址、许可证、维护状态在写作时核对一次，正文给链接。
- Qt 版本、模块归属、许可证条款以 Qt 官方文档为准；不确定的条款写明“以官网为准”。
- 不编造项目内部实现、性能数字和用户案例。引用数据时给出来源。
- 作者自己维护的项目（SARibbon、QWT 分支、QIm、DAWidgets、QtPropertyBrowser、SAColorWidgets、qwindowkit、data-workbench）用第三方口吻写：与同类库放在同一张表里比较，讲能力边界，不写“我的库最好”。

## 九、交付前自检

1. `python -m mkdocs build --strict` 零警告。
2. 章内图号连续，图注不为空，Mermaid 图在浏览器里能渲染。
3. 所有站内链接可点，所有外链指向项目主页或文档。
4. 把正文朗读一遍：如果一句话只有十几个字、连续出现，改成有主从关系的长句。
5. 搜一遍禁用词清单，确认没有漏网。
