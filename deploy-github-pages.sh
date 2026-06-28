#!/bin/bash
# 一鍵建置並推送到 GitHub Pages（首次請先建立 GitHub 空 repo）
set -euo pipefail
cd "$(dirname "$0")"

python3 build-site.py

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  git init
  git branch -M main
fi

git add docs/ build-site.py build-mobile-guide.py deploy-github-pages.sh .gitignore
git add tokyo-2026-guide-light.html tokyo-2026-guide.html journey-maps.html assets/
git status

echo ""
echo "=== 接下來（只需做一次）==="
echo "1. 到 https://github.com/new 建立 repo，例如：tokyo-2026-trip"
echo "2. 執行："
echo "   git remote add origin https://github.com/你的帳號/tokyo-2026-trip.git"
echo "   git commit -m \"Deploy Tokyo trip guide to GitHub Pages\""
echo "   git push -u origin main"
echo "3. GitHub repo → Settings → Pages → Source: Deploy from branch"
echo "   Branch: main  /  Folder: /docs"
echo "4. 等 1–2 分鐘，網址："
echo "   https://你的帳號.github.io/tokyo-2026-trip/"
echo ""
echo "把上面網址傳 Line 給同伴，點開即 Safari 網頁版。"
