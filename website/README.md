# Studio Kavalu — website

The site for **Studio Kavalu by Ananya**, a branding and content house in Bengaluru.

The concept is *the crossroads album*, and the scrapbook is the format of the whole site, not a page.
- Every project is a stamp or a mounted print: taped, cornered or clipped, with typed captions and her
  hand notes.
- Projects open like spreads and are filed under folder tabs.
- A hairline road forks through the site (ಕವಲು means crossroads).

The design rules, uniform across every page, are in **`../BRAND_DESIGN.md`**. The client's own rules
and the work log are in **`../kavalu_instructions.md`**.

Built with Next.js 16 (App Router), React 19.3, GSAP 3.15 (ScrollTrigger, SplitText, Flip, Draggable,
Inertia), Lenis 1.3 and plain CSS Modules. There is no UI kit and no CMS.

## Run it

```bash
npm install
npm run dev        # http://localhost:3000  (this checkout was developed on port 3210: npx next dev -p 3210)
npm run build      # production build
npm run typecheck
```

Node 20.9 or newer.

## Pages

| Route | What it is |
|---|---|
| `/` | Intro (first visit only); hero album page with the flip-book stamp; project spreads; manifesto; the album strip; the four roads; founder; "Choose your road" |
| `/work` | Every project as perforated stamps or as an index (hover shows the stamp); filter by road |
| `/work/[slug]` | Case study, or a shorter page for "snapshot" projects |
| `/studio` | The definition, the four roads in depth, the process road, founder, FAQ |
| `/start` | "Choose your road" as a full page. It also opens as a drawer from every "Start a project" button |
| `/api/brief` | Receives briefs (see *Connecting the inbox*) |

Every page ends the same way, with the folder tabs, then **the desk** ("What we pin above the desk"),
then the STUDIO / KAVALU wordmark:
- the desk holds a ticket to start a project, a contact card, a site index and her pins;
- on desktop you can drag things around; on phones it is a strip you swipe;
- the wordmark's letters arrive from both sides as you reach it.

## Editing content (no components to touch)

All content lives in `src/content/`:

- **`site.ts`**: name, Kannada name, the definition, the headline and brand line, founder (name,
  quote), email, city, Instagram / WhatsApp / booking links, the four services, the process.
  Components read their copy from here.
- **`projects.ts`**: every project. Its title, client, year, sector, deliverables, summary, overview,
  colours (`tone`), the pictures that represent it (`stamps`), and the case-study `blocks`.
  - `kind: "case-study"` gets the full page; `kind: "snapshot"` gets a shorter page.
  - `featured: true` puts a project in the homepage spreads (keep it to 2–4).
  - Captions on images type themselves on; `note` blocks are written in her hand.
- **`desk.ts`**: the pins on the footer desk (her own pieces, palette chips, notes, the ಕವಲು word), each
  with a position, width, tilt and parallax depth. Only her own material goes here; reference images
  are never shown.
- **`onboarding.ts`**: the whole start-a-project flow: roads, questions, budget ranges, promises.

### Swapping in real pictures

Every picture is currently cut from screenshots of the old site, so they are small and marked
`placeholder: true`. While a picture is a placeholder, the site deliberately keeps it small (inside a
stamp) so it never looks blurry. To use a real file:

1. Put the original in `public/work/<project-slug>/` (JPG, PNG or WebP; a long edge of about 2400px is
   plenty, and Next.js makes the smaller sizes automatically).
2. In `projects.ts`, replace the stand-in's `img("…", "alt")` with
   `photo("/work/<slug>/<file>.jpg", width, height, "alt", "#tone")`, using the file's real pixel size.
   Real pictures are no longer placeholders, so covers open to full width with the scroll-expand
   effect, and "full" blocks run edge to edge.

`src/content/image-meta.json` holds the sizes of the current stand-ins. It can be regenerated or
edited by hand.

### Adding a project

Copy one of the objects in `projects.ts` and give it a new `slug`, its pictures and its `tone`:
- `bg` is the project's colour;
- `ink` is the text on it;
- `accent` is kept for its palette.

It then appears in `/work`, the album strip, the hero flip-book and the sitemap automatically. Its
colours are used only inside its own spread and case study (`BRAND_DESIGN.md` §4.4).

## Connecting the inbox ("Choose your road")

