// Content model for the whole site. Pages and components only read these shapes,
// so adding a project or a pin on the footer desk never means touching a component.

export type ServiceKey = "branding" | "identity" | "social" | "film";

export type Img = {
  src: string;
  w: number;
  h: number;
  alt: string;
  /** Dominant colour, used behind the image while it loads and for duotones. */
  tone?: string;
  /** True while the file is a low-resolution stand-in cut from the old site. */
  placeholder?: boolean;
};

export type Swatch = { name: string; hex: string; note?: string };

export type Block =
  | { type: "text"; eyebrow?: string; heading?: string; body: string[] }
  | { type: "image"; image: Img; size: "full" | "wide" | "inset"; caption?: string }
  | { type: "pair"; images: [Img, Img]; caption?: string }
  | { type: "stamps"; images: Img[]; caption?: string }
  | { type: "palette"; heading?: string; colors: Swatch[] }
  | { type: "note"; text: string; by?: string }
  | { type: "quote"; text: string; by?: string };

export type Project = {
  slug: string;
  title: string;
  client: string;
  year?: number;
  city?: string;
  sector: string;
  services: ServiceKey[];
  /** Exactly how the services read on the case study, e.g. "Logo design". */
  deliverables: string[];
  /** One line for cards and the index. */
  summary: string;
  overview: string;
  cover: Img;
  /** The project's own colours: the case study and its transition wear these. */
  tone: { bg: string; ink: string; accent: string };
  /** Images that represent the project in collections, the hero flipbook and the index preview. */
  stamps: Img[];
  blocks: Block[];
  featured?: boolean;
  /** "snapshot" projects have a short page (cover and stamps); "case-study" ones carry the full story in blocks. */
  kind: "case-study" | "snapshot";
};

export type Service = {
  key: ServiceKey;
  /** The brand question this road answers: "What it says", "How it looks"... */
  choice: string;
  title: string;
  line: string;
  items: string[];
  tone: "cream" | "blue";
};

export type ScrapTag = "type" | "colour" | "texture" | "image" | "words" | "process";

export type ScrapItem =
  | {
      kind: "image";
      id: string;
      src: string;
      w: number;
      h: number;
      alt: string;
      caption?: string;
      credit?: string;
      tags: ScrapTag[];
      fix?: "tape" | "clip" | "pin" | "corners" | "stamp";
    }
  | { kind: "note"; id: string; text: string; by?: string; paper: "cream" | "blue" | "plum" | "ox"; tags: ScrapTag[] }
  | { kind: "swatch"; id: string; name: string; hex: string; tags: ScrapTag[] }
  | { kind: "word"; id: string; text: string; script?: "kn" | "en"; tags: ScrapTag[] };
