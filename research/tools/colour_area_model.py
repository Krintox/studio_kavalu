"""colour_area_model.py - estimated colour shares for the five iterations in research/COLOUR_PROPORTION.md.

Run: python -I colour_area_model.py   (no arguments; prints shares and ground switches per page)
These are ESTIMATES that set the targets; research/tools/colour_coverage.py measures the real pages.

Heights: CSS px at 1440 wide, from the v2 build (home 11,248 px, work 3,402, studio 6,811, case studies
4,386-7,708), split by section from the v2 screenshots. Compositions: estimated percent of each
section's area. Families: P plum (plum, deep, ink), B blue (blue, blue-2), C cream (cream, paper,
paper-note), O oxblood, J project colours, X photos.
Reported: palette share = P, B, C, O as percent of (area - photos - project colours); also plum+blue
as percent of all non-photo area; and ground switches (consecutive sections whose ground family differs).
"""
# reusable section recipes: (ground family for switches, composition)
R = {
 'collage_on_P': ('P', dict(P=60, X=25, C=10, B=5)),
 'collage_on_B': ('B', dict(B=60, X=25, C=9, P=5, O=1)),
 'collage_on_C': ('C', dict(C=69, X=25, B=3, P=3)),
 'spread_full': ('J', dict(J=73, X=22, C=5)),
 'spread_inset_P': ('P', dict(P=16, J=58, X=20, C=6)),
 'text_on_P': ('P', dict(P=88, C=7, B=5)),
 'text_on_B': ('B', dict(B=88, P=12)),
 'text_on_C': ('C', dict(C=92, P=6, B=2)),
 'bluesheet_on_P': ('P', dict(P=32, B=62, C=2, O=4)),
 'split_B_P': ('B|P', dict(B=46, P=50, C=2, O=2)),
 'album_on_P': ('P', dict(P=53, X=35, C=8, B=4)),
 'album_on_B': ('B', dict(B=53, X=35, C=8, P=4)),
 'album_on_C': ('C', dict(C=62, X=35, P=3)),
 'bluecards_on_P': ('P', dict(P=52, B=42, C=2, O=4)),
 'mixedcards_on_B': ('B', dict(B=50, C=23, P=23, O=4)),
 'cards_on_C': ('C', dict(C=73, B=18, P=9)),
 'plumcards_on_B': ('B', dict(B=50, P=42, C=4, O=4)),
 'blueposter_on_P': ('P', dict(P=60, B=25, X=6, C=6, O=3)),
 'plumposter_on_B': ('B', dict(B=63, P=22, X=6, C=6, O=3)),
 'blueposter_on_C': ('C', dict(C=70, B=18, X=6, P=6)),
 'letter_on_P': ('P', dict(P=30, C=63, B=4, O=3)),
 'letter_on_B': ('B', dict(B=30, C=63, P=5, O=2)),
 'letter_on_C': ('C', dict(C=91, P=6, B=2, O=1)),
 'bluesheet2_on_B': ('B', dict(B=92, P=6, O=2)),
 'creamsheet_on_B': ('B', dict(B=62, C=30, P=8)),
 'title_on_P': ('P', dict(P=90, C=6, B=4)),
 'title_on_B': ('B', dict(B=92, P=8)),
 'title_on_C': ('C', dict(C=94, P=6)),
 'grid_on_P': ('P', dict(P=40, X=52, C=6, B=2)),
 'grid_on_B': ('B', dict(B=40, X=52, C=6, P=2)),
 'grid_on_C': ('C', dict(C=44, X=52, P=4)),
 'case_hero': ('J', dict(J=78, X=17, C=5)),
 'case_next': ('J', dict(J=83, X=12, C=5)),
 'overview_cream_on_P': ('P', dict(P=45, C=50, B=5)),
 'overview_blue_on_P': ('P', dict(P=40, B=52, C=4, O=4)),
 'overview_plum_on_B': ('B', dict(B=45, P=50, C=5)),
 'overview_ox_on_C': ('C', dict(C=50, O=45, P=5)),
 'blocks_on_P': ('P', dict(P=46, X=40, C=10, B=4)),
 'blocks_desk_sheets': ('P', dict(P=22, B=30, X=38, C=10)),
 'blocks_on_B': ('B', dict(B=44, X=40, C=10, P=6)),
 'blocks_alt': ('B|P', dict(B=30, P=18, X=40, C=10, O=2)),
 'blocks_on_C': ('C', dict(C=50, X=40, P=6, B=2, O=2)),
 'band_on_P': ('P', dict(P=86, B=10, C=4)),
 'band_on_B': ('B', dict(B=88, P=12)),
 'band_on_C': ('C', dict(C=90, P=10)),
 'oxblood_band': ('O', dict(O=90, C=10)),
}
FOOTER = {
 'deep': [('tabs', 260, ('P', dict(P=50, O=25, B=25))), ('desk', 1250, ('P', dict(P=70, X=8, C=12, B=8, O=2))),
          ('wordmark', 900, ('P', dict(P=55, B=45)))],
 'blue': [('tabs', 260, ('P', dict(P=50, O=25, B=25))), ('desk', 1250, ('B', dict(B=68, X=8, C=12, P=10, O=2))),
          ('wordmark', 900, ('P', dict(P=55, B=45)))],
}
H = {
 'home': [('hero', 950), ('spreads', 2300), ('manifesto', 1000), ('album', 1000), ('roads', 1250), ('founder', 1000), ('choose', 1150)],
 'work': [('title', 450), ('grid', 850)],
 'case': [('hero', 900), ('overview', 450), ('blocks', 2300), ('cta', 250), ('next', 450)],
 'studio': [('studioHero', 850), ('studioRoads', 950), ('process', 650), ('founder', 800), ('faq', 600), ('choose', 850)],
}
IT = {
 'today': dict(foot='deep',
   home=['collage_on_C', 'spread_full', 'text_on_C', 'album_on_C', 'cards_on_C', 'blueposter_on_C', 'letter_on_C'],
   work=['title_on_C', 'grid_on_C'],
   case=['case_hero', 'overview_ox_on_C', 'blocks_on_C', 'band_on_C', 'case_next'],
   studio=['text_on_C', 'oxblood_band', 'text_on_C', 'blueposter_on_C', 'text_on_C', 'letter_on_C']),
 'A': dict(foot='deep',
   home=['collage_on_P', 'spread_full', 'text_on_P', 'album_on_P', 'bluecards_on_P', 'blueposter_on_P', 'letter_on_P'],
   work=['title_on_P', 'grid_on_P'],
   case=['case_hero', 'overview_cream_on_P', 'blocks_on_P', 'band_on_P', 'case_next'],
   studio=['text_on_P', 'bluecards_on_P', 'text_on_P', 'blueposter_on_P', 'text_on_P', 'letter_on_P']),
 'B': dict(foot='blue',
   home=['collage_on_B', 'spread_full', 'text_on_P', 'album_on_B', 'mixedcards_on_B', 'plumposter_on_B', 'letter_on_B'],
   work=['title_on_B', 'grid_on_B'],
   case=['case_hero', 'overview_plum_on_B', 'blocks_on_B', 'band_on_B', 'case_next'],
   studio=['text_on_B', 'text_on_P', 'text_on_B', 'plumposter_on_B', 'creamsheet_on_B', 'letter_on_B']),
 'C': dict(foot='deep',
   home=['collage_on_P', 'spread_full', 'text_on_B', 'album_on_P', 'mixedcards_on_B', 'blueposter_on_P', 'letter_on_B'],
   work=['title_on_B', 'grid_on_B'],
   case=['case_hero', 'overview_plum_on_B', 'blocks_alt', 'band_on_P', 'case_next'],
   studio=['text_on_B', 'text_on_P', 'text_on_B', 'blueposter_on_P', 'text_on_B', 'letter_on_B']),
 'D': dict(foot='deep',
   home=['collage_on_P', 'spread_inset_P', 'bluesheet_on_P', 'album_on_P', 'bluecards_on_P', 'blueposter_on_P', 'letter_on_P'],
   work=['title_on_P', 'grid_on_P'],
   case=['case_hero', 'overview_blue_on_P', 'blocks_desk_sheets', 'band_on_P', 'case_next'],
   studio=['bluesheet_on_P', 'bluecards_on_P', 'text_on_P', 'blueposter_on_P', 'bluesheet_on_P', 'letter_on_P']),
 'E': dict(foot='deep',
   home=['collage_on_B', 'spread_full', 'split_B_P', 'album_on_P', 'bluecards_on_P', 'blueposter_on_P', 'letter_on_P'],
   work=['title_on_B', 'grid_on_B'],
   case=['case_hero', 'overview_plum_on_B', 'blocks_on_B', 'band_on_P', 'case_next'],
   studio=['text_on_B', 'plumcards_on_B', 'split_B_P', 'blueposter_on_P', 'text_on_P', 'letter_on_P']),
}

