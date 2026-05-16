from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, path):
    img = Image.new('RGB', (size, size), color='#0c0c0c')
    draw = ImageDraw.Draw(img)
    r = size * 0.22
    cx, cy = size / 2, size / 2
    pad = size * 0.28

    # Draw a stylized "C" corner bracket
    lw = max(4, size // 20)
    col = '#1D9E75'

    # Top-left bracket
    draw.rectangle([pad, pad, pad + r, pad + lw], fill=col)
    draw.rectangle([pad, pad, pad + lw, pad + r], fill=col)

    # Bottom-right bracket
    draw.rectangle([size - pad - r, size - pad - lw, size - pad, size - pad], fill=col)
    draw.rectangle([size - pad - lw, size - pad - r, size - pad, size - pad], fill=col)

    # Center dot
    dot_r = size * 0.06
    draw.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r], fill='#1D9E75')

    img.save(path)
    print(f"Saved {path}")

make_icon(192, '/home/claude/corner-roadmap/icon-192.png')
make_icon(512, '/home/claude/corner-roadmap/icon-512.png')
