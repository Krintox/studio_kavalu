import { Anek_Kannada, Homemade_Apple, Mrs_Saint_Delafield, Schibsted_Grotesk } from "next/font/google";
import localFont from "next/font/local";

// The type system (BRAND_DESIGN.md §5; chosen in research/type/KAVALU_FONT_SHORTLIST.md, system A, after
// three systems were set in the real site: research/type/lab/). Her own lettering is the wordmark (SVG,
// not a font) and the loudest letters on the page; one grotesk does every reading job around it; a
// typewriter appears only where the album has typed paper; Kannada is set in Anek Kannada.

// Display and text: Schibsted Grotesk (Bakken & Baeck for Schibsted, SIL OFL), variable 400-900 with
// italics, and the rupee sign. One family in both roles: --f-display and --f-text (tokens.css) name it.
const grotesk = Schibsted_Grotesk({
  subsets: ["latin", "latin-ext"],
  style: ["normal", "italic"],
  variable: "--font-grotesk",
  display: "swap",
});

// Typed paper only (captions, tickets, postmarks, footnotes, stamps' figure labels): Courier Prime. Its
// capitals are 17% shorter than a modern mono's (0.58 em against ~0.70), so it is set 10% larger at the
// face, and every label size in the CSS stays as designed. Self-hosted (OFL) so the descriptor can be
// declared.
export const mono = localFont({
  src: [
    { path: "../fonts/CourierPrime-Regular.woff2", weight: "400", style: "normal" },
    { path: "../fonts/CourierPrime-Italic.woff2", weight: "400", style: "italic" },
    { path: "../fonts/CourierPrime-Bold.woff2", weight: "700", style: "normal" },
  ],
  declarations: [{ prop: "size-adjust", value: "110%" }],
  variable: "--font-mono",
  display: "swap",
});

// Her notes and signature, until her own hand is scanned and traced as SVG (pending from Ananya): stand-ins.
export const hand = Homemade_Apple({
  subsets: ["latin"],
  weight: "400",
  variable: "--font-hand",
  display: "swap",
});

export const signature = Mrs_Saint_Delafield({
  subsets: ["latin"],
  weight: "400",
  variable: "--font-signature",
  display: "swap",
  preload: false,
});

// Kannada (ಕವಲು and every Kannada word), with its own width axis.
export const kannada = Anek_Kannada({
  subsets: ["kannada", "latin"],
  axes: ["wdth"],
  variable: "--font-kannada",
  display: "swap",
});

export const fontVars = [grotesk, mono, hand, signature, kannada].map((f) => f.variable).join(" ");
