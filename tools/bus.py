"""The site mascot: a 596 bus with eyes.

    python3 tools/bus.py            # writes a preview to bus-preview.html (not committed)

Two marks:
- bus_big(): the hero bus, a 3D box seen through an orthographic camera. Faces are drawn in
  their own flat 2D coordinates and mapped onto the box with affine matrices, so the eyes, the
  596 sign and the lights sit on the front face in perspective. The same projection runs live
  in main.js (busRig): the bus turns toward the pointer by changing the camera yaw/elevation.
  Python renders the rest pose, so the page looks right without JS or with motion off.
- bus_small(): a flat front view for the header, footer, empty states and the favicon.

Both keep the eye contract with main.js: [data-owl] (value = max pupil travel in user units),
a `.owl-pupils` group that follows the pointer and `.owl-lids` that blink.

Projection (must match busRig in main.js):
    U (one unit toward the back)  = (cos t, -sin t * sin e)
    V (one unit across the front) = (cos(t - 90°), -sin(t - 90°) * sin e)
    Y (one unit up)               = (0, -cos e)
    screen(x, z, y) = O + x*U + z*V + y*Y, with O chosen so the box centre lands on CENTER.
The left side and the front stay visible for 90° < t < 180°.
"""
from __future__ import annotations

import math

L, W, H = 220, 135, 116            # length, width, height (stylised: short, wide, tall = friendly)
YAW, ELEV = 135.0, 14.5            # rest pose, degrees
YAW_RANGE, ELEV_RANGE = (104.0, 166.0), (4.0, 28.0)   # what busRig may reach
CENTER = (0.0, 0.0)                # screen position of the box centre (viewBox is built around it)


def axes(t: float, e: float):
    t, e = math.radians(t), math.radians(e)
    s = math.sin(e)
    U = (math.cos(t), -math.sin(t) * s)
    V = (math.cos(t - math.pi / 2), -math.sin(t - math.pi / 2) * s)
    Y = (0.0, -math.cos(e))
    return U, V, Y


def projector(t: float, e: float):
    U, V, Y = axes(t, e)
    ox = CENTER[0] - (L / 2 * U[0] + W / 2 * V[0] + H / 2 * Y[0])
    oy = CENTER[1] - (L / 2 * U[1] + W / 2 * V[1] + H / 2 * Y[1])

    def P(x, z, y):
        return (ox + x * U[0] + z * V[0] + y * Y[0], oy + x * U[1] + z * V[1] + y * Y[1])
    return P, U, V, Y


def poly(pts) -> str:
    return " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)


def matrix(o, ex, ey) -> str:
    """Affine map from a face's local 2D coords (x right, y down) to screen."""
    return f"matrix({ex[0]:.4f} {ex[1]:.4f} {ey[0]:.4f} {ey[1]:.4f} {o[0]:.2f} {o[1]:.2f})"


def pose(t: float = YAW, e: float = ELEV) -> dict:
    """Everything that changes with the camera: face outlines and face matrices."""
    P, U, V, Y = projector(t, e)
    down = (-Y[0], -Y[1])
    return {
        "side": poly([P(0, 0, 0), P(L, 0, 0), P(L, 0, H), P(0, 0, H)]),
        "front": poly([P(0, 0, 0), P(0, W, 0), P(0, W, H), P(0, 0, H)]),
        "roof": poly([P(0, 0, H), P(0, W, H), P(L, W, H), P(L, 0, H)]),
        "side_m": matrix(P(L, 0, H), (-U[0], -U[1]), down),    # local x: back -> front
        "front_m": matrix(P(0, 0, H), V, down),                 # local x: left -> right
        "shadow": P(L / 2, W / 2, 0),
    }


def viewbox(pad: float = 30) -> str:
    """Fixed viewBox that holds the bus in every reachable pose, so turning never rescales it."""
    xs, ys = [], []
    for t in range(int(YAW_RANGE[0]), int(YAW_RANGE[1]) + 1, 2):
        for e in range(int(ELEV_RANGE[0]), int(ELEV_RANGE[1]) + 1, 2):
            P, *_ = projector(t, e)
            for x in (0, L):
                for z in (0, W):
                    for y in (0, H):
                        px, py = P(x, z, y)
                        xs.append(px); ys.append(py)
    w = max(xs) - min(xs) + 2 * pad
    h = max(ys) - min(ys) + 2 * pad + 20
    return f"{min(xs) - pad:.0f} {min(ys) - pad:.0f} {w:.0f} {h:.0f}"


