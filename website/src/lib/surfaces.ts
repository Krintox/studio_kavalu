/*
 * Which ground each section stands on (styles/surfaces.css, BRAND_DESIGN.md §4.5), and any reading
 * surface laid on it as a sheet. The proportion lives here and nowhere else.
 *
 * Brief 5 (24 Oct): plum about 20%, cream and powder blue together 50-60%, the rest for the remaining
 * colours, and a light hero and opening. Chosen after five light arrangements were rendered on the real
 * site and measured (research/palette_lab, L1-L5 and R2): the page opens on cream, her prints sit on
 * powder-blue spreads, the house view is the torn cream sheet that slides over them; then the album
 * strip glows on plum, the four roads stand on cream, the founder on warm oxblood with her blue poster,
 * the letter on blue, and the footer's desk is deep plum. Measured on the home page at 1440 px: plum
 * 19.2%, blue 32.4%, cream 30.2% (cream and blue 62.6%), oxblood 5.9%, photographs 12.3%.
 * (Brief 4's "desk", one plum ground under blue sheets, measured 63% plum and was judged too plum.)
 */
export type Surface = "cream" | "blue" | "blue2" | "plum" | "deep" | "oxblood";

export const GROUNDS = {
  hero: "cream",
  manifesto: "cream",
  album: "plum",
  roads: "cream",
  founder: "oxblood",
  choose: "blue",
  studioHero: "cream",
  studioRoads: "blue",
  process: "blue",
  faq: "cream",
  work: "cream",
  case: "cream",
  start: "cream",
  notFound: "cream",
} as const satisfies Record<string, Surface>;

/** Sheets: a reading surface laid on its section's ground as a large piece of paper (taped where it
 * carries a statement). None in the light arrangement; the mechanism stays for any section that wants
 * one (lib/surfaces.ts was "the desk" under brief 4, with blue sheets for every statement). */
export const SHEETS: Partial<Record<"manifesto" | "roads" | "studioHero" | "process" | "faq" | "caseText" | "start", { surface: Surface; taped: boolean }>> = {};

/** The project spreads take these in turn: her prints on powder-blue paper. */
const SPREADS: readonly Surface[] = ["blue", "blue"];

export type Ground = keyof typeof GROUNDS;
export type Sheet = "manifesto" | "roads" | "studioHero" | "process" | "faq" | "caseText" | "start";

const DARK: ReadonlySet<Surface> = new Set(["plum", "deep", "oxblood"]);

const attrs = (key: string, surface: Surface) =>
  ({ "data-section": key, "data-surface": surface, "data-tone": DARK.has(surface) ? "dark" : "light" }) as const;

/** The attributes that stand a section on its ground: its colours, and the tone the nav and cursor read. */
export function ground(key: Ground) {
  return attrs(key, GROUNDS[key]);
}

/** The attributes that make an element a sheet of paper on its section's ground (none when the key has no sheet). */
export function sheet(key: Sheet) {
  const sh = SHEETS[key];
  if (!sh) return {};
  return { "data-surface": sh.surface, "data-sheet": sh.taped ? "taped" : "", "data-tone": DARK.has(sh.surface) ? "dark" : "light" } as const;
}

/** The ground of the nth project spread (0-based). */
export function spreadGround(n: number) {
  return attrs("spread", SPREADS[n % SPREADS.length]);
}
