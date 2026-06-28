import os
from PIL import Image, ImageDraw, ImageFont

def add_labels():
    # Paths
    base_img_path = "/Users/djiann/.cursor/projects/Users-djiann-VS-workspace-Travel/assets/overview_base.png"
    out_img_path = "/Users/djiann/VS_workspace/Travel/assets/overview.png"
    
    # Load image
    img = Image.open(base_img_path)
    draw = ImageDraw.Draw(img)
    
    # Try to find a Chinese font on macOS
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf"
    ]
    
    font = None
    for path in font_paths:
        if os.path.exists(path):
            font = ImageFont.truetype(path, 48)
            break
            
    if not font:
        font = ImageFont.load_default()
        print("Warning: Could not find a suitable Chinese font. Text might not render correctly.")

    # Define labels and approximate coordinates (1024x1024 image)
    # Adjusting based on a typical schematic map
    labels = {
        "成田機場 (Day 1/7)": (750, 150),
        "晴空塔 (Day 5)": (650, 300),
        "上野 (住宿)": (550, 450),
        "豐洲 (Day 4)": (650, 650),
        "品川 (Day 6)": (450, 700),
        "澀谷 (Day 3)": (250, 550),
        "新宿 (Day 3/6)": (250, 350),
        "橫濱八景島 (Day 2)": (150, 850)
    }
    
    # Draw text with outline for better visibility
    outline_color = "white"
    text_color = "#2a3238" # dark ink color
    
    for text, (x, y) in labels.items():
        # Draw outline
        outline_width = 4
        for dx in range(-outline_width, outline_width+1):
            for dy in range(-outline_width, outline_width+1):
                draw.text((x+dx, y+dy), text, font=font, fill=outline_color)
        # Draw text
        draw.text((x, y), text, font=font, fill=text_color)
        
    # Save
    img.save(out_img_path)
    print(f"Saved labeled map to {out_img_path}")

if __name__ == "__main__":
    add_labels()
