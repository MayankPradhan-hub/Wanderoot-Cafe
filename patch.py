import os

code = """
<style>
/* Coffee Loader */
#coffee-loader {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background-color: #faf8f5;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.5s ease;
}
.cup {
  position: relative;
  width: 60px;
  height: 60px;
  border: 4px solid #3d271d;
  border-top: none;
  border-radius: 0 0 20px 20px;
  display: flex;
  align-items: flex-end;
  overflow: hidden;
}
.cup::after {
  content: "";
  position: absolute;
  top: 10px;
  right: -16px;
  width: 12px;
  height: 30px;
  border: 4px solid #3d271d;
  border-radius: 0 20px 20px 0;
}
.coffee {
  width: 100%;
  background-color: #3d271d;
  animation: fillCoffee 1.5s ease-out forwards;
}
.pour {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 4px;
  height: 100%;
  background-color: #3d271d;
  animation: pourCoffee 1.5s ease-in forwards;
}
@keyframes fillCoffee {
  0% { height: 0%; }
  100% { height: 90%; }
}
@keyframes pourCoffee {
  0% { transform: translateX(-50%) scaleY(0); transform-origin: top; }
  10% { transform: translateX(-50%) scaleY(1); transform-origin: top; }
  90% { transform: translateX(-50%) scaleY(1); transform-origin: top; }
  100% { transform: translateX(-50%) scaleY(0); transform-origin: bottom; }
}

/* Scroll Blur */
body {
  transition: filter 0.2s ease-out;
}
</style>
<script>
document.addEventListener("DOMContentLoaded", () => {
  // Loader
  const loader = document.createElement("div");
  loader.id = "coffee-loader";
  loader.innerHTML = '<div class="cup"><div class="coffee"></div><div class="pour"></div></div>';
  document.body.prepend(loader);
  
  setTimeout(() => {
    loader.style.opacity = "0";
    setTimeout(() => loader.remove(), 500);
  }, 1600);

  // Scroll Blur
  let scrollTimeout;
  window.addEventListener('scroll', () => {
    document.body.style.filter = 'blur(2px)';
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
      document.body.style.filter = 'blur(0px)';
    }, 100);
  });
});
</script>
</head>
"""

for file in ["index.html", "about.html"]:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    if "</head>" in content and "#coffee-loader" not in content:
        content = content.replace("</head>", code)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
