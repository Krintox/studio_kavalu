"""paperlib: the building blocks for Studio Kavalu's procedural paper (textures v3).

Everything here is periodic (wrap-around), so any tile built from it repeats with no seam:
  - spectral noise is synthesised in the Fourier domain of the tile itself;
  - blurs and gradients are circular (FFT / np.roll);
  - fibres are splatted with wrapped pixel indices;
  - domain warps sample with mode="grid-wrap".

Colour maths follows sRGB (IEC 61966-2-1), CIE Lab (D65) and CIEDE2000. The CSS blend modes are the
W3C Compositing Level 1 formulas, applied per channel to sRGB-encoded values, which is what browsers do.
"""
from __future__ import annotations

import numpy as np
from scipy import ndimage

# --------------------------------------------------------------------------------------------
# colour science
# --------------------------------------------------------------------------------------------

M_RGB2XYZ = np.array(
    [
        [0.4124564, 0.3575761, 0.1804375],
        [0.2126729, 0.7151522, 0.0721750],
        [0.0193339, 0.1191920, 0.9503041],
    ]
)
M_XYZ2RGB = np.linalg.inv(M_RGB2XYZ)
WHITE_D65 = np.array([0.95047, 1.0, 1.08883])
LUM = M_RGB2XYZ[1]  # relative-luminance weights for linear sRGB


def hex_to_rgb8(h: str) -> np.ndarray:
    h = h.lstrip("#")
    return np.array([int(h[i : i + 2], 16) for i in (0, 2, 4)], float)


def rgb8_to_hex(rgb) -> str:
    r, g, b = [int(round(float(np.clip(c, 0, 255)))) for c in rgb]
    return f"#{r:02X}{g:02X}{b:02X}"


