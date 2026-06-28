# 🌍 旅程規劃與手繪地圖生成模板 (Travel & Map Prompt Template)

這是一份可重複使用的 AI 提示詞（Prompt）模板，分為「行程規劃」與「地圖繪製」兩階段。下次去不同國家或城市，直接複製並填入括號 `[...]` 中的資訊即可。

---

## 階段一：生成超詳細行程指南 (Text Generation)

**使用時機**：旅程初期，需要 AI 幫你排行程、找餐廳、抓預算時。
**提示詞 (Copy & Paste)**：

```text
請幫我規劃一份詳細的【[填入目的地，如：關西京阪神]】旅遊行程指南。

基本資訊：
- 天數：[填入天數，如：7天6夜]
- 日期：[填入日期，如：2026/11/01 - 11/07]
- 住宿地點：[填入住宿地，如：前三天住京都，後三天住大阪梅田]
- 旅遊成員：[填入成員，如：兩大一小，有推車]
- 必去景點/特殊需求：[填入必去，如：環球影城、清水寺、想吃和牛]

請產出一份結構完整的 Markdown 或 HTML 指南，必須包含以下區塊：
1. 行程總覽：每日主線行程與備案（B計畫）。
2. 每日詳細行程：包含景點停留時間、交通方式。
3. 飲食提案：每餐必須提供 3 個不同選項（含必吃名店與備案）。
4. 交通與票券分析：推薦最適合的交通卡或周遊券。
5. 行前準備：行李清單、天氣預報、預約提醒（如多久前要搶票）。
6. 雨天/緊急備案：如果下雨或遇到突發狀況的替代行程。
```

---

## 階段二：生成插畫風旅程地圖 (Image Generation)

**使用時機**：行程確定後，要用 AI 產出莫蘭迪色系、彩虹蜿蜒道路的可愛地圖時。

### 1. 總覽地圖 Prompt (Overview Map)
**提示詞 (建議直接用英文讓 AI 繪圖模型理解更好)**：
```text
A cute, minimalist travel overview map of [填入目的地] for a [填入天數]-day family trip. Flat vector style, Japanese travel guide aesthetic. Soft pastel tones like beige, light blue, and pale pink. Clean color blocks, no complex shading. Features tiny cute miniature icons for landmarks scattered around: [列出地標1], [列出地標2], [列出地標3]. Light beige background. NO TEXT, NO LABELS, NO WORDS. Relaxing, cute, and warm atmosphere, exactly like a Japanese travel magazine appendix map.
```

**風格說明**：
- **日系旅遊指南插畫風 (Japanese travel guide aesthetic / Flat vector style)**
- **扁平化向量 (Flat vector)**：沒有複雜的光影，色塊分明，看起來乾淨俐落。
- **柔和粉彩色調 (Soft pastel tones)**：使用米白、淺藍、淡粉紅等溫和的顏色，給人輕鬆、可愛、溫馨的感覺。
- **微縮地標圖示 (Tiny cute icons)**：用簡單可愛的小插圖來代表知名地標（例如晴空塔、摩天輪、鳥居等），很像日本旅遊雜誌或手冊裡常見的附錄地圖。

