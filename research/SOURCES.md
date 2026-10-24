# Studio Kavalu — sources

*Every website, page and document the research and design drew on, with links. Built 2026-10-24 from the
capture log (`screens/results.jsonl`), the curated list (`reference_sites.json`), the review notes
(`notes_screens.md`), `motion_catalog.md` and `onboarding_research.md`.*

- **226 websites** were opened in the persistent Chrome (CDP, port 9333) at 1440×900 and captured at three
  scroll depths: `screens/<slug>_0/1/2.jpg`, contact sheets `sheets/sheet_01–57.jpg`. (Mucho appears
  under two domains, so 225 distinct studios.)
- "Stack" is what the page exposed at runtime (framework, GSAP, Lenis, WebGL canvas, video). Bundled
  libraries can hide, so treat it as a floor.

## 1. Where each idea on the site came from

| Idea on the Kavalu site | Sources it was drawn from |
|---|---|
| Stamp motif (perforated frames, colour stamp + duotone twin, flip-book) | [Jacob Hutch — Stamp Series (the client's Pinterest pin)](https://in.pinterest.com/pin/681873199876372589/), [jacobhutch.com](https://www.jacobhutch.com), [Niccolò Miranda — The Paper Portfolio](https://www.niccolomiranda.com/), [Digital Stamp Collection](https://marijanapav.com/stamps) |
| Work first; several views of one collection (stamps ↔ index, filters) | [Pentagram](https://www.pentagram.com), [Base Design](https://www.basedesign.com), [Porto Rocha](https://portorocha.com), [Obys](https://obys.agency), [Olivier Larose](https://www.olivierlarose.com), [Studio Feixen](https://www.studiofeixen.ch/) |
| One confident serif statement with italic emphasis | [Collins](https://www.wearecollins.com), [Here Design](https://www.heredesign.co.uk), [Perky Bros](https://perkybros.com/), [Present](https://www.presentstudio.co/), [Heure Bleue](https://heurebleue.studio/), [Little Plains](https://www.littleplains.com/) |
| Folder tabs (footer, menu) | Her current site's footer; [Mother Design](https://www.motherdesign.com) (desktop toolbar) |
| Live Bengaluru clock in the chrome | [Koto](https://koto.studio), [Porto Rocha](https://portorocha.com), [Boc.Studio](https://boc.studio/), [Commission Studio](https://www.commission.studio/) (live temperature) |
| Torn paper edges, paper as a premium material | [Commission Studio](https://www.commission.studio/), [14islands](https://www.14islands.com), [Immersive Garden](https://immersive-g.com) |
| Pinboard / desk of pinned material (footer) | [LRNCE](https://lrnce.com/) (moodboard hero), [Studio Namma](https://studionamma.com/) (cut-outs + stickers), [Mother Design](https://www.motherdesign.com) (sticky note), [Mr. Panda's Paper Portfolio](https://www.mr-pandas-psychologically-safe-portfolio.com/), [Collage Department](https://collagedepartment.com/) |
| Project spreads in each client's own colours | [Koto](https://koto.studio), [Collins](https://www.wearecollins.com), [Wolff Olins](https://www.wolffolins.com) (case cards), [Perky Bros](https://perkybros.com/) |
| Palette chips with names on case studies | [East Fork — The Palette](https://eastfork.com/) |
| Typewriter / mono captions and bracketed labels | [Quatrième Étage](https://quatriemeetage.studio/), [Odds Studio](https://odds-studio.com/), [Lundgren+Lindqvist](https://lundgrenlindqvist.se) |
| Kannada used as a brand script | [Subko](https://subko.coffee) (multi-script marquee incl. ಸಬ್ಕೊ) |
| Hero stamp expanding to full screen on scroll | [React Bits — scroll expand](https://reactbits.dev/animations/scroll-expand), [Exo Ape](https://exoape.com), [Rejouice](https://www.rejouice.com) |
| Pictures dealing out of a pile into a collage | [Codrops — entrance animation for images](https://tympanus.net/Development/EntranceAnimationForImages/) |
| Spreads zooming out as the next stacks over | [Codrops — sticky sections](https://tympanus.net/Development/StickySections/) |
| Manifesto words inking in | [Codrops — on-scroll text highlight](https://tympanus.net/Development/OnScrollTextHighlight/), [JKR](https://www.jkrglobal.com) |
| Stamp → case-study cover morph, page transitions | [Next.js — view transitions guide](https://nextjs.org/docs/app/guides/view-transitions), [React ViewTransition](https://react.dev/reference/react/ViewTransition) |
| Draggable desk with inertia | [Codrops — infinite parallax grid](https://tympanus.net/codrops/2025/06/11/building-an-infinite-parallax-grid-with-gsap-and-seamless-tiling/), [Osmo — draggable stickers](https://www.osmo.supply/resource/draggable-stickers) |
| Letter that folds into a stamped envelope | [Paperlab](https://paperlab.nawwara.studio/), [Digital Stamp Collection](https://marijanapav.com/stamps) (postcard form) |
| "Start a project" in the nav; booking + WhatsApp | [Perky Bros](https://perkybros.com/), [Poch](https://poch.studio/), [Wishbox](https://wishboxstudio.in/), [Confetti](https://www.confetti.design/), and `onboarding_research.md` §8 |
| Restraint rules (what not to do) | Discount pop-ups on [Fishwife](https://eatfishwife.com), [Brightland](https://brightland.co), [Ghia](https://drinkghia.com); preloaders on [Locomotive](https://locomotive.ca), [Made Thought](https://www.madethought.com); `motion_catalog.md` §7 anti-list |

## 2. All 226 captured websites

### A. Boutique and founder-led studios (46)

| Site | Link | Stack | Notes |
|---|---|---|---|
| A Practice for Everyday Life (London, UK) | https://www.apracticeforeverydaylife.com/ | next | one project per screen, caption only. |
| Agence Foudre (Paris, France) | https://www.agencefoudre.com/ | lenis, canvas, video | loud colour blocks, social-first agency (the "fun" direction to avoid). |
| B&B Studio (London, UK) | https://bandb-studio.co.uk/ | wordpress, video | packaging-first; cookie banners and "Let's chat" CTAs. |
| Beth-Emily (Melbourne, Australia) | https://www.beth-emily.com/ | webflow, gsap, scrolltrigger, splitting | floating pill navigation; Poch puts "Get started" and |
| Bielke&Yang (Oslo, Norway) | https://bielkeyang.com/ | canvas, video | one-line statements, archive-like project strips. |
| Boc.Studio (Barcelona, Spain) | https://boc.studio/ | next, lenis, swup, canvas, video | live CET clock and "online" status in the top bar; dense filterable work grid. |
| Bureau Borsche (Munich, Germany) | https://bureauborsche.com/ | video | archive mosaics; volume of work as the statement. |
| Christopher Doyle & Co (Sydney, Australia) | https://christopherdoyle.co/ | nuxt | Founder-led identity studio; minimal Nuxt site with just projects and profile. |
| Commission Studio (London, UK) | https://www.commission.studio/ | next, locomotive | a tiny pill header with the live temperature ("12°C"); images revealed |
| DutchScot (London, UK) | https://dutch.scot/ | wordpress, video | Hospitality-heavy portfolio (restaurants, cafes, hotels); video intro, long scrolling project index. |
| Folch (Barcelona, Spain) | https://www.folchstudio.com/ | nuxt, video | archive mosaics; volume of work as the statement. |
| Glasfurd & Walker (Vancouver, Canada) | https://glasfurdandwalker.com/ | nuxt, barba, video | Restaurant, hotel and F&B brand worlds; giant condensed serif word lists, Barba transitions. |
| Goodside | https://www.goodside.studio/ | video | serif wordmark over a scattered collage of real objects; centred serif manifesto. |
| Happy Happy Creative | https://www.happyhappycreative.com/ | squarespace, barba | "Brand and Content for Founder-led Brands": cream/olive/powder-blue |
| HATO (London, UK) | https://hato.co/ | — | Black minimal shell with store and publishing; experimental, archive-style project index. |
| Here Design (London, UK) | https://www.heredesign.com/ | next, video | "Here." in huge Baskerville; serif italics for emphasis (closest big-agency tone). |
| Heure Bleue (Hautes-Alpes, France) | https://heurebleue.studio/ | nuxt, lenis, video | giant serif lines ("du beau et du bon") between films. |
| Hey (Barcelona, Spain) | https://heystudio.es/ | wordpress | Founder-led; homepage is a playable Pong game, colourful illustrative identity work. |
| Little Plains (New York, USA) | https://www.littleplains.com/ | next, lenis, canvas, video | centred serif paragraph, clients grouped by era, an "Ask" pill. |
| Lotta Nieminen Studio (New York, USA) | https://www.lottanieminen.com/ | — | Founder-led; split-screen full-bleed product and fashion photography with minimal (S)/L.N. labels; work leads. |
| Maison AUGE | https://maisonauge.com/ | next, video | giant wordmark over film, marquee strap. |
| Meor Studio (St Ives, Cornwall, UK) | https://meorstudio.co.uk/ | wordpress, locomotive, video | hospitality brand + social agency; services list as large type. |
| Mucca (New York, USA) | https://www.mucca.com/ | squarespace | Food, drink and hospitality branding; condensed bold headline, Squarespace image grid. |
| Nido Creative Studio (Oslo, Norway) | https://www.nidocreativestudio.com/ | wix, video | Identity + photography for restaurants and makers; blush tones, soft macro imagery. |
| Odds Studio (Paris, France) | https://odds-studio.com/ | wordpress, gsap | typewriter copy, a mark with a pixel car driving across it; portfolio on request. |
| Ofform (Paris, France) | https://offormdesign.com/ | framer | Editorial Paris studio; full-bleed outdoor poster photography, curated 'selected works' list. |
| OK-RM (London, UK) | https://www.ok-rm.co.uk/ | next | one-line statements, archive-like project strips. |
| Perky Bros (Nashville, USA) | https://perkybros.com/ | wordpress | cream, one large serif paragraph, "START A PROJECT" in the nav, full-bleed project |
| Poch Studio | https://poch.studio/ | framer, video | 'Studio of a few friends'; Framer site with custom cursor and video-heavy project grid. |
| Present | https://www.presentstudio.co/ | next, video | serif statement for e-commerce brands, cookie bar, case cards with serif titles. |
| Quatrième Étage | https://quatriemeetage.studio/ | next, lenis, video | typewriter-style bracketed captions ("[ THOOK ] an album cover..."). |
| Robot Food (Leeds, UK) | https://www.robot-food.com/ | barba | packaging-first; cookie banners and "Let's chat" CTAs. |
| République Studio (Paris, France) | https://www.republique.studio/ | video | Art-direction duo; minimal white shell with highlights/index toggle and filterable categories. |
| Savvy Studio (Mexico City, Mexico) | https://savvy-studio.net/ | squarespace | Hospitality/lifestyle (Casa Bosques); off-white gallery, single centered image, small caps captions. |
| smalltribe (Leipzig, Germany) | https://smalltribe.studio/ | framer, video | Framer, calm, numbered sections ("ST/01"). |
| Smörgåsbord (Amsterdam / Cardiff) | https://smorgasbord.studio/ | video | Duo-led; classical bust over huge type, Astro site with 190+ images. |
| Studio Feixen (Lucerne, Switzerland) | https://www.studiofeixen.ch/ | wordpress, video | archive mosaics; volume of work as the statement. |
| Studio Frith (London, UK) | https://studiofrith.com/ | video | Frith Kerr's founder-led studio; kinetic typographic intro, video-led work. |
| Studio GD (Copenhagen, Denmark) | https://www.studiogd.dk/ | webflow, video | Motion-led identities; text-first home that opens into dense video work grid. |
| Studio Gruhl (Berlin, Germany) | https://www.studiogruhl.com/ | next, lenis, canvas, video | Subculture-rooted studio; dark video hero, marquee, index/projects toggle. |
| Studio Mut (Bolzano, Italy) | https://www.studiomut.com/ | next, video | one-line statements, archive-like project strips. |
| Studio OL (Los Angeles, USA) | https://ol.studio/ | next, lenis | cream, small serif, editorial lifestyle photography, signature logo. |
| StudioBand (Adelaide, Australia) | https://www.studioband.com.au/ | next | Dark editorial grid with red type, project tiles and search prompt overlay. |
| Super Keen (New York, USA) | https://www.superkeen.studio/ | next | Independent culture studio; live NYC clock, image strip, annual report and news posts. |
| Toormix (Barcelona, Spain) | https://toormix.com/ | nuxt, wordpress, video | one-line statements, archive-like project strips. |
| Unspoken Agreement | https://www.unspokenagreement.com/ | next, video | floating pill navigation; Poch puts "Get started" and |

### B. Indian design studios (24)

| Site | Link | Stack | Notes |
|---|---|---|---|
| Animal (New Delhi, India) | https://www.weareanimal.co/ | squarespace, video | Independent agency (Delhi/NY/Toronto); bold 'Relevance is ruthless' headline over video case studies. |
| Beyondesign (Mumbai, India) | https://beyondesign.in/ | framer, lenis | red hero "Communicative design is our language", client-logo wall. |
| Bombay Duck Designs (Mumbai, India) | https://www.bombayduckdesigns.com/ | wordpress | Sibling-run; green flower badge, big-type project index with inline book/object images. |
| Codesign (Gurugram, India) | https://www.codesign.in/ | wordpress | dense, colourful case-study grid (Superyou, Royal Enfield, Licious, PhonePe). |
| Confetti Design (Mumbai, India) | https://www.confetti.design/ | webflow, wordpress, gsap, scrolltrigger, lenis, video | Retail/D2C branding and packaging; 400+ image portfolio, Lenis + GSAP. |
| designmill (India) | https://www.designmill.in/ | gsap, scrolltrigger, lenis | cream, italic serif services list, "We lead human-centered businesses...". Closest |
| Elephant Design (Pune, India) | https://elephantdesign.com/ | squarespace, video | Veteran design-innovation firm; dark gradient hero with oversized headline. |
| Itu Chaudhuri Design (New Delhi, India) | https://icdindia.com/ | next, wordpress, video | Identity/editorial studio; warm blush hero with identity marks, yellow hatched rule. |
| KL11 (Kozhikode, India) | https://kl11.in/ | video | logo |
| LOCAL (India) | https://www.wedesignlocal.com/ | wix | 'Nomadic' studio rooted in local stories; colourful illustrated packaging thumbnails. |
| Locopopo (Mumbai, India) | https://locopopo.com/ | squarespace | illustration-led identity and packaging. |
| Lopez Design (Gurugram, India) | https://thisislopez.com/ | wordpress, gsap, scrolltrigger, pixi, video | Large-scale brand consultancy; full-bleed red hero, ScrollTrigger reveals, image-heavy work grid. |
| November (Mumbai, India) | https://www.nvmbr.in/ | nuxt, video | yellow info panel, project carousel, custom type. |
| Opposite (Goa, India) | https://oppositehq.com/ | — | Swiggy/Sugar/Simba identities; giant outlined wordmark, clean case list. |
| Squadron 14 (New Delhi, India) | https://squadron14.com/ | webflow, gsap, scrolltrigger | logo |
| Studio ABD (Bengaluru, India) | https://studioabd.in/ | wix, video | logo |
| Studio Bigfat (Mumbai, India) | https://studiobigfat.com/ | cargo | Cargo, black, packaging-heavy grid (Subko Cacao, Nike Diwali). |
| Studio N°7 (Studio Number Seven) (India) | https://www.studionumberseven.com/ | wix, video | Founder's friend's studio. Live page is 'Coming Soon'; distressed serif on paper texture. Instagram @studionumberseven_. |
| Studio Ping Pong (Bengaluru, India) | https://studiopingpong.com/ | wordpress, gsap, scrolltrigger, canvas, video | yellow, pixel creature, serif "tiny-mighty" statement. |
| Studio Sorted (Bengaluru, India) | https://www.studiosorted.com/ | webflow, video | yellow, mascot illustration, "Branding for the Seriously Fun.", |
| The Turtle Story (Mumbai, India) | https://www.theturtlestory.com/ | next, squarespace | logo |
| Therefore Design (Pune, India) | https://www.thereforedesign.co.in/ | wix, video | FMCG packaging agency; video hero, packaging tools and quizzes. |
| Whoamama (Chennai, India) | https://whoamama.com/ | next | logo |
| Wishbox Studio (Delhi, India) | https://wishboxstudio.in/ | wordpress, gsap, scrolltrigger | Branding + PR for hospitality and F&B; GSAP scroll sections, marquee client wall. |

### C. Established branding agencies (31)

| Site | Link | Stack | Notes |
|---|---|---|---|
| &Walsh (New York, USA) | https://andwalsh.com/ | video | Jessica Walsh; chrome ampersand, saturated portrait photography, WebGL bits. |
| Anagrama (Mexico City, Mexico) | https://www.anagrama.com/ | — | 'Online showroom' with live clock; dense multi-column project grid. |
| Base Design (Brussels / New York) | https://www.basedesign.com | next, video | Feed / Projects / Index toggle; feed is an archive mosaic. Proof that a studio can |
| Bibliotheque | https://www.bibliothequedesign.com | video |  |
| Collins (New York / San Francisco) | https://www.wearecollins.com | nuxt | one centred serif line ("Rewrite your worth."), awards as tiny bracketed tags, then |
| DixonBaxi (London, UK) | https://www.dixonbaxi.com | next | "Ask us anything." prompt as the hero and an endless horizontal rail of work cards |
| Gretel (New York, USA) | https://gretelny.com | squarespace | tiny type, big images, asymmetrical editorial grid, Squarespace. |
| Here Design | https://www.heredesign.co.uk | next, video | "Here." in huge Baskerville; serif italics for emphasis (closest big-agency tone). |
| Instrument | https://www.instrument.com | nuxt | giant wordmark, colour-blocked sections, filter chips for work. |
| JKR (London / global) | https://www.jkrglobal.com | next, video | statement paragraphs that light up line by line as you scroll (opacity scrub). |
| Kontrapunkt | https://www.kontrapunkt.com | next, lenis, video | serif statement + isometric illustration. Lenis. |
| Koto | https://koto.studio | next, video | full-bleed film hero, live local clock in the nav, one large statement paragraph, sticky |
| Koto (London / global) | https://koto.com/ | next, video | full-bleed film hero, live local clock in the nav, one large statement paragraph, sticky |
| Lundgren+Lindqvist | https://lundgrenlindqvist.se | wordpress, video | dense image grid, typewriter/mono captions. |
| Made Thought (London / New York) | https://www.madethought.com | wordpress, barba, video | giant serif wordmark on white; long intro. |
| Manual (San Francisco, USA) | https://manual.studio/ | astro, video | Serif manifesto headline over product imagery; Astro + Sanity. |
| Mother Design (London / New York) | https://www.motherdesign.com | next | toolbar navigation like a desktop OS, giant name, horizontal strip of floating |
| Mucho (Barcelona / SF / NY) | https://wearemucho.com/ | gsap, scrolltrigger, lenis, video | Full-bleed kinetic type video, Lenis + Barba transitions. |
| Mucho | https://mucho.ws | — |  |
| Mythology | https://www.mythology.com | next, video | one word per screen ("WE"), then full-bleed films. |
| Order (New York, USA) | https://order.design/ | — | Cargo site; dark UI with filterable identity/packaging/website tabs (Salt Lick tea). |
| Pearlfisher | https://www.pearlfisher.com | wordpress, gsap, lenis, video | illustrated hero, grey-to-white statement reveal on scroll, case cards with tags. |
| Pentagram (London / New York) | https://www.pentagram.com | gsap, barba, video | work-first. Plain grid of projects, tiny captions, and a sentence used as the filter |
| Porto Rocha | https://portorocha.com | nuxt | dashboard: live clock + city, collapsible project list, news cards. Dense but ordered. |
| Ragged Edge (London, UK) | https://www.raggededge.com/ | lenis, canvas, video | WebGL/canvas intro, Barba page transitions, bold typographic case studies. |
| Snask (Stockholm, Sweden) | https://www.snask.com | wordpress, video | loud and playful; pink sections; personality in copy ("SNASK OFF!"). |
| Studio Dumbar (Rotterdam, Netherlands) | https://studiodumbar.com | gsap, scrolltrigger, lenis, video | full-screen 3D/motion pieces, one per viewport. Lenis + GSAP ScrollTrigger. |
| Turner Duckworth (London / San Francisco) | https://www.turnerduckworth.com/ | next | Red duotone overlay on packaging grid; huge condensed wordmark. |
| Two Times Elliott | https://www.twotimeselliott.com | — |  |
| Universal Favourite (Sydney, Australia) | https://www.universalfavourite.com.au/ | gsap, lenis, video | Serif statement, iridescent 3D sphere, Lenis + Swup page transitions. |
| Wolff Olins (London / New York) | https://www.wolffolins.com | next, video | full-bleed video hero, serif statement with underlined key words, case cards with |

### D. Motion-led and award-winning studios (35)

| Site | Link | Stack | Notes |
|---|---|---|---|
| 14islands (Stockholm, Sweden) | https://www.14islands.com | next, lenis, canvas, video | big split type; *paper cut-out collage* of images and torn sheets in the second |
| Active Theory (Los Angeles, USA) | https://activetheory.net | canvas, video | WebGL showpieces (Locomotive's capture caught only the |
| Akaru (Lyon, France) | https://www.akaru.fr/ | nuxt, lenis, canvas, video | Awwwards SOTM; WebGL + Nuxt, split-panel loader, motion-rich Lyon agency site. |
| Antinomy | https://antinomy.studio | next, wordpress, canvas, video |  |
| Aristide Benoist | https://aristidebenoist.com | canvas |  |
| Basement Studio (Buenos Aires, Argentina) | https://basement.studio | next, gsap, canvas | Dark, WebGL 3D, lab section; playful dev-led interactions. |
| Buck | https://buck.co | next |  |
| Chipsa | https://chipsa.design/ | next, lenis, canvas, video | WebGL/3D/CGI-led studio; elaborate animation per project. |
| Cuberto (USA) | https://cuberto.com | astro, lenis, video | big centred headline, service accordion cards, logo wall; Lenis. |
| Darkroom Engineering | https://darkroom.engineering | next, gsap, scrolltrigger, lenis, three, video |  |
| Dennis Snellenberg | https://dennissnellenberg.com | gsap, scrolltrigger, locomotive, barba |  |
| Dogstudio (Namur, Belgium / Chicago, USA) | https://dogstudio.co | wordpress, canvas | Awwwards SOTM; dog-mascot loader, dark cinematic case studies. |
| Exo Ape | https://exoape.com | nuxt, video | giant type sliding over full-bleed photography, images scattered on white below. |
| Fiddle.Digital | https://fiddle.digital/ | nuxt, canvas, video | Awwwards portfolio winner; makers of StringTune scroll library, smooth index. |
| Hello Monday | https://hellomonday.com | canvas, video |  |
| Igloo Inc | https://www.igloo.inc | — |  |
| Immersive Garden (Paris, France) | https://immersive-g.com | nuxt, canvas | embossed paper relief in WebGL, serif statements. Paper as material, done |
| Locomotive (Montréal, Canada) | https://locomotive.ca | locomotive, canvas, video | WebGL showpieces (Locomotive's capture caught only the |
| Lusion (Bristol, UK) | https://lusion.co | astro, canvas | WebGL showpieces (Locomotive's capture caught only the |
| Makemepulse (Paris, France) | https://www.makemepulse.com/ | nuxt, lenis, canvas | three.js + GSAP + Lenis; immersive case studies. |
| Merci-Michel (Paris, France) | https://www.merci-michel.com/ | wordpress, three, canvas | Gamification/advergame studio; WebGL playful interactions. |
| Noomo Agency (Los Angeles, USA) | https://noomoagency.com/ | nuxt, canvas, video | Awwwards Site of the Year list; 3D storytelling, ScrollTrigger scenes. |
| Obys (Kharkiv, Ukraine / EU) | https://obys.agency | canvas | vertical film strip of small images in the centre, with a bracket "viewfinder" that frames |
| Phantom (London, UK / Auckland, NZ) | https://www.phantom.land/ | next, canvas | Awwwards portfolio winner; WebGL kinetic grids that evolve on scroll. |
| Rejouice (Paris, France) | https://www.rejouice.com | nuxt, lenis, video | giant wordmark; showreel card expands; Lenis. |
| Resn (Wellington, New Zealand) | https://resn.co.nz | three, canvas | Awwwards SOTM; refractive 3D crystal intro, experimental interactions. |
| Salt and Pepper | https://snp.agency/ | next, canvas | Awwwards portfolio winner; three.js/WebGL, GSAP, Webflow. |
| Studio Freight | https://studiofreight.com/ | nuxt, lenis | Scattered off-white masonry of project images, serif tagline; Lenis smooth scroll. |
| Studio Namma (Paris, France) | https://studionamma.com/ | webflow, gsap, scrolltrigger, lenis, splitting, video | cut-out photo collage with stickers, WhatsApp button, live clock. |
| Studio Null | https://www.madebynull.com/ | webflow, video | Awwwards portfolio winner; glass 3D prism, WebGL, experimental type specimens. |
| Synchronized | https://synchronized.studio/ | nuxt, gsap, pixi, canvas | Awwwards Site of the Year list; WebGL, percentage loader, marquee. |
| The Line Studio (London, UK) | https://thelinestudio.com/ | nuxt, lenis, video | Awwwards SOTM; animation studio, full-bleed animated reel, Lenis scroll. |
| Unseen Studio (Bristol, UK) | https://unseen.co | wordpress, canvas | Awwwards SOTM; WebGL canvas, soft pastel loader, motion-rich case studies. |
| Utsubo | https://www.utsubo.com | astro, lenis, canvas, video |  |
| Watson (Los Angeles, USA) | https://watson.la/ | canvas | Awwwards SOTM; canvas-rendered, minimal LA studio site. |

### E. Tactile, collage, scrapbook and editorial sites (36)

| Site | Link | Stack | Notes |
|---|---|---|---|
| Adrien Lamy (Paris, France) | https://adrienlamy.fr/ | canvas, video | Creative developer; collage layouts and bold type (Muzli). |
| Aimee Xu's Papercraft World | https://aimees-papercraft-world.com/ | lenis, canvas | Awwwards SOTD; textured kraft papers, torn edges, three.js papercraft scenes. |
| Apartamento (Barcelona, Spain) | https://www.apartamentomagazine.com | wordpress, video | magazine calm; Apartamento opens with a newsletter modal. |
| Aralesk — Collages & Motion (Spain) | https://www.aralesk.es/ | gsap, three, canvas, video | Collage artist; three.js/GSAP animated collage pieces. |
| Are.na | https://www.are.na | next | 'Toolkit for assembling new worlds from scraps'; moodboard/channel metaphor. |
| Beci Orpin (Melbourne, Australia) | https://beciorpin.com/ | — | Hand-made textured illustrated objects floating on pale yellow; hidden pet-rock game. |
| Chrissie Abbott | https://chrissieabbott.com/ | cargo | Retro emoji nav, collage-like image grid, Cargo draggable layout. |
| Collage Department | https://collagedepartment.com/ | video | picture research, collages and creative direction for brands' social |
| Cosmos (New York, USA) | https://www.cosmos.so | next, canvas, video | Moodboard platform; search by colour, collections of saved images. |
| davesocozy (Philadelphia, USA) | https://davesocozy.com/ | next, canvas | Handmade collage artist; explorable 3D room of objects, 'a table to cut your own'. |
| Deem Journal | https://www.deemjournal.com/ | cargo | Design journal on Cargo; full-bleed photo heroes, stories, symposium. |
| Emergence Magazine | https://emergencemagazine.org/ | — | Illustrated, immersive long-form stories; Barba transitions. |
| Field Notes (Chicago, USA) | https://fieldnotesbrand.com/ | — | Memo-book brand with kraft covers; tactile product storytelling. |
| Grit Pictures | https://grit.pictures/ | wordpress, canvas | Sticker-outlined cut-out illustrations on black; scrapbook/tattoo-flash collage. |
| hi, 6 — Scrapbook (Hicard Studio) | https://scrapbook.hicard.studio/ | framer | Literal digital scrapbook: scanned tickets and paper ephemera for a studio's 6th anniversary. |
| Hole & Corner (London, UK) | https://www.holeandcorner.com/ | next, wordpress, video | Craft and heritage magazine; maker stories, food, travel. |
| Ikai Asai (India) | https://www.ikaiasai.com/ | wordpress, video | Indian art, craft and design editorial platform; clean editorial grid. |
| KARO (New York, USA) | https://www.karocrafts.com/ | nuxt, canvas | Artist/designer shop; tactile, handmade aesthetic, smiley loader, Shopify. |
| Katrine Mehl (Denmark) | https://katrinemehl.com/ | — | Paper metaphor: a smooth sheet crumples as you scroll. |
| Kinfolk (Copenhagen, Denmark) | https://www.kinfolk.com | wordpress, lenis, video | magazine calm; Apartamento opens with a newsletter modal. |
| Lynn and Tonic (Phoenix, USA) | https://lynnandtonic.com | — | Annual handcrafted redesigns; paper-texture backdrop, serif title, numbered menu. |
| Miranda — Paper Portfolio (Amsterdam, Netherlands) | https://www.niccolomiranda.com/ | webflow, gsap, locomotive, canvas | Awwwards SOTM; tilted newspaper-paper layout, drag sideways to browse. |
| mmm.page | https://mmm.page/ | — | Drag-and-drop scrapbook-style site builder; marker-swash wordmark, scattered objects. |
| Mr. Panda's Paper Portfolio | https://www.mr-pandas-psychologically-safe-portfolio.com/ | canvas | lined notebook paper, handwriting, sticky "About me" note; the |
| MSCHF | https://mschf.com | nuxt |  |
| Openhouse Magazine (Barcelona, Spain) | https://openhouse-magazine.com/ | wordpress | Art/design/culture magazine; image-led editorial stories, shop and studios. |
| Paper Tiger | https://www.papertiger.com/ | — | Awwwards SOTD; layered coloured paper sheets, bold condensed type. |
| Ponpon Mania | https://ponpon-mania.com/ | nuxt, canvas | Awwwards SOTM; interactive comic, WebGL hand-drawn chapters. |
| Poolsuite | https://poolsuite.net | video | Retro Mac-style desktop: windowed player on pastel background. |
| PostHog | https://posthog.com/ | — | Full desktop-OS metaphor: app icons and windows on illustrated grass wallpaper. |
| Present & Correct (London, UK) | https://www.presentandcorrect.com/ | shopify | Stationery shop: paper clips, typewriters, ephemera flatlays; exactly the brief's props. |
| Steph Jeong Scrapbook (Brooklyn, USA) | https://jeongsteph.design/ | nuxt, canvas, video | Designer portfolio framed as 'Scrapbook '20'; 'draw me a stache' doodle interaction. |
| Teenage Engineering | https://teenage.engineering | — |  |
| The Gentlewoman | https://thegentlewoman.co.uk | — |  |
| Tim Van Damme (Max Voltar) | https://timvandamme.com/ | — | Photocopied-zine one-pager: textured paper, halftone photos, red-marker doodles. |
| Working Stiff Films | https://stiff.madebybuzzworthy.com/ | gsap, scrolltrigger, splitting, video | Cream paper-textured background, script logo, draggable work strip. |

### F. Like-minded lifestyle, food and craft brands (29)

| Site | Link | Stack | Notes |
|---|---|---|---|
| Aesop | https://www.aesop.com | video |  |
| ARAKU Coffee (Bengaluru, India) | https://www.arakucoffee.in/ | shopify, splitting, video | Huge serif wordmark over misty valley video; seed-to-cup story. |
| Bhaane (Mumbai, India) | https://www.bhaane.com/ | — | Colour-block fashion editorial; has a 'zine' section. |
| Blue Tokai | https://bluetokaicoffee.com | shopify, video |  |
| Bombay Perfumery (Mumbai, India) | https://www.bombayperfumery.com | shopify | Soft, airy product still-lifes on wood; restrained luxury. |
| Bombay Sweet Shop (Mumbai, India) | https://bombaysweetshop.com | shopify, splitting | Indian craft and lifestyle |
| Brightland | https://brightland.co | shopify | D2C food brands with strong illustration and |
| Diaspora Co (Oakland, USA) | https://www.diasporaco.com | shopify, lenis, taxi | Indian craft and lifestyle |
| Doodlage (New Delhi, India) | https://doodlage.in/ | shopify | Indian craft and lifestyle brands; rich photography, |
| East Fork (Asheville, USA) | https://eastfork.com/ | next, shopify | "The Palette": named glaze swatches (Morel, Malt, Nocturne) - the same idea as the |
| Fishwife | https://eatfishwife.com | shopify | D2C food brands with strong illustration and |
| Ghia (USA) | https://drinkghia.com | shopify, video | D2C food brands with strong illustration and |
| Good Earth (New Delhi, India) | https://www.goodearth.in | canvas | Indian craft and lifestyle |
| Graza (USA) | https://www.graza.co | shopify, pixi, video | D2C food brands with strong illustration and |
| Heath Ceramics (Sausalito, USA) | https://www.heathceramics.com/ | shopify | Ceramics and tile; warm editorial table scenes. |
| Jacquemus | https://www.jacquemus.com | video |  |
| Kama Ayurveda | https://www.kamaayurveda.com | next |  |
| LRNCE (Marrakech, Morocco) | https://lrnce.com/ | wordpress | the hero is a pinned moodboard of textiles and sketches (cork board). |
| Nicobar (New Delhi, India) | https://www.nicobar.com | shopify, video | Indian craft and lifestyle |
| Omsom | https://omsom.com | — | D2C food brands with strong illustration and |
| Paper Boat (Bengaluru, India) | https://paperboatdrinks.com/ | — | Hand-drawn nostalgic illustrations; pastel folder-tab nav (drinks, food, memories). |
| Paul And Mike (India) | https://www.paulandmike.co/ | shopify, splitting | Farm-to-bar chocolate; colourful packaging, festive campaigns. |
| Phool (Kanpur, India) | https://phool.co/ | shopify, splitting, video | Indian craft and lifestyle brands; rich photography, |
| Raw Mango (New Delhi, India) | https://www.rawmango.com/ | shopify | Indian craft and lifestyle brands; rich photography, |
| Studio Arhoj (Copenhagen, Denmark) | https://www.arhoj.com/ | shopify, video | Playful ceramic creatures, quirky voice, colourful shop. |
| Subko | https://subko.coffee | shopify, video | Indian craft and lifestyle |
| The Bombay Canteen (Mumbai, India) | https://www.thebombaycanteen.com/ | shopify | Restaurant site; warm interiors photography, menus, events. |
| The Whole Truth (Mumbai, India) | https://thewholetruthfoods.com/ | next | Bold type with hand-drawn scribbles, sparkles and arrows; honest copy. |
| Toast (London, UK) | https://www.toa.st/ | shopify, video | Calm editorial lifestyle photography, journal content. |

### G. Portfolios of designers, art directors and photographers (25)

| Site | Link | Stack | Notes |
|---|---|---|---|
| Angela Ricciardi | https://www.angelaricciardi.com/ | next | Artist/photographer; single framed image with counter, archive view. |
| Bruno Simon | https://bruno-simon.com | canvas | "click to start" 3D world; the showpiece end of the spectrum. |
| Camille Mormal | https://camillemormal.com/ | canvas | Art director; full-bleed editorial imagery, '+' project navigator. |
| Daniel Blue (San Francisco Bay Area, USA) | https://danielblue.com/ | nuxt, lenis, video | Interiors photographer; spaced text index of projects. |
| Emil Kowalski | https://emilkowal.ski | next | restraint benchmarks for interaction detail. |
| Félix Péault | https://www.felixpeault.com/ | sveltekit, lenis | Photographer of 'unordinary moments'; Svelte + Sanity image-led site. |
| Gianluca Gradogna (Florence, Italy) | https://gianlucagradogna.com/ | nuxt | Awwwards portfolio winner; infinite scroll, subtle transitions. |
| Gil Huybrecht | https://gilhuybrecht.com/ | nuxt, lenis, canvas, video | Awwwards SOTD; editorial websites designer; Lenis, video. |
| Heena Chung | https://heenachung.info/ | cargo, video | Designer archive; thumbnail-size toggle (S/M/L) over video grid. |
| Hugo Ahlberg (Bay Area, USA) | https://hugoahlberg.com/ | cargo, video | Photography/3D/cinematography; dark info layout, Cargo marquee. |
| Jacob Hutch (pin author) | https://www.jacobhutch.com | wix |  |
| Jason Bergh (Seattle, USA) | https://www.jasonbergh.com/ | webflow, gsap, scrolltrigger, locomotive, splitting, canvas, video | Awwwards SOTD; cinematic serif-italic titles over film stills. |
| Juan Mora | https://juanmora.co/ | webflow, gsap, scrolltrigger, lenis, splitting, video | Awwwards SOTD; infinite draggable lab field, poster cloth effects. |
| Julia Noni | https://julianoni.com/ | gsap | Fashion photographer; centred editorial images, [selected] [works]. |
| Kai Blamey Nguyen | https://kaiblamey.com/ | video | Cinematographer; full-bleed still with overlaid project index list. |
| Loli Laboureau | https://www.lolilaboureau.com/ | framer | Collage portfolio: cut-out objects and pop-up windows over B&W photography; Framer. |
| Marianna von Fedak | https://mariannavonfedak.com/ | wordpress, lenis, barba | Creative director; 215 images, Lenis + Barba transitions. |
| Mark Clennon | https://www.markclennon.com/ | webflow, lenis, canvas, video | Photographer/director; vertical photo strips, stills/motion/diary. |
| Olivier Larose | https://www.olivierlarose.com | astro, lenis, locomotive |  |
| Paco Coursey | https://paco.me | next |  |
| Rauno Freiberg | https://rauno.me | next |  |
| Rich Stapleton | https://richstapleton.com/ | nuxt, lenis | Photographer; centred single-image slideshow, generous white space. |
| Sam Thies (Australia) | https://samthies.com/ | lenis, video | Filmmaker/photographer; 180+ image visual stories, Lenis. |
| Stephen Kent Johnson | https://stephenkentjohnson.com/ | wordpress | Interiors photographer; dense mosaic wall of 280 images. |
| Synchrodogs / Synchrostudio (Ukraine) | https://synchrodogs.com/ | nuxt, canvas | Awwwards SOTM; photographer duo; dark brown column of images, WebGL. |

## 3. Brand, client and friends' studios

- Client's landing-page reference (Pinterest pin, Jacob Hutch, *Stamp Series // Visual Experiment 01*): https://in.pinterest.com/pin/681873199876372589/
- Studio Sorted: https://www.studiosorted.com/ · DesignRush profile: https://www.designrush.com/agency/profile/studio-sorted
- Studio N°7 (Studio Number Seven): https://www.studionumberseven.com/ (archived About page via the Wayback Machine, July 2025)
- Online-presence checks for Studio Kavalu: `studiokavalu.com` (no DNS), Instagram `@studiokavalu` (no such account), Behance search, DuckDuckGo and web search (no results).
- Her current website: screenshots in `../current_website/` (palette, wordmark, case-study copy).

## 4. Motion research sources

From `motion_catalog.md` §9 (41 techniques catalogued; see the catalog for which source backs which technique).

**GSAP**

- https://gsap.com/docs/v3/Plugins/ScrollSmoother/
- https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- https://gsap.com/docs/v3/Plugins/Flip/
- https://gsap.com/docs/v3/Plugins/SplitText/
- https://gsap.com/docs/v3/Plugins/ScrambleTextPlugin/
- https://gsap.com/docs/v3/HelperFunctions/helpers/seamlessLoop
- https://gsap.com/docs/v3/Plugins/DrawSVGPlugin/
- https://gsap.com/showcase/

**Lenis / darkroom**

- https://github.com/darkroomengineering/lenis
- https://github.com/darkroomengineering/lenis/blob/main/packages/react/README.md
- https://github.com/darkroomengineering/satus
- https://lenis.dev/showcase

**React / Next.js / MDN**

- https://nextjs.org/docs/app/guides/view-transitions
- https://react-view-transitions-demo.labs.vercel.dev
- https://github.com/nextjs/react-view-transitions-demo
- https://react.dev/reference/react/ViewTransition

**Motion (motion.dev)**

- https://motion.dev/docs/react-upgrade-guide
- https://motion.dev/docs/lenis
- https://motion.dev/examples/

**React Bits**

- https://reactbits.dev/animations/scroll-expand
- https://reactbits.dev/components/accordion-gallery
- https://reactbits.dev/components/scroll-stack
- https://reactbits.dev/components/bounce-cards
- https://github.com/DavidHDev/react-bits
- https://reactbits.dev/components/stack
- https://reactbits.dev/components/masonry
- https://reactbits.dev/components/folder
- https://reactbits.dev/components/tilted-card
- https://reactbits.dev/components/circular-gallery
- https://reactbits.dev/components/dome-gallery
- https://reactbits.dev/components/infinite-menu
- https://reactbits.dev/components/flowing-menu
- https://reactbits.dev/components/card-swap
- https://reactbits.dev/animations/image-trail
- https://reactbits.dev/animations/sticker-peel
- https://reactbits.dev/micro/tear-ticket
- https://reactbits.dev/micro/paper-crumple
- https://reactbits.dev/text-animations/fold-text
- https://reactbits.dev/animations/noise
- https://reactbits.dev/components/counter
- https://reactbits.dev/text-animations/falling-text
- https://reactbits.dev/text-animations/scroll-velocity
- https://reactbits.dev/text-animations/text-type
- https://reactbits.dev/text-animations/split-text
- https://reactbits.dev/text-animations/variable-proximity
- https://reactbits.dev/text-animations/text-pressure
- https://reactbits.dev/animations/magnet
- https://reactbits.dev/micro/folder-float
- https://reactbits.dev/micro/branched-menu
- https://reactbits.dev/backgrounds/grainient
- https://reactbits.dev/animations/ripple-distortion
- https://reactbits.dev/components/morph-slider

**Codrops / tympanus**

- https://tympanus.net/codrops/2024/01/17/a-practical-introduction-to-scroll-driven-animations-with-css-scroll-and-view/
- https://tympanus.net/Development/ScrollCarousel/
- https://tympanus.net/codrops/2025/10/29/building-a-layered-zoom-scroll-effect-with-gsap-scrollsmoother-and-scrolltrigger/
- https://tympanus.net/Tutorials/TelescopeZoom/
- https://tympanus.net/Development/ImageExpansionTypography/
- https://tympanus.net/Development/StickySections/
- https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/
- https://tympanus.net/Development/LayersAnimation/
- https://tympanus.net/Development/FullscreenClipEffect/
- https://tympanus.net/codrops/2025/05/27/animated-product-grid-preview-with-gsap-clip-path/
- https://tympanus.net/Tutorials/GridToFullPreview
- https://tympanus.net/codrops/2026/03/11/svg-mask-transitions-on-scroll-with-gsap-and-scrolltrigger/
- https://tympanus.net/Development/EaseReverseClipMenu
- https://tympanus.net/Tutorials/Scrollaroids/
- https://tympanus.net/codrops/2026/05/21/creating-scroll-driven-svg-map-animations-with-gsap/
- https://tympanus.net/codrops/2026/02/19/creating-a-smooth-horizontal-parallax-gallery-from-dom-to-webgl/
- https://tympanus.net/Tutorials/HorizontalParallaxGallery/index2.html
- https://tympanus.net/Development/3DStackMotion/
- https://tympanus.net/Development/EntranceAnimationForImages/
- https://tympanus.net/codrops/2026/06/04/creating-a-thumbnail-flow-animation-with-gsap-motionpath/
- https://tympanus.net/codrops/2026/01/20/animating-responsive-grid-layout-transitions-with-gsap-flip/
- https://tympanus.net/Tutorials/GridLayoutTransitions/
- https://tympanus.net/Development/GridViewSwitch/
- https://tympanus.net/codrops/2026/07/30/building-an-infinite-gsap-scroll-gallery-with-parallax-and-flip-transitions/
- https://tympanus.net/Tutorials/InfiniteScrollGSAPGallery/
- https://tympanus.net/codrops/2025/09/01/recreating-palmers-draggable-product-grid-with-gsap/
- https://tympanus.net/codrops/2026/07/27/between-print-and-digital-the-making-of-mersis-website/
- https://tympanus.net/codrops/2026/10/08/building-parallel-page-transitions-with-gsap-and-react-router/
- https://tympanus.net/codrops/2026/02/26/building-async-page-transitions-in-vanilla-javascript/
- https://tympanus.net/codrops/2026/10/07/interlude-astro-page-transitions/
- https://tympanus.net/Tutorials/Velvette/
- https://tympanus.net/codrops/2025/05/14/from-splittext-to-morphsvg-5-creative-demos-using-free-gsap-plugins/
- https://tympanus.net/codrops/2025/09/03/7-must-know-gsap-animation-tips-for-creative-developers/
- https://tympanus.net/Development/OnScrollTextHighlight/
- https://tympanus.net/codrops/2025/06/17/building-an-infinite-marquee-along-an-svg-path-with-react-motion/
- https://tympanus.net/codrops/2012/10/17/pfold-paper-like-unfolding-effect/
- https://tympanus.net/Development/GridItemHoverEffect/
- https://madewithgsap.com/codrops
- https://tympanus.net/codrops/2026/05/20/made-with-gsap-building-a-fun-gravity-based-mouse-trail/
- https://tympanus.net/Development/MotionTrailAnimations/
- https://tympanus.net/codrops/2026/09/24/custom-shaped-cursor-trail/
- https://tympanus.net/codrops/2025/06/11/building-an-infinite-parallax-grid-with-gsap-and-seamless-tiling/
- https://tympanus.net/Tutorials/InfiniteLayersGrid
- https://tympanus.net/codrops/2026/01/07/infinite-canvas-building-a-seamless-pan-anywhere-image-space/
- https://tympanus.net/codrops/2026/10/19/paper-shaders-off-background/
- https://tympanus.net/Demos/PaperDrops/
- https://tympanus.net/codrops/2026/10/18/real-folds-real-fire/
- https://tympanus.net/Tutorials/OnScrollFoldingCardboardBox/
- https://tympanus.net/codrops/2026/06/09/building-an-interactive-digital-stamp-collection-with-shaders-postcards-and-playful-inspection/
- https://tympanus.net/Development/RepeatingImageTransition/
- https://tympanus.net/codrops/2025/12/17/building-responsive-scroll-triggered-curved-path-animations-with-gsap/
- https://tympanus.net/codrops/2024/07/18/how-to-create-distortion-and-grain-effects-on-scroll-with-shaders-in-three-js/
- https://tympanus.net/codrops/2025/10/08/how-to-animate-webgl-shaders-with-gsap-ripples-reveals-and-dynamic-blur-effects/
- https://tympanus.net/Tutorials/WebGLBulge/
- https://tympanus.net/Development/IntroGridMotionTransition
- https://tympanus.net/Development/ContextAwareLogoAnimationScroll

**Osmo Supply**

- https://www.osmo.supply/resource/lenis-smooth-scroll-setup
- https://www.osmo.supply/resource/global-parallax-setup
- https://www.osmo.supply/resource/parallax-image-layers
- https://www.osmo.supply/resource/image-to-background-zoom
- https://www.osmo.supply/resource/scaling-element-on-scroll-gsap-flip
- https://www.osmo.supply/resource/stacking-cards-parallax
- https://www.osmo.supply/resource/collage-focus-card-on-hover
- https://www.osmo.supply/resource/horizontal-scrolling-sections
- https://www.osmo.supply/resource/stacking-sticky-cards-bounce
- https://www.osmo.supply/resource/dropping-cards-stack
- https://www.osmo.supply/resource/layout-grid-flip
- https://www.osmo.supply/resource/draw-svg-page-transition
- https://www.osmo.supply/resource/stacked-cards-page-transition
- https://www.osmo.supply/resource/masked-text-reveal
- https://www.osmo.supply/resource/solve-cut-off-letters-split-text
- https://www.osmo.supply/resource/text-scramble-load-scroll-hover
- https://www.osmo.supply/resource/variable-font-weight-hover
- https://www.osmo.supply/resource/draw-random-underline
- https://www.osmo.supply/resource/highlight-marker-text-reveal
- https://www.osmo.supply/resource/marquee-with-scroll-direction
- https://www.osmo.supply/resource/magnetic-hover-effect
- https://www.osmo.supply/resource/image-preview-cursor-follower
- https://www.osmo.supply/resource/velocity-based-custom-cursor
- https://www.osmo.supply/resource/directional-list-hover
- https://www.osmo.supply/resource/stacking-image-trail
- https://www.osmo.supply/resource/infinite-draggable-grid-basic
- https://www.osmo.supply/resource/draggable-stickers
- https://www.osmo.supply/resource/falling-2d-objects-matterjs
- https://www.osmo.supply/resource/auto-image-cycle-slideshow
- https://www.osmo.supply/resource/draw-path-on-scroll
- https://www.osmo.supply/resource/follow-svg-path-on-scroll
- https://www.osmo.supply/resource/film-grain-effect
- https://www.osmo.supply/resource/number-odometer
- https://www.osmo.supply/resource/willem-loading-animation
- https://www.osmo.supply/resource/welcoming-words-loader
- https://www.osmo.supply/resource/footer-parallax-effect
- https://www.osmo.supply/resource/scroll-to-next-page

**Aceternity / Magic UI / Motion Primitives / Cult UI / Animata / Skiper / 21st.dev**

- https://ui.aceternity.com/components/parallax-hero-images
- https://skiper-ui.com/v1/skiper30
- https://21st.dev/@danielpetho/components/parallax-floating
- https://21st.dev/@sshahaider/components/zoom-parallax
- https://21st.dev/@arunachalam/components/scroll-expansion-hero
- https://skiper-ui.com/v1/skiper16
- https://skiper-ui.com/v1/skiper54
- https://21st.dev/@soralabs/components/scroll-gallery
- https://ui.aceternity.com/components/focus-cards
- https://skiper-ui.com/v1/skiper52
- https://skiper-ui.com/v1/skiper17
- https://animata.design/docs/scroll/stacked-sections
- https://animata.design/docs/card/card-spread
- https://motion-primitives.com/docs/morphing-dialog
- https://motion-primitives.com/docs/text-scramble
- https://magicui.design/docs/components/hyper-text
- https://magicui.design/docs/components/highlighter
- https://www.cult-ui.com/docs/components/squiggle-arrow
- https://magicui.design/docs/components/scroll-based-velocity
- https://ui.aceternity.com/components/magnetic-button
- https://motion-primitives.com/docs/magnetic
- https://ui.aceternity.com/components/following-pointer
- https://skiper-ui.com/v1/skiper6
- https://animata.design/docs/image/trailing-image
- https://skiper-ui.com/v1/skiper73
- https://ui.aceternity.com/components/draggable-card
- https://skiper-ui.com/v1/skiper19
- https://ui.aceternity.com/components/tracing-beam
- https://magicui.design/docs/components/noise-texture
- https://magicui.design/docs/components/number-ticker
- https://motion-primitives.com/docs/sliding-number
- https://skiper-ui.com/v1/skiper8
- https://animata.design/docs/preloader/split-reveal

**Paper, physics and other libraries**

- https://github.com/ismamz/next-transition-router
- https://github.com/jorisnoo/matter-dom-plugin
- https://paperlab.nawwara.studio/
- https://kittygiraudel.com/2026/03/05/folded-corner-with-css/
- https://shaders.paper.design
- https://css-generators.com/fancy-frame/
- https://css-generators.com/custom-borders/
- https://github.com/NourMtir0722/Paperlab
- https://www.npmjs.com/package/paperlab
- https://css-shape.com/stamp/
- https://www.npmjs.com/package/vara
- https://www.unicorn.studio/docs/
- https://www.unicorn.studio/terms
- https://www.unicorn.studio/docs/embed/
- https://www.unicorn.studio/docs/performance/
- https://number-flow.barvian.me/

**Demo repos, reference sites and other**

- https://marijanapav.com/stamps
- https://tlb.betteroff.studio/
- https://joffreyspitzer.com/
- https://houseofyellow.nl/
- https://www.mersi-architecture.com
- https://codepen.io/osmosupply/pen/qEEKRrx
- https://www.laxspace.co/
- https://ten.375.studio/en
- https://github.com/JorgeCapillo/infinite-layers-grid
- https://github.com/edoardolunardi/infinite-canvas
- https://github.com/twotwentytwo-studio/codrops-paper
- https://github.com/buka-studio/www-marijanapav
- https://library.obys.agency/
- https://obys.agency/
- https://ponpon-mania.com/
- https://decathlonyestalgia.com/
- https://www.aralesk.es
- https://www.noth.in
- https://lamalama.com/
- https://www.jesperlandberg.com
- https://lightslefton.com
- https://www.mr-pandas-psychologically-safe-portfolio.com/
- https://studiolumio.com/
- https://revelatio.studio/
- https://375.studio/
- http://fantik.studio
- http://mater.agency
- https://guillaumecolombel.fr/
- https://chungsunglau.co.uk
- https://www.eduardbodak.com/
- https://www.12.studio/
- https://gatzara.studio/
- https://haoqi.design/
- https://matvoyce.tv/
- https://format.obys.agency/

## 5. Onboarding research sources

From `onboarding_research.md` §8 (41 studio contact pages surveyed in §2 of that file).

1. NN/g, *Wizards: Definition and Design Recommendations*: https://www.nngroup.com/articles/wizards/
2. GOV.UK Design System, *Question pages*: https://design-system.service.gov.uk/patterns/question-pages/
3. Venture Harbour, *Multi-step lead forms*: https://www.ventureharbour.com/multi-step-lead-forms-get-300-conversions/
4. Baymard Institute, *Checkout flow average form fields* (2024): https://baymard.com/blog/checkout-flow-average-form-fields
5. HubSpot (Dan Zarrella), *3 form fields that kill landing page conversion rates*: https://blog.hubspot.com/blog/tabid/6307/bid/6748/3-form-fields-that-kill-landing-page-conversion-rates.aspx and *Which types of form fields lower landing page conversions*: https://blog.hubspot.com/blog/tabid/6307/bid/6746/which-types-of-form-fields-lower-landing-page-conversions.aspx
6. CXL, *Should you really reduce form fields?*: https://cxl.com/blog/reduce-form-fields/
7. MarketingExperiments, *Testing form field length reduces cost-per-lead by $10.66*: https://marketingexperiments.com/lead-generation/lead-generation-testing-form-field-length-reduces-cost-per-lead-by-10-66
8. NN/g, *Progressive disclosure*: https://www.nngroup.com/articles/progressive-disclosure/
9. Villar, Callegaro and Yang (2013), *Where Am I? A meta-analysis of experiments on the effects of progress indicators for web surveys*, Social Science Computer Review 31(6): https://openaccess.city.ac.uk/id/eprint/14427/
10. Zuko, *Lead generation form analytics*: https://www.zuko.io/industries/lead-generation
11. Luke Wroblewski, *Inline validation in web forms* (A List Apart, 2009): https://alistapart.com/article/inline-validation-in-web-forms/
12. NN/g, *10 design guidelines for reporting errors in forms*: https://www.nngroup.com/articles/errors-forms-design-guidelines/
13. GOV.UK Design System, *Error summary*: https://design-system.service.gov.uk/components/error-summary/
14. NN/g, *Placeholders in form fields are harmful*: https://www.nngroup.com/articles/form-design-placeholders/
15. NN/g, *Marking required fields in forms*: https://www.nngroup.com/articles/required-fields/
16. web.dev, *Sign-up form best practices*: https://web.dev/articles/sign-up-form-best-practices
17. Baymard Institute, *Mobile touch keyboards*: https://baymard.com/blog/mobile-touch-keyboards
18. Telerik, *iPhone Safari zooms into inputs under 16px*: https://docs.telerik.com/devtools/aspnet-ajax/knowledge-base/common-disable-autozoom-input-safari-iphone
19. CXL Institute study of single- vs multi-column forms (Speero reprint): https://speero.com/post/form-field-usability-should-you-use-single-or-multi-column-forms-original-research
20. W3C, WCAG 2.2 Understanding 2.5.8 *Target Size (Minimum)*: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
21. W3C WAI, *Forms tutorial: grouping controls*: https://www.w3.org/WAI/tutorials/forms/grouping/
22. Sara Soueidan, *Inclusively hiding & styling checkboxes and radio buttons*: https://www.sarasoueidan.com/blog/inclusively-hiding-and-styling-checkboxes-and-radio-buttons/
23. Adrian Roselli, *Under-engineered custom radio buttons and checkboxen*: https://adrianroselli.com/2017/05/under-engineered-custom-radio-buttons-and-checkboxen.html
24. W3C WAI-ARIA Authoring Practices, *Radio group pattern*: https://www.w3.org/WAI/ARIA/apg/patterns/radio/
25. W3C, WCAG 2.2 Understanding 1.4.1 *Use of color*: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html; 1.4.11 *Non-text contrast*: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html; 1.3.5 *Identify input purpose*: https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html
26. W3C, *Inaccessibility of CAPTCHA* (Group Draft Note, 16 December 2021): https://www.w3.org/TR/turingtest/
27. Bursztein, Bethard, Fabry, Mitchell and Jurafsky, *How good are humans at solving CAPTCHAs? A large scale evaluation* (IEEE S&P 2010): https://elie.net/publication/how-good-are-humans-at-solving-captchas-a-large-scale-evaluation
28. SEOmoz CAPTCHA test (Casey Henry, 2009), as reported by Konigi: https://konigi.com/blog/captchas-effect-conversion-rates and Akismet: https://akismet.com/blog/captcha-conversion-conundrum/
29. Cloudflare Turnstile, *Plans*: https://developers.cloudflare.com/turnstile/plans/ and *Server-side validation*: https://developers.cloudflare.com/turnstile/get-started/server-side-validation/
30. Convert Forms, *Minimum time to submit*: https://www.tassos.gr/docs/convert-forms/security/min-time-to-submit; Jeff Geerling, *Introducing the Honeypot form spam protection module for Drupal*: https://www.jeffgeerling.com/blog/2011/introducing-honeypot-form-spam/
31. Oldroyd, McElheran and Elkington, *The short life of online sales leads* (HBR, March 2011): https://hbr.org/2011/03/the-short-life-of-online-sales-leads
32. NN/g, *Show prices for common scenarios*: https://www.nngroup.com/articles/show-prices-for-common-scenarios/
33. Gartner press release, *61% of B2B buyers prefer a rep-free buying experience* (25 June 2025): https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience
34. Worchel, Lee and Adewole (1975), *Effects of supply and demand on ratings of object value*, Journal of Personality and Social Psychology 32(5): https://doi.org/10.1037/0022-3514.32.5.906
35. Spiegel Research Center, *How online reviews influence sales*: https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/
36. GOV.UK Design System, *Confirmation pages*: https://design-system.service.gov.uk/patterns/confirmation-pages/
37. Cal.com, *Pricing*: https://cal.com/pricing
38. Cal.com help: embed types https://cal.com/help/embedding/adding-embed; filling in the booking form from an embed https://cal.com/help/embedding/prefill-booking-form-embed; filling in fields https://cal.com/help/bookings/prefill-fields; embed events https://cal.com/help/embedding/embed-events; Cal Pay https://cal.com/help/cal-pay; routing https://cal.com/routing
39. Calendly, *Pricing*: https://calendly.com/pricing
40. Tally, *Pricing*: https://tally.so/pricing
41. Typeform, *Pricing*: https://www.typeform.com/pricing/
42. HoneyBook, *HoneyBook launches in the United Kingdom and Australia*: https://news.honeybook.com/news/honeybook-launches-in-the-united-kingdom-and-australia
43. Dubsado, *Pricing*: https://www.dubsado.com/pricing
44. Bonsai, *Pricing*: https://www.hellobonsai.com/pricing
45. Razorpay, *Pricing*: https://razorpay.com/pricing/ and *Payment Links*: https://razorpay.com/payment-links/
46. Stripe Support, *Stripe accounts are invite-only in India*: https://support.stripe.com/questions/stripe-accounts-are-invite-only-in-india
47. WhatsApp Help Center, *How to use click to chat*: https://faq.whatsapp.com/5913398998672934
48. Resend: pricing https://resend.com/pricing; send-email API (attachments up to 40 MB) https://resend.com/docs/api-reference/emails/send-email; Next.js guide https://resend.com/docs/send-with-nextjs; domains https://resend.com/docs/dashboard/domains/introduction
49. Formspree, *Plans*: https://formspree.io/plans
50. Web3Forms, *Pricing*: https://web3forms.com/pricing
51. Basin, *Pricing*: https://usebasin.com/pricing
52. Supabase, *Pricing*: https://supabase.com/pricing and *Standard uploads*: https://supabase.com/docs/guides/storage/uploads/standard-uploads
53. Google, *Apps Script quotas*: https://developers.google.com/apps-script/guides/services/quotas
54. Vercel: functions limits https://vercel.com/docs/functions/limitations; fair use and commercial use https://vercel.com/docs/limits/fair-use-guidelines; Vercel Blob pricing https://vercel.com/docs/vercel-blob/usage-and-pricing; plans https://vercel.com/pricing
55. Next.js, *serverActions* configuration (body size limit): https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions
56. Netlify Support Forums, *Can we use Netlify free plan for commercial purposes?*: https://answers.netlify.com/t/can-we-use-netlify-free-plan-for-commercial-purposes/41545
57. AZB & Partners, *India's Digital Personal Data Protection Act: phased rollout and key compliance milestones*: https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/
58. Luke Wroblewski, *Mad Libs style form increases conversion 25-40%* (25 February 2010): https://www.lukew.com/ff/entry.asp?1007
59. Adrian Roselli, *Sentence forms (not Mad Libs)* (2021): https://adrianroselli.com/2021/08/sentence-forms-not-mad-libs.html

Studio and template pages are linked in the tables in section 2.

---

## 6. Fonts, licences and tools

- Gambetta, Switzer (Indian Type Foundry) via Fontshare — https://www.fontshare.com/fonts/gambetta · https://www.fontshare.com/fonts/switzer · ITF Free Font License: https://www.fontshare.com/licenses/itf-ffl
- Courier Prime (SIL OFL) — https://fonts.google.com/specimen/Courier+Prime · https://github.com/quoteunquoteapps/CourierPrime
- Homemade Apple, Mrs Saint Delafield, Anek Kannada: Google Fonts (SIL OFL) — https://fonts.google.com
- Compared in the type review (specimens in `research/type/`): Fraunces, Erode, Sentient, Zodiak, Boska, Bespoke Serif, Newsreader; Ranade, Author, Hanken Grotesk; IBM Plex Mono, Cutive Mono, Xanh Mono; Nothing You Could Do, La Belle Aurore, Reenie Beanie, Kalam
- v1 faces, replaced in v2: Fraunces, IBM Plex Mono (Google Fonts); Ranade, Panchang (Fontshare)
- How brand documents are structured: NASA Graphics Standards Manual (Danne & Blackburn, 1975); Foothill–De Anza Brand Guidelines (Jan 2026) https://fhda.edu/_downloads/_FHDA-Brand-Guidelines-January2026.pdf · GitHub Brand Toolkit https://brand.github.com · IBM Carbon motion https://carbondesignsystem.com/elements/motion/overview/ · Atlassian foundations https://atlassian.design/foundations
- Motion studied frame by frame (`research/motion_frames/sites/NOTES.md`): Digital Stamp Collection https://marijanapav.com/stamps · MERSI https://www.mersi-architecture.com · Obys' Design Books https://library.obys.agency/ · The Lookback https://tlb.betteroff.studio/ (did not render in capture)
- Next.js 16 docs (bundled in `website/node_modules/next/dist/docs/`), GSAP docs https://gsap.com/docs/v3/, Lenis https://github.com/darkroomengineering/lenis
