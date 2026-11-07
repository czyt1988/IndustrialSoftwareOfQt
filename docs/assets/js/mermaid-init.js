/* Mermaid 图表渲染。
   页面里出现 `.mermaid` 时才按需加载本地 mermaid.min.js，正文页不背 2.7 MB
   的脚本；配色跟随 Material 的日间 / 夜间模式，切换主题后重绘一次。
   不引 CDN：脚本放在 assets/js/vendor/，随站点一起发布。 */

(function () {
  "use strict";

  var scriptUrl = document.currentScript ? document.currentScript.src : "";
  var vendorUrl = new URL("vendor/mermaid.min.js", scriptUrl).href;
  var loaded = false;
  var loading = false;
  var rendering = false;
  var rerender = false;
  var rerenderForce = false;

  var FONT =
    '"PingFang SC", "HarmonyOS Sans SC", "MiSans", "Source Han Sans SC", ' +
    '"Noto Sans CJK SC", "Microsoft YaHei UI", "Microsoft YaHei", "Segoe UI", sans-serif';

  var LIGHT = {
    fontFamily: FONT,
    fontSize: "15px",
    primaryColor: "#eef2f6",
    primaryTextColor: "#191d23",
    primaryBorderColor: "#2a4a68",
    secondaryColor: "#f4e3c8",
    secondaryTextColor: "#191d23",
    secondaryBorderColor: "#a9621b",
    tertiaryColor: "#f2eee6",
    tertiaryTextColor: "#3d444d",
    tertiaryBorderColor: "#cfc7b8",
    lineColor: "#6d747d",
    textColor: "#3d444d",
    mainBkg: "#eef2f6",
    nodeBorder: "#2a4a68",
    clusterBkg: "#fbf9f4",
    clusterBorder: "#e3ddd2",
    edgeLabelBackground: "#fbf9f4",
    actorBkg: "#eef2f6",
    actorBorder: "#2a4a68",
    actorTextColor: "#191d23",
    signalColor: "#3d444d",
    signalTextColor: "#3d444d",
    labelBoxBkgColor: "#f4e3c8",
    labelBoxBorderColor: "#a9621b",
    labelTextColor: "#191d23",
    noteBkgColor: "#f4e3c8",
    noteTextColor: "#191d23",
    noteBorderColor: "#a9621b",
    sectionBkgColor: "#f2eee6",
    altSectionBkgColor: "#fbf9f4",
    sectionBkgColor2: "#f2eee6",
    taskBkgColor: "#eef2f6",
    taskBorderColor: "#2a4a68",
    taskTextColor: "#191d23",
    activeTaskBkgColor: "#f4e3c8",
    activeTaskBorderColor: "#a9621b",
    gridColor: "#e3ddd2",
    doneTaskBkgColor: "#e3ddd2",
    doneTaskBorderColor: "#6d747d",
    critBorderColor: "#a9621b",
    critBkgColor: "#f4e3c8",
    todayLineColor: "#a9621b"
  };

  var DARK = {
    fontFamily: FONT,
    fontSize: "15px",
    primaryColor: "#1c2a36",
    primaryTextColor: "#e8e3d9",
    primaryBorderColor: "#8fb2d1",
    secondaryColor: "#3a2e1c",
    secondaryTextColor: "#e8e3d9",
    secondaryBorderColor: "#d79148",
    tertiaryColor: "#1a2027",
    tertiaryTextColor: "#c3c0b8",
    tertiaryBorderColor: "#39424c",
    lineColor: "#8d949c",
    textColor: "#c3c0b8",
    mainBkg: "#1c2a36",
    nodeBorder: "#8fb2d1",
    clusterBkg: "#12171d",
    clusterBorder: "#262d35",
    edgeLabelBackground: "#12171d",
    actorBkg: "#1c2a36",
    actorBorder: "#8fb2d1",
    actorTextColor: "#e8e3d9",
    signalColor: "#c3c0b8",
    signalTextColor: "#c3c0b8",
    labelBoxBkgColor: "#3a2e1c",
    labelBoxBorderColor: "#d79148",
    labelTextColor: "#e8e3d9",
    noteBkgColor: "#3a2e1c",
    noteTextColor: "#e8e3d9",
    noteBorderColor: "#d79148",
    sectionBkgColor: "#1a2027",
    altSectionBkgColor: "#12171d",
    sectionBkgColor2: "#1a2027",
    taskBkgColor: "#1c2a36",
    taskBorderColor: "#8fb2d1",
    taskTextColor: "#e8e3d9",
    activeTaskBkgColor: "#3a2e1c",
    activeTaskBorderColor: "#d79148",
    gridColor: "#262d35",
    doneTaskBkgColor: "#262d35",
    doneTaskBorderColor: "#8d949c",
    critBorderColor: "#d79148",
    critBkgColor: "#3a2e1c",
    todayLineColor: "#d79148"
  };

  function isDark() {
    return document.body.getAttribute("data-md-color-scheme") === "slate";
  }

  /* Mermaid 会把目标元素整个替换成 div，图源不能存在目标元素上，
     先套一层宿主节点，图源记在宿主上，换主题时才有东西可重绘。 */
  function ensureHosts() {
    Array.prototype.forEach.call(document.querySelectorAll(".book-mermaid"), function (node) {
      var host = node.closest(".mermaid-host");
      if (!host) {
        host = document.createElement("div");
        host.className = "mermaid-host";
        node.parentNode.insertBefore(host, node);
        host.appendChild(node);
      }
      if (!host.dataset.mermaidSource) {
        host.dataset.mermaidSource = node.textContent;
      }
    });
  }

  function hosts() {
    return Array.prototype.slice.call(document.querySelectorAll(".mermaid-host"));
  }

  function render(force) {
    if (rendering) {
      rerender = true;
      rerenderForce = rerenderForce || Boolean(force);
      return;
    }
    ensureHosts();
    var list = hosts();
    if (!force) {
      list = list.filter(function (host) {
        return !host.querySelector("svg");
      });
    }
    if (!list.length) return;

    var targets = [];
    list.forEach(function (host) {
      delete host.dataset.mermaidReady;
      var node = host.querySelector(".book-mermaid");
      if (!node) {
        node = document.createElement("pre");
        node.className = "book-mermaid";
        host.appendChild(node);
      }
      node.textContent = host.dataset.mermaidSource;
      node.removeAttribute("data-processed");
      targets.push(node);
    });

    window.mermaid.initialize({
      startOnLoad: false,
      securityLevel: "loose",
      theme: "base",
      themeVariables: isDark() ? DARK : LIGHT,
      flowchart: { curve: "basis", htmlLabels: true, useMaxWidth: true },
      sequence: { useMaxWidth: true, mirrorActors: false },
      class: { useMaxWidth: true },
      state: { useMaxWidth: true },
      gantt: { useMaxWidth: true },
      er: { useMaxWidth: true },
      journey: { useMaxWidth: true },
      quadrantChart: { useMaxWidth: true },
      timeline: { useMaxWidth: true },
      mindmap: { useMaxWidth: true }
    });

    rendering = true;
    var done = window.mermaid.run({ nodes: targets });

    function finish() {
      rendering = false;
      list.forEach(function (host) {
        if (host.querySelector("svg")) host.dataset.mermaidReady = "1";
      });
      if (rerender) {
        rerender = false;
        var forceNext = rerenderForce;
        rerenderForce = false;
        render(forceNext);
      }
    }

    if (done && typeof done.then === "function") {
      done.then(finish, function (err) {
        console.error("[mermaid]", err);
        finish();
      });
    } else {
      finish();
    }
  }

  function loadVendor() {
    if (window.mermaid || loading) {
      if (window.mermaid) render();
      return;
    }
    loading = true;
    var script = document.createElement("script");
    script.src = vendorUrl;
    script.async = true;
    script.onload = function () {
      loaded = true;
      loading = false;
      render();
    };
    script.onerror = function () {
      loading = false;
      console.error("[mermaid] 无法加载 " + vendorUrl);
    };
    document.head.appendChild(script);
  }

  function boot() {
    if (!document.querySelector(".book-mermaid")) return;
    if (window.mermaid) {
      if (hosts().some(function (host) { return !host.querySelector("svg"); })) render();
      return;
    }
    /* 等 window.load 之后再注入 Mermaid：它自身会在 load 事件里自动扫一遍
       .mermaid，如果脚本抢在 load 之前加载，两边会同时渲染同一批节点。 */
    if (document.readyState === "complete") {
      loadVendor();
    } else {
      window.addEventListener("load", loadVendor, { once: true });
    }
  }

  boot();

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(boot);
  }

  var scheme = isDark();
  new MutationObserver(function () {
    if (!loaded) return;
    if (scheme === isDark()) return;
    scheme = isDark();
    render(true);
  }).observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"]
  });
})();






