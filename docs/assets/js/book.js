/* 书籍交互：阅读进度条 + 首页标记。
   与 Material 的 instant navigation 兼容：优先订阅 document$。 */

(function () {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function setupPage(root) {
    const doc = root || document;

    // 封面页标记：用于隐藏“上一章 / 下一章”
    document.body.classList.toggle("book-home", Boolean(doc.querySelector(".book-cover")));

    if (!doc.querySelector(".md-content")) return;
    if (document.querySelector(".book-progress")) return;

    const bar = document.createElement("div");
    bar.className = "book-progress";
    bar.setAttribute("aria-hidden", "true");
    document.body.appendChild(bar);

    let ticking = false;

    function update() {
      ticks: {
        const scrollable = document.documentElement.scrollHeight - window.innerHeight;
        const ratio = scrollable > 0 ? Math.min(1, Math.max(0, window.scrollY / scrollable)) : 0;
        bar.style.transform = "scaleX(" + ratio.toFixed(4) + ")";
      }
      ticking = false;
    }

    function onScroll() {
      if (ticking) return;
      ticking = true;
      if (reduceMotion) {
        update();
      } else {
        window.requestAnimationFrame(update);
      }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    update();
  }

  setupPage(document);

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(function (doc) {
      setupPage(doc);
    });
  }
})();
