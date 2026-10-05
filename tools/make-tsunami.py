"""Generate assets/img/tsunami-surfboards.svg — the "AI is a tsunami; we build
surfboards with AI to ride it" illustration. Deterministic (seeded), so the
committed SVG is reproducible: python3 tools/make-tsunami.py"""
import math, random

random.seed(20261005)
W, H = 1600, 760
INK, PAPER, STONE = "#14140f", "#fefdfb", "#ededeb"
FOREST, COPPER, COPPER_L = "#434739", "#913d15", "#d9783f"
DEEP, MID, LIGHT, FOAM = "#0e2f44", "#1f618d", "#5fa8d3", "#f4f8fb"
SAND, SAND_D = "#e9dcc3", "#cdbb98"

def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
            u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1])

out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">')
a('<title id="t">Building surfboards to ride the wave</title>')
a('<desc id="d">A towering wave, its body made of letters, numerals, mathematical signs and code, '
  'curls over a calm sea. Small figures ride its face on copper surfboards. On the shore in the '
  'foreground, two people shape a new surfboard on trestles beside a glowing laptop, while a single '
  'candle burns on a crate: once-scarce intelligence beside an abundance arriving as a wave.</desc>')
a('<defs>')
a(f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{PAPER}"/>'
  f'<stop offset="1" stop-color="{STONE}"/></linearGradient>')
a(f'<linearGradient id="face" x1="0.15" y1="1" x2="0.75" y2="0"><stop offset="0" stop-color="{DEEP}"/>'
  f'<stop offset="0.55" stop-color="{MID}"/><stop offset="1" stop-color="{LIGHT}"/></linearGradient>')
a(f'<linearGradient id="barrel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{DEEP}"/>'
  f'<stop offset="1" stop-color="#174a6b"/></linearGradient>')
a(f'<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{MID}"/>'
  f'<stop offset="1" stop-color="{DEEP}"/></linearGradient>')
a(f'<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffe8b0" stop-opacity="0.95"/>'
  f'<stop offset="1" stop-color="#ffe8b0" stop-opacity="0"/></radialGradient>')
# wave body outline (used as clip for the symbol texture)
WAVE = ("M 430 620 C 640 612, 790 548, 880 440 C 960 340, 1010 210, 1130 150 "
        "C 1250 92, 1410 120, 1480 220 C 1540 305, 1545 420, 1600 470 L 1600 760 L 430 760 L 430 620 Z")
a(f'<clipPath id="waveclip"><path d="{WAVE}"/></clipPath>')
a('</defs>')

