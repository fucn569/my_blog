(function () {
  var e = document.body.parentElement,
    t = [],
    n = null,
    i = document.body.classList.contains("typora-export-collapse-outline"),
    r = function (e, t, n) {
      document.addEventListener(e, function (e) {
        if (!e.defaultPrevented)
          for (var i = e.target; i && i != this; i = i.parentNode)
            if (i.matches(t)) {
              !1 === n.call(i, e) && (e.preventDefault(), e.stopPropagation());
              break
            }
      }, !1)
    };

  function o() {
    return e.scrollTop
  }
  r("click", ".outline-expander", function (e) {
    var t = this.closest(".outline-item-wrapper").classList;
    return t.contains("outline-item-open") ? t.remove("outline-item-open") : t.add(
      "outline-item-open"), d(), !1
  }), r("click", ".outline-item", function (e) {
    var t = this.querySelector(".outline-label");
    if (location.hash = "#" + t.getAttribute("href"), i) {
      var n = this.closest(".outline-item-wrapper").classList;
      n.contains("outline-item-open") || n.add("outline-item-open"), c(), n.add(
        "outline-item-active")
    }
  });
  var a, s, l = function () {
      var e = o();
      n = null;
      for (var i = 0; i < t.length && t[i][1] - e < 60; i++) n = t[i]
    },
    c = function () {
      document.querySelectorAll(".outline-item-active").forEach(e => e.classList.remove(
        "outline-item-active")), document.querySelectorAll(
        ".outline-item-single.outline-item-open").forEach(e => e.classList.remove(
        "outline-item-open"))
    },
    d = function () {
      if (n) {
        c();
        var e = document.querySelector('.outline-label[href="#' + (CSS.escape ? CSS.escape(n[0]) :
          n[0]) + '"]');
        if (e)
          if (i) {
            var t = e.closest(".outline-item-open>ul>.outline-item-wrapper");
            if (t) t.classList.add("outline-item-active");
            else {
              for (var r = (e = e.closest(".outline-item-wrapper")).parentElement.closest(
                  ".outline-item-wrapper"); r;) r = (e = r).parentElement.closest(
                ".outline-item-wrapper");
              e.classList.add("outline-item-active")
            }
          } else e.closest(".outline-item-wrapper").classList.add("outline-item-active")
      }
    };
  window.addEventListener("scroll", function (e) {
    a && clearTimeout(a), a = setTimeout(function () {
      l(), d()
    }, 300)
  });
  var u = function () {
    s = setTimeout(function () {
      ! function () {
        t = [];
        var e = o();
        document.querySelector("#write").querySelectorAll("h1, h2, h3, h4, h5, h6")
          .forEach(n => {
            var i = n.getAttribute("id");
            t.push([i, e + n.getBoundingClientRect().y])
          })
      }(), l(), d()
    }, 300)
  };
  window.addEventListener("resize", function (e) {
    s && clearTimeout(s), u()
  }), u()
})();
