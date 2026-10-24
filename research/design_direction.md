# Studio Kavalu: design direction (working draft)

## The idea in one line
**The crossroads album.** Kavalu (ಕವಲು) is the point where paths meet and split. The site is Ananya's working
album of choices: every project is collected like a stamp, opened like a spread, annotated in her hand, and
filed under folder tabs. One hairline "road" runs through the site and forks where chapters begin.

Why this and not a template studio site: the best studio sites (Pentagram, Koto, Collins, Here, Base) share
three things - they lead with work, they say one thing with confidence, and they own one signature interaction
(Obys' viewfinder, Pentagram's sentence filter, Mother's desktop toolbar). Kavalu's signature is the
crossroads itself: things meeting, splitting and becoming something new, expressed in motion.

## Three motifs, used with restraint
1. **The road** - a 1px plum line that draws as you scroll and forks at section starts. Also the preloader,
   the services diagram ("four roads") and the onboarding progress.
2. **The stamp** - perforated postage-stamp frames for project images (from the Pinterest "Stamp Series"
   landing reference: colour stamp over a duotone twin, flip-book cycling). Stamps are things you collect,
   carry a mark of where they came from, and travel between places - a good metaphor for a studio's work.
3. **The folder tab** - tabbed paper for navigation and the footer, refined from the current site's tabs
   and the Bravora reference.

Ephemera (paper clips, washi tape, handwritten margin notes, typewriter labels, round stickers with
circular Kannada + English text) appear at most once per screen outside the scrapbook. The work carries the
page; the ephemera frame it.

## Palette (unchanged from the current site)
| Token | Hex | Use |
|---|---|---|
| cream | #F3F3E7 | paper, default background |
| oxblood | #491C17 | warm dark panels, overview cards |
| plum | #390D26 | ink for display type, buttons, the road |
| deep plum | #270617 | footer, scrapbook desk |
| powder blue | #ABCDD6 | accent paper, index cards, the footer wordmark |
Project pages wear their own palette (Anokhi terracotta, Nivritti navy) so the work changes the room.

## Homepage, top to bottom
1. **Intro** (first visit, ~1.4 s): a line draws up the page and forks; ಕವಲು appears at the fork; then lifts away.
2. **Hero**: "Every brand hits a *crossroads.* We help you choose the *road.*" beside an album page of
   stamps. The centre stamp is a flip-book of her work (colour above, plum duotone twin below).
   On scroll (pinned): headline lifts, satellite pieces drift apart along their own paths, the centre stamp
   expands to fill the screen and becomes the first project's colour.
3. **Project spreads**: each featured project is a full-screen spread in its own colour; its images deal
   out from a stack into a collage as you scroll in (paths splitting), title in large serif, metadata on a
   typewriter label. Leaving a spread zooms it out slightly while the next slides over it.
4. **Manifesto**: "A brand is a set of choices..." revealed word by word, with tiny inline image pills
   after "what it says / how it looks / where it shows up / who it speaks to".
5. **Four roads** (services): one line forks into four; each road ends at an index card (Branding,
   Visual identity, Social media, Film & photography), each a "choice". "Start here" pre-fills onboarding.
6. **From the scrapbook**: a loose pile of references and notes on a plum desk you can push around;
   "Open the scrapbook".
7. **Founder**: Ananya, duotone circle portrait, the quote, short bio.
8. **Choose your road** (instant onboarding): the four roads as chips, inline on the page; Continue opens
   the five-step flow in a drawer with the choice carried over. *Changed after the onboarding research:*
   ordinary labelled questions (sentence-style blanks test poorly for accessibility), while the letter to
   Ananya writes itself beside them and becomes the review step; on send it folds into an envelope and
   gets stamped with a reference. Book a call / WhatsApp / email alongside.
9. **Footer**: folder tabs, contact, live Bengaluru time, the giant STUDIO KAVALU wordmark.

## Other pages
- **/work** - Stamps view (perforated grid) and Index view (rows; hovering shows the stamp following the
  cursor, slightly turned like a photo held up). Filter by road.
- **/work/[slug]** - cover expands from its stamp; overview card; content blocks (text, full, pair,
  stamps, palette, margin note); next project at the foot.
- **/studio** - the definition, manifesto, four roads in depth, process (Listen, Map, Make, Launch) on a
  drawn road, the founder, FAQ.
- ~~**/scrapbook**~~ *(removed in v2, 24 Oct: the client asked for the scrapbook to be the format of
  the whole site, not a page; its desk became the footer's "What we pin above the desk", holding only
  her own material.)*
- **/start** - the onboarding letter full page, with optional extra detail.

## Motion principles
Weighting: Jakub (production polish) primary, Jhey (playful) secondary for the scrapbook and the
envelope moment, Emil (restraint) for navigation and forms.
- Lenis smooth scroll synced to the GSAP ticker; native scroll on touch.
- Enter: opacity + 12px rise + 4px blur, 0.7-0.9 s, ease `expo.out` (cubic-bezier(0.16, 1, 0.3, 1)).
- Exits subtler than entries. No looping attention-seekers.
- Scroll-scrubbed only where the scroll *is* the story (hero expansion, spreads, the road drawing).
- Everything has a `prefers-reduced-motion` path: no pinning, no scrub, simple fades, static flip-book.
