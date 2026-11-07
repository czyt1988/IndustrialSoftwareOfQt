# 附录 B · 工具与资源清单

这份清单按用途分组，给每项一句用途说明和官方入口。工具版本变化很快，书中不锁定版本号；选型时优先看它是否仍在维护、是否支持你的 Qt 与编译器版本。

## B.1 编译器与构建

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| MSVC | Windows 上 Qt 官方支持最好的编译器 | <https://visualstudio.microsoft.com/> |
| MinGW-w64 | Windows 上的 GCC 工具链，适合开源和跨平台验证 | <https://www.mingw-w64.org/> |
| Clang / LLVM | 跨平台编译器，clangd、clang-tidy 的基础 | <https://llvm.org/> |
| CMake | 跨平台构建系统，Qt 6 官方主推 | <https://cmake.org/> |
| Ninja | 快速的构建执行器，常与 CMake 搭配 | <https://ninja-build.org/> |
| vcpkg | C++ 包管理器，适合统一第三方依赖 | <https://vcpkg.io/> |
| Conan | C++ 包管理器，适合复杂依赖和二进制包管理 | <https://conan.io/> |
| ccache / sccache | 编译缓存，缩短重复构建时间 | <https://ccache.dev/>、<https://github.com/mozilla/sccache> |

## B.2 调试与性能

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Qt Creator | Qt 官方 IDE，调试、界面预览、CMake 集成 | <https://www.qt.io/product/development-tools> |
| Visual Studio | Windows 调试器与性能分析器 | <https://visualstudio.microsoft.com/> |
| WinDbg | Windows 崩溃转储与内核/用户态调试 | <https://learn.microsoft.com/windows-hardware/drivers/debugger/> |
| GDB / LLDB | Linux/macOS 调试器 | <https://sourceware.org/gdb/>、<https://lldb.llvm.org/> |
| perf | Linux CPU 采样与火焰图数据源 | <https://perf.wiki.kernel.org/> |
| Windows Performance Analyzer | Windows ETW 与性能时间线 | <https://learn.microsoft.com/windows-hardware/test/wpt/> |
| heaptrack | Linux 堆分配跟踪 | <https://github.com/KDE/heaptrack> |
| Valgrind | 内存错误与泄漏检测 | <https://valgrind.org/> |
| RenderDoc | GPU 帧捕获与图形调试 | <https://renderdoc.org/> |
| Intel VTune | CPU/GPU 性能分析 | <https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html> |

## B.3 静态分析与格式化

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| clang-tidy | C++ 静态检查与现代化重构 | <https://clang.llvm.org/extra/clang-tidy/> |
| clang-format | 统一代码格式 | <https://clang.llvm.org/docs/ClangFormat.html> |
| cppcheck | 轻量静态分析，适合补充 clang-tidy | <https://cppcheck.sourceforge.io/> |
| PVS-Studio | 商业静态分析工具 | <https://pvs-studio.com/> |
| include-what-you-use | 头文件依赖清理 | <https://include-what-you-use.org/> |

## B.4 测试

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Qt Test | Qt 自带测试框架，支持 GUI 事件模拟 | <https://doc.qt.io/qt-6/qtest-overview.html> |
| Catch2 | 现代 C++ 单元测试框架 | <https://github.com/catchorg/Catch2> |
| GoogleTest | Google 的 C++ 测试框架 | <https://github.com/google/googletest> |
| Google Benchmark | C++ 微基准测试 | <https://github.com/google/benchmark> |
| CTest | CMake 集成的测试驱动 | <https://cmake.org/cmake/help/latest/manual/ctest.1.html> |
| Squish | 商业 GUI 自动化测试 | <https://www.qt.io/product/quality-assurance/squish> |

## B.5 打包与发布

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| windeployqt | 收集 Windows 上的 Qt 运行库与插件 | <https://doc.qt.io/qt-6/windeployqt.html> |
| macdeployqt | 收集 macOS 上的 Qt 依赖 | <https://doc.qt.io/qt-6/macdeployqt.html> |
| linuxdeploy / AppImage | Linux 便携包 | <https://github.com/linuxdeploy/linuxdeploy>、<https://appimage.org/> |
| Inno Setup | Windows 安装器 | <https://jrsoftware.org/isinfo.php> |
| WiX Toolset | Windows 安装器（MSI） | <https://wixtoolset.org/> |
| CPack | CMake 自带的打包工具 | <https://cmake.org/cmake/help/latest/module/CPack.html> |
| GitHub Actions | CI/CD 与发布流水线 | <https://github.com/features/actions> |
| 7-Zip | 高压缩率归档 | <https://www.7-zip.org/> |

## B.6 文档

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Doxygen | 从 C++ 注释生成 API 文档 | <https://www.doxygen.nl/> |
| Sphinx | 文档站与 API 文档编排 | <https://www.sphinx-doc.org/> |
| Breathe | Sphinx 与 Doxygen 的桥接 | <https://breathe.readthedocs.io/> |
| MkDocs | 静态文档站 | <https://www.mkdocs.org/> |
| Material for MkDocs | 本书使用的 MkDocs 主题 | <https://squidfunk.github.io/mkdocs-material/> |
| Mermaid | 文本绘制的流程图、时序图、类图 | <https://mermaid.js.org/> |
| Qt Help | Qt 离线帮助系统 | <https://doc.qt.io/qt-6/qthelp-framework.html> |

## B.7 图形、几何与数据

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| OpenCASCADE | 几何内核 | <https://dev.opencascade.org/> |
| VTK | 科学可视化 | <https://vtk.org/> |
| GDAL | 地理数据读写 | <https://gdal.org/> |
| PROJ | 坐标参考系转换 | <https://proj.org/> |
| GEOS | 几何运算 | <https://libgeos.org/> |
| HDF5 | 科学数据容器 | <https://www.hdfgroup.org/solutions/hdf5/> |
| SQLite | 嵌入式数据库 | <https://sqlite.org/> |
| protobuf | 结构化序列化 | <https://protobuf.dev/> |
| Blender | 三维内容与格式转换 | <https://www.blender.org/> |
| Inkscape | SVG 图标与矢量图编辑 | <https://inkscape.org/> |

## B.8 学习资源

| 资源 | 用途 | 入口 |
| --- | --- | --- |
| Qt 官方文档 | 版本、模块、许可、构建 | <https://doc.qt.io/> |
| Qt 发布与支持周期 | 判断版本能否长期使用 | <https://doc.qt.io/qt-6/qt-releases.html> |
| Qt 许可页面 | 模块级许可证 | <https://doc.qt.io/qt-6/licensing.html> |
| KDAB 博客 | Qt 性能、图形、调试的深度文章 | <https://www.kdab.com/blog/> |
| Qt Wiki | 社区经验与平台说明 | <https://wiki.qt.io/> |
| C++ Core Guidelines | C++ 编码与设计规范 | <https://isocpp.github.io/CppCoreGuidelines/> |
| OpenCASCADE 文档 | 几何内核模块与示例 | <https://dev.opencascade.org/doc/overview/html/> |
| VTK 示例 | 可视化管线与交互 | <https://examples.vtk.org/> |

工具清单容易越写越长，真正重要的是把少数几个工具用熟，并写进项目的 `README` 或 `AGENTS.md`：构建命令、测试命令、格式化命令、打包命令。工具只有进入流水线才算数，装在个人机器上只能算个人偏好。