# Round 2 (the dial) for D: the same arrangement at about 75% and about 90% plum+blue
R['overview_cream_on_P'] = ('P', dict(P=45, C=50, B=5))
R['blocks_desk_paper'] = ('P', dict(P=22, C=30, X=38, B=4, O=6))
R['creamsheet_on_P'] = ('P', dict(P=32, C=62, B=2, O=4))
R['bluesheet2letter_on_P'] = ('P', dict(P=30, B=64, O=3, C=3))
R['collage_on_P_cool'] = ('P', dict(P=60, X=25, C=6, B=9))
FOOTER['deep_cool'] = [('tabs', 260, ('P', dict(P=50, O=25, B=25))),
                       ('desk', 1250, ('P', dict(P=70, X=8, C=8, B=12, O=2))), ('wordmark', 900, ('P', dict(P=55, B=45)))]
IT['D-75'] = dict(foot='deep',
   home=['collage_on_P', 'spread_inset_P', 'creamsheet_on_P', 'album_on_P', 'bluecards_on_P', 'blueposter_on_P', 'letter_on_P'],
   work=['title_on_P', 'grid_on_P'],
   case=['case_hero', 'overview_cream_on_P', 'blocks_desk_paper', 'band_on_P', 'case_next'],
   studio=['bluesheet_on_P', 'bluecards_on_P', 'text_on_P', 'blueposter_on_P', 'creamsheet_on_P', 'letter_on_P'])