# sky + sun
a(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
a(f'<circle cx="300" cy="170" r="92" fill="{COPPER_L}" opacity="0.28"/>')
a(f'<circle cx="300" cy="170" r="60" fill="{COPPER_L}" opacity="0.35"/>')
# distant sea and swell lines
a(f'<path d="M 0 560 L 1600 560 L 1600 {H} L 0 {H} Z" fill="url(#sea)"/>')
# distant swells on the horizon (depth, and the wave's smaller kin)
for (cx, s) in [(150, 0.55), (395, 0.8)]:
    a(f'<g transform="translate({cx} 562) scale({s})">'
      f'<path d="M -120 0 C -60 -4, -20 -40, 20 -70 C 50 -92, 95 -88, 110 -60 C 85 -78, 55 -70, 45 -52 '
      f'C 38 -38, 52 -30, 62 -36 C 52 -22, 30 -22, 26 -40 C 10 -20, -20 -2, -40 0 Z" fill="{MID}"/>'
      f'<path d="M 20 -70 C 50 -92, 95 -88, 110 -60" fill="none" stroke="{FOAM}" stroke-width="5" stroke-linecap="round"/>'
      f'</g>')
for i in range(9):
    y = 568 + i * 9
    x0 = random.randint(-40, 200)
    d = f"M {x0} {y}"
    x = x0
    while x < 520:
        d += f" q 18 -6 36 0"
        x += 36
    a(f'<path d="{d}" fill="none" stroke="{FOAM}" stroke-width="1.6" opacity="{0.25 + 0.05*i:.2f}"/>')

# wave body
a(f'<path d="{WAVE}" fill="url(#face)"/>')
# symbol texture inside the wave: accumulated human symbols
glyphs = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + \
    ["∑", "∫", "π", "Δ", "λ", "θ", "∞", "≈", "√", "∂", "α", "β", "Ω", "{ }", "</>", "f(x)", "if", "for",
     "p<.05", "R²", "σ", "μ", "x̄", "→", "⊕", "≠", "∴", "§", "¶", "&", "#", "@", "%"]
a('<g clip-path="url(#waveclip)" font-family="Noto Sans Mono, Menlo, monospace" fill="#ffffff">')
for row in range(0, 24):
    y = 140 + row * 21
    x = 430 + (row % 2) * 9
    while x < 1600:
        g = random.choice(glyphs)
        size = random.choice([10, 11, 12, 13, 15, 18])
        op = random.uniform(0.05, 0.20)
        # brighter toward the crest
        op += max(0, (360 - y)) / 1400
        a(f'<text x="{x}" y="{y}" font-size="{size}" opacity="{min(op,0.42):.2f}">{g.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")}</text>')
        x += random.randint(26, 52) + len(g) * 6
a('</g>')

# the hollow inside the curl (the barrel), soft and translucent
a(f'<path d="M 1068 340 C 1110 330, 1135 292, 1125 252 C 1112 205, 1060 190, 1020 215 '
  f'C 1080 205, 1108 240, 1100 282 C 1094 312, 1080 330, 1068 340 Z" fill="{DEEP}" opacity="0.55"/>')
a(f'<path d="M 1068 340 C 1120 360, 1175 330, 1185 270 C 1192 225, 1170 190, 1130 175" fill="none" '
  f'stroke="{DEEP}" stroke-width="22" opacity="0.18" stroke-linecap="round"/>')
# the lip (curl) — lighter water
a(f'<path d="M 1130 150 C 1250 92, 1410 120, 1480 220 C 1420 168, 1300 150, 1215 178 '
  f'C 1120 210, 1050 255, 1035 300 C 1025 330, 1045 348, 1068 340 C 1040 372, 990 368, 975 330 '
  f'C 955 270, 1020 185, 1130 150 Z" fill="{LIGHT}"/>')

# foam claws along the lip (Hokusai fingers)
p0, p1, p2, p3 = (975, 330), (950, 230), (1120, 120), (1250, 105)
q0, q1, q2, q3 = (1250, 105), (1360, 95), (1450, 150), (1490, 225)
claws = []
for seg in [(p0, p1, p2, p3, 22), (q0, q1, q2, q3, 14)]:
    A, B, C, D, n = seg
    for k in range(n):
        t = (k + 0.5) / n
        x, y = bez(A, B, C, D, t)
        x2, y2 = bez(A, B, C, D, min(1, t + 0.01))
        ang = math.degrees(math.atan2(y2 - y, x2 - x))
        s = random.uniform(1.35, 2.1)
        claws.append((x, y, ang, s))
for (x, y, ang, s) in claws:
    a(f'<g transform="translate({x:.1f} {y:.1f}) rotate({ang - 90:.1f}) scale({s:.2f})">'
      f'<path d="M 0 0 c -9 -6 -16 -20 -8 -30 c 5 -6 14 -4 15 3 c -5 -3 -10 1 -8 6 '
      f'c 3 6 8 7 11 3 c -1 8 -3 14 -10 18 Z" fill="{FOAM}" stroke="#7fb3d5" stroke-width="1.1" stroke-linejoin="round"/>'
      f'<circle cx="-3" cy="-24" r="2.4" fill="{FOAM}" stroke="#7fb3d5" stroke-width="0.8"/></g>')
# a second, smaller row of claws just inside the first, and a foam edge
for (x, y, ang, s) in claws[::2]:
    a(f'<g transform="translate({x + 6:.1f} {y + 8:.1f}) rotate({ang - 70:.1f}) scale({s * 0.6:.2f})">'
      f'<path d="M 0 0 c -9 -6 -16 -20 -8 -30 c 5 -6 14 -4 15 3 c -5 -3 -10 1 -8 6 '
      f'c 3 6 8 7 11 3 c -1 8 -3 14 -10 18 Z" fill="{FOAM}" stroke="#7fb3d5" stroke-width="1.4" opacity="0.9"/></g>')
a(f'<path d="M 975 330 C 950 230, 1120 120, 1250 105 C 1360 95, 1450 150, 1490 225" fill="none" '
  f'stroke="{FOAM}" stroke-width="7" stroke-linecap="round" opacity="0.9"/>')
# spray dots
for _ in range(140):
    t = random.random()
    x, y = bez(q0, q1, q2, q3, t) if random.random() < 0.5 else bez(p0, p1, p2, p3, t)
    x += random.gauss(0, 18); y -= abs(random.gauss(14, 14))
    a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(1, 3.2):.1f}" fill="{LIGHT}" opacity="{random.uniform(0.35, 0.8):.2f}"/>')