def bus_big(cls: str = "bus-big") -> str:
    g = pose()
    door_x = L - 46                       # front door, just behind the front face
    win = "".join(
        f'<rect class="bus-glass" x="{x}" y="16" width="31" height="36" rx="5"/>'
        for x in range(10, door_x - 34, 39))
    wheel = lambda cx: (f'<g class="bus-wheel"><circle cx="{cx}" cy="{H}" r="18"/>'
                        f'<circle class="bus-hub" cx="{cx}" cy="{H}" r="6.5"/></g>')
    side = (f'<g class="bus-side-g" transform="{g["side_m"]}">'
            f'<path class="bus-roof-rim" d="M4 6H{L - 4}"/>'
            f'{win}'
            f'<rect class="bus-door" x="{door_x}" y="16" width="33" height="84" rx="5"/>'
            f'<path class="bus-door-line" d="M{door_x + 16.5} 20v76"/>'
            f'<path class="bus-stripe" d="M8 66H{door_x - 10}"/>'
            f'<text class="bus-side-num" x="{(door_x - 4) / 2:.0f}" y="94" text-anchor="middle">596</text>'
            f'{wheel(46)}{wheel(L - 74)}'
            f'</g>')
    # front face drawing, local coords 0..W x 0..H
    m = W / 2
    eye_y, eyes_x = 48, (m - 27, m + 27)
    rings = "".join(f'<circle class="owl-eye bus-eye" cx="{x}" cy="{eye_y}" r="18"/>' for x in eyes_x)
    pupils = "".join(f'<circle class="owl-pupil" cx="{x}" cy="{eye_y + 1}" r="7.4"/>'
                     f'<circle class="bus-glint" cx="{x + 2.8}" cy="{eye_y - 2}" r="2"/>' for x in eyes_x)
    front = (f'<g class="bus-front-g" transform="{g["front_m"]}">'
             f'<rect class="bus-sign" x="{m - 46}" y="5" width="92" height="21" rx="4"/>'
             f'<text class="bus-sign-num" x="{m}" y="21.5" text-anchor="middle">596</text>'
             f'<rect class="bus-windshield" x="10" y="29" width="{W - 20}" height="40" rx="10"/>'
             f'<g class="owl-lids">{rings}</g>'
             f'<g class="owl-pupils">{pupils}</g>'
             f'<path class="bus-smile" d="M{m - 11} 81q11 6.5 22 0"/>'
             f'<circle class="bus-light" cx="22" cy="85" r="7"/><circle class="bus-light" cx="{W - 22}" cy="85" r="7"/>'
             f'<rect class="bus-bumper" x="8" y="97" width="{W - 16}" height="10" rx="4"/>'
             f'</g>')
    sx, sy = g["shadow"]
    data = f'{L} {W} {H} {YAW} {ELEV} {YAW_RANGE[0]} {YAW_RANGE[1]} {ELEV_RANGE[0]} {ELEV_RANGE[1]}'
    return (f'<svg class="{cls}" data-owl="4" data-bus="{data}" viewBox="{viewbox()}" fill="none" aria-hidden="true">'
            f'<ellipse class="bus-shadow" cx="{sx:.1f}" cy="{sy + 16:.1f}" rx="{L * 0.62:.0f}" ry="24"/>'
            f'<g class="bus-rig"><g class="bus-body">'
            f'<polygon class="bus-side" points="{g["side"]}"/>'
            f'<polygon class="bus-roof" points="{g["roof"]}"/>'
            f'<polygon class="bus-front" points="{g["front"]}"/>'
            f'{side}{front}'
            f'</g></g></svg>')


def bus_small(cls: str = "logo-mark", eyes: bool = False) -> str:
    data = ' data-owl="2.2"' if eyes else ""
    return (f'<svg class="{cls}"{data} viewBox="0 0 64 64" fill="none" aria-hidden="true">'
            '<rect class="bus-s-body" x="9" y="6" width="46" height="48" rx="9"/>'
            '<path class="bus-s-sign" d="M20 13.5h24"/>'
            '<g class="owl-lids"><circle class="owl-eye" cx="23" cy="30" r="8"/><circle class="owl-eye" cx="41" cy="30" r="8"/></g>'
            '<g class="owl-pupils"><circle class="owl-pupil" cx="23" cy="30.5" r="3.4"/><circle class="owl-pupil" cx="41" cy="30.5" r="3.4"/></g>'
            '<path class="bus-s-line" d="M17 45h30"/>'
            '<path class="bus-s-wheel" d="M17 54v4M47 54v4"/>'
            '</svg>')


FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke-linecap="round" stroke-linejoin="round">'
           '<rect width="64" height="64" rx="16" fill="#0f131c"/>'
           '<rect x="9" y="6" width="46" height="48" rx="9" stroke="#e9e3d6" stroke-width="3.4"/>'
           '<path d="M20 13.5h24" stroke="#f2b35b" stroke-width="3.4"/>'
           '<circle cx="23" cy="30" r="8" stroke="#e9e3d6" stroke-width="3.4"/><circle cx="41" cy="30" r="8" stroke="#e9e3d6" stroke-width="3.4"/>'
           '<circle cx="23" cy="30.5" r="3.6" fill="#f2b35b"/><circle cx="41" cy="30.5" r="3.6" fill="#f2b35b"/>'
           '<path d="M17 45h30M17 54v4M47 54v4" stroke="#e9e3d6" stroke-width="3.4"/></svg>')


if __name__ == "__main__":
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    css = (root / "src/assets/css/main.css").read_text(encoding="utf-8")
    fonts = (root / "src/assets/css/fonts.css").read_text(encoding="utf-8").replace("../fonts/", "src/assets/fonts/")
    html = (f'<!doctype html><meta charset="utf-8"><style>{fonts}{css} body{{padding:40px;display:flex;gap:40px;align-items:center}}'
            f' .bus-big{{width:520px}}</style>{bus_big()}<div style="display:flex;gap:16px">{bus_small()}{bus_small("empty-owl", True)}</div>')
    (root / "bus-preview.html").write_text(html, encoding="utf-8")
    print("wrote bus-preview.html")
