"""The site mascot: a 596 bus with eyes.

    python3 tools/bus.py            # writes a preview to bus-preview.html (not committed)

Two marks:
- bus_big(): the hero bus, a 3/4 axonometric view. Faces are drawn in their own flat 2D
  coordinates and mapped onto the box with an affine matrix, so the eyes, the 596 sign and the
  lights sit on the front face in perspective, and the pupils move in that face's plane.
- bus_small(): a flat front view for the header, footer, empty states and the favicon.

Both keep the owl's contract with main.js: an element with [data-owl] (its value = max pupil
travel in user units), a `.owl-pupils` group that follows the pointer and `.owl-lids` that blink.
"""
from __future__ import annotations

# ---------------------------------------------------------------- 3D box -> screen
# axes in screen units: back along the bus (left, up), across the front (right, up), up
U = (-0.80, -0.22)     # one unit of length toward the back
V = (0.96, -0.17)      # one unit of width, left -> right across the front
Y = (0.0, -1.0)        # one unit of height

L, W, H = 200, 104, 116          # bus length, width, height (stylised: a bit short and tall, friendly)
ORIGIN = (150, 236)              # screen position of the front-left-bottom corner


def P(x: float, z: float, y: float) -> tuple[float, float]:
    """3D point (x back, z across, y up) -> screen."""
    return (ORIGIN[0] + x * U[0] + z * V[0] + y * Y[0],
            ORIGIN[1] + x * U[1] + z * V[1] + y * Y[1])


def poly(*pts) -> str:
    return " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)


def matrix(o, ex, ey) -> str:
    """Affine map from a face's local 2D coords (x right, y down) to screen."""
    return f"matrix({ex[0]:.4f} {ex[1]:.4f} {ey[0]:.4f} {ey[1]:.4f} {o[0]:.2f} {o[1]:.2f})"


# front face: local x = 0..W (left -> right), local y = 0..H (top -> bottom)
FRONT = matrix(P(0, 0, H), V, (-Y[0], -Y[1]))
# left side face: local x = 0..L (back -> front), local y = 0..H (top -> bottom)
SIDE = matrix(P(L, 0, H), (-U[0], -U[1]), (-Y[0], -Y[1]))


def bus_big(cls: str = "bus-big") -> str:
    r = 10  # corner rounding on the face drawings
    side_face = poly(P(0, 0, 0), P(L, 0, 0), P(L, 0, H), P(0, 0, H))
    front_face = poly(P(0, 0, 0), P(0, W, 0), P(0, W, H), P(0, 0, H))
    roof = poly(P(0, 0, H), P(0, W, H), P(L, W, H), P(L, 0, H))

    # side: windows, door, a stripe and the route number, all in side-local coords
    door_x = L - 44                       # front door, just behind the front face
    win = "".join(
        f'<rect class="bus-glass" x="{x}" y="16" width="30" height="36" rx="5"/>'
        for x in range(10, door_x - 34, 38))
    wheel = lambda cx: (f'<g class="bus-wheel"><circle cx="{cx}" cy="{H}" r="17"/>'
                        f'<circle class="bus-hub" cx="{cx}" cy="{H}" r="6"/></g>')
    side = (f'<g transform="{SIDE}">'
            f'<path class="bus-roof-rim" d="M4 6H{L - 4}"/>'
            f'{win}'
            f'<rect class="bus-door" x="{door_x}" y="16" width="32" height="84" rx="5"/>'
            f'<path class="bus-door-line" d="M{door_x + 16} 20v76"/>'
            f'<path class="bus-stripe" d="M8 66H{door_x - 10}"/>'
            f'<text class="bus-side-num" x="{(door_x - 4) / 2:.0f}" y="94" text-anchor="middle">596</text>'
            f'{wheel(44)}{wheel(L - 70)}'
            f'</g>')

    # front: route sign with 596, windshield holding the eyes, lights and bumper
    eye_y = 47
    eyes_x = (30, 74)
    rings = "".join(f'<circle class="owl-eye bus-eye" cx="{x}" cy="{eye_y}" r="15.5"/>' for x in eyes_x)
    pupils = "".join(f'<circle class="owl-pupil" cx="{x}" cy="{eye_y + 1}" r="6.4"/>'
                     f'<circle class="bus-glint" cx="{x + 2.4}" cy="{eye_y - 1.8}" r="1.7"/>' for x in eyes_x)
    front = (f'<g transform="{FRONT}">'
             f'<rect class="bus-sign" x="14" y="5" width="76" height="20" rx="4"/>'
             f'<text class="bus-sign-num" x="52" y="21" text-anchor="middle">596</text>'
             f'<rect class="bus-windshield" x="8" y="29" width="88" height="38" rx="{r}"/>'
             f'<g class="owl-lids">{rings}</g>'
             f'<g class="owl-pupils">{pupils}</g>'
             f'<path class="bus-smile" d="M42 80q10 6 20 0"/>'
             f'<circle class="bus-light" cx="17" cy="84" r="6"/><circle class="bus-light" cx="87" cy="84" r="6"/>'
             f'<rect class="bus-bumper" x="6" y="96" width="92" height="10" rx="4"/>'
             f'</g>')

    # front wheels peek out under the front corners (on the side plane, at the front)
    xs = [p[0] for p in (P(0, 0, 0), P(L, 0, 0), P(L, 0, H), P(0, W, H), P(0, W, 0), P(L, W, H))]
    ys = [p[1] for p in (P(0, 0, 0), P(L, 0, 0), P(L, 0, H), P(0, W, H), P(0, W, 0), P(L, W, H))]
    pad = 26
    vb = f"{min(xs) - pad:.0f} {min(ys) - pad:.0f} {max(xs) - min(xs) + 2 * pad:.0f} {max(ys) - min(ys) + 2 * pad + 12:.0f}"
    shadow_c = P(L / 2, W / 2, 0)
    return (f'<svg class="{cls}" data-owl="5.5" viewBox="{vb}" fill="none" aria-hidden="true">'
            f'<ellipse class="bus-shadow" cx="{shadow_c[0]:.1f}" cy="{shadow_c[1] + 14:.1f}" rx="{L * 0.78:.0f}" ry="22"/>'
            f'<g class="bus-body">'
            f'<polygon class="bus-side" points="{side_face}"/>'
            f'<polygon class="bus-roof" points="{roof}"/>'
            f'<polygon class="bus-front" points="{front_face}"/>'
            f'{side}{front}'
            f'</g></svg>')


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