def srgb_to_linear(v):
    v = np.asarray(v, float)
    return np.where(v <= 0.04045, v / 12.92, ((v + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(l):
    l = np.clip(np.asarray(l, float), 0.0, 1.0)
    return np.where(l <= 0.0031308, 12.92 * l, 1.055 * np.power(l, 1 / 2.4) - 0.055)


def _f(t):
    d = 6 / 29
    return np.where(t > d**3, np.cbrt(t), t / (3 * d * d) + 4 / 29)


def _finv(t):
    d = 6 / 29
    return np.where(t > d, t**3, 3 * d * d * (t - 4 / 29))


def linear_to_lab(lin):
    """lin: (..., 3) linear sRGB -> (..., 3) CIE Lab (D65)."""
    xyz = np.asarray(lin, float) @ M_RGB2XYZ.T
    fx, fy, fz = [_f(xyz[..., i] / WHITE_D65[i]) for i in range(3)]
    return np.stack([116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)], -1)


def lab_to_linear(lab):
    lab = np.asarray(lab, float)
    fy = (lab[..., 0] + 16) / 116
    fx = fy + lab[..., 1] / 500
    fz = fy - lab[..., 2] / 200
    xyz = np.stack([_finv(fx) * WHITE_D65[0], _finv(fy) * WHITE_D65[1], _finv(fz) * WHITE_D65[2]], -1)
    return xyz @ M_XYZ2RGB.T


def srgb8_to_lab(rgb8):
    return linear_to_lab(srgb_to_linear(np.asarray(rgb8, float) / 255.0))


def lstar_from_Y(Y):
    return 116 * _f(np.asarray(Y, float)) - 16


def Y_from_lstar(L):
    return _finv((np.asarray(L, float) + 16) / 116)


def delta_e76(lab1, lab2):
    return float(np.sqrt(np.sum((np.asarray(lab1) - np.asarray(lab2)) ** 2)))


def delta_e2000(lab1, lab2):
    """CIEDE2000 between two Lab colours (Sharma, Wu, Dalal 2005)."""
    L1, a1, b1 = [float(x) for x in lab1]
    L2, a2, b2 = [float(x) for x in lab2]
    C1, C2 = np.hypot(a1, b1), np.hypot(a2, b2)
    Cb = (C1 + C2) / 2
    G = 0.5 * (1 - np.sqrt(Cb**7 / (Cb**7 + 25**7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = np.hypot(a1p, b1), np.hypot(a2p, b2)
    h1p = np.degrees(np.arctan2(b1, a1p)) % 360
    h2p = np.degrees(np.arctan2(b2, a2p)) % 360
    dLp = L2 - L1
    dCp = C2p - C1p
    if C1p * C2p == 0:
        dhp = 0.0
    else:
        dhp = h2p - h1p
        if dhp > 180:
            dhp -= 360
        elif dhp < -180:
            dhp += 360
    dHp = 2 * np.sqrt(C1p * C2p) * np.sin(np.radians(dhp) / 2)
    Lbp = (L1 + L2) / 2
    Cbp = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hbp = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hbp = (h1p + h2p) / 2
    elif h1p + h2p < 360:
        hbp = (h1p + h2p + 360) / 2
    else:
        hbp = (h1p + h2p - 360) / 2
    T = (
        1
        - 0.17 * np.cos(np.radians(hbp - 30))
        + 0.24 * np.cos(np.radians(2 * hbp))
        + 0.32 * np.cos(np.radians(3 * hbp + 6))
        - 0.20 * np.cos(np.radians(4 * hbp - 63))
    )
    dtheta = 30 * np.exp(-(((hbp - 275) / 25) ** 2))
    Rc = 2 * np.sqrt(Cbp**7 / (Cbp**7 + 25**7))
    Sl = 1 + 0.015 * (Lbp - 50) ** 2 / np.sqrt(20 + (Lbp - 50) ** 2)
    Sc = 1 + 0.045 * Cbp
    Sh = 1 + 0.015 * Cbp * T
    Rt = -np.sin(np.radians(2 * dtheta)) * Rc
    return float(
        np.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2 + Rt * (dCp / Sc) * (dHp / Sh))
    )


def rel_luminance_srgb8(rgb8):
    """WCAG relative luminance of sRGB 8-bit colour(s), shape (..., 3)."""
    return srgb_to_linear(np.asarray(rgb8, float) / 255.0) @ LUM


def contrast_ratio(y1, y2):
    hi, lo = np.maximum(y1, y2), np.minimum(y1, y2)
    return (hi + 0.05) / (lo + 0.05)


# --------------------------------------------------------------------------------------------
# periodic fields
# --------------------------------------------------------------------------------------------


def kgrid(n: int):
    f = np.fft.fftfreq(n)  # cycles per pixel
    kx, ky = np.meshgrid(f, f)
    return kx, ky


def normalise(f):
    f = f - f.mean()
    s = f.std()
    return f / s if s > 0 else f


def gblur(field, sigma, aniso: float = 1.0):
    """Circular Gaussian blur (FFT). aniso > 1 keeps features longer along x."""
    if sigma <= 0:
        return field.copy()
    n = field.shape[0]
    kx, ky = kgrid(n)
    G = np.exp(-2 * np.pi**2 * sigma**2 * ((kx * aniso) ** 2 + ky**2))
    return np.fft.ifft2(np.fft.fft2(field) * G).real


def band_noise(n, rng, sigma, hp_wavelength=None, aniso=1.0):
    """Periodic Gaussian-filtered white noise, unit std. hp_wavelength (px) removes the very largest
    scales so a tile never carries a slow gradient that would show the repeat."""
    W = np.fft.fft2(rng.standard_normal((n, n)))
    kx, ky = kgrid(n)
    k2 = (kx * aniso) ** 2 + ky**2
    F = np.exp(-2 * np.pi**2 * sigma**2 * k2)
    if hp_wavelength:
        F = F * (1 - np.exp(-k2 * hp_wavelength**2))
    F[0, 0] = 0
    return normalise(np.fft.ifft2(W * F).real)


def warp(field, dx, dy, order=3):
    n = field.shape[0]
    yy, xx = np.mgrid[0:n, 0:n].astype(float)
    return ndimage.map_coordinates(field, [yy + dy, xx + dx], order=order, mode="grid-wrap")


def grad(field):
    """Periodic central differences (d/dx, d/dy)."""
    gx = (np.roll(field, -1, 1) - np.roll(field, 1, 1)) * 0.5
    gy = (np.roll(field, -1, 0) - np.roll(field, 1, 0)) * 0.5
    return gx, gy


def shade(height, light_deg=225.0):
    """Lambert-style relief term for a gentle height field, light from light_deg (225 = top-left,
    image y down). Positive where a slope faces the light."""
    gx, gy = grad(height)
    a = np.radians(light_deg)
    lx, ly = np.cos(a), np.sin(a)  # direction pointing toward the light
    return -(gx * lx + gy * ly)


def soft_knee(x, knee, limit):
    """Leave x below knee untouched; compress the part above knee smoothly toward limit."""
    x = np.asarray(x, float)
    over = np.maximum(x - knee, 0)
    span = limit - knee
    return np.where(x > knee, knee + span * np.tanh(over / span), x)


# --------------------------------------------------------------------------------------------
# fibres
# --------------------------------------------------------------------------------------------


def splat(n, x, y, w):
    """Bilinear splat with wrapped indices; returns (n, n)."""
    x0 = np.floor(x)
    y0 = np.floor(y)
    fx = x - x0
    fy = y - y0
    x0 = x0.astype(np.int64) % n
    y0 = y0.astype(np.int64) % n
    x1 = (x0 + 1) % n
    y1 = (y0 + 1) % n
    acc = np.zeros(n * n)
    for xi, yi, ww in (
        (x0, y0, (1 - fx) * (1 - fy)),
        (x1, y0, fx * (1 - fy)),
        (x0, y1, (1 - fx) * fy),
        (x1, y1, fx * fy),
    ):
        acc += np.bincount(yi * n + xi, weights=w * ww, minlength=n * n)
    return acc.reshape(n, n)


def fibres(
    n,
    rng,
    count,
    length_px=14.0,
    length_spread=0.45,
    length_range=(3.0, 90.0),
    bend=0.10,
    width_sigma=0.55,
    contrast=None,
    step=0.35,
    vis_mod=0.75,
    angle_kappa=0.0,
    density=None,
):
    """Render `count` thin, slightly curved, tapered fibres into a periodic field.

    Each fibre is a quadratic Bezier with a random bend; its strength fades in and out along its
    length (it dips under other fibres) and tapers at both ends. The cross-section is Gaussian
    (sigma = width_sigma px), normalised so a fibre's peak equals its contrast value.

    contrast: per-fibre signed strengths (array of len count) or None for +1.
    angle_kappa: 0 for fully random orientation; > 0 biases fibres toward the x (machine) direction.
    density: optional (n, n) non-negative map; fibre centres are drawn proportionally to it
             (flocculation).
    Returns (albedo, height): albedo carries the signed contrast, height is the unsigned body.
    """
    if count <= 0:
        z = np.zeros((n, n))
        return z, z.copy()
    if density is not None:
        p = density.ravel() / density.sum()
        cells = rng.choice(n * n, size=count, p=p)
        cy = (cells // n) + rng.uniform(0, 1, count)
        cx = (cells % n) + rng.uniform(0, 1, count)
    else:
        cx = rng.uniform(0, n, count)
        cy = rng.uniform(0, n, count)
    L = np.exp(rng.normal(np.log(length_px), length_spread, count))
    L = np.clip(L, *length_range)
    if angle_kappa > 0:
        th = rng.vonmises(0.0, angle_kappa, count) / 2.0  # axial: von Mises on 2*theta
    else:
        th = rng.uniform(0, np.pi, count)
    b = rng.normal(0, bend, count)
    c = np.ones(count) if contrast is None else np.asarray(contrast, float)

    m = np.maximum(3, np.ceil(L / step)).astype(np.int64)
    idx = np.repeat(np.arange(count), m)
    starts = np.cumsum(m) - m
    j = np.arange(m.sum()) - np.repeat(starts, m)
    t = (j + 0.5) / np.repeat(m, m)

    ux, uy = np.cos(th), np.sin(th)
    vx, vy = -uy, ux
    p0x, p0y = cx - L / 2 * ux, cy - L / 2 * uy
    p2x, p2y = cx + L / 2 * ux, cy + L / 2 * uy
    p1x, p1y = cx + b * L * vx, cy + b * L * vy
    T = t
    a0 = (1 - T) ** 2
    a1 = 2 * (1 - T) * T
    a2 = T**2
    x = a0 * p0x[idx] + a1 * p1x[idx] + a2 * p2x[idx]
    y = a0 * p0y[idx] + a1 * p1y[idx] + a2 * p2y[idx]

    taper = np.sin(np.pi * T) ** 0.6
    if vis_mod > 0:
        f = rng.uniform(0.3, 1.6, count)
        ph = rng.uniform(0, 1, count)
        v = 0.5 + 0.5 * np.sin(2 * np.pi * (f[idx] * T + ph[idx]))
        vis = (1 - vis_mod) + vis_mod * v**1.5
    else:
        vis = 1.0
    seg = (L / m)[idx]
    body = seg * taper * vis

    height = splat(n, x, y, body)
    albedo = splat(n, x, y, body * c[idx])
    # Gaussian cross-section; the bilinear splat itself adds about 0.4 px of blur
    s_eff = np.sqrt(width_sigma**2 + 0.4**2)
    norm = np.sqrt(2 * np.pi) * s_eff
    return gblur(albedo, width_sigma) * norm, gblur(height, width_sigma) * norm


def signed_strengths(rng, count, mean_abs, light_share=0.5, cap=None):
    """Exponentially distributed magnitudes (most fibres faint, a few clearer), random sign."""
    mag = rng.exponential(mean_abs, count)
    if cap is not None:
        mag = cap * np.tanh(mag / cap)
    sign = np.where(rng.uniform(0, 1, count) < light_share, 1.0, -1.0)
    return mag * sign


# --------------------------------------------------------------------------------------------
# CSS blend modes (W3C Compositing 1), per channel, values in [0, 1]
# --------------------------------------------------------------------------------------------


def blend_multiply(b, s):
    return b * s


def blend_screen(b, s):
    return b + s - b * s


def blend_overlay(b, s):
    return np.where(b <= 0.5, 2 * b * s, 1 - 2 * (1 - b) * (1 - s))


def blend_soft_light(b, s):
    d = np.where(b <= 0.25, ((16 * b - 12) * b + 4) * b, np.sqrt(b))
    return np.where(s <= 0.5, b - (1 - 2 * s) * b * (1 - b), b + (2 * s - 1) * (d - b))


BLENDS = {
    "multiply": blend_multiply,
    "screen": blend_screen,
    "overlay": blend_overlay,
    "soft-light": blend_soft_light,
}


def css_blend(base_rgb8, tile01, mode, opacity=1.0):
    """Simulate `background-color: base; background-image: tile; background-blend-mode: mode`
    (opacity < 1 = the same tile on a pseudo-element with mix-blend-mode and that opacity).
    tile01: (h, w) or (h, w, 3) in [0, 1]. Returns float sRGB 0..255, (h, w, 3)."""
    b = np.asarray(base_rgb8, float) / 255.0
    s = tile01 if tile01.ndim == 3 else tile01[..., None]
    out = BLENDS[mode](b[None, None, :], s)
    out = b + opacity * (out - b)
    return np.clip(out, 0, 1) * 255.0


# --------------------------------------------------------------------------------------------
# measurement
# --------------------------------------------------------------------------------------------


def mean_colour_report(img8, target_hex):
    """Mean colour of an image vs its target hex: the sRGB-encoded mean (what a downscale or a
    blurred eyedropper reads) and the linear-light mean (what the eye integrates at a distance)."""
    img = np.asarray(img8, float)[..., :3]
    tgt = hex_to_rgb8(target_hex)
    lab_t = srgb8_to_lab(tgt)
    m_srgb = img.reshape(-1, 3).mean(0)
    lin = srgb_to_linear(img / 255.0).reshape(-1, 3).mean(0)
    m_lin8 = linear_to_srgb(lin) * 255
    med = np.median(img.reshape(-1, 3), 0)
    out = {}
    for name, v in (("mean_srgb", m_srgb), ("mean_linear", m_lin8), ("median", med)):
        lab = srgb8_to_lab(v)
        out[name] = {
            "rgb": [round(float(c), 2) for c in v],
            "hex": rgb8_to_hex(v),
            "dE00": round(delta_e2000(lab_t, lab), 3),
            "dE76": round(delta_e76(lab_t, lab), 3),
        }
    L = linear_to_lab(srgb_to_linear(img / 255.0))[..., 0]
    out["L_std"] = round(float(L.std()), 3)
    out["L_p01_p99"] = [round(float(np.percentile(L, 1)), 2), round(float(np.percentile(L, 99)), 2)]
    out["L_target"] = round(float(lab_t[0]), 2)
    return out


def seam_score(tile):
    """Ratio of the mean absolute step across the wrap boundary to the mean step inside the tile
    (both axes). A seamless tile scores about 1.0; a visible seam scores well above it."""
    t = np.asarray(tile, float)
    if t.ndim == 3:
        t = t.mean(-1)
    inner_x = np.abs(np.diff(t, axis=1)).mean()
    inner_y = np.abs(np.diff(t, axis=0)).mean()
    edge_x = np.abs(t[:, 0] - t[:, -1]).mean()
    edge_y = np.abs(t[0, :] - t[-1, :]).mean()
    return round(float(edge_x / inner_x), 3), round(float(edge_y / inner_y), 3)


def seam_rank(tile):
    """Percentage of interior neighbour pairs (columns for x, rows for y) whose mean step is larger
    than the step across the wrap. A real seam sits far out in the tail (about 0 %); an invisible one
    lands among ordinary pairs. Robust where seam_score is not: lossy codecs make block edges step more
    than block interiors, so the plain ratio overstates a codec's wrap edge."""
    t = np.asarray(tile, float)
    if t.ndim == 3:
        t = t.mean(-1)
    cols = np.abs(np.diff(t, axis=1)).mean(0)
    rows = np.abs(np.diff(t, axis=0)).mean(1)
    wx = np.abs(t[:, 0] - t[:, -1]).mean()
    wy = np.abs(t[0, :] - t[-1, :]).mean()
    return round(float((cols > wx).mean() * 100), 1), round(float((rows > wy).mean() * 100), 1)
