import os
from PIL import Image, ImageDraw, ImageFont

def draw_rounded_rect(draw, xy, radius, fill):
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
    draw.pieslice([x0, y0, x0 + radius * 2, y0 + radius * 2], 180, 270, fill=fill)
    draw.pieslice([x1 - radius * 2, y0, x1, y0 + radius * 2], 270, 360, fill=fill)
    draw.pieslice([x0, y1 - radius * 2, x0 + radius * 2, y1], 90, 180, fill=fill)
    draw.pieslice([x1 - radius * 2, y1 - radius * 2, x1, y1], 0, 90, fill=fill)

def add_labels():
    base_img_path = "/Users/djiann/.cursor/projects/Users-djiann-VS-workspace-Travel/assets/overview_detailed.png"
    out_img_path = "/Users/djiann/VS_workspace/Travel/assets/overview.png"

    img = Image.open(base_img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)

    font_path = "/System/Library/Fonts/PingFang.ttc"
    if not os.path.exists(font_path):
        font_path = "/Library/Fonts/Arial Unicode.ttf"

    try:
        font_title = ImageFont.truetype(font_path, 42)
        font_day = ImageFont.truetype(font_path, 28)
        font_desc = ImageFont.truetype(font_path, 20)
    except:
        font_title = font_day = font_desc = ImageFont.load_default()

    labels = [
        {"day": "Day 1: 上野", "desc": "阿美橫町、不忍池、夏祭", "pos": (500, 400)},
        {"day": "Day 2: 橫濱八景島", "desc": "水族館、海島樂園", "pos": (50, 800)},
        {"day": "Day 3: 澀谷 & 新宿", "desc": "SKY夜景、寶可夢光雕秀", "pos": (100, 250)},
        {"day": "Day 4: 豐洲 & 葛西", "desc": "市場海鮮、teamLab", "pos": (620, 700)},
        {"day": "Day 5: 晴空塔 & 隅田川", "desc": "墨田水族館、花火大會", "pos": (600, 150)},
        {"day": "Day 6: 品川 & 新宿", "desc": "海豚秀、哥吉拉光雕", "pos": (150, 600)},
        {"day": "Day 7: 成田機場", "desc": "Skyliner 賦歸", "pos": (750, 50)},
    ]

    # Draw Title
    title = "🗼 東京 7 日親子行總覽"
    draw_rounded_rect(draw, [30, 30, 520, 100], 15, (255, 255, 255, 230))
    draw.text((50, 40), title, font=font_title, fill=(42, 50, 56, 255))

    for item in labels:
        x, y = item["pos"]
        day_text = item["day"]
        desc_text = item["desc"]

        # Calculate text size to draw background box
        bbox_day = draw.textbbox((0, 0), day_text, font=font_day)
        bbox_desc = draw.textbbox((0, 0), desc_text, font=font_desc)

        w = max(bbox_day[2], bbox_desc[2]) + 30
        h = bbox_day[3] + bbox_desc[3] + 40

        # Draw semi-transparent background
        draw_rounded_rect(draw, [x, y, x + w, y + h], 10, (255, 255, 255, 240))

        # Draw text
        draw.text((x + 15, y + 10), day_text, font=font_day, fill=(212, 86, 106, 255)) # accent color
        draw.text((x + 15, y + 15 + bbox_day[3]), desc_text, font=font_desc, fill=(107, 122, 136, 255)) # muted color

    img.convert("RGB").save(out_img_path)
    print(f"Saved detailed labeled map to {out_img_path}")

if __name__ == "__main__":
    add_labels()
