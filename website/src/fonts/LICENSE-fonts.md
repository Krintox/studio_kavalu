# Self-hosted fonts

**Courier Prime** (typed paper: captions, tickets, postmarks, footnotes) is self-hosted from Google
Fonts' latin files under the SIL Open Font License 1.1 (`CourierPrime-OFL.txt`, which must travel with
the files). It is local rather than loaded through `next/font/google` only so that a `size-adjust`
descriptor can be declared.

**Schibsted Grotesk** (display and text), **Anek Kannada** (Kannada), and the two stand-ins for her
hand, **Homemade Apple** and **Mrs Saint Delafield**, come from Google Fonts through `next/font/google`
(SIL Open Font License), self-hosted by Next.js at build time.

Gambetta and Switzer (Indian Type Foundry, Fontshare FFL) were removed on 2026-10-24 with the v3 type
change (`research/type/KAVALU_FONT_SHORTLIST.md`); nothing on the site uses an FFL font any more.

The wordmark is not a font: it is Ananya's own lettering, redrawn as SVG paths
(`components/brand/wordmark-paths.ts`).