IT['D-90'] = dict(foot='deep_cool',
   home=['collage_on_P_cool', 'spread_inset_P', 'bluesheet_on_P', 'album_on_P', 'bluecards_on_P', 'blueposter_on_P', 'bluesheet2letter_on_P'],
   work=['title_on_P', 'grid_on_P'],
   case=['case_hero', 'overview_blue_on_P', 'blocks_desk_sheets', 'band_on_P', 'case_next'],
   studio=['bluesheet_on_P', 'bluecards_on_P', 'text_on_P', 'blueposter_on_P', 'bluesheet_on_P', 'bluesheet2letter_on_P'])

WEIGHT = dict(home=1, work=1, case=3, studio=1)


def sections(it, page):
    out = []
    for (name, h), recipe in zip(H[page], IT[it][page]):
        g, comp = R[recipe]
        out.append((name, h, g, comp))
    for name, h, (g, comp) in FOOTER[IT[it]['foot']]:
        out.append((name, h, g, comp))
    return out


def tally(secs, w=1):
    t = dict(P=0.0, B=0.0, C=0.0, O=0.0, J=0.0, X=0.0)
    for _, h, _, comp in secs:
        s = sum(comp.values())
        for k, v in comp.items():
            t[k] += w * h * v / s
    return t


def switches(secs):
    seq = []
    for _, _, g, _ in secs:
        seq += g.split('|')
    return sum(1 for a, b in zip(seq, seq[1:]) if a != b)


def report(t):
    pal = t['P'] + t['B'] + t['C'] + t['O']
    nonphoto = pal + t['J']
    r = {k: 100 * t[k] / pal for k in 'PBCO'}
    r['PBn'] = 100 * (t['P'] + t['B']) / nonphoto
    r['J'] = 100 * t['J'] / nonphoto
    return r


if __name__ == '__main__':
    for it in IT:
        site = dict(P=0.0, B=0.0, C=0.0, O=0.0, J=0.0, X=0.0)
        lines = []
        for page in H:
            secs = sections(it, page)
            t = tally(secs)
            for k in site: site[k] += WEIGHT[page] * t[k]
            r = report(t)
            lines.append(f"      {page:7s} plum {r['P']:3.0f} blue {r['B']:3.0f} cream {r['C']:3.0f} oxblood {r['O']:2.0f}"
                         f"  P+B {r['P'] + r['B']:3.0f}%  (non-photo {r['PBn']:3.0f}%, project {r['J']:2.0f}%)  switches {switches(secs)}")
        r = report(site)
        print(f"{it:5s} SITE    plum {r['P']:3.0f} blue {r['B']:3.0f} cream {r['C']:3.0f} oxblood {r['O']:2.0f}"
              f"  P+B {r['P'] + r['B']:3.0f}%  (non-photo {r['PBn']:3.0f}%, project {r['J']:2.0f}%)")
        print('\n'.join(lines))
