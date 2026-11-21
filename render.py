#!/usr/bin/env python3
"""Render the Friday 20 November 2026 front page, entry.png (1024x1024).

Drawn from scratch with Pillow. All stories are from the verified
stories file: events that happened, or were first reported, on
Friday 20 November 2026. Deterministic output: same bytes every run.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
CREAM = (247, 242, 228)
NAVY = (21, 37, 73)
NAVY2 = (28, 52, 96)
GOLD = (195, 154, 43)
RED = (179, 39, 30)
INK = (26, 26, 26)
GREY = (107, 107, 107)
LINE = (180, 172, 150)
SEA = (207, 227, 238)
LAND = (232, 222, 196)

FD = "/usr/share/fonts/truetype/dejavu"
SERIF = os.path.join(FD, "DejaVuSerif.ttf")
SERIF_B = os.path.join(FD, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FD, "DejaVuSans.ttf")
SANS_B = os.path.join(FD, "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading=None):
    """Draw lines of text; returns the y below the block."""
    lh = leading or int(fnt.size * 1.22)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def section_bar(draw, y, label, right=""):
    """Navy section header bar with a label and optional right note."""
    draw.rectangle([0, y, W, y + 26], fill=NAVY)
    draw.text((10, y + 5), label, font=font(SANS_B, 15), fill=(255, 255, 255))
    if right:
        rw = draw.textlength(right, font=font(SANS, 12))
        draw.text((W - 10 - rw, y + 7), right, font=font(SANS, 12),
                  fill=(200, 205, 220))


img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 116], fill=NAVY)
d.rectangle([0, 116, W, 119], fill=GOLD)
d.text((16, 10), "THE WORLD IN ONE DAY  ·  FRIDAY EDITION",
       font=font(SANS_B, 14), fill=GOLD)
d.text((16, 28), "Friday 20 November 2026",
       font=font(SERIF_B, 58), fill=(250, 248, 240))
d.text((16, 92), "Kyiv's bridges hit  ·  Cyclone Akvan ashore  ·  Asia's markets plunge",
       font=font(SERIF, 19), fill=(215, 220, 232))
d.text((W - 16 - d.textlength("36 STORIES", font=font(SANS_B, 15)), 12),
       "36 STORIES", font=font(SANS_B, 15), fill=GOLD)

# ------------------------------------------------------- five-moments band
y = 119
d.text((10, y + 2), "FRIDAY IN FIVE MOMENTS",
       font=font(SANS_B, 13), fill=NAVY)
moments = [
    ("OVERNIGHT", "KYIV", "Bridges hit in the barrage"),
    ("MORNING", "GOPALPUR", "Akvan landfall begins"),
    ("MIDDAY", "BRUSSELS", "UK\u2013EU deal sealed"),
    ("EVENING", "JUN\u00cdN, PERU", "6.7 quake, 7:09 pm"),
    ("LATE", "ANTALYA", "COP31 talks run over"),
]
col_w = (W - 20) // 5
for i, (when, place, what) in enumerate(moments):
    x = 10 + i * col_w
    d.text((x, y + 20), when, font=font(SANS_B, 12), fill=RED)
    d.text((x, y + 36), place, font=font(SANS_B, 13), fill=INK)
d.line([0, 172, W, 172], fill=LINE, width=1)

# ---------------------------------------------------------------- stat strip
stats = [
    ("400+", "DRONES FIRED"),
    ("110+", "MISSILES"),
    ("372,000", "EVACUATED"),
    ("\u22123.7%", "S&P 500"),
    ("100,000", "YOUTH VISAS / YR"),
    ("6.7", "PERU QUAKE"),
]
sy = 176
box_w = (W - 20) // 6
for i, (num, lab) in enumerate(stats):
    x = 10 + i * box_w
    d.rectangle([x, sy, x + box_w - 6, sy + 44], outline=LINE, width=1)
    nw = d.textlength(num, font=font(SANS_B, 20))
    d.text((x + (box_w - 6 - nw) / 2, sy + 3), num,
           font=font(SANS_B, 20), fill=NAVY)
    lw = d.textlength(lab, font=font(SANS, 10))
    d.text((x + (box_w - 6 - lw) / 2, sy + 27), lab,
           font=font(SANS, 10), fill=GREY)


# ------------------------------------------------------------- hero panels
def draw_kyiv(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(16, 24, 52))
    # stars / missile trails
    for (tx, ty, ln) in [(18, 22, 34), (52, 12, 40), (92, 30, 30)]:
        d.line([x + tx, y + ty, x + tx + ln, y + ty + ln // 2],
               fill=(255, 220, 120), width=2)
        d.ellipse([x + tx - 2, y + ty - 2, x + tx + 2, y + ty + 2],
                  fill=(255, 240, 180))
    # river
    d.rectangle([x, y + s - 26, x + s, y + s], fill=(52, 84, 130))
    # three bridge arches
    for cx in (28, 70, 112):
        d.arc([x + cx - 20, y + s - 58, x + cx + 20, y + s - 18],
              180, 360, fill=(240, 240, 235), width=3)
        d.line([x + cx - 20, y + s - 38, x + cx + 20, y + s - 38],
               fill=(240, 240, 235), width=2)
    # blast flashes on the middle span
    d.ellipse([x + 62, y + s - 66, x + 78, y + s - 50], fill=(255, 150, 40))
    d.ellipse([x + 66, y + s - 62, x + 74, y + s - 54], fill=(255, 230, 120))


def draw_akvan(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(178, 214, 232))
    d.rectangle([x, y + s - 30, x + s, y + s], fill=(222, 205, 160))
    cx, cy = x + s // 2, y + s // 2 - 6
    for r in (52, 40, 28, 16):
        d.arc([cx - r, cy - r, cx + r, cy + r], 20, 300,
              fill=(255, 255, 255), width=5)
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(21, 37, 73))
    d.line([x, y + s - 30, x + s, y + s - 30], fill=(140, 160, 120), width=2)


def draw_markets(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(255, 255, 255))
    for gy in range(0, s, 28):
        d.line([x, y + gy, x + s, y + gy], fill=(232, 232, 232), width=1)
    pts = [(8, 26), (32, 40), (54, 34), (78, 62), (100, 78), (124, 108)]
    pts = [(x + px, y + py) for px, py in pts]
    d.line(pts, fill=RED, width=4)
    for px, py in pts:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED)
    d.text((x + 8, y + s - 22), "-5.06%", font=font(SANS_B, 14), fill=RED)


def draw_mercury(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(10, 10, 16))
    for (sx, sy) in [(14, 18), (44, 8), (120, 22), (96, 10), (130, 48)]:
        d.ellipse([x + sx, y + sy, x + sx + 2, y + sy + 2], fill=(255, 255, 255))
    cx, cy, r = x + 74, y + 82, 46
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(168, 162, 150))
    for (ox, oy, orad) in [(-18, -12, 9), (12, 6, 12), (-4, 18, 7), (22, -18, 6)]:
        d.ellipse([cx + ox - orad, cy + oy - orad, cx + ox + orad, cy + oy + orad],
                  fill=(140, 134, 122))
    # small craft above the planet
    d.rectangle([x + 96, y + 16, x + 116, y + 26], fill=(200, 200, 200))
    d.line([x + 96, y + 21, x + 84, y + 21], fill=(200, 200, 200), width=3)
    d.line([x + 116, y + 21, x + 128, y + 21], fill=(200, 200, 200), width=3)


HEROES = [
    ("WAR IN UKRAINE", "Missiles rain on Kyiv's bridges",
     "Three Dnipro crossings hit in an overnight barrage of 400+ drones and "
     "110+ missiles. Eight killed across Ukraine; power and water cut in the capital.",
     "Kyiv Independent", draw_kyiv),
    ("CYCLONE AKVAN", "Akvan comes ashore, spares lives",
     "About 372,000 moved to shelters as the storm crosses Odisha at 70\u201380 km/h. "
     "No deaths reported as it weakens to a depression.",
     "New Indian Express", draw_akvan),
    ("MARKETS", "AI sell-off drags markets down",
     "The S&P 500 falls 3.7% into correction and the Nikkei drops 5.06% as "
     "worries over AI spending hit shares.",
     "One Turn News", draw_markets),
    ("SPACE", "Mercury: almost there",
     "After eight years and six billion miles, the European\u2013Japanese mission "
     "closes in on the innermost planet; thrusters fire Saturday to enter "
     "orbit \u2014 tonight is the eve of arrival.",
     "ESA", draw_mercury),
]

hy = 224
for hi, (kick, head, deck, src, painter) in enumerate(HEROES):
    hx = 10 + (hi % 2) * 502
    hyy = hy + (hi // 2) * 140
    painter(d, hx, hyy, 140)
    tx = hx + 150
    d.text((tx, hyy + 2), kick, font=font(SANS_B, 12), fill=RED)
    yy = text_block(d, tx, hyy + 20,
                    wrap(d, head, font(SERIF_B, 19), 352),
                    font(SERIF_B, 19), INK)
    yy = text_block(d, tx, yy + 2,
                    wrap(d, deck, font(SANS, 12), 352),
                    font(SANS, 12), INK)
    d.text((tx, hyy + 126), src, font=font(SANS, 11), fill=GREY)
    if hi % 2 == 0:
        d.line([hx + 496, hyy, hx + 496, hyy + 140], fill=LINE, width=1)
d.line([0, 508, W, 508], fill=LINE, width=1)

# ------------------------------------------------------------ the day's ten
section_bar(d, 512, "THE DAY'S TEN", "SOURCES TAGGED ON EVERY STORY")
TEN = [
    ("TWO RUSSIAN MISSILES LAND IN POLAND",
     "Kh-101s down in a field; NATO jets scrambled",
     "People's Daily Online"),
    ("UK\u2013EU RESET SEALED",
     "Food pact \u00a35.1bn/yr, 100,000 youth visas",
     "Reuters"),
    ("HUNGARY LIFTS UKRAINE VETO",
     "Last block on EU accession clusters removed",
     "Kyiv Post"),
    ("COP31 ENDS THE DAY WITHOUT A DEAL",
     "Draft drops fossil fuels and the $120bn target",
     "Al Jazeera"),
    ("ICJ: MYANMAR GUILTY OF GENOCIDE",
     "First state ever held responsible; reparations ordered",
     "Daily Star"),
    ("PALISADES FIRE ARSON CONVICTION",
     "Jury convicts after the first trial deadlocked",
     "Reuters"),
    ("CALIFORNIA SUBPOENAS NVIDIA",
     "Probe into China chips and investor disclosures",
     "IANS"),
    ("DATA OF 16,000+ LEAKED",
     "JPMorgan, Visa, Mastercard customers hit",
     "TechSpot"),
    ("GTA 6: $2.36BN ON DAY ONE",
     "24.58m copies, biggest entertainment launch ever",
     "Dunya News"),
    ("IRAQ MOVES ON MILITIA STRONGHOLD",
     "Troops enter Jurf al-Nasr, first time in 12 years",
     "One Turn News"),
]
ty = 542
for i, (head, deck, src) in enumerate(TEN):
    col = i % 2
    row = i // 2
    x = 10 + col * 502
    yy = ty + row * 28
    d.text((x, yy), str(i + 1), font=font(SERIF_B, 15), fill=RED)
    d.text((x + 26, yy), head, font=font(SANS_B, 12), fill=INK)
    sw = d.textlength(src, font=font(SANS, 10))
    d.text((x + 492 - sw, yy + 1), src, font=font(SANS, 10), fill=GREY)
    d.text((x + 26, yy + 15), deck, font=font(SANS, 11), fill=GREY)


# ------------------------------------------------------------------- map
section_bar(d, 684, "WHERE IT HAPPENED", "SCHEMATIC \u2014 NOT TO SCALE")
MAP_X, MAP_Y = 10, 714
d.rectangle([MAP_X, MAP_Y, MAP_X + 590, MAP_Y + 96], fill=SEA)
CONTINENTS = [
    [(20, 25), (70, 10), (130, 8), (165, 20), (155, 45), (115, 55),
     (85, 48), (55, 58), (22, 45)],
    [(135, 60), (170, 58), (185, 80), (165, 105), (140, 95)],
    [(275, 12), (312, 8), (325, 26), (300, 38), (278, 30)],
    [(280, 44), (325, 42), (338, 74), (312, 100), (288, 80)],
    [(330, 10), (520, 8), (558, 32), (540, 60), (480, 68), (420, 62),
     (370, 50), (332, 34)],
    [(480, 88), (534, 84), (546, 102), (506, 110), (484, 100)],
]
for poly in CONTINENTS:
    pts = [(MAP_X + px, MAP_Y + py) for px, py in poly]
    d.polygon(pts, fill=LAND, outline=(150, 140, 110))
PINS = [
    (308, 24, "Kyiv \u2014 bridges hit"),
    (468, 52, "Gopalpur \u2014 Akvan ashore"),
    (292, 20, "Brussels \u2014 UK\u2013EU deal"),
    (150, 88, "Jun\u00edn \u2014 6.7 quake"),
    (318, 34, "Antalya \u2014 COP31 overtime"),
    (306, 16, "SE Poland \u2014 missiles land"),
    (362, 52, "Riyadh \u2014 tower hit"),
    (352, 44, "Jurf al-Nasr \u2014 troops move in"),
    (448, 48, "Delhi \u2014 Pakistan minister visits"),
    (536, 26, "Tokyo \u2014 inflation at year high"),
    (92, 32, "New York \u2014 Sikh plot sentencing"),
    (52, 42, "Los Angeles \u2014 arson verdict"),
]
for i, (px, py, label) in enumerate(PINS):
    cx, cy = MAP_X + px, MAP_Y + py
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=RED,
              outline=(255, 255, 255), width=1)
    num = str(i + 1)
    nw = d.textlength(num, font=font(SANS_B, 9))
    d.text((cx - nw / 2, cy - 5), num, font=font(SANS_B, 9),
           fill=(255, 255, 255))
for i, (px, py, label) in enumerate(PINS):
    col = i // 6
    row = i % 6
    x = 612 + col * 205
    yy = MAP_Y + 4 + row * 16
    d.text((x, yy), "%d  %s" % (i + 1, label), font=font(SANS, 11), fill=INK)

# ---------------------------------------------------------- also on friday
section_bar(d, 814, "ALSO ON FRIDAY", "22 MORE STORIES \u2014 36 IN ALL")
BRIEFS = [
    ("Estonia to shut Russia border crossings for 6+ months", "One Turn News"),
    ("Denmark expels Russia's defence attach\u00e9; France seeks UN session",
     "EuropeSays"),
    ("US Senate blocks Iran war-powers vote, 51\u201348", "Dunya News"),
    ("Houthi missile hits Riyadh's tallest tower", "Dawn"),
    ("Israeli strikes kill Palestinians in Gaza", "One Turn News"),
    ("US blockade tightens on Hormuz; IEA calls it the biggest energy shock",
     "Standard Topic"),
    ("Pakistan minister visits Delhi, first since 2025 conflict",
     "Standard Topic"),
    ("Clashes in Bangladesh ahead of Hasina's return", "One Turn News"),
    ("Indian man jailed 19+ years in Sikh leader murder plot", "Standard Topic"),
    ("TSMC and Samsung pause advanced chip sales bound for China",
     "Standard Topic"),
    ("China bars Bloomberg reporter from Trump\u2013Xi\u2013Putin summit",
     "Standard Topic"),
    ("Magnitude 6.7 quake hits central Peru", "TRT World"),
    ("Funeral boat capsizes in Nigeria", "One Turn News"),
    ("Judge approves $7.25bn Bayer Roundup settlement", "One Turn News"),
    ("Anthropic shares slide ~15% on day two after record IPO",
     "Business Standard"),
    ("Japan core inflation hits a year high", "One Turn News"),
    ("Trump fires White House cyber director after outages", "Jerusalem Post"),
    ("US measles: CDC reports 5,838 cases", "Contagion Live"),
    ("Pete Rose pardoned posthumously by Trump", "Dunya News"),
    ("Pakistan beat Sri Lanka by 8 wickets, clinch Test series", "Apex Sports"),
    ("UAE Bulls win Abu Dhabi T10 final", "ScoreZaap"),
    ("India A thrash Nepal by 306 runs", "Apex Sports"),
]
for i, (head, src) in enumerate(BRIEFS):
    col = i // 11
    row = i % 11
    x = 10 + col * 502
    yy = 844 + row * 10
    d.text((x, yy), "%d. %s \u2014 %s" % (11 + i, head, src),
           font=font(SANS, 10), fill=INK)

# ------------------------------------------------------- date check + footer
d.rectangle([0, 962, W, 984], fill=(232, 214, 160))
d.text((10, 967),
       "DATE CHECK \u2014 LEFT OUT (THURSDAY 19 NOV): Anthropic's Nasdaq debut \u00b7 "
       "ICJ verdict itself (Friday's reactions are in) \u00b7 GTA 6 launch day "
       "(Friday's sales figures are in)",
       font=font(SANS_B, 10), fill=INK)
foot1 = "Every story here happened, or was first reported, on Friday 20 November 2026."
fw = d.textlength(foot1, font=font(SERIF_B, 13))
d.text(((W - fw) / 2, 990), foot1, font=font(SERIF_B, 13), fill=NAVY)
foot2 = ("Sources: Reuters \u00b7 Al Jazeera \u00b7 Kyiv Post \u00b7 Kyiv Independent \u00b7 "
         "New Indian Express \u00b7 TRT World \u00b7 Dawn \u00b7 Daily Star \u00b7 TechSpot \u00b7 "
         "Dunya News \u00b7 Business Standard \u00b7 IANS \u00b7 Apex Sports")
fw2 = d.textlength(foot2, font=font(SANS, 10))
d.text(((W - fw2) / 2, 1008), foot2, font=font(SANS, 10), fill=GREY)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG")
print("wrote", out, img.size, os.path.getsize(out), "bytes")