# foam line along the wave base
a(f'<path d="M 430 620 C 640 612, 790 548, 880 440" fill="none" stroke="{FOAM}" stroke-width="5" opacity="0.7" stroke-linecap="round"/>')

def surfer(x, y, rot, scale=1.0, flip=False):
    sx = -scale if flip else scale
    a(f'<g transform="translate({x} {y}) rotate({rot}) scale({sx} {scale})">')
    # board
    a(f'<path d="M -46 6 C -30 -2, 30 -4, 50 2 C 34 10, -28 12, -46 6 Z" fill="{COPPER}"/>')
    a(f'<path d="M -30 5 L 34 3" stroke="#f3c9a5" stroke-width="1.2" stroke-dasharray="4 3"/>')
    # rider (crouched)
    a(f'<path d="M -10 2 L -2 -18 L 8 -2" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    a(f'<path d="M -2 -18 L 2 -38" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    a(f'<path d="M 0 -32 L -20 -26 M 1 -31 L 20 -38" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    a(f'<circle cx="3" cy="-46" r="6.5" fill="{INK}"/>')
    a('</g>')

surfer(805, 470, -32, 1.0)
surfer(905, 395, -48, 0.85)
surfer(720, 548, -18, 1.1)

# shore (foreground)
a(f'<path d="M 0 640 C 220 610, 420 620, 640 655 C 760 675, 820 700, 860 {H} L 0 {H} Z" fill="{SAND}"/>')
a(f'<path d="M 0 640 C 220 610, 420 620, 640 655 C 760 675, 820 700, 860 {H}" fill="none" stroke="{FOAM}" stroke-width="4" opacity="0.9"/>')
for _ in range(60):
    a(f'<circle cx="{random.uniform(10, 760):.0f}" cy="{random.uniform(660, 750):.0f}" r="1.3" fill="{SAND_D}"/>')

# workshop: two trestles + a board being shaped
a(f'<g stroke="{FOREST}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none">'
  f'<path d="M 252 704 L 270 664 L 288 704"/><path d="M 412 704 L 430 664 L 448 704"/>'
  f'<path d="M 260 688 L 280 688 M 420 688 L 440 688"/></g>')
a(f'<path d="M 230 660 C 280 646, 430 644, 480 656 C 440 668, 280 670, 230 660 Z" fill="{COPPER_L}"/>')
a(f'<path d="M 250 658 L 460 656" stroke="{PAPER}" stroke-width="1.4" opacity="0.8"/>')
# shaper 1 (planing)
a(f'<g stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none">'
  f'<path d="M 520 742 L 530 700 L 545 742"/><path d="M 530 700 L 520 660"/>'
  f'<path d="M 522 668 L 470 652 M 522 672 L 476 660"/></g>'
  f'<circle cx="518" cy="646" r="9" fill="{INK}"/>')
# shaper 2 (holding a tablet of glyphs)
a(f'<g stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none">'
  f'<path d="M 170 742 L 180 700 L 192 742"/><path d="M 180 700 L 186 660"/>'
  f'<path d="M 184 668 L 214 676 M 186 672 L 212 686"/></g>'
  f'<circle cx="188" cy="646" r="9" fill="{INK}"/>')
# laptop with a glow (the AI in the workshop)
a('<ellipse cx="610" cy="700" rx="60" ry="34" fill="url(#glow)"/>')
a(f'<path d="M 580 712 L 640 712 L 646 720 L 574 720 Z" fill="{FOREST}"/>')
a(f'<path d="M 584 712 L 588 680 L 636 680 L 632 712 Z" fill="{INK}"/>')
a(f'<path d="M 591 708 L 594 684 L 630 684 L 627 708 Z" fill="{LIGHT}"/>')
a(f'<text x="598" y="702" font-family="Noto Sans Mono, Menlo, monospace" font-size="11" fill="{PAPER}">{{ }}</text>')
# the candle on a crate: scarce intelligence
a(f'<rect x="60" y="690" width="56" height="40" fill="{SAND_D}" stroke="{FOREST}" stroke-width="2"/>')
a(f'<rect x="83" y="668" width="10" height="22" fill="{PAPER}" stroke="{FOREST}" stroke-width="1.5"/>')
a('<ellipse cx="88" cy="660" rx="16" ry="18" fill="url(#glow)"/>')
a(f'<path d="M 88 650 C 83 658, 84 664, 88 666 C 92 664, 93 658, 88 650 Z" fill="{COPPER_L}"/>')
a('</svg>')

open("assets/img/tsunami-surfboards.svg", "w").write("\n".join(out))
print("wrote assets/img/tsunami-surfboards.svg")
