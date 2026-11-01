# 사용법: python3 make_icons.py 내이미지.png   (Pillow 필요: pip install pillow)
import sys
from PIL import Image
src = Image.open(sys.argv[1]).convert("RGBA")
side = min(src.size)
l, t = (src.width - side) // 2, (src.height - side) // 2
sq = src.crop((l, t, l + side, t + side))
for n in (192, 512):
    sq.resize((n, n), Image.LANCZOS).save(f"icons/icon-{n}.png")
bg = Image.new("RGBA", (512, 512), (10, 18, 13, 255))   # maskable: 안전영역(중앙 80%) 안에 배치
inner = sq.resize((360, 360), Image.LANCZOS)
bg.paste(inner, (76, 76), inner)
bg.save("icons/icon-maskable-512.png")
