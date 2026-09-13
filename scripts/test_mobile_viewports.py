#!/usr/bin/env python3
"""Geometry-only checks for the fixed 16:9 gameplay core inside common mobile viewports."""
from dataclasses import dataclass

ASPECT = 16 / 9
@dataclass(frozen=True)
class Case:
    name: str
    w: int
    h: int
    safe_l: int = 0
    safe_r: int = 0
    safe_t: int = 0
    safe_b: int = 0

CASES = [
    Case('Android compact 16:9', 640, 360),
    Case('iPhone 6/7/8 landscape', 667, 375),
    Case('iPhone Plus landscape', 736, 414),
    Case('Android 20:9 compact', 800, 360),
    Case('iPhone 12/13 landscape safe-area', 844, 390, 47, 47),
    Case('iPhone 14/15 landscape safe-area', 852, 393, 47, 47),
    Case('Android flagship 20:9', 915, 412),
    Case('iPhone Pro Max landscape safe-area', 932, 430, 59, 59),
    Case('iPad landscape', 1024, 768),
]

def fit(case: Case):
    aw = case.w - case.safe_l - case.safe_r
    ah = case.h - case.safe_t - case.safe_b
    assert aw > 0 and ah > 0
    if aw / ah >= ASPECT:
        ch = ah
        cw = ch * ASPECT
    else:
        cw = aw
        ch = cw / ASPECT
    x = case.safe_l + (aw - cw) / 2
    y = case.safe_t + (ah - ch) / 2
    return cw, ch, x, y

for c in CASES:
    cw, ch, x, y = fit(c)
    scale = ch / 720
    # 60 logical px + 14 px hit slop on both sides.
    effective_button = (60 + 28) * scale
    assert x >= c.safe_l - 1e-6
    assert y >= c.safe_t - 1e-6
    assert x + cw <= c.w - c.safe_r + 1e-6
    assert y + ch <= c.h - c.safe_b + 1e-6
    assert abs(cw / ch - ASPECT) < 1e-9
    assert cw >= 568 or c.name.startswith('iPad'), (c.name, cw)
    print(f'{c.name:38s} viewport={c.w}x{c.h} safe=({c.safe_l},{c.safe_r},{c.safe_t},{c.safe_b}) '
          f'canvas={cw:.1f}x{ch:.1f} offset=({x:.1f},{y:.1f}) button-hit≈{effective_button:.1f}px')
print('PASS:', len(CASES), 'viewport geometries')
