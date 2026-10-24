import meta from "./image-meta.json";
import type { Img, Project } from "./types";

const sizes = meta as Record<string, { w: number; h: number; avg: string; hq?: boolean }>;

/**
 * The images came from screenshots of the previous site, so they were tiny and marked `placeholder`.
 * Those regenerated at high quality (research/images_hq/MANIFEST.md: the same picture, checked against
 * its source) carry `hq` in image-meta.json and are no longer placeholders. To swap in an original:
 * drop it into /public/work/<slug>/ with the same file name, set its size and `hq` in image-meta.json.
 */
function img(key: string, alt: string): Img {
  const d = sizes[key];
  return { src: `/work/${key}.jpg`, w: d.w, h: d.h, alt, tone: d.avg, placeholder: !d.hq };
}

/**
 * A real, full-resolution picture. Use this instead of img() once the original arrives, e.g.
 *   photo("/work/studio-anokhi/cover.jpg", 2400, 1600, "Hands at the wheel", "#523A2F")
 * w/h are the file's pixel size; tone is the colour shown while it loads.
 */
export function photo(src: string, w: number, h: number, alt: string, tone?: string): Img {
  return { src, w, h, alt, tone, placeholder: false };
}

const anokhi = {
  wheel: img("studio-anokhi/hero-wheel", "Hands shaping clay on a wheel behind the Studio Anokhi wordmark"),
  pattern: img("studio-anokhi/wordmark-pattern", "Studio Anokhi wordmarks and the अ mark repeated on a terracotta field"),
  vases: img("studio-anokhi/vases-wordmark", "Black clay vases scattered around the anokhi wordmark on cream"),
  mark: img("studio-anokhi/mark-orange", "The अ logo mark in cream on an ochre card"),
  evolution: img("studio-anokhi/mark-evolution", "A pot silhouette turning into the Hindi letter अ in three steps"),
  wordSearch: img("studio-anokhi/word-search", "A word-search grid over hands working clay, the word 'something' circled"),
  ochre: img("studio-anokhi/stationery-ochre", "Studio Anokhi stationery on an ochre gradient"),
  olive: img("studio-anokhi/stationery-olive", "Studio Anokhi stationery on an olive gradient"),
  slow: img("studio-anokhi/slow-making", "Hands trimming a pot on the wheel, captioned 'A glimpse of slow making'"),
  collage: img("studio-anokhi/collage-wheel", "Clay on the wheel with the studio anokhi wordmark"),
};

const nivritti = {
  sign: img("nivritti/sign-street", "The Nivritti hanging sign on a street of old balconies"),
  cards: img("nivritti/business-cards", "Navy and forest-green Nivritti business cards on dark linen"),
  box: img("nivritti/packaging-box", "Cream Nivritti packaging with a botanical illustration"),
  bottle: img("nivritti/cleanser-bottle", "A dark Nivritti hemp cleanser bottle topped with foam"),
  orange: img("nivritti/logo-orange", "The Nivritti mountain logo in cream on burnt orange"),
  navy: img("nivritti/logo-navy", "The Nivritti mountain logo in cream on navy"),
};

const content = {
  onam: img("content/not-so-onam", "A woman in a pink sequinned dress with the title Not-So-Onam?"),
  fillers: img("content/fillers-not-yet", "Friends dancing at a celebration under the line I'm not getting the fillers yet"),
  redRoom: img("content/red-room-portrait", "A portrait in tinted glasses against a red-orange wall"),
  redSaree: img("content/red-saree-portrait", "A woman in a red saree seated with a cup of tea"),
};

