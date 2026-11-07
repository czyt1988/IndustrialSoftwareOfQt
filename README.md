# Qt 工业软件工程实践

> 架构、交付与 AI 协作

一本关于大型 Qt 工业软件开发的电子书。它不罗列功能，也不做 API 教程，而是讨论工程结构、模块化与插件化、性能、稳定性、交付流水线，以及 2026 年之后 AI Agent 如何进入 Qt 项目的日常开发。

**在线阅读：<https://czyt1988.github.io/IndustrialSoftwareOfQt/>**

## 内容

全书分五部十二章，约 10 万中文字，配 40 余张项目截图与 Mermaid 示意图：

- **第一部 · 应用与选型背景**：工业软件版图、桌面框架选型。
- **第二部 · 工程基础**：Qt 版本与许可证、开发环境、大型项目工程结构。
- **第三部 · 架构与工程经验**：模块化与插件化、文档与质量、性能、稳定性、交付部署。
- **第四部 · 参考**：常见第三方库推荐。
- **第五部 · AI**：AI 驱动开发。

外加工业软件项目索引、工具与资源清单、术语表、截图来源四个附录。

## 本地预览

需要 Python 3.10 以上。

```bash
pip install -r requirements.txt
mkdocs serve -a 127.0.0.1:8000
```

打开 <http://127.0.0.1:8000>。修改 `docs/` 下的文件会自动重新构建。

发布前做一次严格构建：

```bash
mkdocs build --strict
```

## 仓库结构

```text
docs/
  index.md            封面与书目
  preface.md          前言
  chapters/           正文，一章一文件
  appendix/           附录 A–D
  assets/
    css/book.css      全部自定义样式
    js/book.js        阅读进度条
    js/mermaid-init.js  Mermaid 按需渲染与主题切换
    js/vendor/        本地 Mermaid 运行时
    images/           站点图片（由脚本生成的 WebP）
screenshot/           原始截图，素材来源
drafts/v1/            v1 旧稿，仅作素材，不参与构建
overrides/            主题模板覆盖
hooks.py              章节号、字数、阅读时长注入
tools/                图片转换、仓库元数据、引号规范化
mkdocs.yml            站点配置与目录
OUTLINE.md            全书大纲
STYLE.md              写作规范
AGENTS.md             仓库维护约定
```

## 图片与图表

`docs/assets/images/` 下的文件全部由脚本生成，不要手工替换：

```bash
python tools/build_images.py
```

原始截图保留在 `screenshot/` 与 `screenshot-visualization2D/`，新增图片时先在 `tools/build_images.py` 的 `ASSETS` 里登记映射。

正文中的流程图、类图、时序图、状态图用 Mermaid 编写。运行时是本地文件 `docs/assets/js/vendor/mermaid.min.js`，不依赖 CDN；只在包含 Mermaid 图的页面按需加载，并跟随日间/夜间模式重绘。

## 构建与部署

推送 `main` 分支后，GitHub Actions 会执行 `mkdocs build --strict` 并发布到 GitHub Pages，工作流见 `.github/workflows/pages.yml`。首次启用时，需要在仓库的 **Settings → Pages** 里把 Source 设为 **GitHub Actions**。

## 许可

代码与文字均以 [MIT](LICENSE) 协议发布。书中提到的开源项目，版权与许可证归各自作者所有；引用仅为技术讨论，不构成法律意见。
