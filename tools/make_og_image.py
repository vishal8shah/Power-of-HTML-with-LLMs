#!/usr/bin/env python3
"""Build-time generator for assets/og-image.png (1200x630 LinkedIn/OG card).

Not referenced by any page at runtime. Re-run after changing the title:
    python3 tools/make_og_image.py
Requires Pillow and the DejaVu fonts shipped with most Linux distributions.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1200, 630
INK = (22, 32, 46)        # --ink
DARK_TEXT = (232, 237, 244)
DARK_SOFT = (159, 176, 195)
M365 = (61, 90, 219)      # --lens-m365
GH = (14, 124, 107)       # --lens-gh
HONEST = (255, 246, 232)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
bold = lambda s: ImageFont.truetype(str(FONT_DIR / "DejaVuSans-Bold.ttf"), s)
sans = lambda s: ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), s)
mono = lambda s: ImageFont.truetype(str(FONT_DIR / "DejaVuSansMono.ttf"), s)

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# top hairline gradient bar: indigo -> teal
for x in range(W):
    t = x / W
    c = tuple(round(M365[i] + (GH[i] - M365[i]) * t) for i in range(3))
    d.line([(x, 0), (x, 10)], fill=c)

x = 84
d.text((x, 96), "POWER-OF-HTML/ENTERPRISE", font=mono(22), fill=DARK_SOFT)

d.text((x, 160), "The artifact is the demo —", font=bold(64), fill=DARK_TEXT)
d.text((x, 240), "HTML in the enterprise", font=bold(64), fill=DARK_TEXT)

# twin underline bars
d.rectangle([x, 340, x + 210, 352], fill=M365)
d.rectangle([x + 222, 340, x + 432, 352], fill=GH)

d.text((x, 396), "13 self-contained HTML artifacts for M365 Copilot and", font=sans(30), fill=DARK_SOFT)
d.text((x, 440), "GitHub Copilot users in a governed enterprise.", font=sans(30), fill=DARK_SOFT)

d.text((x, 530), "Every claim demonstrated live or cited  ·  0 external requests  ·  works from file://",
       font=mono(21), fill=DARK_SOFT)

out = Path(__file__).resolve().parent.parent / "assets" / "og-image.png"
out.parent.mkdir(exist_ok=True)
img.save(out, "PNG")
print(f"wrote {out} ({out.stat().st_size} bytes)")