The form works with **nothing configured**. In development, briefs are written to
`.data/briefs.jsonl`. In production the API answers "not configured" and the form offers to send the
letter by email instead (the letter is pre-written). To receive briefs properly, copy `.env.example`
to `.env.local` and set:

1. **Resend** (email): `RESEND_API_KEY`, `BRIEF_TO_EMAIL`, `BRIEF_FROM_EMAIL`. Verify a sending
   domain such as `mail.studiokavalu.com` in Resend (it gives the SPF/DKIM DNS records). The studio
   gets every answer in a table, with reply-to set to the client. The client gets a short copy that
   never repeats what they typed.
2. **Spam**: `FORM_SIGNING_SECRET` (any long random string). Cloudflare Turnstile is optional:
   `NEXT_PUBLIC_TURNSTILE_SITE_KEY` + `TURNSTILE_SECRET_KEY`. Suspicious briefs are flagged `[check]`
   in the subject, not dropped.
3. **Booking and WhatsApp**: `NEXT_PUBLIC_CAL_LINK` (for example `studiokavalu/intro` on Cal.com, which
   is free) and `NEXT_PUBLIC_WHATSAPP_NUMBER`. They appear after sending and in the client's email.
4. **Google Sheet log** (optional): `SHEETS_WEBHOOK_URL`, `SHEETS_WEBHOOK_SECRET`.

Full research behind the flow: `../research/onboarding_research.md`.

## Deploying

Any Node host works. On **Vercel**, the free Hobby plan is for non-commercial use, so a studio site
belongs on Pro (or use Netlify). Set the environment variables there, point the domain, and set
`NEXT_PUBLIC_SITE_URL`.

## Motion and accessibility

- Smooth scroll (Lenis) is driven by GSAP's ticker, so ScrollTrigger and scrolling share one clock.
- **Motion is paper physics** (`BRAND_DESIGN.md` §9): pieces land, lift, are pressed, drawn, written
  and typed, once.
  - Her hand notes write themselves in word by word (`src/lib/handmade.ts`).
  - Typed captions type on.
  - Only the flip-book moves on its own, and it can be paused.
- **Every animation has a reduced-motion path:** no intro, no pinning or scrubbing, no flip-book, no
  writing or typing, instant page swaps. Everything is at rest from the first frame.
- The flip-book pauses on hover or focus, has a pause button, and stops when off-screen.
- The drawer and the mobile menu move focus in, trap it, close on Escape and give focus back.
- Chips in the form are real checkboxes and radios; errors are announced; focus moves to each step.
- Page transitions use React's `<ViewTransition>` (stamps morph into case-study covers).

## Fonts

- Her lettering (STUDIO / KAVALU and the K mark) is the logo, drawn as SVG
  (`src/components/brand/`); it is never typeset.
- **Gambetta** (display) and **Switzer** (text) are by Indian Type Foundry under the ITF Free Font
  License.
- **Courier Prime** (labels) is under the SIL OFL.

All three are self-hosted from `src/fonts/` (see `src/fonts/LICENSE-fonts.md`; do not put those files in
a public repository). Homemade Apple, Mrs Saint Delafield and Anek Kannada come from Google Fonts,
self-hosted by Next.js. Why these: `../research/type/TYPE_REVIEW.md`.

## Checking the site without a dev server

`../research/tools/preview.py` serves the production build from disk into a Chrome tab through the
DevTools Fetch domain, with no server process and no port. On top of it:
- `site_check.py` walks every page at desktop, mobile and reduced-motion sizes;
- `uniformity_audit.py` audits computed styles against the brand doc;
- `handwork_motion_check.py` measures the write and type motion frame by frame.

## Still to confirm with Ananya

- Her original logo files, if she has vectors, to compare with the rebuilt lettering.
- Original project images, a portrait, and her bio.
- Details for the snapshot projects (client, year, what was done).
- Budget ranges, "starts at" prices, reply and proposal promises, advance % (`onboarding.ts`).
- Instagram handle, WhatsApp number, Cal.com link (`site.ts` or env).
- Copy marked `confirm` in `site.ts` (service one-liners, process, bio) and the FAQ on `/studio`.
- The list of projects with notes, the reference videos and the scrapbook references she mentioned
  (the references stay inspiration, never content).
