"""Apply the site's "Aberasi" filter (haze palette + radial chromatic aberration) to an image.

Usage: python tools/haze.py input.jpg output.jpg WIDTH HEIGHT [crop_center_y 0..1]
Mirrors HAZE_LUT and applyFilter() in public/index.html.
"""
import sys
import numpy as np
from PIL import Image

STOPS = [(0.00, (128, 54, 6)), (0.45, (234, 124, 18)), (0.75, (250, 168, 36)), (1.00, (255, 218, 112))]
KEEP, ABERRATION, VIGNETTE, GRAIN = 0.1, 0.024, 0.25, 18


def lut():
    t = np.linspace(0, 1, 256)
    xs = [s[0] for s in STOPS]
    return np.stack([np.interp(t, xs, [s[1][c] for s in STOPS]) for c in range(3)], axis=1)


def cover_crop(im, w, h, cy):
    scale = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    top = int(min(max(cy * im.height - h / 2, 0), im.height - h))
    left = (im.width - w) // 2
    return im.crop((left, top, left + w, top + h))


def main():
    src, dst, w, h = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    cy = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5
    im = cover_crop(Image.open(src).convert("RGB"), w, h, cy)
    a = np.asarray(im).astype(np.float32)

    l = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]) / 255
    l = 0.12 + l * 0.8
    tone = lut()[(l * 255).astype(np.int32)] * (1 - KEEP) + a * KEEP

    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    half = min(w, h) / 2
    dx, dy = (xs - w / 2) / (w / 2), (ys - h / 2) / (h / 2)
    d2 = dx * dx + dy * dy
    shift = half * 2 * ABERRATION
    ox, oy = dx * d2 * shift, dy * d2 * shift
    rx = np.clip(xs - ox, 0, w - 1).astype(np.int32); ry = np.clip(ys - oy, 0, h - 1).astype(np.int32)
    bx = np.clip(xs + ox, 0, w - 1).astype(np.int32); by = np.clip(ys + oy, 0, h - 1).astype(np.int32)
    out = np.stack([tone[ry, rx, 0], tone[..., 1], tone[by, bx, 2]], axis=-1)

    v = 1 - np.minimum(1, d2) * VIGNETTE
    g = (np.random.default_rng(7).random((h, w)) - 0.5) * GRAIN
    out = out * v[..., None] + g[..., None]
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(dst, quality=90)


if __name__ == "__main__":
    main()
