"""Update the loading animation to a refined kettle-pour SVG style and reduce scroll blur."""
import re

new_style_content = """/* Coffee Loader — Kettle Pour Animation */
#coffee-loader {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background-color: #faf8f5;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.6s ease;
}
.loader-svg .pour-stream {
  transform-origin: center top;
  opacity: 0;
  animation: streamPour 1.6s ease-in-out 0.2s forwards;
}
@keyframes streamPour {
  0%   { opacity: 0; transform: scaleY(0); }
  12%  { opacity: 0.9; transform: scaleY(1); }
  78%  { opacity: 0.9; transform: scaleY(1); }
  100% { opacity: 0; transform: scaleY(0.7); }
}
.loader-svg .coffee-fill {
  transform-origin: center bottom;
  transform: scaleY(0);
  animation: fillCup 1.6s ease-out 0.4s forwards;
}
@keyframes fillCup {
  0%   { transform: scaleY(0); }
  100% { transform: scaleY(1); }
}

/* Scroll Blur */
body {
  transition: filter 0.15s ease-out;
}"""

svg_html = '<svg class="loader-svg" viewBox="0 0 160 200" width="110" height="138" fill="none" xmlns="http://www.w3.org/2000/svg"><g transform="rotate(-22, 88, 48)"><polygon points="72,28 108,28 104,62 76,62" stroke="#c4b5ad" stroke-width="1.5" fill="none" stroke-linejoin="round"/><polygon points="82,28 98,28 95,19 85,19" stroke="#c4b5ad" stroke-width="1.5" fill="none" stroke-linejoin="round"/><path d="M76,48 Q66,48 66,56 L66,76" stroke="#c4b5ad" stroke-width="1.5" fill="none" stroke-linecap="round"/></g><ellipse class="pour-stream" cx="78" cy="95" rx="2" ry="14" fill="#3d271d"/><path d="M28,108 L28,158 Q28,178 52,178 L108,178 Q132,178 132,158 L132,108" stroke="#3d271d" stroke-width="2" fill="none" stroke-linecap="round"/><defs><clipPath id="cc"><path d="M29,108 L29,158 Q29,177 52,177 L108,177 Q131,177 131,158 L131,108 Z"/></clipPath></defs><rect class="coffee-fill" x="29" y="108" width="102" height="70" fill="#3d271d" opacity="0.85" clip-path="url(#cc)"/></svg>'

js_template = """document.addEventListener("DOMContentLoaded", () => {
  // Loader — Kettle Pour Animation
  const loader = document.createElement("div");
  loader.id = "coffee-loader";
  loader.innerHTML = 'SVGPLACEHOLDER';
  document.body.prepend(loader);

  setTimeout(() => {
    loader.style.opacity = "0";
    setTimeout(() => loader.remove(), 600);
  }, 2100);

  // Scroll Blur (subtle)
  let scrollTimeout;
  window.addEventListener('scroll', () => {
    document.body.style.filter = 'blur(1px)';
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
      document.body.style.filter = 'blur(0px)';
    }, 100);
  });
});"""

new_js_content = js_template.replace('SVGPLACEHOLDER', svg_html)

new_block = "<style>\n" + new_style_content + "\n</style>\n<script>\n" + new_js_content + "\n</script>"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the style block containing "Coffee Loader" followed by the script block
    pattern = r'<style>\s*/\* Coffee Loader.*?</style>\s*<script>\s*document\.addEventListener\("DOMContentLoaded".*?</script>'

    result, count = re.subn(pattern, new_block, content, flags=re.DOTALL)

    if count == 0:
        print(f"WARNING: No match found in {filepath}")
    else:
        print(f"Updated {count} block(s) in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)

update_file(r'c:\Users\admin\Documents\Wanderoot cafe\index.html')
update_file(r'c:\Users\admin\Documents\Wanderoot cafe\about.html')
print("Done!")
