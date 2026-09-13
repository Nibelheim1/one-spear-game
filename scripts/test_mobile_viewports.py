#!/usr/bin/env python3
"""Geometry checks for a fixed 1280x720 landscape stage on landscape and portrait phones."""
from dataclasses import dataclass
ASPECT=16/9
@dataclass(frozen=True)
class Case:
    name:str; w:int; h:int; safe_l:int=0; safe_r:int=0; safe_t:int=0; safe_b:int=0
CASES=[
    Case('Android compact landscape',640,360),
    Case('iPhone 12/13 landscape safe-area',844,390,47,47),
    Case('Android flagship landscape',915,412),
    Case('iPhone portrait 390x844',390,844,0,0,47,34),
    Case('iPhone Pro Max portrait 430x932',430,932,0,0,59,34),
    Case('Android portrait 412x915',412,915),
]
def landscape_fit(c):
    aw=c.w-c.safe_l-c.safe_r; ah=c.h-c.safe_t-c.safe_b
    if aw/ah>=ASPECT: ch=ah; cw=ch*ASPECT
    else: cw=aw; ch=cw/ASPECT
    return cw,ch

def portrait_rotated_fit(c):
    # CSS unrotated canvas width is constrained by physical safe height and by physical width*16/9.
    cw=min(c.h-c.safe_t-c.safe_b, c.w*ASPECT)
    ch=cw/ASPECT
    # after rotate(90deg), visual bounding box is ch x cw
    return ch,cw
for c in CASES:
    if c.h>c.w:
        vw,vh=portrait_rotated_fit(c)
        assert vw<=c.w+1e-6 and vh<=c.h+1e-6
        assert abs((vh/vw)-ASPECT)<1e-9
        print(f'{c.name:38s} viewport={c.w}x{c.h} rotated-visual={vw:.1f}x{vh:.1f}')
    else:
        vw,vh=landscape_fit(c)
        assert vw<=c.w+1e-6 and vh<=c.h+1e-6
        assert abs((vw/vh)-ASPECT)<1e-9
        print(f'{c.name:38s} viewport={c.w}x{c.h} canvas={vw:.1f}x{vh:.1f}')
print('PASS:',len(CASES),'fixed-landscape viewport geometries')
