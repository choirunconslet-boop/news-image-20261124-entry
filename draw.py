#!/usr/bin/env python3
"""Draw the 1024x1024 front page for Tuesday 24 November 2026.

All stories were first reported on 24 November 2026 (cross-checked in at
least two live news sources each). The lead picture is an AI-generated
editorial illustration (hero.jpg, made with the media image tool, no text
in the artwork); the masthead, headlines and panels are crisp PIL vector
drawing so every word stays legible.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 234)
INK = (26, 26, 26)
RED = (164, 30, 34)
GREY = (90, 86, 76)
PANEL = (255, 253, 245)
RULE = (200, 192, 172)
YELLOW = (255, 200, 60)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning list of lines fitting `width` px."""
    lines = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for w in words:
            trial = (line + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = w
        if line:
            lines.append(line)
    return lines


def text_block(draw, x, y, text, fnt, width, fill=INK, leading=1.25):
    lines = wrap(draw, text, fnt, width)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def icon_ship(d, x, y, s, c):
    # hull + cabin + mast + waves
    d.polygon([(x, y + 0.55 * s), (x + s, y + 0.55 * s),
               (x + 0.85 * s, y + 0.85 * s), (x + 0.15 * s, y + 0.85 * s)], fill=c)
    d.rectangle([x + 0.32 * s, y + 0.30 * s, x + 0.62 * s, y + 0.55 * s], fill=c)
    d.line([x + 0.5 * s, y + 0.05 * s, x + 0.5 * s, y + 0.32 * s], fill=c, width=4)
    d.polygon([(x + 0.5 * s, y + 0.05 * s), (x + 0.78 * s, y + 0.22 * s),
               (x + 0.5 * s, y + 0.22 * s)], fill=RED)
    for i in range(3):
        d.arc([x - 0.1 * s + i * 0.35 * s, y + 0.88 * s,
               x + 0.25 * s + i * 0.35 * s, y + 1.08 * s],
              0, 180, fill=c, width=3)


def icon_jet(d, x, y, s, c):
    # fighter jet in side profile, nose right: tapered fuselage, swept
    # wings, tail fin, cockpit bump
    d.polygon([(x + 0.05 * s, y + 0.50 * s), (x + 0.45 * s, y + 0.42 * s),
               (x + 0.95 * s, y + 0.47 * s), (x + 0.95 * s, y + 0.57 * s),
               (x + 0.45 * s, y + 0.62 * s)], fill=c)
    d.polygon([(x + 0.44 * s, y + 0.44 * s), (x + 0.56 * s, y + 0.20 * s),
               (x + 0.63 * s, y + 0.44 * s)], fill=c)
    d.polygon([(x + 0.43 * s, y + 0.60 * s), (x + 0.54 * s, y + 0.82 * s),
               (x + 0.61 * s, y + 0.60 * s)], fill=c)
    d.polygon([(x + 0.10 * s, y + 0.46 * s), (x + 0.18 * s, y + 0.26 * s),
               (x + 0.27 * s, y + 0.46 * s)], fill=c)
    d.ellipse([x + 0.60 * s, y + 0.42 * s, x + 0.74 * s, y + 0.50 * s], fill=PAPER)


def icon_flame(d, x, y, s, c):
    # proper flame: red outer silhouette, yellow inner flame, pale core
    d.polygon([(x + 0.58 * s, y + 0.02 * s), (x + 0.80 * s, y + 0.22 * s),
               (x + 0.92 * s, y + 0.48 * s), (x + 0.95 * s, y + 0.68 * s),
               (x + 0.78 * s, y + 0.97 * s), (x + 0.22 * s, y + 0.97 * s),
               (x + 0.05 * s, y + 0.68 * s), (x + 0.12 * s, y + 0.44 * s),
               (x + 0.34 * s, y + 0.26 * s)], fill=RED)
    d.polygon([(x + 0.52 * s, y + 0.42 * s), (x + 0.68 * s, y + 0.60 * s),
               (x + 0.72 * s, y + 0.76 * s), (x + 0.50 * s, y + 0.90 * s),
               (x + 0.30 * s, y + 0.76 * s), (x + 0.34 * s, y + 0.60 * s),
               (x + 0.44 * s, y + 0.50 * s)], fill=YELLOW)
    d.polygon([(x + 0.50 * s, y + 0.62 * s), (x + 0.60 * s, y + 0.74 * s),
               (x + 0.50 * s, y + 0.84 * s), (x + 0.40 * s, y + 0.74 * s)],
              fill=PAPER)


def icon_building(d, x, y, s, c):
    d.rectangle([x + 0.10 * s, y + 0.35 * s, x + 0.90 * s, y + 0.95 * s], fill=c)
    d.rectangle([x + 0.30 * s, y + 0.15 * s, x + 0.70 * s, y + 0.35 * s], fill=c)
    for r in range(2):
        for col in range(3):
            d.rectangle([x + (0.20 + col * 0.24) * s, y + (0.45 + r * 0.22) * s,
                         x + (0.36 + col * 0.24) * s, y + (0.60 + r * 0.22) * s],
                        fill=PAPER)
    d.ellipse([x + 0.55 * s, y - 0.08 * s, x + 0.75 * s, y + 0.12 * s], fill=GREY)
    d.ellipse([x + 0.70 * s, y - 0.22 * s, x + 0.95 * s, y + 0.03 * s], fill=GREY)


def icon_gavel(d, x, y, s, c):
    # judge's gavel, head slanted: parallelogram head, diagonal handle,
    # red sound block = lawsuit
    d.polygon([(x + 0.08 * s, y + 0.22 * s), (x + 0.52 * s, y + 0.05 * s),
               (x + 0.62 * s, y + 0.25 * s), (x + 0.18 * s, y + 0.42 * s)],
              fill=c)
    d.line([x + 0.38 * s, y + 0.30 * s, x + 0.82 * s, y + 0.82 * s],
           fill=c, width=max(4, int(0.09 * s)))
    d.rectangle([x + 0.08 * s, y + 0.84 * s, x + 0.92 * s, y + 0.95 * s], fill=RED)


def icon_handshake(d, x, y, s, c):
    # two overlapping flags = politics / election
    d.line([x + 0.20 * s, y + 0.10 * s, x + 0.20 * s, y + 0.95 * s], fill=c, width=4)
    d.polygon([(x + 0.20 * s, y + 0.10 * s), (x + 0.55 * s, y + 0.22 * s),
               (x + 0.20 * s, y + 0.34 * s)], fill=RED)
    d.line([x + 0.80 * s, y + 0.10 * s, x + 0.80 * s, y + 0.95 * s], fill=c, width=4)
    d.polygon([(x + 0.80 * s, y + 0.10 * s), (x + 0.45 * s, y + 0.22 * s),
               (x + 0.80 * s, y + 0.34 * s)], fill=c)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=4)
    d.rectangle([18, 18, W - 19, H - 19], outline=RULE, width=1)

    # ---- masthead ----
    f_mast = font(SERIF, 88)
    d.text((W // 2, 30), "THE WORLD", font=f_mast, fill=INK, anchor="ma")
    d.line([40, 128, W - 40, 128], fill=INK, width=3)
    d.text((W // 2, 138), "Tuesday, 24 November 2026", font=font(SERIF, 28),
           fill=RED, anchor="ma")
    d.text((W // 2, 176), "THE DAY'S NEWS IN ONE PAGE  —  ALL STORIES FIRST REPORTED TODAY",
           font=font(SANS, 18), fill=GREY, anchor="ma")
    d.line([40, 208, W - 40, 208], fill=INK, width=2)

    # ---- lead story: Nvidia ----
    lx, ly, lw, lh = 40, 222, W - 80, 240
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=PANEL, outline=RULE, width=1)
    d.text((lx + 20, ly + 12), "TECH  •  LEAD STORY", font=font(SANS_B, 17), fill=RED)
    d.text((lx + 20, ly + 38), "Huang is back at Nvidia",
           font=font(SERIF, 40), fill=INK)
    text_block(d, lx + 20, ly + 92,
               "Board reinstates its CEO after Trump steps in; shares jump by a third.",
               font(SANS, 20), 580, leading=1.25)
    text_block(d, lx + 20, ly + 146,
               "Eleven days after he quit over affairs — one with an alleged Chinese "
               "spy — the board votes unanimously to bring Jensen Huang back. The US "
               "blacklists Singapore chip firm Megaspeed.",
               font(SANS, 18), 580, fill=GREY, leading=1.25)
    # lead picture: generated editorial illustration, cropped to the
    # warship / jets / tankers band, right side of the lead panel
    hero = Image.open("hero.jpg").convert("RGB")
    hw, hh = hero.size
    art = hero.crop((int(0.156 * hw), int(0.1125 * hh),
                     hw, int(0.831 * hh)))
    art = art.resize((296, 224), Image.LANCZOS)
    img.paste(art, (lx + lw - 296 - 12, ly + 8))
    d.rectangle([lx + lw - 296 - 12, ly + 8,
                 lx + lw - 12, ly + 8 + 224], outline=RULE, width=1)

    # ---- six panels, 2 cols x 3 rows ----
    panels = [
        ("LIBYA", "Ukrainian drones sink Russian warship",
         "Corvette Merkury sunk in Benghazi; cargo ship Angara hit, helicopter destroyed.",
         icon_ship),
        ("KOREA", "Russian jets enter Korea's air zone",
         "Seoul scrambles fighters; island alert as jets near Ulleungdo. No airspace breach.",
         icon_jet),
        ("GULF", "Iran strikes resume; US hits back",
         "Iran strikes resume; US downs drones off Bahrain and hits 'shadow banks'.",
         icon_flame),
        ("KYIV", "Kyiv toll rises to 14 killed",
         "Russian strikes kill 14 in Kyiv region and damage 21 sites, including homes.",
         icon_building),
        ("TECH LAW", "Two US states sue SpaceX over Grok",
         "Virginia and Oregon allege Grok's 'spicy mode' made sexual images of children.",
         icon_gavel),
        ("SPAIN", "Spain's right set to oust Sánchez",
         "Polls put Feijóo's PP ahead before the snap election on 29 November.",
         icon_handshake),
    ]
    pw, ph, gap = 462, 140, 20
    x0, y0 = 40, 476
    for i, (kick, head, body, icon) in enumerate(panels):
        x = x0 + (i % 2) * (pw + gap)
        y = y0 + (i // 2) * (ph + 12)
        d.rectangle([x, y, x + pw, y + ph], fill=PANEL, outline=RULE, width=1)
        d.text((x + 14, y + 8), kick, font=font(SANS_B, 15), fill=RED)
        tx = x + 14
        ty = text_block(d, tx, y + 30, head, font(SANS_B, 22), pw - 110, leading=1.12)
        # body uses the same narrow width as the headline so its lines can
        # never run into the icon at the panel's right edge
        text_block(d, tx, ty + 4, body, font(SANS, 17), pw - 110, fill=GREY, leading=1.18)
        icon(d, x + pw - 74, y + 30, 52, INK)

    # ---- in brief strip ----
    by = y0 + 3 * ph + 2 * 12 + 12
    d.line([40, by, W - 40, by], fill=INK, width=2)
    d.text((40, by + 10), "IN BRIEF", font=font(SANS_B, 17), fill=RED)
    text_block(d, 40, by + 34,
               "• Democrats clinch a House majority of at least 258 seats, the largest since 1992.  "
               "• NATO vows space defence after a report of a Russian nuclear satellite.  "
               "• Colombia files a complaint against Starlink over prison signals.",
               font(SANS, 16), W - 80, leading=1.25)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
