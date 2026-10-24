import meta from "./image-meta.json";
import { site } from "./site";
import type { ScrapItem } from "./types";

/*
 * "What we pin above the desk": the footer's pinboard. Only the studio's own material lives here
 * (her project pieces, her palette, her words). The reference images the brief came with are
 * inspiration, not content, and are never shown on the site.
 */

const size = meta as Record<string, { w: number; h: number; avg: string }>;
const work = (key: string, alt: string, caption: string, fix: "tape" | "clip" | "pin" | "corners" | "stamp"): ScrapItem => ({
  kind: "image",
  id: key,
  src: `/work/${key}.jpg`,
  w: size[key].w,
  h: size[key].h,
  alt,
  caption,
  tags: ["image"],
  fix,
});

export type DeskPin = {
  item: ScrapItem;
  /** centre of the pin on the board, in % of the board */
  x: number;
  y: number;
  /** width in px at desktop size (0 = natural) */
  w: number;
  /** resting tilt in degrees */
  r: number;
  /** pointer-parallax depth: 0 = fixed, 1 = moves most */
  depth: number;
};

export const deskPins: DeskPin[] = [
  { item: work("studio-anokhi/mark-orange", "The Studio Anokhi mark on an ochre card", "Studio Anokhi · mark", "stamp"), x: 33, y: 70, w: 118, r: -7, depth: 0.6 },
  { item: work("nivritti/logo-orange", "The Nivritti mountain logo on burnt orange", "Nivritti · logo", "tape"), x: 94, y: 62, w: 132, r: 6, depth: 0.8 },
  { item: work("content/red-room-portrait", "A portrait from a recent shoot, red wall", "On set", "clip"), x: 70, y: 70, w: 138, r: 4, depth: 0.5 },
  { item: { kind: "swatch", id: "chip-plum", name: "Plum", hex: "#390D26", tags: ["colour"] }, x: 4.5, y: 68, w: 96, r: 8, depth: 0.9 },
  { item: { kind: "swatch", id: "chip-blue", name: "Powder blue", hex: "#ABCDD6", tags: ["colour"] }, x: 61, y: 5, w: 92, r: -9, depth: 0.7 },
  {
    item: { kind: "note", id: "note-def", text: site.definition.split("; ")[1], paper: "cream", tags: ["words"] },
    x: 15, y: 82, w: 230, r: -3, depth: 0.4,
  },
  {
    item: { kind: "note", id: "note-story", text: site.founder.quote.join(" "), by: site.founder.name, paper: "blue", tags: ["words"] },
    x: 83, y: 84, w: 236, r: 3, depth: 0.45,
  },
  { item: { kind: "word", id: "word-kavalu", text: "ಕವಲು", script: "kn", tags: ["words"] }, x: 47, y: 86, w: 0, r: -5, depth: 0.65 },
];