### 2. 繁中旅程路線圖 Prompt (Traditional Chinese Route Map)
**提示詞（適合產出含標題、DAY 站點、必吃清單與旅行小貼士的總覽圖）**：
```text
Create a polished illustrated travel route overview map in Traditional Chinese for a [填入目的地] [填入天數]-day family trip, based on a Japanese travel guide appendix style.

Canvas and style: landscape poster, cute minimalist flat vector, Japanese travel guide aesthetic, soft pastel palette, clean color blocks, warm beige background, light blue rivers, pale pink and mint accents, no complex shading. Overall tone coordinated, family-friendly, summer vacation mood.

Title area at the top in Traditional Chinese:
- Main title: 「[填入主標題，例如：東京 7 日親子深度行]」
- Subtitle: 「[填入副標，例如：上野住宿基地｜水族館・夏祭・花火・光雕秀・美食散策]」
Use large friendly rounded Traditional Chinese typography.

Main composition: draw one large winding gradient road, like a board game path, starting at [填入起點，例如：成田機場] and ending at [填入終點，例如：成田機場]. The road should snake across the whole map with a smooth gradient color from sky blue to mint green to peach pink to warm coral to represent trip progress. Add an airplane/train/transport icon at both start and finish. Add a small compass, clouds, sun, moon, sparkles, and a cute travel mascot with a suitcase.

Every day must be a large circular stop along the road, with different pastel theme colors and clearly readable labels in Traditional Chinese/English day format: 「DAY 1」, 「DAY 2」, 「DAY 3」... Inside or next to each circle, include tiny illustrated landmarks, Traditional Chinese place names, and a must-eat food icon.

Day station details:
DAY 1: label 「[Day1 區域/主題]」, illustrations: [Day1 主要景點插畫]. Food icon: [Day1 必吃美食小圖示]. Food label 「[Day1 必吃美食]」.
DAY 2: label 「[Day2 區域/主題]」, illustrations: [Day2 主要景點插畫]. Food icon: [Day2 必吃美食小圖示]. Food label 「[Day2 必吃美食]」.
DAY 3: label 「[Day3 區域/主題]」, illustrations: [Day3 主要景點插畫]. Food icon: [Day3 必吃美食小圖示]. Food label 「[Day3 必吃美食]」.
DAY 4: label 「[Day4 區域/主題]」, illustrations: [Day4 主要景點插畫]. Food icon: [Day4 必吃美食小圖示]. Food label 「[Day4 必吃美食]」.
DAY 5: label 「[Day5 區域/主題]」, illustrations: [Day5 主要景點插畫]. Food icon: [Day5 必吃美食小圖示]. Food label 「[Day5 必吃美食]」.
DAY 6: label 「[Day6 區域/主題]」, illustrations: [Day6 主要景點插畫]. Food icon: [Day6 必吃美食小圖示]. Food label 「[Day6 必吃美食]」.
DAY 7: label 「[Day7 區域/主題]」, illustrations: [Day7 主要景點插畫]. Food icon: [Day7 必吃美食小圖示]. Food label 「[Day7 必吃美食]」.

Side information panels:
Left side panel title: 「必吃美食清單」. Include cute illustrated icons and Traditional Chinese items, with dotted pastel connector lines to matching day circles: [列出每日必吃美食，例如：HARBS 千層蛋糕 to DAY 1, 海鮮 BBQ to DAY 2, 迴轉壽司 to DAY 3].

Right side panel title: 「必喝飲品＋旅行小貼士」. Include icons and Traditional Chinese bullets: [列出必喝飲品，例如：冰咖啡、抹茶拿鐵、便利商店冰飲], [列出旅行小貼士，例如：Suica 嗶卡最方便、防曬＋雨具必備、花火日先卡位].

Decoration along the road: small buildings, train tracks, torii gates, festival lanterns, local food icons, vending machine, cute clouds, summer sun, crescent moon, fireworks, waves, tiny family travelers. Each day uses a different pastel circle shade but feels harmonious. Make text legible and not crowded. Avoid any English labels except DAY 1 to DAY 7. No copyrighted characters or brand logos.
```

### 3. 每日行程地圖 Prompt (Daily Map)
**提示詞（每天替換 `[ ]` 內的景點與圖示）**：
```text
A hand-drawn kawaii illustration style travel journey map for DAY [填入天數, e.g., 1] in [填入目的地, e.g., Kyoto]. Morandi color palette, fresh and clean aesthetic. A winding rainbow gradient road with dashed branch lines for alternative routes. 

Stops along the road include: 
- [景點1英文] ([對應小圖示, e.g., temple])
- [景點2英文] ([對應小圖示, e.g., matcha ice cream])
- [景點3英文] ([對應小圖示, e.g., deer])

Traditional Chinese text labels. Sidebars with '必吃美食' (must-eat food) and '旅行小貼士' (travel tips). Decorations like compass, clouds, [選擇: sun/moon/stars/sunset], cute mascots. High quality, infographic style.
```

### 💡 AI 繪圖防翻車小貼士 (Tips for Image Gen)
1. **版權角色**：如果行程有迪士尼、寶可夢等版權 IP，AI 繪圖常會被阻擋（Safety Policy）。請將 Prompt 中的 `Pokemon` 改成 `cute monster`，`Disney` 改成 `fairy tale castle` 來繞過限制。
2. **文字亂碼**：AI 產生的繁體中文有時會變亂碼或簡體。如果要求極高，建議 Prompt 加上 `No text, only illustrations`（只產圖不產字），再自己用 Canva 或 Figma 壓上中文字。
3. **岔路表現**：關鍵字 `dashed branch lines for alternative routes` 能讓 AI 畫出虛線備案。
4. **色調控制**：關鍵字 `Morandi color palette` (莫蘭迪色) 與 `fresh and clean aesthetic` (清新質感) 是維持日系質感的靈魂。
