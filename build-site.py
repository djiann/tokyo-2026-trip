#!/usr/bin/env python3
"""Build static site in docs/ for GitHub Pages (Safari-friendly HTTPS link)."""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
ASSETS_SRC = ROOT / "assets"
MOBILE_SRC = ROOT / "tokyo-2026-guide-mobile.html"

WEB_BANNER_OLD = """<div id="mobile-open-help" class="mobile-open-help">
  <b>📱 iPhone 必讀（折疊打不開 = 開錯 App）</b><br>
  ① 檔案 App <b>長按</b>此檔 → <b>分享 → 在 Safari 中打開</b>（勿直接點檔名）<br>
  ② Safari 開啟後 → 下方 <b>分享 → 加入主畫面</b>（之後從桌面圖示開，最穩）<br>
  <span class="muted" style="font-size:12px">iOS 無法把本機 HTML 預設用 Safari 開，只能手動分享或加主畫面。</span>
</div>"""

WEB_BANNER_NEW = """<div id="mobile-open-help" class="mobile-open-help web-ok">
  <b>✅ 網頁版</b>：已用 Safari / Chrome 開啟，<b>折疊區塊可點擊</b>。<br>
  建議：Safari 下方 <b>分享 → 加入主畫面</b>，之後像 App 一樣開，日本當地也能用。
</div>"""

WEB_BANNER_STYLE = """
.web-ok{background:#e8f5ee!important;border-color:#2d8a62!important;color:#1a4a32!important}
"""

MAP_NAMES = [
    "overview.png",
    *(f"day-{day:02d}.png" for day in range(1, 8)),
]


def use_external_map_images(html: str) -> str:
    """GitHub Pages serves assets/ alongside HTML — use full-res PNG, not embedded JPEG."""
    for name in MAP_NAMES:
        html = re.sub(
            rf'(<a[^>]*href="assets/{re.escape(name)}"[^>]*>\s*<img[^>]*src=")data:image/[^"]+(")',
            rf"\1assets/{name}\2",
            html,
            count=1,
        )
        html = re.sub(
            rf'(<img id="map-overview"[^>]*src=")data:image/[^"]+(")',
            rf"\1assets/{name}\2",
            html,
            count=1,
        ) if name == "overview.png" else html
    html = html.replace(
        ".map-img{width:100%;max-width:480px;",
        ".map-link{display:block;line-height:0}.map-img{width:100%;max-width:960px;height:auto;",
    )
    return html


def run_mobile_build() -> None:
    subprocess.run([sys.executable, str(ROOT / "build-mobile-guide.py")], check=True)


def build_docs() -> None:
    run_mobile_build()

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    assets_dest = DOCS / "assets"
    assets_dest.mkdir()

    for name in [
        "overview.png",
        "day-01.png",
        "day-02.png",
        "day-03.png",
        "day-04.png",
        "day-05.png",
        "day-06.png",
        "day-07.png",
    ]:
        src = ASSETS_SRC / name
        if src.exists():
            shutil.copy2(src, assets_dest / name)

    mobile = MOBILE_SRC.read_text(encoding="utf-8")
    mobile = mobile.replace(WEB_BANNER_OLD, WEB_BANNER_NEW)
    mobile = mobile.replace("</style>\n<script>", WEB_BANNER_STYLE + "</style>\n<script>", 1)
    mobile = use_external_map_images(mobile)
    (DOCS / "index.html").write_text(mobile, encoding="utf-8")

    shutil.copy2(ROOT / "journey-maps.html", DOCS / "maps.html")
    shutil.copy2(ROOT / "tokyo-2026-guide-light.html", DOCS / "guide.html")

    # fix maps.html link to full guide on hosted site
    maps = (DOCS / "maps.html").read_text(encoding="utf-8")
    maps = maps.replace('href="tokyo-2026-guide-light.html"', 'href="guide.html"')
    (DOCS / "maps.html").write_text(maps, encoding="utf-8")

    guide = (DOCS / "guide.html").read_text(encoding="utf-8")
    guide = guide.replace('href="journey-maps.html"', 'href="maps.html"')
    (DOCS / "guide.html").write_text(guide, encoding="utf-8")

    print(f"Site ready: {DOCS}/")
    print("  index.html  ← 分享這個網址（同伴主入口）")
    print("  maps.html   ← 插畫地圖分頁")
    print("  guide.html  ← 完整指南（清新版）")


if __name__ == "__main__":
    build_docs()
