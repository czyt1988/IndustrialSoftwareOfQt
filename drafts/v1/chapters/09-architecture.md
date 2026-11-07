---
title: 架构模式：命令、插件、脚本与线程
chapter: 9
part: 第三部 · 工程
---

# 架构模式：命令、插件、脚本与线程

!!! abstract "本章要点"
    这一章把前六章反复出现的结构抽出来，给出可落地的最小实现：文档对象、撤销命令、插件接口、脚本暴露、线程与进度、渲染接入。它们不是银弹，但每一个都经过了三十年、上百个项目的验证。你可以不喜欢，但很难绕开。

## 9.1 文档对象：给数据一个根

工业软件的第一个架构决定，是“数据存在哪里”。散落在窗口类里的数据，三个月后一定失控。

最小可用的文档模型长这样：

```cpp
class Document : public QObject {
    Q_OBJECT
public:
    Node *createNode(const QString &type);
    void removeNode(Node *node);
    const QList<Node *> &nodes() const { return m_nodes; }
    QUndoStack *undoStack() { return &m_undo; }
signals:
    void nodeAdded(Node *node);
    void nodeRemoved(Node *node);
    void modifiedChanged(bool modified);
private:
    QList<Node *> m_nodes;
    QUndoStack m_undo;
};
```

三个要点。

**节点有稳定 ID。** 用 `QUuid` 或递增整数，不要用指针当下标。序列化、复制、跨文档引用都依赖它。

**修改走信号。** 视图不直接改文档，文档也不直接刷视图。中间隔一层信号，将来加“只读模式”“多人协作”“批量模式”时才不用改所有调用点。

**文档负责脏标记。** `QUndoStack::cleanChanged` 是现成的实现：保存时 `setClean()`，标题栏跟着变星号。

节点本身要不要做成树，取决于领域。CAD 需要树（装配、特征），GIS 需要图层树，仿真需要流程树。树形结构的关键不是父子指针，而是**父节点对子节点的失效传播**：改一个参数，下游哪些节点要重算。

## 9.2 命令与撤销

`QUndoStack` 有两种用法：一种是把每个操作包成 `QUndoCommand`，另一种是用 `QUndoStack::push` 配合事务。前者简单，后者适合复合操作。

```cpp
class MoveCommand : public QUndoCommand {
public:
    MoveCommand(Item *item, const QPointF &delta, QUndoCommand *parent = nullptr)
        : QUndoCommand(QStringLiteral("移动 %1").arg(item->name()), parent)
        , m_item(item), m_delta(delta) {}

    void undo() override { m_item->moveBy(-m_delta); }
    void redo() override { m_item->moveBy(m_delta); }

    int id() const override { return CommandId::Move; }

    bool mergeWith(const QUndoCommand *other) override {
        auto *next = static_cast<const MoveCommand *>(other);
        if (next->m_item != m_item) return false;
        m_delta += next->m_delta;   // 连续拖动合并成一条撤销记录
        return true;
    }

private:
    Item *m_item;
    QPointF m_delta;
};
```

`id()` 与 `mergeWith()` 是容易被忽略的两个细节。没有它们，用户拖一次滑块会产生两百条撤销记录；有了它们，一次连续操作只留一条。

事务的写法是 `beginMacro()` / `endMacro()`，但要注意：宏里的每条命令仍然会执行 `redo()`，所以命令的构造函数**不要**修改模型，修改只放在 `redo()` 里。这个约定违反了，撤销就会错乱。

## 9.3 插件：把扩展点冻住

Qt 的插件机制分两步：定义接口，导出实现。

```cpp
// 1. 接口，发布后二进制兼容
class IModule {
public:
    virtual ~IModule() = default;
    virtual QString name() const = 0;
    virtual bool initialize(QWidget *parent) = 0;
};

#define IModule_iid "com.example.IModule/1.0"
Q_DECLARE_INTERFACE(IModule, IModule_iid)
```

```cpp
// 2. 插件实现
class CsvImportModule : public QObject, public IModule {
    Q_OBJECT
    Q_PLUGIN_METADATA(IID IModule_iid FILE "csvimport.json")
    Q_INTERFACES(IModule)
public:
    QString name() const override { return QStringLiteral("CSV 导入"); }
    bool initialize(QWidget *parent) override;
};
```

```cpp
// 3. 宿主加载
for (const QString &path : pluginPaths) {
    auto *loader = new QPluginLoader(path, this);
    if (auto *module = qobject_cast<IModule *>(loader->instance()))
        module->initialize(mainWindow);
}
```