export const projects: Project[] = [
  {
    slug: "studio-anokhi",
    title: "Studio Anokhi",
    client: "Studio Anokhi",
    year: 2025,
    city: "Bengaluru",
    sector: "Pottery studio",
    services: ["branding", "identity", "social"],
    deliverables: ["Brand identity", "Visual identity", "Social media strategy"],
    // Card summary is new copy, written for the index; confirm with Ananya.
    summary: "A warm, handmade identity for a pottery studio, made to sit quietly beside the clay.",
    overview:
      "Studio Anokhi is a creative pottery studio in Bangalore founded by designer Archana Keshore. Rooted in a love for all things handmade, the studio creates handcrafted ceramic pieces and hosts pottery workshops. The goal was to build a warm, approachable identity that complements the pottery rather than competing with it, leaving room for the studio's creativity and craft to take centre stage.",
    cover: anokhi.wheel,
    tone: { bg: "#9F4A30", ink: "#FAEBCA", accent: "#CF8A3F" },
    stamps: [anokhi.collage, anokhi.pattern, anokhi.mark, anokhi.vases, anokhi.slow, anokhi.ochre, anokhi.wordSearch, anokhi.olive],
    blocks: [
      {
        type: "text",
        eyebrow: "The approach",
        body: [
          "The identity draws from the studio's handmade ethos, balancing simplicity with a sense of character. A soft, rounded sans-serif forms the primary logo, with its letters stacked closely together like interlocking puzzle pieces.",
          "The logo mark draws from a Hindi letterform whose silhouette also evokes the shape of a pot, subtly connecting the identity to the craft.",
        ],
      },
      { type: "image", image: anokhi.pattern, size: "full" },
      { type: "pair", images: [anokhi.vases, anokhi.mark] },
      { type: "image", image: anokhi.evolution, size: "wide", caption: "Logo mark: from the pot to the letterform." },
      { type: "note", text: "pot → letter → mark" },
      {
        type: "text",
        eyebrow: "Visual identity",
        body: [
          "The colour palette takes cues from the materials and surroundings of the studio. Terracotta and red oxide reference the clay and flooring, while earthy green and yellow introduce brighter accents. Ivory and cream provide a softer contrast.",
          "The brand assets take inspiration from the different pottery forms created at the studio. Hand-drawn, clay-inspired illustrations bring these shapes into the wider identity, complementing the minimal logo with a more tactile, human quality. Slightly irregular contours and imperfect edges echo the nature of handmade ceramics, giving the visual language a sense of individuality without making it feel cluttered.",
        ],
      },
      {
        type: "palette",
        heading: "Palette",
        // Sampled from the old site's images; replace with the guideline values.
        colors: [
          { name: "Terracotta", hex: "#9F4A30" },
          { name: "Red oxide", hex: "#7C3320" },
          { name: "Earthy green", hex: "#5B5A3B" },
          { name: "Yellow", hex: "#CF8A3F" },
          { name: "Ivory", hex: "#FAEBCA" },
          { name: "Cream", hex: "#E5D7BD" },
        ],
      },
      { type: "pair", images: [anokhi.wordSearch, anokhi.ochre] },
      { type: "pair", images: [anokhi.olive, anokhi.slow] },
    ],
    featured: true,
    kind: "case-study",
  },
  {
    slug: "nivritti",
    title: "Nivritti",
    client: "Nivritti",
    year: 2023,
    city: "Delhi NCR",
    sector: "Ayurvedic hemp wellness",
    services: ["branding", "identity"],
    deliverables: ["Logo design", "Visual identity", "Packaging"],
    summary: "A hand-cut Himalayan identity for an Ayurvedic hemp brand: premium, never exclusive.",
    overview:
      "Nivritti is a Delhi NCR-based Ayurvedic hemp brand on a mission to support de-addiction through thoughtfully crafted products made with carefully sourced ingredients. The challenge was to create a brand identity that felt premium without feeling exclusive, connecting with a younger, urban audience aged 18–30 across Tier 1 cities.",
    cover: nivritti.sign,
    tone: { bg: "#07253D", ink: "#EFE9DA", accent: "#994215" },
    stamps: [nivritti.sign, nivritti.orange, nivritti.cards, nivritti.navy, nivritti.box, nivritti.bottle],
    blocks: [
      { type: "image", image: nivritti.cards, size: "full" },
      {
        type: "text",
        eyebrow: "The approach",
        body: [
          "We looked to the source of Nivritti's ingredients for inspiration. The Himalayan foothills, where hemp grows in its natural environment, became the foundation of the visual direction, alongside the cultural associations of Shiva and Vijaya.",
          "The logo features a linocut-style illustration of the Himalayas, bringing a raw, handcrafted quality to the identity. Paired with a bold serif typeface with contrasting stroke weights, it balances premium appeal with a slightly imperfect, homegrown character.",
        ],
      },
      { type: "pair", images: [nivritti.box, nivritti.bottle] },
      {
        type: "text",
        eyebrow: "Visual identity",
        body: [
          "The colour palette draws from nature, using greens and blues to retain a connection to the Ayurvedic category while standing apart from the muted beige tones commonly found on its shelves.",
        ],
      },
      {
        type: "palette",
        heading: "Palette",
        colors: [
          { name: "Navy", hex: "#07253D" },
          { name: "Forest green", hex: "#314133" },
          { name: "Burnt orange", hex: "#994215" },
          { name: "Bone", hex: "#EFE9DA" },
        ],
      },
      { type: "pair", images: [nivritti.orange, nivritti.navy] },
    ],
    featured: true,
    kind: "case-study",
  },
  {
    slug: "not-so-onam",
    title: "Not-So-Onam?",
    client: "",
    sector: "Festive campaign",
    services: ["social", "film"],
    // Snapshot details are unknown: fill in client, year, deliverables and a real summary.
    deliverables: ["Social media", "Film & photography"],
    summary: "Festive social content.",
    overview: "",
    cover: content.onam,
    tone: { bg: "#A11F5B", ink: "#F8E9EF", accent: "#E6C34A" },
    stamps: [content.onam],
    blocks: [],
    kind: "snapshot",
  },
  {
    slug: "fillers-not-yet",
    title: "I'm not getting the fillers yet",
    client: "",
    sector: "Social content",
    services: ["social", "film"],
    deliverables: ["Social media", "Film & photography"],
    summary: "Social content.",
    overview: "",
    cover: content.fillers,
    tone: { bg: "#3F1B0E", ink: "#F6E7B6", accent: "#E8C840" },
    stamps: [content.fillers],
    blocks: [],
    kind: "snapshot",
  },
  {
    slug: "shoot-stills",
    title: "Shoot stills",
    client: "",
    sector: "Film & photography",
    services: ["film"],
    deliverables: ["Film & photography"],
    summary: "Frames from recent shoots.",
    overview: "",
    cover: content.redRoom,
    tone: { bg: "#A32D02", ink: "#FBE3D6", accent: "#F2A07B" },
    stamps: [content.redRoom, content.redSaree],
    blocks: [],
    kind: "snapshot",
  },
];

export const featured = projects.filter((p) => p.featured);
export const getProject = (slug: string) => projects.find((p) => p.slug === slug);

/** Every stamp across all projects, interleaved so neighbours come from different projects. */
export function allStamps() {
  const lists = projects.map((p) => p.stamps.map((image) => ({ image, project: p })));
  const out: { image: Img; project: Project }[] = [];
  for (let i = 0; lists.some((l) => l[i]); i++) for (const l of lists) if (l[i]) out.push(l[i]);
  return out;
}
