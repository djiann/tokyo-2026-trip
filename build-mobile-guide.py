#!/usr/bin/env python3
"""Build self-contained mobile HTML with embedded map images."""
import base64
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
BUILD = ROOT / ".mobile-build"
SOURCE = ROOT / "tokyo-2026-guide-light.html"
OUTPUT = ROOT / "tokyo-2026-guide-mobile.html"

IMAGE_MAP = {
    "overview.png": "overview.png",
    "day-01.png": "day-01.png",
    "day-02.png": "day-02.png",
    "day-03.png": "day-03.png",
    "day-04.png": "day-04.png",
    "day-05.png": "day-05.png",
    "day-06.png": "day-06.png",
    "day-07.png": "day-07.png",
}

MOBILE_BANNER = """
<div id="mobile-open-help" class="mobile-open-help">
  <b>📱 iPhone 必讀（折疊打不開 = 開錯 App）</b><br>
  ① 檔案 App <b>長按</b>此檔 → <b>分享 → 在 Safari 中打開</b>（勿直接點檔名）<br>
  ② Safari 開啟後 → 下方 <b>分享 → 加入主畫面</b>（之後從桌面圖示開，最穩）<br>
  <span class="muted" style="font-size:12px">iOS 無法把本機 HTML 預設用 Safari 開，只能手動分享或加主畫面。</span>
</div>
<style>
.mobile-open-help{
  position:sticky;top:0;z-index:9999;
  background:#fff3cd;border-bottom:2px solid #e0b020;
  padding:12px 14px;font-size:13px;line-height:1.55;color:#5c4a00;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
}
.map-img{width:100%;max-width:480px;border-radius:16px;margin:16px auto;display:block;box-shadow:var(--shadow-lg)}
/* mobile: larger tap targets for collapsible sections */
details summary{
  display:block;min-height:48px;padding:14px 8px!important;
  -webkit-tap-highlight-color:rgba(58,143,159,.2);touch-action:manipulation;
  cursor:pointer;user-select:none;-webkit-user-select:none;
}
details summary::before{pointer-events:none}
details summary *{pointer-events:none}
</style>
<script>
(function(){
  function wireDetails(){
    document.querySelectorAll("details").forEach(function(d){
      var s=d.querySelector("summary");
      if(!s||s.dataset.wired)return;
      s.dataset.wired="1";
      s.addEventListener("click",function(e){
        e.preventDefault();
        d.open=!d.open;
      });
    });
  }
  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",wireDetails);
  }else{wireDetails();}
})();
</script>
"""


def compress_jpeg(src: Path, dest: Path, max_px: int = 720, quality: int = 82) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".tmp.png")
    subprocess.run(
        ["sips", "-Z", str(max_px), str(src), "--out", str(tmp)],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "sips",
            "-s",
            "format",
            "jpeg",
            "-s",
            "formatOptions",
            str(quality),
            str(tmp),
            "--out",
            str(dest),
        ],
        check=True,
        capture_output=True,
    )
    tmp.unlink(missing_ok=True)


def data_uri_jpeg(path: Path) -> str:
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{data}"


def prepare_images() -> dict[str, str]:
    uris: dict[str, str] = {}
    for html_name, asset_name in IMAGE_MAP.items():
        src = ASSETS / asset_name
        if not src.exists():
            raise FileNotFoundError(src)
        jpg_name = html_name.replace(".png", ".jpg")
        out = BUILD / jpg_name
        compress_jpeg(src, out)
        uris[html_name] = data_uri_jpeg(out)
        print(f"  {html_name}: {out.stat().st_size // 1024} KB (jpeg)")
    return uris


def patch_html(html: str, uris: dict[str, str]) -> str:
    for name, uri in uris.items():
        html = html.replace(f'src="assets/{name}"', f'src="{uri}"')

    # normalize inline img styles → class for smaller HTML
    html = re.sub(
        r'<img src="(data:image/jpeg;base64,[^"]+)" alt="([^"]+)" style="[^"]*"',
        r'<img class="map-img" src="\1" alt="\2"',
        html,
    )

    html = html.replace(
        '  🗺️ <b>冒險地圖</b>：開啟 <a href="journey-maps.html"><b>旅程地圖（8 張插畫風）</b></a>，可存 PNG 帶著走。<br>\n  📱 <b>存成 PDF</b>：手機用 Safari/Chrome 開此檔 → 分享/列印 → <b>「儲存為 PDF」</b>。電腦 <code>Cmd/Ctrl+P</code> → 目的地選 PDF。列印時所有折疊區塊會自動展開。',
        '  📱 <b>手機單檔版</b>：地圖已內嵌，可離線使用。請用 Safari / Chrome 開啟（見頂部黃色說明）。<br>\n  🗺️ <b>地圖</b>：各 Day 章節頂部有插畫地圖；目錄可點「總覽地圖」。',
    )
    html = html.replace(
        '<a href="journey-maps.html">🗺️ 冒險地圖</a>\n  ',
        '<a href="#map-overview">🗺️ 總覽地圖</a>\n  ',
    )

    overview_uri = uris["overview.png"]
    html = html.replace(
        f'<img class="map-img" src="{overview_uri}" alt="旅程總覽地圖"',
        f'<img id="map-overview" class="map-img" decoding="async" src="{overview_uri}" alt="旅程總覽地圖"',
    )
    html = html.replace(
        '<img class="map-img" src="',
        '<img class="map-img" loading="lazy" decoding="async" src="',
    )
    html = html.replace(
        '<img id="map-overview" class="map-img" loading="lazy" decoding="async"',
        '<img id="map-overview" class="map-img" decoding="async"',
    )

    html = html.replace(
        "<title>東京 7 日親子行 完整指南 2026/7/21–7/27（清新版）</title>",
        "<title>東京 7 日親子行 完整指南 2026/7/21–7/27（手機單檔版）</title>",
    )
    html = html.replace(
        "暗色原版：<code>tokyo-2026-guide.html</code>",
        "單檔版：下載後用 Safari / Chrome 開啟，可離線使用。",
    )
    html = html.replace("<body>", "<body>" + MOBILE_BANNER, 1)
    html = html.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0" />',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
        '<meta name="apple-mobile-web-app-capable" content="yes" />\n'
        '<meta name="apple-mobile-web-app-title" content="東京行程" />',
        1,
    )

    return html


def main() -> None:
    print("Preparing images...")
    uris = prepare_images()
    html = SOURCE.read_text(encoding="utf-8")
    html = patch_html(html, uris)
    OUTPUT.write_text(html, encoding="utf-8")
    size_mb = OUTPUT.stat().st_size / (1024 * 1024)
    print(f"Wrote {OUTPUT.name} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