接口设计的三个经验：

- **接口越窄越好。** 一个 `IModule` 加两三个方法，比二十个方法的“全能接口”稳定十年。
- **版本号写进 IID。** 改接口就换 IID，宿主不加载旧插件，比运行时崩溃好。
- **插件不碰主窗口。** 给插件一个上下文对象（文档、命令栈、日志），而不是 `QMainWindow *`。否则插件的每次界面改动都会传导到主程序。

## 9.4 脚本：把能力暴露出去

脚本是工业软件性价比最高的扩展方式。Qt 自带 `QJSEngine`，适合轻量的自动化和表达式；Python 适合重度的二次开发。

```cpp
QJSEngine engine;
QJSValue doc = engine.newQObject(document);
engine.globalObject().setProperty("doc", doc);
engine.evaluate("doc.createBox(10, 20, 30);");
```

`Document` 的槽函数需要 `Q_INVOKABLE` 或声明为 `slots`，属性需要 `Q_PROPERTY`，才能被脚本访问。

Python 的路线通常是用 PySide 的 `shiboken` 生成绑定，或者自己写一层 `pybind11`。代价是构建复杂度上升，收益是生态：科学计算、机器学习、数据处理，Python 都有现成的库。

不管用哪种，**脚本 API 的设计原则和 C++ 接口一样**：窄、稳定、有版本。脚本一旦被用户写进生产流程，改 API 的代价比改 C++ 还高。

## 9.5 线程：别在界面线程里算

Qt 的规则很简单：界面只能在一个线程里碰，计算放到别的线程，用信号回传结果。

```cpp
class Solver : public QObject {
    Q_OBJECT
public slots:
    void run(Job job) {
        for (int i = 0; i < job.steps(); ++i) {
            if (m_cancelled.loadRelaxed()) { emit cancelled(); return; }
            computeStep(i);
            emit progress(100 * (i + 1) / job.steps());
        }
        emit finished(result());
    }
signals:
    void progress(int percent);
    void finished(const Result &result);
    void cancelled();

private:
    std::atomic_bool m_cancelled{false};
};
```

三个坑：

- **信号跨线程默认排队**，传大对象会复制。用 `const Result &` 时要注册元类型，或者传 `std::shared_ptr`。
- **取消要能被检查到**，所以计算循环里必须有 `atomic` 标志或 `QThread::isInterruptionRequested()`。
- **进度不要刷太快**。每秒发一千次 `progress`，界面线程会被事件淹没。在计算侧节流。

## 9.6 渲染：把视口当成外来户

把自研渲染器塞进 Qt，有三条路线：

- `QOpenGLWidget`：最直接，自己管 VAO/VBO，适合 Qt 5 和中轻量渲染。
- `QRhi`：Qt 6 的渲染抽象层，能跑 Vulkan、Metal、D3D11、OpenGL，适合新项目。
- 第三方视口（VTK、Coin3D、OSG）：用它们提供的 Qt 控件，或者自己包一层 `QWindow`。

共同的坑是**上下文与事件**。多视图共享纹理要开 `Qt::AA_ShareOpenGLContexts`；高 DPI 下要处理 `devicePixelRatio`，否则线会糊；Qt 的事件系统和渲染库的交互器会抢鼠标，通常只保留一个。

## 9.7 一张模式表

| 问题 | 模式 | Qt 提供 | 你要做的 |
| --- | --- | --- | --- |
| 数据放哪 | 文档对象 + 树 | `QObject`、信号 | 稳定 ID、失效传播、序列化 |
| 怎么撤销 | 命令 + 合并 | `QUndoStack` | 所有修改走命令、粒度控制 |
| 怎么扩展 | 窄接口插件 | `QPluginLoader` | 版本化 IID、上下文对象 |
| 怎么自动化 | 脚本绑定 | `QJSEngine`、PySide | 稳定的脚本 API |
| 怎么不卡 | 工作线程 | `QThread`、信号 | 可取消、节流、生命周期 |
| 怎么渲染 | 视口组件 | `QOpenGLWidget`、`QRhi` | 上下文共享、DPR、事件归属 |

这些模式单独看都不复杂，难的是**同时成立**：撤销要能覆盖脚本发起的修改，插件要能安全地加命令，工作线程的结果要能进撤销栈。真正的架构能力，体现在这些交叉点上。
