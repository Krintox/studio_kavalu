# Fonts used by design studios around the world

*24 October 2026 · research for Studio Kavalu (brief 3: "make a list of fonts used by the studios all
over the world")*

**What this is.** The typefaces on the websites of 195 design and branding studios: global
agencies, independent studios, Indian studios, digital and motion studios, and designers' own
practices, in at least 21 countries. 185 of them have at least one identified face. Most rows come
from our own browser census of 226 sites; the rest were added or rechecked one by one from Fonts In
Use, Typewolf, foundry pages, the studios' own stylesheets and credits. §5 counts what is most used, by
studio type; §6 indexes every face with its classification, foundry and licence. The companion
`FONT_GUIDE.md` turns this into advice by kind of company, and `KAVALU_FONT_SHORTLIST.md` applies it to
Kavalu.

**How to read the tables.** *Display* is the headline face, *Text* the body face, *Mono / label* any
monospaced face. A `*` means the role was inferred rather than observed (§7). *Classification*,
*Foundry* and *Licence* describe the faces in that row, in order. "CSS census" in *Source* means the
faces were read from the site itself on 24 Oct 2026; other rows link their own source.

---

## 1. What the list shows

1. **There is no "studio font"; there is a studio class.** The most-used face, Helvetica, is loaded by 10
   of 185 studio sites (5%), and no other face passes 4% (§5.1). But 83% load a sans and 46% a
   neo-grotesk, and where the headline face is known it is a sans in 72 of 105 cases (§5.4–5.6).
2. **One or two families.** 45% of studio sites load one family and 37% two: 82% in all (§5.8).
3. **A fifth pair a serif with the sans.** 30% load a serif and 22% pair one with a sans. Contemporary
   editorial serifs lead (10%), then Didone and Garalde (6% each) (§5.4–5.5).
4. **Monospaced labels are a studio habit, typewriters are not.** 14% load a mono (21% of digital and
   motion studios); only 2% load a typewriter face (§5.4–5.5).
5. **Handwriting is almost absent.** 2% load a script or handwriting face, all of them designers' own
   portfolios (§5.4).
6. **Studios pay for type.** 72% load at least one paid face, 84% of independent studios. The shelf is the
   Helvetica family (13% of studios), Pangram Pangram (9%; its licences must be renewed every year),
   Dinamo (8%), Klim (6%), Swiss Typefaces and Colophon (4% each), Grilli Type, Optimo and Commercial Type
   (3% each) (§5.2, §5.7).
7. **The biggest agencies own their type.** 17% of the global agencies load a custom face: Koto's GT
   Kotoheim, JKR's Ritchie and Knowles, Kontrapunkt's Tomo, Landor Sans and Saffron's family. Others run
   foundries: Kurppa Hosk's KH Type, Studio Feixen's fonts, and November's Shiva Nallaperumal drew Delegate
   for Commercial Type (§3, §6).
8. **AI-default faces are rare among studios.** 14% load one of the faces generated sites converge on
   (Inter, Poppins, Montserrat, Satoshi, DM Sans, Plus Jakarta Sans, Instrument Serif…), only 7% of
   global agencies, but 35% of Indian studios (§5.9).
9. **Indian studio sites lean on free and platform fonts.** 31% of them load only free faces, against 10%
   of global agencies, and 15% load four or more families. Many run on Wix, Webflow, Squarespace or
   Semplice, which hide their fonts, so fewer could be verified (§2, §5.7–5.8).
10. **Typewolf agrees.** Its most popular fonts (Apercu, GT America, Futura, Founders Grotesk, Neue Haas
    Grotesk, Canela, Graphik, Proxima Nova, GT Walsheim, Avenir) are mostly grotesks from independent
    foundries ([Typewolf](https://www.typewolf.com/site-of-the-day), sidebar, 24 Oct 2026).

---

## 2. How the list was built, and what could not be verified

The census captured 226 sites in seven groups (`research/SOURCES.md`). 175 of them are studios or
designers; the other 48 are brands and magazines, listed separately in §4. Three duplicate captures were
merged. We then rechecked the census rows whose fonts were missing, hidden or suspicious, and added
leading studios the census lacked, including those named in the brief, verifying each from a source.

These were searched but could not be verified, so they are not in §3:

| Studio | Place | What was found | Source |
|---|---|---|---|
| Kombai (named in the brief) | India (per brief) | No design studio named Kombai found; kombai.com is an AI 'design engineer' software product | [kombai.com](https://kombai.com/) |
| Thought Over Design | Mumbai, India | WordPress + Semplice site; fonts sit in Semplice settings, not exposed; no colophon or Fonts In Use entry | [thoughtoverdesign.com](https://thoughtoverdesign.com/wp-json/) |
| Studio Eksaat | New Delhi, India | WordPress + Semplice; page API exposes only font IDs (font_4ziak6uqo etc.), not family names | [studioeksaat.com](https://www.studioeksaat.com/wp-json/semplice/v1/frontend/posts/131378) |
| Supari Studios | Mumbai, India | Webflow site (design by Pigeon&Co.); stylesheet hash not discoverable, no font credit on page | [suparistudios.com](https://www.suparistudios.com/) |
| Sideways | Mumbai, India | Webflow site; stylesheet not discoverable without page source; no font credit found | [sideways.co.in](https://www.sideways.co.in/) |
| Grandmother India | Mumbai, India | Domain shows a GoDaddy 'Launching Soon' placeholder on 2026-10-24; no fonts to record | [grandmotherindia.com](https://www.grandmotherindia.com/) |
| Studio Nari (named in the brief) | London, UK | It's Nice That 2020: typographic identity from letterpress blocks, typeface unnamed; Next.js site, no colophon | [itsnicethat.com](https://www.itsnicethat.com/articles/nari-graphic-design-130220) |
| Kahani Designworks | Mumbai, India | Squarespace site; site JSON has empty typekitId and no font keys; no colophon | [kahanidesignworks.com](https://www.kahanidesignworks.com/?format=json-pretty) |
| Ray+Keshavan | Bengaluru (per brief; not stated on site), India | Site exposes no assets, credits, REST API or guessable CSS; no Fonts In Use entry found | [rayandkeshavan.com](https://rayandkeshavan.com/about-us/) |
| DY Works | Mumbai (per brief), India | dyworks.in returns an empty client-rendered page to fetch; no font source found | [dyworks.in](https://www.dyworks.in/) |
| Kokaachi | Kochi (per brief), India | kokaachi.com answered every request with HTTP 429 (bot wall), so skipped; no Fonts In Use entries | [fontsinuse.com](https://fontsinuse.com/search?terms=Kokaachi) |
| Kurppa Hosk (named in the brief) | Stockholm, Sweden | Runs own foundry KH Type (KH Teka, Giga, Einheit); no source says which face its site uses | [kurppahosk.com](https://www.kurppahosk.com/news/launching-kh-type) |
| Further, formerly DesignStudio (named in the brief) | London, UK | Rebranded Sept 2025; accessible coverage names no typeface; Design Week article returned 403 | [further.group](https://www.further.group/news/designstudio-is-now-further) |
| Build (named in the brief) | Otley, near Leeds, UK | Studio is at studio.build (build.co.uk redirects to retailer build.com); Webflow site, no colophon | [studio.build](https://www.studio.build/info) |
| Wednesday (named in the brief) | London, UK | Fashion/luxury agency (BBDO stake 2016); wednesdayagency.com did not resolve; wednesday.agency is unrelated | [campaignlive.com](https://campaignlive.com/article/bbdo-buys-majority-stake-wednesday-agency-group/1378650) |
| Ogilvy India design (named in the brief) | Mumbai, India | No distinct Ogilvy India design unit found; ogilvy.com (Drupal) has no font credit; no Fonts In Use entry | [fontsinuse.com](https://fontsinuse.com/search?terms=Ogilvy+identity) |


## 3. The studios

### 3.1 Global agencies (31)

| Studio | City, country | Site | Display | Text | Mono / label | Classification | Foundry | Licence | Source |
|---|---|---|---|---|---|---|---|---|---|
| &Walsh | New York, USA | [andwalsh.com](https://andwalsh.com/) | Maison Neue | same | — | neo-grotesk | Milieu Grotesque | paid | CSS census, 24 Oct 2026 ([site](https://andwalsh.com/)) |
| Anagrama | Mexico City, Mexico | [anagrama.com](https://www.anagrama.com/) | Neue Haas Grotesk* | same | — | neo-grotesk | Font Bureau / Monotype (C. Schwartz) | paid | CSS census, 24 Oct 2026 ([site](https://www.anagrama.com/)) |
| Base Design | Brussels / New York | [basedesign.com](https://www.basedesign.com) | Muoto* | same | — | neo-grotesk | 205TF | paid | CSS census, 24 Oct 2026 ([site](https://www.basedesign.com)) |
| Bibliotheque | London, UK | [bibliothequedesign.com](https://www.bibliothequedesign.com) | — | acute (unidentified), Unica77 (roles not separated) | — | unverified · neo-grotesk | unverified · Lineto | unverified · paid | CSS census, 24 Oct 2026 ([site](https://www.bibliothequedesign.com)) |
| Collins | New York / San Francisco | [wearecollins.com](https://www.wearecollins.com) | Portrait | Graphik | — | contemporary editorial serif · neo-grotesk | Commercial Type | paid | CSS census, 24 Oct 2026 ([site](https://www.wearecollins.com)) |
| DixonBaxi | London, UK | [dixonbaxi.com](https://www.dixonbaxi.com) | Aeonik Fono | Iskry | Aeonik Fono | grotesk mono · contemporary editorial serif | CoType Foundry · Laïc | paid | CSS census, 24 Oct 2026 ([site](https://www.dixonbaxi.com)) |
| Gretel | New York, USA | [gretelny.com](https://gretelny.com) | Akkurat | DIN 2014 | — | neo-grotesk · DIN/industrial sans | Lineto · ParaType | paid | CSS census, 24 Oct 2026 ([site](https://gretelny.com)) |
| Instrument | Portland, USA | [instrument.com](https://www.instrument.com) | — | Instrument Sans, Instrument Serif (roles not separated) | — | neo-grotesk · Didone/high-contrast serif | Instrument | free/open | CSS census, 24 Oct 2026 ([site](https://www.instrument.com)) |
| JKR | London / global | [jkrglobal.com](https://www.jkrglobal.com) | — | JKR Ritchie, JKR Knowles (roles not separated) | — | unverified | JKR (in-house or commissioned) | custom | CSS census, 24 Oct 2026 ([site](https://www.jkrglobal.com)) |
| Kontrapunkt | Copenhagen, Denmark | [kontrapunkt.com](https://www.kontrapunkt.com) | Kontrapunkt Tomo Slab | Kontrapunkt Tomo | — | slab/Clarendon serif · unverified | Kontrapunkt (in-house) | custom | CSS census, 24 Oct 2026 ([site](https://www.kontrapunkt.com)) |
| Koto | London / global | [koto.com](https://koto.com/) | — | GT Kotoheim, GT Kotoheim Condensed (roles not separated) | GT Kotoheim Mono | geometric sans · grotesk mono · condensed display sans | Grilli Type (derivative of GT Walsheim, inferred) · Grilli Type (inferred) | custom | CSS census, 24 Oct 2026 ([site](https://koto.com/)) |
| Landor | San Francisco / global, USA | [landor.com](https://landor.com) | Landor Sans | same | — | grotesque | Landor (in-house type studio) | custom | It's Nice That 2023: new identity uses Landor Sans, custom grotesque, plus serif wordmark; website not documented ([itsnicethat.com](https://www.itsnicethat.com/news/landor-graphic-design-211123)) — identity-only |
| Lundgren+Lindqvist | Gothenburg, Sweden | [lundgrenlindqvist.se](https://lundgrenlindqvist.se) | PxGrotesk* | same | — | grotesque | Optimo | paid | CSS census, 24 Oct 2026 ([site](https://lundgrenlindqvist.se)) |
| Made Thought | London / New York | [madethought.com](https://www.madethought.com) | — | Items Light, Futura (roles not separated) | — | contemporary editorial serif · geometric sans | Schick Toikka · Bauer / ParaType (Futura PT) / Linotype | paid | CSS census, 24 Oct 2026 ([site](https://www.madethought.com)) |
| Manual | San Francisco, USA | [manual.studio](https://manual.studio/) | ABC Oracle | ABC Otto | — | grotesque · soft/wonky serif | Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://manual.studio/)) |
| Mother Design | London / New York | [motherdesign.com](https://www.motherdesign.com) | Basis Grotesque* | same | Basis Grotesque Mono | grotesque · grotesk mono | Colophon | paid | CSS census, 24 Oct 2026 ([site](https://www.motherdesign.com)) |
| Mucho | Barcelona / SF / NY | [wearemucho.com](https://wearemucho.com/) | ABC Repro | same | — | grotesque | Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://wearemucho.com/)) |
| Mythology | London, UK | [mythology.com](https://www.mythology.com) | — | Plantin, Theinhardt (roles not separated) | — | old-style/Garalde serif · grotesque | Monotype · Optimo | paid | CSS census, 24 Oct 2026 ([site](https://www.mythology.com)) |
| Order | New York, USA | [order.design](https://order.design/) | — | — | Pitch Sans | grotesk mono | Klim | paid | CSS census, 24 Oct 2026 ([site](https://order.design/)) |
| Pearlfisher | London, UK | [pearlfisher.com](https://www.pearlfisher.com) | Inter | same | — | neo-grotesk | Rasmus Andersson | free/open | Theme CSS sets body and h1-h6 to 'Inter'; separate brand face not documented on Fonts In Use ([pearlfisher.com](https://www.pearlfisher.com/wp-content/themes/pearlfisher/style.css)) — recheck: verified |
| Pentagram | London / New York | [pentagram.com](https://www.pentagram.com) | Plain* | same | — | neo-grotesk | Optimo | paid | CSS census, 24 Oct 2026 ([site](https://www.pentagram.com)) |
| Porto Rocha | New York, USA | [portorocha.com](https://www.portorocha.com) | SF Pro | same | — | neo-grotesk | Apple | system | Census saw faces named sf-pro-text/display on Nuxt site; files not inspectable; no Fonts In Use entry ([portorocha.com](https://www.portorocha.com/)) — recheck: unverified |
| Ragged Edge | London, UK | [raggededge.com](https://www.raggededge.com/) | ABC Diatype Expanded | ABC Diatype (+ Grit (unidentified)) | — | extended/wide sans · neo-grotesk · unverified | Dinamo · unverified | paid · unverified | CSS census, 24 Oct 2026 ([site](https://www.raggededge.com/)) |
| Saffron Brand Consultants | London / Madrid, UK | [saffron-consultants.com](https://saffron-consultants.com) | Custom family (unnamed) | same | — | custom | the studio (name not published) | custom | Designers Journal 2017: identity uses a bespoke type family with four variants; names not given ([designersjournal.net](https://www.designersjournal.net/agencies/a-new-spirit)) — identity-only |
| Siegel+Gale | New York, USA | [siegelgale.com](https://www.siegelgale.com) | Suisse Int'l | same | — | neo-grotesk | Swiss Typefaces | paid | Theme CSS self-hosts a 'Suisse' family, Thin to Black; display and body classes use it ([siegelgale.com](https://www.siegelgale.com/app/themes/simplicity/dist/styles/main_cc33d236.css)) |
| Snask | Stockholm, Sweden | [snask.com](https://www.snask.com) | F37 Snaskface | Apercu (+ Lacrima Senza) | — | display/novelty · grotesque · humanist sans | F37 Foundry x Snask · Colophon · Milieu Grotesque | paid | CSS census, 24 Oct 2026 ([site](https://www.snask.com)) |
| Studio Dumbar | Rotterdam, Netherlands | [studiodumbar.com](https://studiodumbar.com) | Neue Haas Grotesk* | same | — | neo-grotesk | Font Bureau / Monotype (C. Schwartz) | paid | CSS census, 24 Oct 2026 ([site](https://studiodumbar.com)) |
| Turner Duckworth | London / San Francisco | [turnerduckworth.com](https://www.turnerduckworth.com/) | Founders Grotesk* | same | Founders Grotesk Mono | grotesque · grotesk mono | Klim | paid | CSS census, 24 Oct 2026 ([site](https://www.turnerduckworth.com/)) |
| Two Times Elliott | London, UK | [twotimeselliott.com](https://www.twotimeselliott.com) | — | no web font loaded (system fonts, or type drawn as images) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://www.twotimeselliott.com)); recheck found nothing more: Studio domain is 2xelliott.co.uk (per Fonts In Use); it returned HTTP 526, site unreachable ([fontsinuse.com](https://fontsinuse.com/designers/3556/two-times-elliott)) |
| Universal Favourite | Sydney, Australia | [universalfavourite.com.au](https://www.universalfavourite.com.au/) | Editorial New | Banana Grotesk | — | Didone/high-contrast serif · grotesque | Pangram Pangram · Monkey Type | free-personal · paid | CSS census, 24 Oct 2026 ([site](https://www.universalfavourite.com.au/)) |
| Wolff Olins | London / New York | [wolffolins.com](https://www.wolffolins.com) | — | ABC Monument Grotesk, Untitled Serif (roles not separated) | — | grotesque · transitional serif | Dinamo · Klim | paid | CSS census, 24 Oct 2026 ([site](https://www.wolffolins.com)) |

### 3.2 Independent studios (59)

| Studio | City, country | Site | Display | Text | Mono / label | Classification | Foundry | Licence | Source |
|---|---|---|---|---|---|---|---|---|---|
| A Practice for Everyday Life | London, UK | [apracticeforeverydaylife.com](https://www.apracticeforeverydaylife.com/) | Friedel* | same | — | neo-grotesk | APFEL (A Practice for Everyday Life) | paid | CSS census, 24 Oct 2026 ([site](https://www.apracticeforeverydaylife.com/)) |
| Agence Foudre | Paris, France | [agencefoudre.com](https://www.agencefoudre.com/) | — | Clash Grotesk, Beni (roles not separated) | — | grotesque · condensed display sans | Indian Type Foundry (Fontshare) · Nois | free-commercial · paid | CSS census, 24 Oct 2026 ([site](https://www.agencefoudre.com/)) |
| B&B Studio | London, UK | [bandb-studio.co.uk](https://bandb-studio.co.uk/) | Neue Haas Grotesk | same | — | neo-grotesk | Font Bureau / Monotype (C. Schwartz) | paid | CSS census, 24 Oct 2026 ([site](https://bandb-studio.co.uk/)) |
| Beth-Emily | Melbourne, Australia | [beth-emily.com](https://www.beth-emily.com/) | — | Satoshi, Merriweather, Oswald (roles not separated) | — | geometric sans · transitional serif · condensed display sans | Indian Type Foundry (Fontshare) · Sorkin Type · Vernon Adams | free-commercial · free/open | CSS census, 24 Oct 2026 ([site](https://www.beth-emily.com/)) |
| Bielke&Yang | Oslo, Norway | [bielkeyang.com](https://bielkeyang.com/) | Martina Plantijn | Deckard | ABC Rom Mono | old-style/Garalde serif · unverified · grotesk mono | Klim · unknown (Bobby Tannam) · Dinamo | paid · unknown | CSS census, 24 Oct 2026 ([site](https://bielkeyang.com/)) |
| Boc.Studio | Barcelona, Spain | [boc.studio](https://boc.studio/) | PP Mori | same | — | neo-grotesk | Pangram Pangram | free-personal | CSS census, 24 Oct 2026 ([site](https://boc.studio/)) |
| Bureau Borsche | Munich, Germany | [bureauborsche.com](https://bureauborsche.com) | BB Grotesk | same | — | grotesque | Bureau Borsche (in-house) | custom | maxibestof.one listing (seen via search index; page returns 403) credits custom BB Grotesk ([maxibestof.one](https://maxibestof.one/websites/60440-bureau-borsche)) — recheck: partial |
| Bureau for Visual Affairs | London, UK | [bureau-va.com](https://bureau-va.com) | Scto Grotesk | same | — | grotesque | Schick Toikka | paid | Typewolf Site of the Day, March 2022: website uses Scto Grotesk (only font listed) ([typewolf.com](https://www.typewolf.com/site-of-the-day/bureau-va)) |
| Character | San Francisco, USA | [withcharacter.com](https://withcharacter.com) | Sharp Grotesk | same | — | grotesque | Sharp Type | paid | Typewolf Site of the Day, April 2022: Character website set in Sharp Grotesk (only font listed) ([typewolf.com](https://www.typewolf.com/site-of-the-day/with-character)) |
| Christopher Doyle & Co | Sydney, Australia | [christopherdoyle.co](https://christopherdoyle.co/) | — | Die Grotesk, Founders Grotesk X-Condensed (roles not separated) | — | neo-grotesk · condensed display sans | Klim Type Foundry · Klim | paid | CSS census, 24 Oct 2026 ([site](https://christopherdoyle.co/)) |
| Commission Studio | London, UK | [commission.studio](https://www.commission.studio/) | Futura* | same | — | geometric sans | Bauer / ParaType (Futura PT) / Linotype | paid | CSS census, 24 Oct 2026 ([site](https://www.commission.studio/)) |
| DutchScot | London, UK | [dutch.scot](https://dutch.scot/) | Caslon Doric | same | — | grotesque | Commercial Type | paid | CSS census, 24 Oct 2026 ([site](https://dutch.scot/)) |
| Folch | Barcelona, Spain | [folchstudio.com](https://www.folchstudio.com/) | — | FFF Tool Sans, FFF Tool Serif (roles not separated) | — | unverified | Folch | paid | CSS census, 24 Oct 2026 ([site](https://www.folchstudio.com/)) |
| Foreign Policy Design Group | Singapore, Singapore | [foreignpolicy.design](https://foreignpolicy.design) | Panama | — (+ Basetica, FF More) | — | contemporary editorial serif · neo-grotesk · unverified | The Temporary State (Roman Gornitsky) · Base Design (in-house, predecessor of Muoto) · unverified | paid · custom · unverified | Typewolf Site of the Day, May 2022: website uses Panama, Basetica and FF More ([typewolf.com](https://www.typewolf.com/site-of-the-day/foreign-policy-2022)) |
| Glasfurd & Walker | Vancouver, Canada | [glasfurdandwalker.com](https://glasfurdandwalker.com/) | Fancy-Serif (unidentified)* | same (+ unnamed/obfuscated face) | — | unverified | unverified | unverified | CSS census, 24 Oct 2026 ([site](https://glasfurdandwalker.com/)) |
| Goksøyr & Martens | Oslo, Norway | [goksoyrmartens.com](https://goksoyrmartens.com) | Suisse Works | — (+ Suisse Int'l) | Suisse Int'l Mono | contemporary editorial serif · grotesk mono · neo-grotesk | Swiss Typefaces | paid | Typewolf Site of the Day, March 2022: Suisse Works, Suisse Int'l, Suisse Int'l Mono ([typewolf.com](https://www.typewolf.com/site-of-the-day/goksoyr-martens)) |
| Goodside | — | [goodside.studio](https://www.goodside.studio/) | Epicene | same | — | transitional serif | Klim | paid | CSS census, 24 Oct 2026 ([site](https://www.goodside.studio/)) |
| Happy Happy Creative | — | [happyhappycreative.com](https://www.happyhappycreative.com/) | loretta-7v3rxf (unidentified) | ITC Avant Garde Gothic (+ Inter, Almarai) | — | unverified · geometric sans · neo-grotesk | unverified · ITC / Monotype · Rasmus Andersson · Boutros | unverified · paid · free/open | CSS census, 24 Oct 2026 ([site](https://www.happyhappycreative.com/)) |
| HATO | London, UK | [hato.co](https://hato.co) | Helvetica / Helvetica Neue | same | — | neo-grotesk | Linotype / Monotype | paid | Census: h1 computed as Helvetica, no webfont loaded; site colophon credits only Vue, UnoCSS, GSAP ([hato.co](https://hato.co/about)) — recheck: partial |
| Here Design | London, UK | [heredesign.com](https://www.heredesign.com/) | Baskerville (display) | Untitled Sans (+ New Baskerville) | — | transitional serif · neo-grotesk | unverified · Klim · ITC / Monotype | paid | CSS census, 24 Oct 2026 ([site](https://www.heredesign.com/)) |
| Heure Bleue | Hautes-Alpes, France | [heurebleue.studio](https://heurebleue.studio/) | — | Neue Montreal, PP Acma (roles not separated) | — | neo-grotesk · condensed display sans | Pangram Pangram | free-personal | CSS census, 24 Oct 2026 ([site](https://heurebleue.studio/)) |
| Hey | Barcelona, Spain | [heystudio.es](https://heystudio.es) | Helvetica / Helvetica Neue | same (+ Arial, Arial) | — | neo-grotesk | Linotype / Monotype · Monotype (system font) | paid · system | Theme CSS sets body to Helvetica, Helvetica Neue, Arial; no @font-face, so no webfont loaded ([heystudio.es](https://heystudio.es/wp-content/themes/heystudio/style.css)) — recheck: verified |
| Human After All | London, UK | [humanafterall.studio](https://humanafterall.studio) | Mabry | — (+ Cooper) | — | grotesque · soft/wonky serif | Colophon · after Oswald Cooper (several digitisations) | paid | Typewolf Site of the Day, June 2020: website uses Mabry and Cooper ([typewolf.com](https://www.typewolf.com/site-of-the-day/human-after-all)) |
| Little Plains | New York, USA | [littleplains.com](https://www.littleplains.com/) | JJannon Display* | same | — | old-style/Garalde serif | Optimo | paid | CSS census, 24 Oct 2026 ([site](https://www.littleplains.com/)) |
| Lotta Nieminen Studio | New York, USA | [lottanieminen.com](https://www.lottanieminen.com/) | Romie | Unica77 | — | Didone/high-contrast serif · neo-grotesk | Margot Lévêque Studio · Lineto | paid | CSS census, 24 Oct 2026 ([site](https://www.lottanieminen.com/)) |
| Maison AUGE | — | [maisonauge.com](https://maisonauge.com/) | Neue Montreal* | same | — | neo-grotesk | Pangram Pangram | free-personal | CSS census, 24 Oct 2026 ([site](https://maisonauge.com/)) |
| Meor Studio | St Ives, Cornwall, UK | [meorstudio.co.uk](https://meorstudio.co.uk) | Neue Haas Grotesk | same | Proxima Nova, Juana | neo-grotesk · geometric sans · unverified | Font Bureau / Monotype (C. Schwartz) · Mark Simonson · unverified | paid · unverified | Theme CSS declares Neue Haas Grotesk for body and headings but has no @font-face; census saw no webfont loaded ([meorstudio.co.uk](https://meorstudio.co.uk/wp-content/themes/meor/style.css)) — recheck: partial |
| Moving Brands | London / San Francisco, UK | [movingbrands.com](https://movingbrands.com) | Gellix | same | — | geometric sans | Displaay (Martin Vácha) | paid | Theme CSS @font-face Gellix Medium/Bold; h1-h6, buttons and .font-body use Gellix ([movingbrands.com](https://movingbrands.com/wp-content/themes/movingbrands/style.css)) |
| Mucca | New York, USA | [mucca.com](https://www.mucca.com/) | BronzaGrotesqueGX (unidentified) | EB Garamond (+ Poppins, Galaxie Copernicus, Aktiv Grotesk) | — | unverified · old-style/Garalde serif · geometric sans · neo-grotesk | unverified · Georg Duffner / Octavio Pardo · Indian Type Foundry · Village · Dalton Maag | unverified · free/open · paid · paid (Adobe Fonts) | CSS census, 24 Oct 2026 ([site](https://www.mucca.com/)) |
| NB Studio | London, UK | [nbstudio.co.uk](https://nbstudio.co.uk) | Noi Grotesk | same | — | grotesque | Studio Feixen (Robin Eberwein, Felix Pfäffli) | paid | Theme CSS self-hosts Noi Grotesk Light, Medium, Semibold via @font-face; no other family declared ([nbstudio.co.uk](https://nbstudio.co.uk/wp-content/themes/nb/style.css)) |
| Nido Creative Studio | Oslo, Norway | [nidocreativestudio.com](https://www.nidocreativestudio.com/) | Questrial | Holyriver | — | geometric sans · display/novelty | Joe Prince · Sancrea | free/open · paid | CSS census, 24 Oct 2026 ([site](https://www.nidocreativestudio.com/)) |
| Odds Studio | Paris, France | [odds-studio.com](https://odds-studio.com/) | GT Flexa* | same | — | grotesque | Grilli Type | paid | CSS census, 24 Oct 2026 ([site](https://odds-studio.com/)) |
| Ofform | Paris, France | [offormdesign.com](https://offormdesign.com/) | Suisse Int'l | same | — | neo-grotesk | Swiss Typefaces | paid | CSS census, 24 Oct 2026 ([site](https://offormdesign.com/)) |
| OK-RM | London, UK | [ok-rm.co.uk](https://www.ok-rm.co.uk/) | Times New Roman / Times Seven | same | — | transitional serif | Monotype | paid | CSS census, 24 Oct 2026 ([site](https://www.ok-rm.co.uk/)) |
| Perky Bros | Nashville, USA | [perkybros.com](https://perkybros.com/) | — | Dada Grotesk, Quadrant Text (roles not separated) | — | grotesque · slab/Clarendon serif | Optimo · Matter of Sorts | paid | CSS census, 24 Oct 2026 ([site](https://perkybros.com/)) |
| Poch Studio | — | [poch.studio](https://poch.studio/) | Season Mix | Season Sans (+ Fontdiner Swanky, Lacquer) | — | contemporary editorial serif · neo-grotesk · display/novelty | Displaay Type Foundry · Font Diner · Niki Polyocan, Eli Block | paid · free/open | CSS census, 24 Oct 2026 ([site](https://poch.studio/)) |
| Present | — | [presentstudio.co](https://www.presentstudio.co/) | Syllabus | same | — | old-style/Garalde serif | Matter of Sorts | paid | CSS census, 24 Oct 2026 ([site](https://www.presentstudio.co/)) |
| Quatrième Étage | — | [quatriemeetage.studio](https://quatriemeetage.studio/) | ABC Monument Grotesk* | same | ABC Monument Grotesk Mono | grotesque · grotesk mono | Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://quatriemeetage.studio/)) |
| Red Antler | New York, USA | [redantler.com](https://www.redantler.com) | Helvetica Now | same | — | neo-grotesk | Monotype | paid | Typewolf Site of the Day, March 2024: Red Antler website set in Helvetica Now (only font listed) ([typewolf.com](https://www.typewolf.com/site-of-the-day/red-antler-2024)) |
| Robot Food | Leeds, UK | [robot-food.com](https://www.robot-food.com/) | DM Serif* | DM Sans* | DM Mono | Didone/high-contrast serif · geometric sans · grotesk mono | Colophon (for Google) | free/open | CSS census, 24 Oct 2026 ([site](https://www.robot-food.com/)) |
| République Studio | Paris, France | [republique.studio](https://www.republique.studio/) | ABC Diatype* | same | — | neo-grotesk | Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://www.republique.studio/)) |
| Savvy Studio | Mexico City, Mexico | [savvy-studio.net](https://savvy-studio.net/) | — | Contax, Adobe Caslon, Futura (roles not separated) | — | geometric sans · old-style/Garalde serif | Type Innovations · Adobe (Carol Twombly) · Bauer / ParaType (Futura PT) / Linotype | paid · paid (Adobe Fonts) | CSS census, 24 Oct 2026 ([site](https://savvy-studio.net/)) |
| smalltribe | Leipzig, Germany | [smalltribe.studio](https://smalltribe.studio/) | Klarheit Kurrent | Klarheit Grotesk | — | geometric sans | Extraset | paid | CSS census, 24 Oct 2026 ([site](https://smalltribe.studio/)) |
| Smörgåsbord | Amsterdam / Cardiff | [smorgasbord.studio](https://smorgasbord.studio/) | Akkurat* | same | — | neo-grotesk | Lineto | paid | CSS census, 24 Oct 2026 ([site](https://smorgasbord.studio/)) |
| Studio Ambre | (city not stated), Switzerland | [studioambre.com](https://www.studioambre.com) | TWK Continental | same | TWK Continental, custom 'Ambre' cut | grotesque · custom | Weltkern (TWK) · Weltkern for Studio Ambre | paid · custom | Site style.css self-hosts TWK Continental for body and a custom ContinentalAmbre cut for tags ([studioambre.com](https://www.studioambre.com/style.css)) |
| Studio Blackburn | London, UK | [studioblackburn.com](https://studioblackburn.com) | Union | same | — | grotesque | RP Digital Type Foundry (Radim Peško) | paid | Typewolf Site of the Day, October 2021: website uses Union (only font listed) ([typewolf.com](https://www.typewolf.com/site-of-the-day/studio-blackburn)) |
| Studio Feixen | Lucerne, Switzerland | [studiofeixen.ch](https://www.studiofeixen.ch/) | Studio Feixen Sans* | same | — | neo-grotesk | Studio Feixen Fonts | paid | CSS census, 24 Oct 2026 ([site](https://www.studiofeixen.ch/)) |
| Studio Frith | London, UK | [studiofrith.com](https://studiofrith.com/) | Eidetic Neo* | same | — | contemporary editorial serif | Emigre | paid | CSS census, 24 Oct 2026 ([site](https://studiofrith.com/)) |
| Studio GD | Copenhagen, Denmark | [studiogd.dk](https://www.studiogd.dk/) | Helvetica / Helvetica Neue* | same | — | neo-grotesk | Linotype / Monotype | paid | CSS census, 24 Oct 2026 ([site](https://www.studiogd.dk/)) |
| Studio Gruhl | Berlin, Germany | [studiogruhl.com](https://www.studiogruhl.com/) | Greed | same | — | neo-grotesk | Displaay Type Foundry | paid | CSS census, 24 Oct 2026 ([site](https://www.studiogruhl.com/)) |
| Studio Mut | Bolzano, Italy | [studiomut.com](https://www.studiomut.com) | Akzidenz-Grotesk | same | — | grotesque | Berthold | paid | Typewolf 2015 lists Akzidenz Grotesk; current Next.js site loads an unnamed self-hosted face ('font') ([typewolf.com](https://www.typewolf.com/site-of-the-day/studio-mut)) — recheck: partial |
| Studio OL | Los Angeles, USA | [ol.studio](https://ol.studio/) | acp (unidentified)* | same | — | unverified | unverified | unverified | CSS census, 24 Oct 2026 ([site](https://ol.studio/)) |
| Studio Output | London / Nottingham, UK | [studio-output.com](https://www.studio-output.com) | PP Radio Grotesk | same | Recife Text | grotesque · contemporary editorial serif | Pangram Pangram · Luzi Type (Luzi Gantenbein) | free-personal · paid | Theme CSS self-hosts PP Radio Grotesk for body and headings, Recife Text for quotes ([studio-output.com](https://www.studio-output.com/app/themes/studio-output/public/build/assets/app-CcIae0oq.css)) |
| StudioBand | Adelaide, Australia | [studioband.com.au](https://www.studioband.com.au/) | Aeonik | same | — | neo-grotesk | CoType Foundry | paid | CSS census, 24 Oct 2026 ([site](https://www.studioband.com.au/)) |
| Super Keen | New York, USA | [superkeen.studio](https://www.superkeen.studio/) | — | no web font loaded (system fonts, or type drawn as images) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://www.superkeen.studio/)); recheck found nothing more: Next.js site with no colophon or exposed assets; census saw only ui-sans-serif fallback ([superkeen.studio](https://www.superkeen.studio/about)) |
| Toormix | Barcelona, Spain | [toormix.com](https://toormix.com/) | Bandit | GT America | GT America Mono | unverified · American gothic · grotesk mono | AllCaps · Grilli Type | paid | CSS census, 24 Oct 2026 ([site](https://toormix.com/)) |
| Unspoken Agreement | — | [unspokenagreement.com](https://www.unspokenagreement.com/) | Lausanne* | same | — | neo-grotesk | Weltkern (TWK) | paid | CSS census, 24 Oct 2026 ([site](https://www.unspokenagreement.com/)) |
| Werklig | Helsinki, Finland | [werklig.com](https://werklig.com) | Werklig Sans | same | — | neo-grotesk | Werklig (in-house) | custom | Theme.json self-hosts in-house Werklig Sans (WerkligSansBeta07) for body and headings ([werklig.com](https://werklig.com/wp-content/themes/werklig/theme.json)) |
| Zeus Jones | Minneapolis, USA | [zeusjones.com](https://zeusjones.com) | Cambon | — (+ Relative) | — | contemporary editorial serif · grotesque | General Type Studio (Stéphane Elbaz) · Colophon | paid | Typewolf Site of the Day, January 2020: website uses Cambon and Relative ([typewolf.com](https://www.typewolf.com/site-of-the-day/zeus-jones)) |

### 3.3 Indian studios (26)

| Studio | City, country | Site | Display | Text | Mono / label | Classification | Foundry | Licence | Source |
|---|---|---|---|---|---|---|---|---|---|
| Animal | New Delhi, India | [weareanimal.co](https://www.weareanimal.co/) | Archivo | Lora | — | grotesque · contemporary editorial serif | Omnibus-Type · Cyreal | free/open | CSS census, 24 Oct 2026 ([site](https://www.weareanimal.co/)) |
| Beyondesign | Mumbai, India | [beyondesign.in](https://beyondesign.in/) | Plus Jakarta Sans | Inter | — | geometric sans · neo-grotesk | Tokotype · Rasmus Andersson | free/open | CSS census, 24 Oct 2026 ([site](https://beyondesign.in/)) |
| Bombay Duck Designs | Mumbai, India | [bombayduckdesigns.com](https://www.bombayduckdesigns.com/) | Neue Haas Grotesk | same | — | neo-grotesk | Font Bureau / Monotype (C. Schwartz) | paid | CSS census, 24 Oct 2026 ([site](https://www.bombayduckdesigns.com/)) |
| Codesign | Gurugram, India | [codesign.in](https://www.codesign.in/) | Sentinel | Whitney | — | slab/Clarendon serif · humanist sans | Hoefler&Co. | paid | CSS census, 24 Oct 2026 ([site](https://www.codesign.in/)) |
| Confetti Design | Mumbai, India | [confetti.design](https://www.confetti.design/) | Helvetica / Helvetica Neue | Archivo (+ DM Serif, Inter, Poppins) | — | neo-grotesk · grotesque · Didone/high-contrast serif · geometric sans | Linotype / Monotype · Omnibus-Type · Colophon (for Google) · Rasmus Andersson · Indian Type Foundry | paid · free/open | CSS census, 24 Oct 2026 ([site](https://www.confetti.design/)) |
| designmill | India | [designmill.in](https://www.designmill.in/) | Poppins | same | — | geometric sans | Indian Type Foundry | free/open | CSS census, 24 Oct 2026 ([site](https://www.designmill.in/)) |
| Elephant Design | Pune, India | [elephantdesign.com](https://elephantdesign.com/) | — | Open Sans, Syne (roles not separated) | — | humanist sans · display/novelty | Steve Matteson · Bonjour Monde | free/open | CSS census, 24 Oct 2026 ([site](https://elephantdesign.com/)) |
| Itu Chaudhuri Design | New Delhi, India | [icdindia.com](https://icdindia.com/) | Akzidenz-Grotesk | FF Tundra Light | — | grotesque · contemporary editorial serif | Berthold · FontFont (Monotype) | paid | CSS census, 24 Oct 2026 ([site](https://icdindia.com/)) |
| KL11 | Kozhikode, India | [kl11.in](https://kl11.in/) | Tiempos | same | — | contemporary editorial serif | Klim | paid | CSS census, 24 Oct 2026 ([site](https://kl11.in/)) |
| LOCAL | India | [wedesignlocal.com](https://www.wedesignlocal.com) | Open Sans | Avenir (+ Lulo Clean, Sora) | — | humanist sans · geometric sans · extended/wide sans | Steve Matteson · Linotype (Adrian Frutiger) · Yellow Design Studio · Barnbrook / Julián Moncada | free/open · paid | Census: h1 computed Open Sans; Wix built-ins Avenir, Lulo Clean, Sora also loaded ([wedesignlocal.com](https://www.wedesignlocal.com/)) — recheck: partial |
| Locopopo | Mumbai, India | [locopopo.com](https://locopopo.com/) | Aktiv Grotesk Extended | Aktiv Grotesk | — | extended/wide sans · neo-grotesk | Dalton Maag | paid (Adobe Fonts) | CSS census, 24 Oct 2026 ([site](https://locopopo.com/)) |
| Lollypop Design Studio | Bengaluru, India | [lollypop.design](https://lollypop.design) | Franklin (Libre Franklin) | same | — | American gothic | Impallari Type | free/open | Theme 'lollypop' style.css is a Twenty Seventeen copy declaring Libre Franklin; custom CSS not inspected ([lollypop.design](https://lollypop.design/wp-content/themes/lollypop/style.css)) — partial |
| Lopez Design | Gurugram, India | [thisislopez.com](https://thisislopez.com/) | — | Open Sans, Acumin, Fira Sans (roles not separated) | — | humanist sans · neo-grotesk | Steve Matteson · Adobe (Robert Slimbach) · Carrois / Mozilla | free/open · paid (Adobe Fonts) | CSS census, 24 Oct 2026 ([site](https://thisislopez.com/)) |
| November | Mumbai, India | [nvmbr.in](https://www.nvmbr.in/) | Delegate | same | Delegate Mono | American gothic · grotesk mono | Commercial Type | paid | CSS census, 24 Oct 2026 ([site](https://www.nvmbr.in/)) |
| Opposite | Goa, India | [oppositehq.com](https://oppositehq.com/) | Roobert | same | — | geometric sans | Displaay | paid | CSS census, 24 Oct 2026 ([site](https://oppositehq.com/)) |
| Squadron 14 | New Delhi, India | [squadron14.com](https://squadron14.com/) | Untitled Sans* | same | — | neo-grotesk | Klim | paid | CSS census, 24 Oct 2026 ([site](https://squadron14.com/)) |
| Studio ABD | India | [studioabd.in](https://www.studioabd.in) | — | Helvetica / Helvetica Neue, Wix Madefor (roles not separated) | — | neo-grotesk | Linotype / Monotype · Dalton Maag for Wix | paid · free/open | Census lists Wix built-ins plus three uploaded fonts; full upload IDs not captured, so names unreadable ([studioabd.in](https://www.studioabd.in/)) — recheck: unverified |
| Studio Bigfat | Mumbai, India | [studiobigfat.com](https://studiobigfat.com/) | Big Caslon | same | Space Mono | old-style/Garalde serif · grotesk mono | Font Bureau (Matthew Carter) · Colophon (for Google) | paid · free/open | CSS census, 24 Oct 2026 ([site](https://studiobigfat.com/)) |
| Studio N°7 (Studio Number Seven) | India (census bucket; unconfirmed) | [studionumberseven.com](https://www.studionumberseven.com) | Editorial New | Wix Madefor | — | Didone/high-contrast serif · neo-grotesk | Pangram Pangram · Dalton Maag for Wix | free-personal · free/open | Census h1 font file wfont_ef2f9f_b4e8ad... name table reads Editorial New Ultralight, Pangram Pangram; site is coming-soon page ([static.wixstatic.com](https://static.wixstatic.com/ufonts/ef2f9f_b4e8ad21f8f74098860e9ca3304d1cbd/ttf/file.ttf)) — recheck: partial |
| Studio Ping Pong | Bengaluru, India | [studiopingpong.com](https://studiopingpong.com/) | Dejanire Text | Obviously Narrow (+ Argent Pixel CF) | Degular Mono | transitional serif · condensed display sans · grotesk mono · pixel/bitmap | Retype · OH no Type Co. · Connary Fagen | paid · paid (Adobe Fonts) | CSS census, 24 Oct 2026 ([site](https://studiopingpong.com/)) |
| Studio Sorted | Bengaluru, India | [studiosorted.com](https://www.studiosorted.com/) | — | Apfel Grotezk, Cabinet Grotesk, Satoshi, Montserrat (roles not separated) | — | grotesque · geometric sans | Collletttivo · Indian Type Foundry (Fontshare) · Julieta Ulanovsky | free/open · free-commercial | CSS census, 24 Oct 2026 ([site](https://www.studiosorted.com/)) |
| The Turtle Story | Mumbai, India | [theturtlestory.com](https://www.theturtlestory.com/) | Inter | Poppins | — | neo-grotesk · geometric sans | Rasmus Andersson · Indian Type Foundry | free/open | CSS census, 24 Oct 2026 ([site](https://www.theturtlestory.com/)) |
| Therefore Design | India | [thereforedesign.co.in](https://www.thereforedesign.co.in) | Exo 2 | Helvetica / Helvetica Neue | — | geometric sans · neo-grotesk | Natanael Gama · Linotype / Monotype | free/open · paid | Census h1 font file wfont_0ce401_7b9dda... name table reads Exo 2 Regular by Natanael Gama ([static.wixstatic.com](https://static.wixstatic.com/ufonts/0ce401_7b9dda96909b4af5b3c6e0352208cf7a/ttf/file.ttf)) — recheck: partial |
| Whoamama | Chennai, India | [whoamama.com](https://whoamama.com/) | Helvetica / Helvetica Neue | Hanken Grotesk | — | neo-grotesk | Linotype / Monotype · Hanken Design Co. | paid · free/open | CSS census, 24 Oct 2026 ([site](https://whoamama.com/)) |
| Wishbox Studio | Delhi, India | [wishboxstudio.in](https://wishboxstudio.in/) | Recoleta | Neue Haas Unica | — | soft/wonky serif · neo-grotesk | Latinotype · Monotype (Toshi Omagari) | paid | CSS census, 24 Oct 2026 ([site](https://wishboxstudio.in/)) |
| Zensciences | Bengaluru, India | [zensciences.com](https://zensciences.com) | Cabin | same | Inter | humanist sans · neo-grotesk | Impallari Type · Rasmus Andersson | free/open | Child-theme CSS sets body to Cabin, overriding parent's Raleway; Inter for banner text ([zensciences.com](https://zensciences.com/wp-content/themes/ultra-print-child/style.css)) |

### 3.4 Digital and motion studios (35)

| Studio | City, country | Site | Display | Text | Mono / label | Classification | Foundry | Licence | Source |
|---|---|---|---|---|---|---|---|---|---|
| 14islands | Stockholm, Sweden | [14islands.com](https://www.14islands.com) | — | Aften Screen, Benton Sans (roles not separated) | — | humanist sans · American gothic | Monokrom · Font Bureau | paid | CSS census, 24 Oct 2026 ([site](https://www.14islands.com)) |
| Active Theory | Los Angeles, USA | [activetheory.net](https://activetheory.net) | NB Architekt* | same | — | geometric sans | Neubau (NeubauLaden) | paid | CSS census, 24 Oct 2026 ([site](https://activetheory.net)) |
| Akaru | Lyon, France | [akaru.fr](https://www.akaru.fr/) | Alliance | Alliance Platt | — | grotesque · unverified | Degarism Studio · Degarism Studio (presumed) | paid | CSS census, 24 Oct 2026 ([site](https://www.akaru.fr/)) |
| Antinomy | — | [antinomy.studio](https://antinomy.studio) | ABC Diatype | same | — | neo-grotesk | Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://antinomy.studio)) |
| Aristide Benoist | — | [aristidebenoist.com](https://aristidebenoist.com) | — | TNY, jws (roles not separated) | — | unverified | unknown | unknown | CSS census, 24 Oct 2026 ([site](https://aristidebenoist.com)) |
| Basement Studio | Buenos Aires, Argentina | [basement.studio](https://basement.studio) | Geist | FFFLAUTA | Geist Mono | neo-grotesk · pixel/bitmap · grotesk mono | Vercel / Basement Studio · Basement Foundry (basement.studio) | free/open · paid | CSS census, 24 Oct 2026 ([site](https://basement.studio)) |
| Buck | Los Angeles / New York | [buck.co](https://buck.co) | Mabry* | same | — | grotesque | Colophon | paid | CSS census, 24 Oct 2026 ([site](https://buck.co)) |
| Chipsa | — | [chipsa.design](https://chipsa.design/) | PP Right Grotesk | Neue Montreal | — | grotesque · neo-grotesk | Pangram Pangram | free-personal | CSS census, 24 Oct 2026 ([site](https://chipsa.design/)) |
| Cuberto | USA | [cuberto.com](https://cuberto.com) | Suisse Int'l | same | — | neo-grotesk | Swiss Typefaces | paid | CSS census, 24 Oct 2026 ([site](https://cuberto.com)) |
| Darkroom Engineering | — | [darkroom.engineering](https://darkroom.engineering) | therma (unidentified) | sauce (unidentified) (+ unnamed/obfuscated face) | — | unverified | unverified | unverified | CSS census, 24 Oct 2026 ([site](https://darkroom.engineering)) |
| Dennis Snellenberg | — | [dennissnellenberg.com](https://dennissnellenberg.com) | Dennis Sans | same | — | unverified | unknown | unknown | CSS census, 24 Oct 2026 ([site](https://dennissnellenberg.com)) |
| Dogstudio | Namur, Belgium / Chicago, USA | [dogstudio.co](https://dogstudio.co) | GT Sectra* | Heebo* (+ Gilroy) | — | contemporary editorial serif · neo-grotesk · geometric sans | Grilli Type · Oded Ezer · Radomir Tinkov | paid · free/open | CSS census, 24 Oct 2026 ([site](https://dogstudio.co)) |
| Exo Ape | — | [exoape.com](https://exoape.com) | Lausanne | same | — | neo-grotesk | Weltkern (TWK) | paid | CSS census, 24 Oct 2026 ([site](https://exoape.com)) |
| Fiddle.Digital | — | [fiddle.digital](https://fiddle.digital/) | — | KH Teka, Manrope (roles not separated) (+ unnamed/obfuscated face) | KH Teka Mono | neo-grotesk · grotesk mono · geometric sans | KH Type (Kurppa Hosk) · Mikhail Sharanda | paid · free/open | CSS census, 24 Oct 2026 ([site](https://fiddle.digital/)) |
| Hello Monday | Copenhagen / New York | [hellomonday.com](https://hellomonday.com) | Clarendon | NB International | — | slab/Clarendon serif · neo-grotesk | Bitstream / Monotype · Neubau | paid | CSS census, 24 Oct 2026 ([site](https://hellomonday.com)) |
| Immersive Garden | Paris, France | [immersive-g.com](https://immersive-g.com) | PS Times | Helvetica / Helvetica Neue | — | transitional serif · neo-grotesk | Parker Studio (unconfirmed) · Linotype / Monotype | unknown · paid | CSS census, 24 Oct 2026 ([site](https://immersive-g.com)) |
| Locomotive | Montreal, Canada | [locomotive.ca](https://locomotive.ca) | Editorial New | Helvetica Now | — | Didone/high-contrast serif · neo-grotesk | Pangram Pangram · Monotype | free-personal · paid | Fonts In Use, 2023: Locomotive's own portfolio website combines Editorial New with Helvetica Now ([fontsinuse.com](https://fontsinuse.com/uses/61459/locomotive-portfolio-website-and-visual-ident)) — recheck: verified |
| Lusion | Bristol, UK | [lusion.co](https://lusion.co) | Aeonik | same | IBM Plex Mono, LusionMono | neo-grotesk · grotesk mono | CoType Foundry · IBM / Bold Monday · Lusion (in-house) | paid · free/open · custom | CSS census, 24 Oct 2026 ([site](https://lusion.co)) |
| Makemepulse | Paris, France | [makemepulse.com](https://www.makemepulse.com/) | Beatrice Display | Biotif | — | neo-grotesk · geometric sans | Sharp Type · Degarism Studio | paid | CSS census, 24 Oct 2026 ([site](https://www.makemepulse.com/)) |
| Merci-Michel | Paris, France | [merci-michel.com](https://www.merci-michel.com/) | Mnm* | same | — | unverified | Merci-Michel (in-house) | custom | CSS census, 24 Oct 2026 ([site](https://www.merci-michel.com/)) |
| Noomo Agency | Los Angeles, USA | [noomoagency.com](https://noomoagency.com/) | PP Neue Machina | NeueRoman (unidentified) | — | geometric sans · unverified | Pangram Pangram · unverified | free-personal · unverified | CSS census, 24 Oct 2026 ([site](https://noomoagency.com/)) |
| Obys | Kharkiv, Ukraine / EU | [obys.agency](https://obys.agency) | — | Obys, OTF Obys NG (roles not separated) | — | unverified · neo-grotesk | Obys (in-house) | custom | CSS census, 24 Oct 2026 ([site](https://obys.agency)) |
| Phantom | London, UK / Auckland, NZ | [phantom.land](https://www.phantom.land/) | Helvetica Now | same | Ballinger Mono | neo-grotesk · grotesk mono | Monotype · Signal Type Foundry | paid | CSS census, 24 Oct 2026 ([site](https://www.phantom.land/)) |
| Rejouice | Paris, France | [rejouice.com](https://www.rejouice.com) | Suisse Int'l | same | — | neo-grotesk | Swiss Typefaces | paid | CSS census, 24 Oct 2026 ([site](https://www.rejouice.com)) |
| Resn | Wellington, New Zealand | [resn.co.nz](https://resn.co.nz) | Fort | same | — | DIN/industrial sans | MCKL | paid | CSS census, 24 Oct 2026 ([site](https://resn.co.nz)) |
| Salt and Pepper | — | [snp.agency](https://snp.agency/) | — | Suisse Int'l, ABC Favorit (roles not separated) | — | neo-grotesk · grotesque | Swiss Typefaces · Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://snp.agency/)) |
| Stink Studios | New York / London, USA | [stinkstudios.com](https://www.stinkstudios.com) | Times New Roman / Times Seven | — (+ Helvetica / Helvetica Neue) | Courier | transitional serif · typewriter mono · neo-grotesk | Monotype · system font · Linotype / Monotype | paid · system | Typewolf Site of the Day, February 2022: Times New Roman, Helvetica, Courier ([typewolf.com](https://www.typewolf.com/site-of-the-day/stink-studios)) |
| Studio Freight | — | [studiofreight.com](https://studiofreight.com/) | JJannon | same | Publico Text Mono | old-style/Garalde serif · typewriter mono | Optimo · Commercial Type | paid | CSS census, 24 Oct 2026 ([site](https://studiofreight.com/)) |
| Studio Namma | Paris, France | [studionamma.com](https://studionamma.com/) | Mixtape Extra Condensed (unidentified) | Mixtape (unidentified) | GT Pressura Mono | unverified · grotesk mono | unverified · Grilli Type | unverified · paid | CSS census, 24 Oct 2026 ([site](https://studionamma.com/)) |
| Studio Null | — | [madebynull.com](https://www.madebynull.com/) | ABC Areal* | same | — | neo-grotesk | Dinamo | custom | CSS census, 24 Oct 2026 ([site](https://www.madebynull.com/)) |
| Synchronized | — | [synchronized.studio](https://synchronized.studio/) | — | no web font loaded (system fonts, or type drawn as images) (+ unnamed/obfuscated face) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://synchronized.studio/)) |
| The Line Studio | London, UK | [thelinestudio.com](https://thelinestudio.com/) | DenimWeb (unidentified)* | same | — | unverified | unverified | unverified | CSS census, 24 Oct 2026 ([site](https://thelinestudio.com/)) |
| Unseen Studio | Bristol, UK | [unseen.co](https://unseen.co) | Neue Montreal | Saol | — | neo-grotesk · Didone/high-contrast serif | Pangram Pangram · Schick Toikka | free-personal · paid | CSS census, 24 Oct 2026 ([site](https://unseen.co)) |
| Utsubo | — | [utsubo.com](https://www.utsubo.com) | PP Mori | same | — | neo-grotesk | Pangram Pangram | free-personal | CSS census, 24 Oct 2026 ([site](https://www.utsubo.com)) |
| Watson | Los Angeles, USA | [watson.la](https://watson.la/) | — | no web font loaded (system fonts, or type drawn as images) (+ unnamed/obfuscated face) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://watson.la/)) |

### 3.5 Designers and founder-led studios (44)

| Studio | City, country | Site | Display | Text | Mono / label | Classification | Foundry | Licence | Source |
|---|---|---|---|---|---|---|---|---|---|
| Adrien Lamy | Paris, France | [adrienlamy.fr](https://adrienlamy.fr/) | Comic CAT (unidentified)* | same | — | unverified | unverified | unverified | CSS census, 24 Oct 2026 ([site](https://adrienlamy.fr/)) |
| Aimee Xu's Papercraft World | — | [aimees-papercraft-world.com](https://aimees-papercraft-world.com/) | Slime Box* | same | — | display/novelty | Heaven Castro (FontSpace) | free-commercial | CSS census, 24 Oct 2026 ([site](https://aimees-papercraft-world.com/)) |
| Angela Ricciardi | — | [angelaricciardi.com](https://www.angelaricciardi.com/) | Neue Haas Unica* | same | — | neo-grotesk | Monotype (Toshi Omagari) | paid | CSS census, 24 Oct 2026 ([site](https://www.angelaricciardi.com/)) |
| Aralesk — Collages & Motion | Spain | [aralesk.es](https://www.aralesk.es/) | Anton | Montserrat (+ Bebas Neue) | — | condensed display sans · geometric sans | Vernon Adams · Julieta Ulanovsky · Ryoichi Tsunekawa (Dharma Type) | free/open | CSS census, 24 Oct 2026 ([site](https://www.aralesk.es/)) |
| Beci Orpin | Melbourne, Australia | [beciorpin.com](https://beciorpin.com/) | droulers (unidentified)* | same | — | unverified | unverified | unverified | CSS census, 24 Oct 2026 ([site](https://beciorpin.com/)) |
| Bruno Simon | Paris, France | [bruno-simon.com](https://bruno-simon.com) | — | Nunito, Amatic SC, Pally (roles not separated) | — | rounded sans · handwriting | Vernon Adams et al. · Vernon Adams · Indian Type Foundry (Fontshare) | free/open · free-commercial | CSS census, 24 Oct 2026 ([site](https://bruno-simon.com)) |
| Camille Mormal | — | [camillemormal.com](https://camillemormal.com/) | — | no web font loaded (system fonts, or type drawn as images) (+ unnamed/obfuscated face) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://camillemormal.com/)) |
| Chrissie Abbott | — | [chrissieabbott.com](https://chrissieabbott.com/) | — | ABC Favorit, Young Serif (roles not separated) | — | grotesque · old-style/Garalde serif | Dinamo · Bastien Sozeau | paid · free/open | CSS census, 24 Oct 2026 ([site](https://chrissieabbott.com/)) |
| Collage Department | — | [collagedepartment.com](https://collagedepartment.com/) | Kharkiv Tone* | same | — | rounded sans | Kate Drozd | free-commercial | CSS census, 24 Oct 2026 ([site](https://collagedepartment.com/)) |
| Daniel Blue | San Francisco Bay Area, USA | [danielblue.com](https://danielblue.com/) | — | ABC Arizona, Season Mix (roles not separated) | — | contemporary editorial serif | Dinamo · Displaay Type Foundry | paid | CSS census, 24 Oct 2026 ([site](https://danielblue.com/)) |
| davesocozy | Philadelphia, USA | [davesocozy.com](https://davesocozy.com/) | Martian Mono | same | Martian Mono | grotesk mono | Evil Martians | free/open | CSS census, 24 Oct 2026 ([site](https://davesocozy.com/)) |
| Emil Kowalski | — | [emilkowal.ski](https://emilkowal.ski) | — | no web font loaded (system fonts, or type drawn as images) (+ unnamed/obfuscated face) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://emilkowal.ski)) |
| Félix Péault | — | [felixpeault.com](https://www.felixpeault.com/) | Suisse Int'l Condensed | Archivo | — | condensed display sans · grotesque | Swiss Typefaces · Omnibus-Type | paid · free/open | CSS census, 24 Oct 2026 ([site](https://www.felixpeault.com/)) |
| Gianluca Gradogna | Florence, Italy | [gianlucagradogna.com](https://gianlucagradogna.com/) | Neue Montreal | same (+ unnamed/obfuscated face) | — | neo-grotesk | Pangram Pangram | free-personal | CSS census, 24 Oct 2026 ([site](https://gianlucagradogna.com/)) |
| Gil Huybrecht | — | [gilhuybrecht.com](https://gilhuybrecht.com/) | — | no web font loaded (system fonts, or type drawn as images) (+ unnamed/obfuscated face) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://gilhuybrecht.com/)) |
| Grit Pictures | — | [grit.pictures](https://grit.pictures/) | Bebas Neue | Roboto (+ Poppins) | — | condensed display sans · neo-grotesk · geometric sans | Ryoichi Tsunekawa (Dharma Type) · Google (Christian Robertson) · Indian Type Foundry | free/open | CSS census, 24 Oct 2026 ([site](https://grit.pictures/)) |
| Heena Chung | — | [heenachung.info](https://heenachung.info/) | TeX Gyre Heros* | same | — | neo-grotesk | GUST (Helvetica-metric clone) | free/open | CSS census, 24 Oct 2026 ([site](https://heenachung.info/)) |
| hi, 6 — Scrapbook (Hicard Studio) | — | [scrapbook.hicard.studio](https://scrapbook.hicard.studio/) | Inter Display* | same | — | neo-grotesk | Rasmus Andersson | free/open | CSS census, 24 Oct 2026 ([site](https://scrapbook.hicard.studio/)) |
| Hugo Ahlberg | Bay Area, USA | [hugoahlberg.com](https://hugoahlberg.com/) | ABC Walter Neue* | same | — | humanist sans | Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://hugoahlberg.com/)) |
| Ikai Asai | India | [ikaiasai.com](https://www.ikaiasai.com/) | Neue Haas Grotesk | Lexend Deca (+ Roboto) | Cutive Mono | neo-grotesk · geometric sans · typewriter mono | Font Bureau / Monotype (C. Schwartz) · Bonnie Shaver-Troup et al. · Vernon Adams · Google (Christian Robertson) | paid · free/open | CSS census, 24 Oct 2026 ([site](https://www.ikaiasai.com/)) |
| Jacob Hutch (pin author) | — | [jacobhutch.com](https://www.jacobhutch.com) | Helvetica / Helvetica Neue* | same | — | neo-grotesk | Linotype / Monotype | paid | CSS census, 24 Oct 2026 ([site](https://www.jacobhutch.com)) |
| Jason Bergh | Seattle, USA | [jasonbergh.com](https://www.jasonbergh.com/) | — | Editorial New, ABC Monument Grotesk (roles not separated) | ABC Monument Grotesk Mono, ABC Simon Mono | Didone/high-contrast serif · grotesk mono · grotesque | Pangram Pangram · Dinamo | free-personal · paid | CSS census, 24 Oct 2026 ([site](https://www.jasonbergh.com/)) |
| Juan Mora | — | [juanmora.co](https://juanmora.co/) | Goga | same | — | geometric sans | Narrow Type | paid | CSS census, 24 Oct 2026 ([site](https://juanmora.co/)) |
| Julia Noni | — | [julianoni.com](https://julianoni.com/) | Suisse Int'l* | same | — | neo-grotesk | Swiss Typefaces | paid | CSS census, 24 Oct 2026 ([site](https://julianoni.com/)) |
| Kai Blamey Nguyen | — | [kaiblamey.com](https://kaiblamey.com/) | ABC Schengen* | same | — | neo-grotesk | Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://kaiblamey.com/)) |
| Katrine Mehl | Denmark | [katrinemehl.com](https://katrinemehl.com/) | Graphik | same | — | neo-grotesk | Commercial Type | paid | CSS census, 24 Oct 2026 ([site](https://katrinemehl.com/)) |
| Loli Laboureau | — | [lolilaboureau.com](https://www.lolilaboureau.com/) | Inter* | same | Fragment Mono, Azeret Mono | neo-grotesk · grotesk mono | Rasmus Andersson · Wei Huang / URW · Displaay (Martin Vácha) | free/open | CSS census, 24 Oct 2026 ([site](https://www.lolilaboureau.com/)) |
| Lynn and Tonic | Phoenix, USA | [lynnandtonic.com](https://lynnandtonic.com) | Hubano Rough | Sydonia Atramentiqua | — | display/novelty · old-style/Garalde serif | SimpleBits · Piotr Wardziukiewicz | paid | CSS census, 24 Oct 2026 ([site](https://lynnandtonic.com)) |
| Marianna von Fedak | — | [mariannavonfedak.com](https://mariannavonfedak.com/) | — | no web font loaded (system fonts, or type drawn as images) (+ unnamed/obfuscated face) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://mariannavonfedak.com/)) |
| Mark Clennon | — | [markclennon.com](https://www.markclennon.com/) | Boogy Brut Poster* | same | — | contemporary editorial serif | Bureau Brut | paid | CSS census, 24 Oct 2026 ([site](https://www.markclennon.com/)) |
| Miranda — Paper Portfolio | Amsterdam, Netherlands | [niccolomiranda.com](https://www.niccolomiranda.com/) | Canopée | Domaine Display (+ Editorial New) | — | condensed display sans · Didone/high-contrast serif | VJ-Type · Klim · Pangram Pangram | paid · free-personal | CSS census, 24 Oct 2026 ([site](https://www.niccolomiranda.com/)) |
| Mr. Panda's Paper Portfolio | — | [mr-pandas-psychologically-safe-portfolio.com](https://www.mr-pandas-psychologically-safe-portfolio.com/) | Plus Jakarta Sans* | same | — | geometric sans | Tokotype | free/open | CSS census, 24 Oct 2026 ([site](https://www.mr-pandas-psychologically-safe-portfolio.com/)) |
| Olivier Larose | — | [olivierlarose.com](https://www.olivierlarose.com) | Editorial New | Neue Montreal (+ Great Vibes, PP Mondwest) | PP Supply Mono | Didone/high-contrast serif · neo-grotesk · grotesk mono · script · pixel/bitmap | Pangram Pangram · TypeSETit (Robert Leuschke) | free-personal · free/open | CSS census, 24 Oct 2026 ([site](https://www.olivierlarose.com)) |
| Paco Coursey | — | [paco.me](https://paco.me) | — | Inter, Newsreader, Söhne (roles not separated) | — | neo-grotesk · contemporary editorial serif · grotesque | Rasmus Andersson · Production Type · Klim | free/open · paid | CSS census, 24 Oct 2026 ([site](https://paco.me)) |
| Paper Tiger | — | [papertiger.com](https://www.papertiger.com/) | — | no web font loaded (system fonts, or type drawn as images) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://www.papertiger.com/)); recheck found nothing more: Site behind Cloudflare bot wall (403 to fetch, blocked in census); skipped ([papertiger.com](https://www.papertiger.com/)) |
| Rauno Freiberg | — | [rauno.me](https://rauno.me) | — | no web font loaded (system fonts, or type drawn as images) (+ unnamed/obfuscated face) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://rauno.me)) |
| Rich Stapleton | — | [richstapleton.com](https://richstapleton.com/) | Perpetua* | same | — | old-style/Garalde serif | Monotype (Eric Gill) | paid | CSS census, 24 Oct 2026 ([site](https://richstapleton.com/)) |
| RoAndCo | New York, USA | [roandcostudio.com](https://www.roandcostudio.com) | Tiempos | — (+ Founders Grotesk) | — | contemporary editorial serif · grotesque | Klim | paid | Typewolf Site of the Day, January 2022: Tiempos Fine and Founders Grotesk ([typewolf.com](https://www.typewolf.com/site-of-the-day/roandco-studio)) |
| Sam Thies | Australia | [samthies.com](https://samthies.com/) | — | — | Quadrant Text Mono | typewriter mono | Matter of Sorts | paid | CSS census, 24 Oct 2026 ([site](https://samthies.com/)) |
| Steph Jeong Scrapbook | Brooklyn, USA | [jeongsteph.design](https://jeongsteph.design/) | PP Telegraf | Self Modern | — | geometric sans · contemporary editorial serif | Pangram Pangram · Bretagne | free-personal · paid | CSS census, 24 Oct 2026 ([site](https://jeongsteph.design/)) |
| Stephen Kent Johnson | — | [stephenkentjohnson.com](https://stephenkentjohnson.com/) | DIN 2014* | same | — | DIN/industrial sans | ParaType | paid | CSS census, 24 Oct 2026 ([site](https://stephenkentjohnson.com/)) |
| Synchrodogs / Synchrostudio | Ukraine | [synchrodogs.com](https://synchrodogs.com/) | Garnett | GT America | — | grotesque · American gothic | Sharp Type · Grilli Type | paid | CSS census, 24 Oct 2026 ([site](https://synchrodogs.com/)) |
| Tim Van Damme (Max Voltar) | — | [timvandamme.com](https://timvandamme.com/) | Proxima Soft | Felt Tip Roman | — | rounded sans · handwriting | Mark Simonson · Mark Simonson Studio | paid | CSS census, 24 Oct 2026 ([site](https://timvandamme.com/)) |
| Working Stiff Films | — | [stiff.madebybuzzworthy.com](https://stiff.madebybuzzworthy.com/) | Grand (unidentified) | Neue Montreal | — | unverified · neo-grotesk | unverified · Pangram Pangram | unverified · free-personal | CSS census, 24 Oct 2026 ([site](https://stiff.madebybuzzworthy.com/)) |

## 4. Brands and publications in the census

Not studios, but the like-minded brands and magazines the census captured; `FONT_GUIDE.md` draws on them.

| Brand or publication | City, country | Site | Display | Text | Mono / label | Classification | Foundry | Licence | Source |
|---|---|---|---|---|---|---|---|---|---|
| Aesop | Melbourne, Australia | [aesop.com](https://www.aesop.com) | Suisse Int'l | Zapf Humanist 601 (Optima) | — | neo-grotesk · glyphic/incised | Swiss Typefaces · Bitstream (after Hermann Zapf's Optima) | paid | CSS census, 24 Oct 2026 ([site](https://www.aesop.com)) |
| Apartamento | Barcelona, Spain | [apartamentomagazine.com](https://www.apartamentomagazine.com) | Futura | same | — | geometric sans | Bauer / ParaType (Futura PT) / Linotype | paid | CSS census, 24 Oct 2026 ([site](https://www.apartamentomagazine.com)) |
| ARAKU Coffee | Bengaluru, India | [arakucoffee.in](https://www.arakucoffee.in/) | Roc Grotesk | Gotham (+ T-Star (unidentified)) | — | grotesque · geometric sans · unverified | Kostic Type Foundry · Hoefler&Co. · unverified | paid (Adobe Fonts) · paid · unverified | CSS census, 24 Oct 2026 ([site](https://www.arakucoffee.in/)) |
| Are.na | — | [are.na](https://www.are.na) | ABC Areal* | same | — | neo-grotesk | Dinamo | custom | CSS census, 24 Oct 2026 ([site](https://www.are.na)) |
| Bhaane | Mumbai, India | [bhaane.com](https://www.bhaane.com/) | — | no web font loaded (system fonts, or type drawn as images) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://www.bhaane.com/)) |
| Blue Tokai | — | [bluetokaicoffee.com](https://bluetokaicoffee.com) | Cormorant | Brandon Grotesque (+ TASA Orbiter) | — | old-style/Garalde serif · geometric sans · neo-grotesk | Christian Thalmann · HVD Fonts · Taiwan Space Agency / Local Remote | free/open · paid | CSS census, 24 Oct 2026 ([site](https://bluetokaicoffee.com)) |
| Bombay Perfumery | Mumbai, India | [bombayperfumery.com](https://www.bombayperfumery.com) | Assistant* | same | — | American gothic | Ben Nathan (from Source Sans) | free/open | CSS census, 24 Oct 2026 ([site](https://www.bombayperfumery.com)) |
| Bombay Sweet Shop | Mumbai, India | [bombaysweetshop.com](https://bombaysweetshop.com) | Fraunces | Jost | — | soft/wonky serif · geometric sans | Undercase Type · Owen Earl | free/open | CSS census, 24 Oct 2026 ([site](https://bombaysweetshop.com)) |
| Brightland | — | [brightland.co](https://brightland.co) | — | Circular, Advercase (roles not separated) | — | geometric sans · old-style/Garalde serif | Lineto · Indieground | paid | CSS census, 24 Oct 2026 ([site](https://brightland.co)) |
| Cosmos | New York, USA | [cosmos.so](https://www.cosmos.so) | ABC Oracle | same | — | grotesque | Dinamo | paid | CSS census, 24 Oct 2026 ([site](https://www.cosmos.so)) |
| Deem Journal | — | [deemjournal.com](https://www.deemjournal.com/) | Cheltenham | Roobert | — | old-style/Garalde serif · geometric sans | ITC / Monotype · Displaay | paid | CSS census, 24 Oct 2026 ([site](https://www.deemjournal.com/)) |
| Diaspora Co | Oakland, USA | [diasporaco.com](https://www.diasporaco.com) | P22 Mackinac | Source Sans (+ Fustat, Figtree, GT Standard) | — | contemporary editorial serif · American gothic · humanist sans · geometric sans · neo-grotesk | P22 Type Foundry · Adobe (Paul D. Hunt) · Mohamed Gaber et al. · Erik Kennedy · Grilli Type | paid (Adobe Fonts) · free/open · paid | CSS census, 24 Oct 2026 ([site](https://www.diasporaco.com)) |
| Doodlage | New Delhi, India | [doodlage.in](https://doodlage.in/) | Jost | same | — | geometric sans | Owen Earl | free/open | CSS census, 24 Oct 2026 ([site](https://doodlage.in/)) |
| East Fork | Asheville, USA | [eastfork.com](https://eastfork.com/) | Galano Classic | Toma (unidentified) (+ Quincy CF) | — | geometric sans · unverified · contemporary editorial serif | René Bieder · unverified · Connary Fagen | paid · unverified | CSS census, 24 Oct 2026 ([site](https://eastfork.com/)) |
| Emergence Magazine | — | [emergencemagazine.org](https://emergencemagazine.org/) | — | no web font loaded (system fonts, or type drawn as images) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://emergencemagazine.org/)) |
| Field Notes | Chicago, USA | [fieldnotesbrand.com](https://fieldnotesbrand.com/) | — | Century Schoolbook, Futura (roles not separated) | — | transitional serif · geometric sans | Linotype / Monotype · Bauer / ParaType (Futura PT) / Linotype | paid | CSS census, 24 Oct 2026 ([site](https://fieldnotesbrand.com/)) |
| Fishwife | — | [eatfishwife.com](https://eatfishwife.com) | Recoleta | Albert Sans | — | soft/wonky serif · geometric sans | Latinotype · Andreas Rasmussen | paid · free/open | CSS census, 24 Oct 2026 ([site](https://eatfishwife.com)) |
| Ghia | USA | [drinkghia.com](https://drinkghia.com) | FHA Condensed French NC | Vivey 22 Positive (unidentified) (+ Vevey22 (unidentified)) | — | slab/Clarendon serif · unverified | Fontry West · unverified | free-personal · unverified | CSS census, 24 Oct 2026 ([site](https://drinkghia.com)) |
| Good Earth | New Delhi, India | [goodearth.in](https://www.goodearth.in) | Montserrat* | same (+ unnamed/obfuscated face) | — | geometric sans | Julieta Ulanovsky | free/open | CSS census, 24 Oct 2026 ([site](https://www.goodearth.in)) |
| Graza | USA | [graza.co](https://www.graza.co) | — | ITC Garamond Condensed, Apercu (roles not separated) | GT Alpina Typewriter | old-style/Garalde serif · typewriter mono · grotesque | ITC / Monotype · Grilli Type · Colophon | paid | CSS census, 24 Oct 2026 ([site](https://www.graza.co)) |
| Heath Ceramics | Sausalito, USA | [heathceramics.com](https://www.heathceramics.com/) | Benton Sans | Century Schoolbook (+ Grotesque MT Extended) | — | American gothic · transitional serif · extended/wide sans | Font Bureau · Linotype / Monotype · Monotype | paid | CSS census, 24 Oct 2026 ([site](https://www.heathceramics.com/)) |
| Hole & Corner | London, UK | [holeandcorner.com](https://www.holeandcorner.com/) | GT Super | Sabon (+ GT America) | — | Didone/high-contrast serif · old-style/Garalde serif · American gothic | Grilli Type · Linotype (Jan Tschichold) | paid | CSS census, 24 Oct 2026 ([site](https://www.holeandcorner.com/)) |
| Igloo Inc | — | [igloo.inc](https://www.igloo.inc) | — | no web font loaded (system fonts, or type drawn as images) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://www.igloo.inc)) |
| Jacquemus | Paris, France | [jacquemus.com](https://www.jacquemus.com) | Futura* | same | — | geometric sans | Bauer / ParaType (Futura PT) / Linotype | paid | CSS census, 24 Oct 2026 ([site](https://www.jacquemus.com)) |
| Kama Ayurveda | — | [kamaayurveda.com](https://www.kamaayurveda.com) | Bell MT | Barlow (+ Open Sans) | — | transitional serif · DIN/industrial sans · humanist sans | Monotype · Jeremy Tribby · Steve Matteson | paid · free/open | CSS census, 24 Oct 2026 ([site](https://www.kamaayurveda.com)) |
| KARO | New York, USA | [karocrafts.com](https://www.karocrafts.com/) | Helvetica / Helvetica Neue | same | — | neo-grotesk | Linotype / Monotype | paid | CSS census, 24 Oct 2026 ([site](https://www.karocrafts.com/)) |
| Kinfolk | Copenhagen, Denmark | [kinfolk.com](https://www.kinfolk.com) | Kinfolk Serif | Kinfolk Sans | — | contemporary editorial serif · unverified | Schick Toikka (with Alex Hunting Studio) | custom | CSS census, 24 Oct 2026 ([site](https://www.kinfolk.com)) |
| LRNCE | Marrakech, Morocco | [lrnce.com](https://lrnce.com/) | Georgia | Harmonia Sans | — | transitional serif · geometric sans | Microsoft (Matthew Carter) · Monotype (Jim Wasco) | system · paid | CSS census, 24 Oct 2026 ([site](https://lrnce.com/)) |
| mmm.page | — | [mmm.page](https://mmm.page/) | Playfair Display* | Inter* (+ National Park, Lato, Patrick Hand, Calistoga, EB Garamond) | — | Didone/high-contrast serif · neo-grotesk · display/novelty · humanist sans · handwriting · soft/wonky serif · old-style/Garalde serif | Claus Eggers Sørensen · Rasmus Andersson · Andrea Herstowski, Ben Hoepner, Jeremy Shellhorn · Łukasz Dziedzic · Patrick Wagesreiter · Yvonne Schüttler · Georg Duffner / Octavio Pardo | free/open | CSS census, 24 Oct 2026 ([site](https://mmm.page/)) |
| MSCHF | New York, USA | [mschf.com](https://mschf.com) | — | — | MSCHF Sans Mono | grotesk mono | MSCHF (in-house) | custom | CSS census, 24 Oct 2026 ([site](https://mschf.com)) |
| Nicobar | New Delhi, India | [nicobar.com](https://www.nicobar.com) | — | Euclid Flex, NewParis Text (roles not separated) | — | geometric sans · Didone/high-contrast serif | Swiss Typefaces | paid | CSS census, 24 Oct 2026 ([site](https://www.nicobar.com)) |
| Omsom | — | [omsom.com](https://omsom.com) | — | no web font loaded (system fonts, or type drawn as images) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://omsom.com)) |
| Openhouse Magazine | Barcelona, Spain | [openhouse-magazine.com](https://openhouse-magazine.com/) | Sneak | EB Garamond (+ Hind, Montserrat) | — | neo-grotesk · old-style/Garalde serif · humanist sans · geometric sans | TIGHTYPE · Georg Duffner / Octavio Pardo · Indian Type Foundry · Julieta Ulanovsky | paid · free/open | CSS census, 24 Oct 2026 ([site](https://openhouse-magazine.com/)) |
| Paper Boat | Bengaluru, India | [paperboatdrinks.com](https://paperboatdrinks.com/) | Montserrat | Patrick Hand | — | geometric sans · handwriting | Julieta Ulanovsky · Patrick Wagesreiter | free/open | CSS census, 24 Oct 2026 ([site](https://paperboatdrinks.com/)) |
| Paul And Mike | India | [paulandmike.co](https://www.paulandmike.co/) | Montserrat | same | — | geometric sans | Julieta Ulanovsky | free/open | CSS census, 24 Oct 2026 ([site](https://www.paulandmike.co/)) |
| Phool | Kanpur, India | [phool.co](https://phool.co/) | Gotham Rounded | Open Sans | — | rounded sans · humanist sans | Hoefler&Co. · Steve Matteson | paid · free/open | CSS census, 24 Oct 2026 ([site](https://phool.co/)) |
| Ponpon Mania | — | [ponpon-mania.com](https://ponpon-mania.com/) | Franklin (Libre Franklin)* | same | — | American gothic | Impallari Type | free/open | CSS census, 24 Oct 2026 ([site](https://ponpon-mania.com/)) |
| Poolsuite | — | [poolsuite.net](https://poolsuite.net) | — | Everyday (unidentified), Pixolde, ChiKareGo 2, Ishmeria (roles not separated) | — | unverified · pixel/bitmap | unverified · jeti (DaFont) · unknown · Caveras (DaFont) | unverified · free/open · unknown · free-personal | CSS census, 24 Oct 2026 ([site](https://poolsuite.net)) |
| PostHog | — | [posthog.com](https://posthog.com/) | RoundHog | same | Source Code Pro | rounded sans · grotesk mono | PostHog (in-house) · Adobe (Paul D. Hunt) | custom · free/open | CSS census, 24 Oct 2026 ([site](https://posthog.com/)) |
| Present & Correct | London, UK | [presentandcorrect.com](https://www.presentandcorrect.com/) | Inter | same | — | neo-grotesk | Rasmus Andersson | free/open | CSS census, 24 Oct 2026 ([site](https://www.presentandcorrect.com/)) |
| Raw Mango | New Delhi, India | [rawmango.com](https://www.rawmango.com/) | — | Assistant, D-DIN (roles not separated) | — | American gothic · DIN/industrial sans | Ben Nathan (from Source Sans) · Datto | free/open | CSS census, 24 Oct 2026 ([site](https://www.rawmango.com/)) |
| Studio Arhoj | Copenhagen, Denmark | [arhoj.com](https://www.arhoj.com/) | FF DIN* | same | — | DIN/industrial sans | FontFont / Monotype | paid | CSS census, 24 Oct 2026 ([site](https://www.arhoj.com/)) |
| Subko | Mumbai, India | [subko.coffee](https://subko.coffee) | Dashiell Bright | IBM Plex Sans | — | old-style/Garalde serif · neo-grotesk | Signal Type Foundry · IBM / Bold Monday | paid · free/open | CSS census, 24 Oct 2026 ([site](https://subko.coffee)) |
| Teenage Engineering | Stockholm, Sweden | [teenage.engineering](https://teenage.engineering) | — | te-20, TechnoType (roles not separated) | — | unverified | Teenage Engineering (in-house) | custom | CSS census, 24 Oct 2026 ([site](https://teenage.engineering)) |
| The Bombay Canteen | Mumbai, India | [thebombaycanteen.com](https://www.thebombaycanteen.com/) | Murden CF | Soleil | — | unverified · geometric sans | Connary Fagen (probable) · TypeTogether | paid | CSS census, 24 Oct 2026 ([site](https://www.thebombaycanteen.com/)) |
| The Gentlewoman | London, UK | [thegentlewoman.co.uk](https://thegentlewoman.co.uk) | — | no web font loaded (system fonts, or type drawn as images) | — | — | — | — | CSS census, 24 Oct 2026 ([site](https://thegentlewoman.co.uk)) |
| The Whole Truth | Mumbai, India | [thewholetruthfoods.com](https://thewholetruthfoods.com/) | Obviously Narrow | Obviously (+ GoodDog New) | IBM Plex Mono | condensed display sans · grotesque · grotesk mono · handwriting | OH no Type Co. · IBM / Bold Monday · Fonthead Design | paid (Adobe Fonts) · free/open · paid | CSS census, 24 Oct 2026 ([site](https://thewholetruthfoods.com/)) |
| Toast | London, UK | [toa.st](https://www.toa.st/) | Freight | Freight Sans | — | contemporary editorial serif · humanist sans | Darden Studio / GarageFonts | paid (Adobe Fonts) | CSS census, 24 Oct 2026 ([site](https://www.toa.st/)) |

## 5. Frequency tables

*185 studios with at least one identified face loaded (of 195 listed).*

### 5.1 The most-used faces

| Face | Classification | Foundry | Licence | Studios | Share |
|---|---|---|---|---|---|
| Helvetica / Helvetica Neue | neo-grotesk | Linotype / Monotype | paid | 10 | 5.4% |
| Inter | neo-grotesk | Rasmus Andersson | free/open | 8 | 4.3% |
| Suisse Int'l | neo-grotesk | Swiss Typefaces | paid | 7 | 3.8% |
| Neue Montreal | neo-grotesk | Pangram Pangram | free-personal | 7 | 3.8% |
| Neue Haas Grotesk | neo-grotesk | Font Bureau / Monotype (C. Schwartz) | paid | 6 | 3.2% |
| Editorial New | Didone/high-contrast serif | Pangram Pangram | free-personal | 6 | 3.2% |
| Poppins | geometric sans | Indian Type Foundry | free/open | 5 | 2.7% |
| ABC Monument Grotesk | grotesque | Dinamo | paid | 3 | 1.6% |
| Futura | geometric sans | Bauer / ParaType (Futura PT) / Linotype | paid | 3 | 1.6% |
| Helvetica Now | neo-grotesk | Monotype | paid | 3 | 1.6% |
| ABC Diatype | neo-grotesk | Dinamo | paid | 3 | 1.6% |
| Archivo | grotesque | Omnibus-Type | free/open | 3 | 1.6% |
| Open Sans | humanist sans | Steve Matteson | free/open | 3 | 1.6% |
| Graphik | neo-grotesk | Commercial Type | paid | 2 | 1.1% |
| Akkurat | neo-grotesk | Lineto | paid | 2 | 1.1% |
| DIN 2014 | DIN/industrial sans | ParaType | paid | 2 | 1.1% |
| Unica77 | neo-grotesk | Lineto | paid | 2 | 1.1% |
| Aeonik | neo-grotesk | CoType Foundry | paid | 2 | 1.1% |
| Lausanne | neo-grotesk | Weltkern (TWK) | paid | 2 | 1.1% |
| Mabry | grotesque | Colophon | paid | 2 | 1.1% |
| PP Mori | neo-grotesk | Pangram Pangram | free-personal | 2 | 1.1% |
| Untitled Sans | neo-grotesk | Klim | paid | 2 | 1.1% |
| DM Serif | Didone/high-contrast serif | Colophon (for Google) | free/open | 2 | 1.1% |
| Times New Roman / Times Seven | transitional serif | Monotype | paid | 2 | 1.1% |
| Akzidenz-Grotesk | grotesque | Berthold | paid | 2 | 1.1% |
| GT America | American gothic | Grilli Type | paid | 2 | 1.1% |
| Aktiv Grotesk | neo-grotesk | Dalton Maag | paid (Adobe Fonts) | 2 | 1.1% |
| Satoshi | geometric sans | Indian Type Foundry (Fontshare) | free-commercial | 2 | 1.1% |
| Season Mix | contemporary editorial serif | Displaay Type Foundry | paid | 2 | 1.1% |
| ABC Monument Grotesk Mono | grotesk mono | Dinamo | paid | 2 | 1.1% |

### 5.2 Families of faces and foundries

| Group | Studios using at least one | Share |
|---|---|---|
| Helvetica lineage | 24 | 13% |
| Pangram Pangram faces | 17 | 9% |
| Dinamo (ABC) faces | 15 | 8% |
| Klim faces | 12 | 6% |
| Indian Type Foundry (incl. Fontshare) | 9 | 5% |
| Swiss Typefaces faces | 8 | 4% |
| Colophon faces | 8 | 4% |
| Grilli Type faces | 6 | 3% |
| Optimo faces | 6 | 3% |
| Commercial Type faces | 5 | 3% |
| Lineto faces | 4 | 2% |

### 5.3 Most-used faces by studio type

| Type | Studios | Most-used faces (studios) |
|---|---|---|
| Global agencies | 30 | Neue Haas Grotesk (2), Plain (1), Portrait (1), Graphik (1), Aeonik Fono (1), Iskry (1), SF Pro (1), Basis Grotesque (1) |
| Independent studios | 58 | Helvetica / Helvetica Neue (3), Neue Haas Grotesk (2), Futura (2), Suisse Int'l (2), Neue Montreal (2), Romie (1), Unica77 (1), Dada Grotesk (1) |
| Indian studios | 26 | Inter (4), Helvetica / Helvetica Neue (4), Open Sans (3), Poppins (3), Wix Madefor (2), Archivo (2), Apfel Grotezk (1), Cabinet Grotesk (1) |
| Digital / motion | 33 | Suisse Int'l (3), Helvetica Now (2), Helvetica / Helvetica Neue (2), Neue Montreal (2), Editorial New (1), Aeonik (1), IBM Plex Mono (1), LusionMono (1) |
| Designers, founder-led | 38 | Editorial New (3), Neue Montreal (3), Inter (2), Bebas Neue (2), Roboto (2), Hubano Rough (1), Sydonia Atramentiqua (1), Helvetica / Helvetica Neue (1) |

### 5.4 Classes by studio type (share of studios using at least one face of the class)

| Type | Studios | Any sans | Any serif | Any mono | Any script / hand | Any display / pixel | Sans only (+ mono) | Serif + sans |
|---|---|---|---|---|---|---|---|---|
| Global agencies | 30 | 26 (87%) | 9 (30%) | 5 (17%) | 0 (0%) | 1 (3%) | 18 (60%) | 7 (23%) |
| Independent studios | 58 | 49 (84%) | 19 (33%) | 5 (9%) | 0 (0%) | 2 (3%) | 35 (60%) | 13 (22%) |
| Indian studios | 26 | 24 (92%) | 9 (35%) | 3 (12%) | 0 (0%) | 2 (8%) | 16 (62%) | 7 (27%) |
| Digital / motion | 33 | 26 (79%) | 7 (21%) | 7 (21%) | 0 (0%) | 1 (3%) | 19 (58%) | 6 (18%) |
| Designers, founder-led | 38 | 29 (76%) | 11 (29%) | 6 (16%) | 3 (8%) | 3 (8%) | 20 (53%) | 7 (18%) |
| **All** | 185 | 154 (83%) | 55 (30%) | 26 (14%) | 3 (2%) | 9 (5%) | 108 (58%) | 40 (22%) |

### 5.5 Sub-classes (share of all studios using at least one)

| Classification | Studios | Share |
|---|---|---|
| neo-grotesk | 86 | 46% |
| grotesque | 39 | 21% |
| geometric sans | 31 | 17% |
| grotesk mono | 22 | 12% |
| contemporary editorial serif | 18 | 10% |
| Didone/high-contrast serif | 11 | 6% |
| old-style/Garalde serif | 11 | 6% |
| condensed display sans | 10 | 5% |
| transitional serif | 8 | 4% |
| humanist sans | 8 | 4% |
| display/novelty | 6 | 3% |
| American gothic | 5 | 3% |
| slab/Clarendon serif | 4 | 2% |
| typewriter mono | 4 | 2% |
| DIN/industrial sans | 3 | 2% |
| pixel/bitmap | 3 | 2% |
| rounded sans | 3 | 2% |
| soft/wonky serif | 3 | 2% |
| extended/wide sans | 3 | 2% |
| handwriting | 2 | 1% |
| custom | 2 | 1% |
| script | 1 | 1% |

### 5.6 The display face, where the role is known (105 studios)

| Display classification | Studios | Share |
|---|---|---|
| neo-grotesk | 32 | 30% |
| grotesque | 18 | 17% |
| geometric sans | 10 | 10% |
| contemporary editorial serif | 7 | 7% |
| transitional serif | 6 | 6% |
| Didone/high-contrast serif | 5 | 5% |
| old-style/Garalde serif | 4 | 4% |
| condensed display sans | 4 | 4% |
| slab/Clarendon serif | 3 | 3% |
| grotesk mono | 2 | 2% |
| display/novelty | 2 | 2% |
| unverified | 2 | 2% |
| American gothic | 2 | 2% |
| extended/wide sans | 2 | 2% |
| humanist sans | 2 | 2% |
| soft/wonky serif | 1 | 1% |
| rounded sans | 1 | 1% |
| DIN/industrial sans | 1 | 1% |
| custom | 1 | 1% |

### 5.7 Licences

| Type | Studios | Any paid face | Any Adobe Fonts face | Any free-for-personal-use face (licence bought) | Any custom face | Only free faces |
|---|---|---|---|---|---|---|
| Global agencies | 30 | 22 (73%) | 0 (0%) | 1 (3%) | 5 (17%) | 3 (10%) |
| Independent studios | 58 | 49 (84%) | 2 (3%) | 4 (7%) | 4 (7%) | 2 (3%) |
| Indian studios | 26 | 17 (65%) | 3 (12%) | 1 (4%) | 0 (0%) | 8 (31%) |
| Digital / motion | 33 | 23 (70%) | 0 (0%) | 5 (15%) | 4 (12%) | 0 (0%) |
| Designers, founder-led | 38 | 23 (61%) | 0 (0%) | 6 (16%) | 0 (0%) | 10 (26%) |
| **All** | 185 | 134 (72%) | 5 (3%) | 17 (9%) | 13 (7%) | 23 (12%) |

### 5.8 How many families a studio site loads

| Type | Studios | 1 family | 2 | 3 | 4 or more |
|---|---|---|---|---|---|
| Global agencies | 30 | 13 (43%) | 14 (47%) | 3 (10%) | 0 (0%) |
| Independent studios | 58 | 32 (55%) | 14 (24%) | 9 (16%) | 3 (5%) |
| Indian studios | 26 | 6 (23%) | 15 (58%) | 1 (4%) | 4 (15%) |
| Digital / motion | 33 | 12 (36%) | 15 (45%) | 6 (18%) | 0 (0%) |
| Designers, founder-led | 38 | 20 (53%) | 9 (24%) | 6 (16%) | 3 (8%) |
| **All** | 185 | 83 (45%) | 67 (36%) | 25 (14%) | 10 (5%) |

### 5.9 Where the AI-default faces turn up

| Face | Studios | Which | By type |
|---|---|---|---|
| Inter | 8 | Pearlfisher, Paco Coursey, Happy Happy Creative, Beyondesign, The Turtle Story, Confetti Design, Loli Laboureau, Zensciences | Indian studios 4, Designers, founder-led 2, Global agencies 1, Independent studios 1 |
| Inter Display | 1 | hi, 6 — Scrapbook (Hicard Studio) | Designers, founder-led 1 |
| Geist | 1 | Basement Studio | Digital / motion 1 |
| Poppins | 5 | Mucca, designmill, The Turtle Story, Confetti Design, Grit Pictures | Indian studios 3, Independent studios 1, Designers, founder-led 1 |
| Montserrat | 2 | Studio Sorted, Aralesk — Collages & Motion | Indian studios 1, Designers, founder-led 1 |
| DM Sans | 1 | Robot Food | Independent studios 1 |
| Manrope | 1 | Fiddle.Digital | Digital / motion 1 |
| Plus Jakarta Sans | 2 | Beyondesign, Mr. Panda's Paper Portfolio | Indian studios 1, Designers, founder-led 1 |
| Satoshi | 2 | Beth-Emily, Studio Sorted | Independent studios 1, Indian studios 1 |
| Clash Grotesk | 1 | Agence Foudre | Independent studios 1 |
| Cabinet Grotesk | 1 | Studio Sorted | Indian studios 1 |
| Syne | 1 | Elephant Design | Indian studios 1 |
| DM Serif | 2 | Robot Food, Confetti Design | Independent studios 1, Indian studios 1 |
| Instrument Serif | 1 | Instrument | Global agencies 1 |
| Instrument Sans | 1 | Instrument | Global agencies 1 |
| Lora | 1 | Animal | Indian studios 1 |
| Newsreader | 1 | Paco Coursey | Designers, founder-led 1 |
| IBM Plex Mono | 1 | Lusion | Digital / motion 1 |
| Space Mono | 1 | Studio Bigfat | Indian studios 1 |
| DM Mono | 1 | Robot Food | Independent studios 1 |

At least one of these faces: 25 (14%) of studios; by type: Global agencies 2 (7%); Independent studios 5 (9%); Indian studios 9 (35%); Digital / motion 3 (9%); Designers, founder-led 6 (16%).

## 6. Face index

Every identified face in §3 and §4, with how many studios in §3–4 load it. Foundry pages are the source for classification and licence; "probable" and "unverified" are marked.

| Face | Classification | Foundry | Licence | Studios in this list | Source |
|---|---|---|---|---|---|
| Helvetica / Helvetica Neue | neo-grotesk | Linotype / Monotype | paid | 11 | [monotype.com](https://www.monotype.com/fonts/helvetica) |
| Inter | neo-grotesk | Rasmus Andersson | free/open | 10 | [rsms.me](https://rsms.me/inter/) |
| Suisse Int'l | neo-grotesk | Swiss Typefaces | paid | 8 | [swisstypefaces.com](https://www.swisstypefaces.com/fonts/suisse/) |
| Neue Montreal | neo-grotesk | Pangram Pangram | free-personal | 7 | [pangrampangram.com](https://pangrampangram.com/products/neue-montreal) |
| Editorial New | Didone/high-contrast serif | Pangram Pangram | free-personal | 6 | [pangrampangram.com](https://pangrampangram.com/products/editorial-new) |
| Futura | geometric sans | Bauer / ParaType (Futura PT) / Linotype | paid | 6 | [paratype.com](https://www.paratype.com/fonts/pt/futura-pt) |
| Montserrat | geometric sans | Julieta Ulanovsky | free/open | 6 | [fonts.google.com](https://fonts.google.com/specimen/Montserrat) |
| Neue Haas Grotesk | neo-grotesk | Font Bureau / Monotype (C. Schwartz) | paid | 6 | [monotype.com](https://www.monotype.com/fonts/neue-haas-grotesk) |
| Open Sans | humanist sans | Steve Matteson | free/open | 5 | [fonts.google.com](https://fonts.google.com/specimen/Open+Sans) |
| Poppins | geometric sans | Indian Type Foundry | free/open | 5 | [fonts.google.com](https://fonts.google.com/specimen/Poppins) |
| ABC Diatype | neo-grotesk | Dinamo | paid | 3 | [abcdinamo.com](https://abcdinamo.com/typefaces/diatype) |
| ABC Monument Grotesk | grotesque | Dinamo | paid | 3 | [abcdinamo.com](https://abcdinamo.com/typefaces/monument-grotesk) |
| Archivo | grotesque | Omnibus-Type | free/open | 3 | [fonts.google.com](https://fonts.google.com/specimen/Archivo) |
| EB Garamond | old-style/Garalde serif | Georg Duffner / Octavio Pardo | free/open | 3 | [fonts.google.com](https://fonts.google.com/specimen/EB+Garamond) |
| GT America | American gothic | Grilli Type | paid | 3 | [grillitype.com](https://www.grillitype.com/typeface/gt-america) |
| Helvetica Now | neo-grotesk | Monotype | paid | 3 | [monotype.com](https://www.monotype.com/fonts/helvetica-now) |
| ABC Areal | neo-grotesk | Dinamo | custom | 2 | [are.na](https://www.are.na/editorial/introducing-areal-are-nas-new-typeface) |
| ABC Favorit | grotesque | Dinamo | paid | 2 | [abcdinamo.com](https://abcdinamo.com/typefaces/favorit) |
| ABC Monument Grotesk Mono | grotesk mono | Dinamo | paid | 2 | [abcdinamo.com](https://abcdinamo.com/typefaces/monument-grotesk) |
| ABC Oracle | grotesque | Dinamo | paid | 2 | [abcdinamo.com](https://abcdinamo.com/typefaces/oracle) |
| Aeonik | neo-grotesk | CoType Foundry | paid | 2 | [cotypefoundry.com](https://cotypefoundry.com/our-fonts/aeonik/) |
| Akkurat | neo-grotesk | Lineto | paid | 2 | [lineto.com](https://lineto.com/typefaces/akkurat) |
| Aktiv Grotesk | neo-grotesk | Dalton Maag | paid (Adobe Fonts) | 2 | [daltonmaag.com](https://www.daltonmaag.com/font-library/aktiv-grotesk.html) |
| Akzidenz-Grotesk | grotesque | Berthold | paid | 2 | [bertholdtypes.com](https://bertholdtypes.com) |
| Apercu | grotesque | Colophon | paid | 2 | [colophon-foundry.org](https://www.colophon-foundry.org/typefaces/apercu) |
| Assistant | American gothic | Ben Nathan (from Source Sans) | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/Assistant) |
| Bebas Neue | condensed display sans | Ryoichi Tsunekawa (Dharma Type) | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/Bebas+Neue) |
| Benton Sans | American gothic | Font Bureau | paid | 2 | [fontbureau.typenetwork.com](https://fontbureau.typenetwork.com/typefaces/benton-sans) |
| Century Schoolbook | transitional serif | Linotype / Monotype | paid | 2 | [monotype.com](https://www.monotype.com) |
| DIN 2014 | DIN/industrial sans | ParaType | paid | 2 | [paratype.com](https://www.paratype.com/fonts/pt/din-2014) |
| DM Serif | Didone/high-contrast serif | Colophon (for Google) | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/DM+Serif+Display) |
| Founders Grotesk | grotesque | Klim | paid | 2 | [klim.co.nz](https://klim.co.nz/retail-fonts/founders-grotesk/) |
| Franklin (Libre Franklin) | American gothic | Impallari Type | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/Libre+Franklin) |
| Graphik | neo-grotesk | Commercial Type | paid | 2 | [commercialtype.com](https://commercialtype.com/catalog/graphik) |
| IBM Plex Mono | grotesk mono | IBM / Bold Monday | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/IBM+Plex+Mono) |
| Jost | geometric sans | Owen Earl | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/Jost) |
| Lausanne | neo-grotesk | Weltkern (TWK) | paid | 2 | [weltkern.com](https://weltkern.com/typefaces/lausanne) |
| Mabry | grotesque | Colophon | paid | 2 | [colophon-foundry.org](https://www.colophon-foundry.org/typefaces/mabry) |
| Neue Haas Unica | neo-grotesk | Monotype (Toshi Omagari) | paid | 2 | [monotype.com](https://www.monotype.com/fonts/neue-haas-unica) |
| Obviously Narrow | condensed display sans | OH no Type Co. | paid (Adobe Fonts) | 2 | [ohnotype.co](https://ohnotype.co/fonts/obviously) |
| Patrick Hand | handwriting | Patrick Wagesreiter | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/Patrick+Hand) |
| Plus Jakarta Sans | geometric sans | Tokotype | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/Plus+Jakarta+Sans) |
| PP Mori | neo-grotesk | Pangram Pangram | free-personal | 2 | [pangrampangram.com](https://pangrampangram.com/products/mori) |
| Recoleta | soft/wonky serif | Latinotype | paid | 2 | [latinotype.com](https://latinotype.com/font/recoleta/) |
| Roboto | neo-grotesk | Google (Christian Robertson) | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/Roboto) |
| Roobert | geometric sans | Displaay | paid | 2 | [displaay.net](https://displaay.net/typeface/roobert) |
| Satoshi | geometric sans | Indian Type Foundry (Fontshare) | free-commercial | 2 | [fontshare.com](https://www.fontshare.com/fonts/satoshi) |
| Season Mix | contemporary editorial serif | Displaay Type Foundry | paid | 2 | [displaay.net](https://displaay.net/typeface/season/) |
| Tiempos | contemporary editorial serif | Klim | paid | 2 | [klim.co.nz](https://klim.co.nz/retail-fonts/tiempos-text/) |
| Times New Roman / Times Seven | transitional serif | Monotype | paid | 2 | [monotype.com](https://www.monotype.com/fonts/times-new-roman) |
| Unica77 | neo-grotesk | Lineto | paid | 2 | [lineto.com](https://lineto.com/typefaces/unica77) |
| Untitled Sans | neo-grotesk | Klim | paid | 2 | [klim.co.nz](https://klim.co.nz/retail-fonts/untitled-sans/) |
| Wix Madefor | neo-grotesk | Dalton Maag for Wix | free/open | 2 | [fonts.google.com](https://fonts.google.com/specimen/Wix+Madefor+Text) |
| ABC Arizona | contemporary editorial serif | Dinamo | paid | 1 | [abcdinamo.com](https://abcdinamo.com/typefaces/arizona) |
| ABC Diatype Expanded | extended/wide sans | Dinamo | paid | 1 | [abcdinamo.com](https://abcdinamo.com/typefaces/diatype) |
| ABC Otto | soft/wonky serif | Dinamo | paid | 1 | [abcdinamo.com](https://abcdinamo.com/typefaces/otto) |
| ABC Repro | grotesque | Dinamo | paid | 1 | [abcdinamo.com](https://abcdinamo.com/typefaces/repro) |
| ABC Rom Mono | grotesk mono | Dinamo | paid | 1 | [abcdinamo.com](https://abcdinamo.com/typefaces/rom) |
| ABC Schengen | neo-grotesk | Dinamo | paid | 1 | [abcdinamo.com](https://abcdinamo.com/typefaces/schengen) |
| ABC Simon Mono | grotesk mono | Dinamo | paid | 1 | [abcdinamo.com](https://abcdinamo.com/typefaces/simon) |
| ABC Walter Neue | humanist sans | Dinamo | paid | 1 | [abcdinamo.com](https://abcdinamo.com/newsletter/release-walter-alte-walter-neue) |
| Acumin | neo-grotesk | Adobe (Robert Slimbach) | paid (Adobe Fonts) | 1 | [fonts.adobe.com](https://fonts.adobe.com/fonts/acumin) |
| Adobe Caslon | old-style/Garalde serif | Adobe (Carol Twombly) | paid (Adobe Fonts) | 1 | [fonts.adobe.com](https://fonts.adobe.com/fonts/adobe-caslon) |
| Advercase | old-style/Garalde serif | Indieground | paid | 1 | [youworkforthem.com](https://www.youworkforthem.com/font/T25140/advercase) |
| Aeonik Fono | grotesk mono | CoType Foundry | paid | 1 | [cotypefoundry.com](https://cotypefoundry.com/our-fonts/aeonik-fono/) |
| Aften Screen | humanist sans | Monokrom | paid | 1 | [luc.devroye.org](https://luc.devroye.org/fonts-63805.html) |
| Aktiv Grotesk Extended | extended/wide sans | Dalton Maag | paid (Adobe Fonts) | 1 | [daltonmaag.com](https://www.daltonmaag.com/font-library/aktiv-grotesk.html) |
| Albert Sans | geometric sans | Andreas Rasmussen | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Albert+Sans) |
| Alliance | grotesque | Degarism Studio (probable) | paid | 1 | [myfonts.com](https://www.myfonts.com/fonts/degarism-studio/alliance) |
| Alliance Platt | unverified | Degarism Studio (presumed) (unverified) | paid | 1 | [myfonts.com](https://www.myfonts.com/fonts/degarism-studio/alliance) |
| Almarai | geometric sans | Boutros | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Almarai) |
| Amatic SC | handwriting | Vernon Adams | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Amatic+SC) |
| Anton | condensed display sans | Vernon Adams | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Anton) |
| Apfel Grotezk | grotesque | Collletttivo | free/open | 1 | [collletttivo.it](https://www.collletttivo.it) |
| Argent Pixel CF | pixel/bitmap | Connary Fagen | paid | 1 | [connary.com](https://www.connary.com/argentpixel.html) |
| Arial | neo-grotesk | Monotype (system font) | system | 1 | — |
| Avenir | geometric sans | Linotype (Adrian Frutiger) | paid | 1 | [monotype.com](https://www.monotype.com/fonts/avenir) |
| Azeret Mono | grotesk mono | Displaay (Martin Vácha) | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Azeret+Mono) |
| Ballinger Mono | grotesk mono | Signal Type Foundry | paid | 1 | [myfonts.com](https://myfonts.com/fonts/signal/ballinger-mono) |
| Banana Grotesk | grotesque | Monkey Type | paid | 1 | [typewolf.com](https://www.typewolf.com/banana-grotesk) |
| Bandit | unverified | AllCaps (probable) | paid | 1 | [maxibestof.one](https://maxibestof.one/typefaces/bandit) |
| Barlow | DIN/industrial sans | Jeremy Tribby | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Barlow) |
| Basetica | neo-grotesk | Base Design (in-house, predecessor of Muoto) (probable) | custom | 1 | — |
| Basis Grotesque | grotesque | Colophon | paid | 1 | [colophon-foundry.org](https://www.colophon-foundry.org/typefaces/basis-grotesque) |
| Basis Grotesque Mono | grotesk mono | Colophon | paid | 1 | [colophon-foundry.org](https://www.colophon-foundry.org/typefaces/basis-grotesque) |
| Baskerville (display) | transitional serif | unverified | paid | 1 | — |
| BB Grotesk | grotesque | Bureau Borsche (in-house) (probable) | custom | 1 | — |
| Beatrice Display | neo-grotesk | Sharp Type | paid | 1 | [typewolf.com](https://www.typewolf.com/beatrice) |
| Bell MT | transitional serif | Monotype | paid | 1 | [monotype.com](https://www.monotype.com) |
| Beni | condensed display sans | Nois | paid | 1 | [myfonts.com](https://myfonts.com/fonts/nois/beni) |
| Big Caslon | old-style/Garalde serif | Font Bureau (Matthew Carter) | paid | 1 | [fontbureau.typenetwork.com](https://fontbureau.typenetwork.com) |
| Biotif | geometric sans | Degarism Studio | paid | 1 | [fontspring.com](https://fontspring.com/fonts/degarism-studio/biotif) |
| Boogy Brut Poster | contemporary editorial serif | Bureau Brut | paid | 1 | [typewolf.com](https://www.typewolf.com/boogy-brut) |
| Brandon Grotesque | geometric sans | HVD Fonts | paid | 1 | [hvdfonts.com](https://www.hvdfonts.com/fonts/brandon-grotesque) |
| Cabin | humanist sans | Impallari Type | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Cabin) |
| Cabinet Grotesk | grotesque | Indian Type Foundry (Fontshare) | free-commercial | 1 | [fontshare.com](https://www.fontshare.com/fonts/cabinet-grotesk) |
| Calistoga | soft/wonky serif | Yvonne Schüttler | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Calistoga) |
| Cambon | contemporary editorial serif | General Type Studio (Stéphane Elbaz) | paid | 1 | [typewolf.com](https://typewolf.com/cambon) |
| Canopée | condensed display sans | VJ-Type | paid | 1 | [typewolf.com](https://www.typewolf.com/canopee) |
| Caslon Doric | grotesque | Commercial Type | paid | 1 | [commercialtype.com](https://commercialtype.com/catalog/caslon_doric) |
| Cheltenham | old-style/Garalde serif | ITC / Monotype | paid | 1 | [monotype.com](https://www.monotype.com) |
| ChiKareGo 2 | pixel/bitmap | unknown (unverified) | unknown | 1 | [en.wikipedia.org](https://en.wikipedia.org/wiki/Chicago_(typeface)) |
| Circular | geometric sans | Lineto | paid | 1 | [lineto.com](https://lineto.com/typefaces/circular) |
| Clarendon | slab/Clarendon serif | Bitstream / Monotype | paid | 1 | [monotype.com](https://www.monotype.com) |
| Clash Grotesk | grotesque | Indian Type Foundry (Fontshare) | free-commercial | 1 | [fontshare.com](https://www.fontshare.com/fonts/clash-grotesk) |
| Contax | geometric sans | Type Innovations (probable) | paid | 1 | [typewolf.com](https://www.typewolf.com/contax-sans) |
| Cooper | soft/wonky serif | after Oswald Cooper (several digitisations) | paid | 1 | — |
| Cormorant | old-style/Garalde serif | Christian Thalmann | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Cormorant) |
| Courier | typewriter mono | system font | system | 1 | — |
| Custom family (unnamed) | custom | the studio (name not published) (identity-only) | custom | 1 | — |
| Cutive Mono | typewriter mono | Vernon Adams | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Cutive+Mono) |
| D-DIN | DIN/industrial sans | Datto | free/open | 1 | [fontsquirrel.com](https://www.fontsquirrel.com/fonts/d-din) |
| Dada Grotesk | grotesque | Optimo | paid | 1 | [typewolf.com](https://www.typewolf.com/dada-grotesk) |
| Dashiell Bright | old-style/Garalde serif | Signal Type Foundry | paid | 1 | [slanted.de](https://www.slanted.de/?p=621926) |
| Deckard | unverified | unknown (Bobby Tannam) (probable) | unknown | 1 | [maxibestof.nuxt.dev](https://maxibestof.nuxt.dev/typefaces/deckard) |
| Degular Mono | grotesk mono | OH no Type Co. | paid (Adobe Fonts) | 1 | [ohnotype.co](https://ohnotype.co/fonts/degular) |
| Dejanire Text | transitional serif | Retype | paid | 1 | [re-type.com](https://www.re-type.com/fonts/dejanire/) |
| Delegate | American gothic | Commercial Type | paid | 1 | [commercialtype.com](https://commercialtype.com/catalog/delegate) |
| Delegate Mono | grotesk mono | Commercial Type | paid | 1 | [commercialtype.com](https://commercialtype.com/catalog/delegate) |
| Dennis Sans | unverified | unknown (unverified) | unknown | 1 | [dennissnellenberg.com](https://dennissnellenberg.com/) |
| Die Grotesk | neo-grotesk | Klim Type Foundry | paid | 1 | [klim.co.nz](https://klim.co.nz/fonts/die-grotesk/) |
| DM Mono | grotesk mono | Colophon (for Google) | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/DM+Mono) |
| DM Sans | geometric sans | Colophon (for Google) | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/DM+Sans) |
| Domaine Display | Didone/high-contrast serif | Klim | paid | 1 | [klim.co.nz](https://klim.co.nz/retail-fonts/domaine-display/) |
| Eidetic Neo | contemporary editorial serif | Emigre | paid | 1 | [emigre.com](https://www.emigre.com/EF.php?fid=91) |
| Epicene | transitional serif | Klim | paid | 1 | [klim.co.nz](https://klim.co.nz/retail-fonts/epicene-text/) |
| Euclid Flex | geometric sans | Swiss Typefaces | paid | 1 | [swisstypefaces.com](https://www.swisstypefaces.com/fonts/euclid/) |
| Exo 2 | geometric sans | Natanael Gama | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Exo+2) |
| F37 Snaskface | display/novelty | F37 Foundry x Snask | paid | 1 | [f37.com](https://f37.com/f37x/f37-snaskface) |
| Felt Tip Roman | handwriting | Mark Simonson Studio | paid | 1 | [marksimonson.com](https://www.marksimonson.com/fonts/view/felt-tip-roman) |
| FF DIN | DIN/industrial sans | FontFont / Monotype | paid | 1 | [monotype.com](https://www.monotype.com) |
| FF More | unverified | unverified | unverified | 1 | — |
| FF Tundra Light | contemporary editorial serif | FontFont (Monotype) (probable) | paid | 1 | [myfonts.com](https://myfonts.com/collections/ff-tundra-font-fontfont) |
| FFF Tool Sans | unverified | Folch | paid | 1 | [tool.folchstudio.com](https://tool.folchstudio.com/) |
| FFF Tool Serif | unverified | Folch | paid | 1 | [tool.folchstudio.com](https://tool.folchstudio.com/) |
| FFFLAUTA | pixel/bitmap | Basement Foundry (basement.studio) | paid | 1 | [foundry.basement.studio](https://foundry.basement.studio/fonts/ffflauta) |
| FHA Condensed French NC | slab/Clarendon serif | Fontry West | free-personal | 1 | [fontspace.com](https://www.fontspace.com/fha-condensed-french-font-f15426) |
| Figtree | geometric sans | Erik Kennedy | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Figtree) |
| Fira Sans | humanist sans | Carrois / Mozilla | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Fira+Sans) |
| Fontdiner Swanky | display/novelty | Font Diner | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Fontdiner+Swanky) |
| Fort | DIN/industrial sans | MCKL | paid | 1 | [typewolf.com](https://www.typewolf.com/fort) |
| Founders Grotesk Mono | grotesk mono | Klim | paid | 1 | [klim.co.nz](https://klim.co.nz/retail-fonts/founders-grotesk-mono/) |
| Founders Grotesk X-Condensed | condensed display sans | Klim | paid | 1 | [klim.co.nz](https://klim.co.nz/retail-fonts/founders-grotesk-x-condensed/) |
| Fragment Mono | grotesk mono | Wei Huang / URW | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Fragment+Mono) |
| Fraunces | soft/wonky serif | Undercase Type | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Fraunces) |
| Freight | contemporary editorial serif | Darden Studio / GarageFonts | paid (Adobe Fonts) | 1 | [fonts.adobe.com](https://fonts.adobe.com/fonts/freight-text) |
| Freight Sans | humanist sans | Darden Studio / GarageFonts | paid (Adobe Fonts) | 1 | [fonts.adobe.com](https://fonts.adobe.com/fonts/freight-sans) |
| Friedel | neo-grotesk | APFEL (A Practice for Everyday Life) | paid | 1 | [apracticeforeverydaylife.com](https://apracticeforeverydaylife.com/typefaces/friedel) |
| Fustat | humanist sans | Mohamed Gaber et al. | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Fustat) |
| Galano Classic | geometric sans | René Bieder | paid | 1 | [renebieder.com](https://www.renebieder.com) |
| Galaxie Copernicus | old-style/Garalde serif | Village (probable) | paid | 1 | [fontreviewjournal.com](https://fontreviewjournal.com/galaxie-copernicus/) |
| Garnett | grotesque | Sharp Type | paid | 1 | [typewolf.com](https://www.typewolf.com/garnett) |
| Geist | neo-grotesk | Vercel / Basement Studio | free/open | 1 | [vercel.com](https://vercel.com/font) |
| Geist Mono | grotesk mono | Vercel / Basement Studio | free/open | 1 | [vercel.com](https://vercel.com/font) |
| Gellix | geometric sans | Displaay (Martin Vácha) | paid | 1 | [typewolf.com](https://typewolf.com/gellix) |
| Georgia | transitional serif | Microsoft (Matthew Carter) | system | 1 | [learn.microsoft.com](https://learn.microsoft.com/typography/font-list/georgia) |
| Gilroy | geometric sans | Radomir Tinkov | paid | 1 | [tinkov.info](https://www.tinkov.info/gilroy.html) |
| Goga | geometric sans | Narrow Type | paid | 1 | [myfonts.com](https://myfonts.com/collections/goga-font-narrow-type) |
| GoodDog New | handwriting | Fonthead Design | paid | 1 | [myfonts.com](https://www.myfonts.com/fonts/fonthead/good-dog-new) |
| Gotham | geometric sans | Hoefler&Co. | paid | 1 | [typography.com](https://www.typography.com/fonts/gotham) |
| Gotham Rounded | rounded sans | Hoefler&Co. | paid | 1 | [typography.com](https://www.typography.com/fonts/gotham-rounded) |
| Great Vibes | script | TypeSETit (Robert Leuschke) | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Great+Vibes) |
| Greed | neo-grotesk | Displaay Type Foundry | paid | 1 | [typewolf.com](https://www.typewolf.com/greed) |
| Grotesque MT Extended | extended/wide sans | Monotype | paid | 1 | [monotype.com](https://www.monotype.com) |
| GT Alpina Typewriter | typewriter mono | Grilli Type | paid | 1 | [grillitype.com](https://www.grillitype.com/typeface/gt-alpina) |
| GT America Mono | grotesk mono | Grilli Type | paid | 1 | [grillitype.com](https://www.grillitype.com/typeface/gt-america) |
| GT Flexa | grotesque | Grilli Type | paid | 1 | [grillitype.com](https://www.grillitype.com/typeface/gt-flexa) |
| GT Kotoheim | geometric sans | Grilli Type (derivative of GT Walsheim, inferred) (probable) | custom | 1 | [maxibestof.one](https://maxibestof.one/typefaces/gt-kotoheim) |
| GT Kotoheim Condensed | condensed display sans | Grilli Type (inferred) (probable) | custom | 1 | [maxibestof.one](https://maxibestof.one/typefaces/gt-kotoheim) |
| GT Kotoheim Mono | grotesk mono | Grilli Type (inferred) (probable) | custom | 1 | [maxibestof.one](https://maxibestof.one/typefaces/gt-kotoheim-mono) |
| GT Pressura Mono | grotesk mono | Grilli Type | paid | 1 | [grillitype.com](https://www.grillitype.com/typeface/gt-pressura) |
| GT Sectra | contemporary editorial serif | Grilli Type | paid | 1 | [grillitype.com](https://www.grillitype.com/typeface/gt-sectra) |
| GT Standard | neo-grotesk | Grilli Type | paid | 1 | [grillitype.com](https://www.grillitype.com/typeface/gt-standard) |
| GT Super | Didone/high-contrast serif | Grilli Type | paid | 1 | [grillitype.com](https://www.grillitype.com/typeface/gt-super) |
| Hanken Grotesk | neo-grotesk | Hanken Design Co. | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Hanken+Grotesk) |
| Harmonia Sans | geometric sans | Monotype (Jim Wasco) | paid | 1 | [monotype.com](https://www.monotype.com) |
| Heebo | neo-grotesk | Oded Ezer | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Heebo) |
| Hind | humanist sans | Indian Type Foundry | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Hind) |
| Holyriver | display/novelty | Sancrea (probable) | paid | 1 | [creativemarket.com](https://creativemarket.com/sancreastd./5458008-Holyriver-Typeface) |
| Hubano Rough | display/novelty | SimpleBits | paid | 1 | [fontspring.com](https://fontspring.com/fonts/simplebits/hubano) |
| IBM Plex Sans | neo-grotesk | IBM / Bold Monday | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/IBM+Plex+Sans) |
| Instrument Sans | neo-grotesk | Instrument | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Instrument+Sans) |
| Instrument Serif | Didone/high-contrast serif | Instrument | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Instrument+Serif) |
| Inter Display | neo-grotesk | Rasmus Andersson | free/open | 1 | [rsms.me](https://rsms.me/inter/) |
| Ishmeria | pixel/bitmap | Caveras (DaFont) | free-personal | 1 | [dafont.com](https://www.dafont.com/ishmeria.font) |
| Iskry | contemporary editorial serif | Laïc | paid | 1 | [luc.devroye.org](https://luc.devroye.org/fonts-89065.html) |
| ITC Avant Garde Gothic | geometric sans | ITC / Monotype | paid | 1 | [monotype.com](https://www.monotype.com) |
| ITC Garamond Condensed | old-style/Garalde serif | ITC / Monotype | paid | 1 | [monotype.com](https://www.monotype.com) |
| Items Light | contemporary editorial serif | Schick Toikka (probable) | paid | 1 | [schick-toikka.com](https://www.schick-toikka.com/items) |
| JJannon | old-style/Garalde serif | Optimo | paid | 1 | [typographica.org](https://typographica.org/?p=29913) |
| JJannon Display | old-style/Garalde serif | Optimo | paid | 1 | [typographica.org](https://typographica.org/?p=29913) |
| JKR Knowles | unverified | JKR (in-house or commissioned) (unverified) | custom | 1 | [jkrglobal.com](https://www.jkrglobal.com/llm) |
| JKR Ritchie | unverified | JKR (in-house or commissioned) (unverified) | custom | 1 | [jkrglobal.com](https://www.jkrglobal.com/llm) |
| Juana | unverified | unverified | unverified | 1 | — |
| jws | unverified | unknown (unverified) | unknown | 1 | [styles.refero.design](https://styles.refero.design/style/0803e911-23ac-46aa-a770-007674906e73) |
| KH Teka | neo-grotesk | KH Type (Kurppa Hosk) | paid | 1 | [slanted.de](https://www.slanted.de/kh-type/) |
| KH Teka Mono | grotesk mono | KH Type (Kurppa Hosk) | paid | 1 | [slanted.de](https://www.slanted.de/kh-type/) |
| Kharkiv Tone | rounded sans | Kate Drozd (probable) | free-commercial | 1 | [cap.wp.st-andrews.ac.uk](https://cap.wp.st-andrews.ac.uk/?p=412) |
| Kinfolk Sans | unverified | Schick Toikka (with Alex Hunting Studio) | custom | 1 | [itsnicethat.com](https://itsnicethat.com/news/kinfolk-tenth-anniversary-redesign-schick-toikka-publication-graphic-design-230621) |
| Kinfolk Serif | contemporary editorial serif | Schick Toikka (with Alex Hunting Studio) | custom | 1 | [itsnicethat.com](https://itsnicethat.com/news/kinfolk-tenth-anniversary-redesign-schick-toikka-publication-graphic-design-230621) |
| Klarheit Grotesk | geometric sans | Extraset | paid | 1 | [type-01.com](https://type-01.com/extreme-cuts-and-authentic-approaches-with-extraset/) |
| Klarheit Kurrent | geometric sans | Extraset | paid | 1 | [type-01.com](https://type-01.com/extreme-cuts-and-authentic-approaches-with-extraset/) |
| Kontrapunkt Tomo | unverified | Kontrapunkt (in-house) (unverified) | custom | 1 | [type.kontrapunkt.com](https://type.kontrapunkt.com/api/fonts.json) |
| Kontrapunkt Tomo Slab | slab/Clarendon serif | Kontrapunkt (in-house) (unverified) | custom | 1 | [type.kontrapunkt.com](https://type.kontrapunkt.com/api/fonts.json) |
| Lacquer | display/novelty | Niki Polyocan, Eli Block | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Lacquer) |
| Lacrima Senza | humanist sans | Milieu Grotesque | paid | 1 | [typewolf.com](https://www.typewolf.com/lacrima-senza) |
| Landor Sans | grotesque | Landor (in-house type studio) (identity-only) | custom | 1 | [itsnicethat.com](https://www.itsnicethat.com/news/landor-graphic-design-211123) |
| Lato | humanist sans | Łukasz Dziedzic | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Lato) |
| Lexend Deca | geometric sans | Bonnie Shaver-Troup et al. | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Lexend+Deca) |
| Lora | contemporary editorial serif | Cyreal | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Lora) |
| Lulo Clean | extended/wide sans | Yellow Design Studio | paid | 1 | [yellowdesignstudio.com](https://www.yellowdesignstudio.com) |
| LusionMono | grotesk mono | Lusion (in-house) (unverified) | custom | 1 | [lusion.co](https://lusion.co/) |
| Maison Neue | neo-grotesk | Milieu Grotesque | paid | 1 | [typewolf.com](https://www.typewolf.com/maison-neue) |
| Manrope | geometric sans | Mikhail Sharanda | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Manrope) |
| Martian Mono | grotesk mono | Evil Martians | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Martian+Mono) |
| Martina Plantijn | old-style/Garalde serif | Klim | paid | 1 | [klim.co.nz](https://klim.co.nz/retail-fonts/martina-plantijn/) |
| Merriweather | transitional serif | Sorkin Type | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Merriweather) |
| Mnm | unverified | Merci-Michel (in-house) (unverified) | custom | 1 | [merci-michel.com](https://www.merci-michel.com/) |
| MSCHF Sans Mono | grotesk mono | MSCHF (in-house) (unverified) | custom | 1 | [mschf.com](https://mschf.com/) |
| Muoto | neo-grotesk | 205TF | paid | 1 | [basedesign.com](https://basedesign.com/opinions/matthieu-cortat-roller-interview) |
| Murden CF | unverified | Connary Fagen (probable) (probable) | paid | 1 | [connary.com](https://www.connary.com/) |
| National Park | display/novelty | Andrea Herstowski, Ben Hoepner, Jeremy Shellhorn | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/National+Park) |
| NB Architekt | geometric sans | Neubau (NeubauLaden) | paid | 1 | [luc.devroye.org](https://luc.devroye.org/fonts-37346.html) |
| NB International | neo-grotesk | Neubau | paid | 1 | [neubauberlin.com](https://neubauberlin.com) |
| New Baskerville | transitional serif | ITC / Monotype | paid | 1 | [monotype.com](https://www.monotype.com) |
| NewParis Text | Didone/high-contrast serif | Swiss Typefaces | paid | 1 | [swisstypefaces.com](https://www.swisstypefaces.com/media/ul/fonts/pdf/2019-11-21_swisstypefaces_NewParis.pdf) |
| Newsreader | contemporary editorial serif | Production Type | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Newsreader) |
| Noi Grotesk | grotesque | Studio Feixen (Robin Eberwein, Felix Pfäffli) | paid | 1 | [typewolf.com](https://typewolf.com/noi-grotesk) |
| Nunito | rounded sans | Vernon Adams et al. | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Nunito) |
| Obviously | grotesque | OH no Type Co. | paid (Adobe Fonts) | 1 | [ohnotype.co](https://ohnotype.co/fonts/obviously) |
| Obys | unverified | Obys (in-house) (unverified) | custom | 1 | [tympanus.net](https://tympanus.net/codrops/?p=114394) |
| Oswald | condensed display sans | Vernon Adams | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Oswald) |
| OTF Obys NG | neo-grotesk | Obys (in-house) (probable) | custom | 1 | [tympanus.net](https://tympanus.net/codrops/?p=114394) |
| P22 Mackinac | contemporary editorial serif | P22 Type Foundry | paid (Adobe Fonts) | 1 | [fonts.adobe.com](https://fonts.adobe.com/fonts/p22-mackinac) |
| Pally | rounded sans | Indian Type Foundry (Fontshare) | free-commercial | 1 | [fontshare.com](https://www.fontshare.com/fonts/pally) |
| Panama | contemporary editorial serif | The Temporary State (Roman Gornitsky) | paid | 1 | [typewolf.com](https://typewolf.com/panama) |
| Perpetua | old-style/Garalde serif | Monotype (Eric Gill) | paid | 1 | [monotype.com](https://www.monotype.com) |
| Pitch Sans | grotesk mono | Klim | paid | 1 | [klim.co.nz](https://klim.co.nz/retail-fonts/pitch-sans/) |
| Pixolde | pixel/bitmap | jeti (DaFont) | free/open | 1 | [dafont.com](https://www.dafont.com/pixolde.font) |
| Plain | neo-grotesk | Optimo | paid | 1 | [optimo.ch](https://optimo.ch) |
| Plantin | old-style/Garalde serif | Monotype | paid | 1 | [monotype.com](https://www.monotype.com/fonts/plantin) |
| Playfair Display | Didone/high-contrast serif | Claus Eggers Sørensen | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Playfair+Display) |
| Portrait | contemporary editorial serif | Commercial Type | paid | 1 | [commercialtype.com](https://commercialtype.com/catalog/portrait) |
| PP Acma | condensed display sans | Pangram Pangram | free-personal | 1 | [pangrampangram.com](https://pangrampangram.com/products/acma) |
| PP Mondwest | pixel/bitmap | Pangram Pangram | free-personal | 1 | [pangrampangram.com](https://pangrampangram.com/products/mondwest) |
| PP Neue Machina | geometric sans | Pangram Pangram | free-personal | 1 | [pangrampangram.com](https://pangrampangram.com/products/neue-machina) |
| PP Radio Grotesk | grotesque | Pangram Pangram | free-personal | 1 | [pangrampangram.com](https://pangrampangram.com/products/radio-grotesk) |
| PP Right Grotesk | grotesque | Pangram Pangram | free-personal | 1 | [pangrampangram.com](https://pangrampangram.com/products/right-grotesk) |
| PP Supply Mono | grotesk mono | Pangram Pangram | free-personal | 1 | [pangrampangram.com](https://pangrampangram.com/products/supply) |
| PP Telegraf | geometric sans | Pangram Pangram | free-personal | 1 | [pangrampangram.com](https://pangrampangram.com/products/telegraf) |
| Proxima Nova | geometric sans | Mark Simonson | paid | 1 | [marksimonson.com](https://www.marksimonson.com/fonts/view/proxima-nova) |
| Proxima Soft | rounded sans | Mark Simonson | paid | 1 | [marksimonson.com](https://www.marksimonson.com/fonts/view/proxima-soft) |
| PS Times | transitional serif | Parker Studio (unconfirmed) (unverified) | unknown | 1 | [maxibestof.one](https://maxibestof.one/typefaces/inter/pairing/ps-times) |
| Publico Text Mono | typewriter mono | Commercial Type | paid | 1 | [commercialtype.com](https://commercialtype.com/catalog/publico) |
| PxGrotesk | grotesque | Optimo | paid | 1 | [optimo.ch](https://optimo.ch) |
| Quadrant Text | slab/Clarendon serif | Matter of Sorts | paid | 1 | [matterofsorts.com](https://matterofsorts.com/) |
| Quadrant Text Mono | typewriter mono | Matter of Sorts | paid | 1 | [matterofsorts.com](https://matterofsorts.com/) |
| Questrial | geometric sans | Joe Prince | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Questrial) |
| Quincy CF | contemporary editorial serif | Connary Fagen | paid | 1 | [connary.com](https://www.connary.com/quincy.html) |
| Recife Text | contemporary editorial serif | Luzi Type (Luzi Gantenbein) | paid | 1 | [typewolf.com](https://typewolf.com/recife) |
| Relative | grotesque | Colophon | paid | 1 | [colophon-foundry.org](https://www.colophon-foundry.org) |
| Roc Grotesk | grotesque | Kostic Type Foundry | paid (Adobe Fonts) | 1 | [fonts.adobe.com](https://fonts.adobe.com/fonts/roc-grotesk) |
| Romie | Didone/high-contrast serif | Margot Lévêque Studio | paid | 1 | [typewolf.com](https://www.typewolf.com/romie) |
| RoundHog | rounded sans | PostHog (in-house) (unverified) | custom | 1 | [posthog.com](https://posthog.com/) |
| Sabon | old-style/Garalde serif | Linotype (Jan Tschichold) | paid | 1 | [monotype.com](https://www.monotype.com/fonts/sabon) |
| Saol | Didone/high-contrast serif | Schick Toikka | paid | 1 | [schick-toikka.com](https://www.schick-toikka.com/saol-standard) |
| Scto Grotesk | grotesque | Schick Toikka | paid | 1 | [schick-toikka.com](https://www.schick-toikka.com) |
| Season Sans | neo-grotesk | Displaay Type Foundry | paid | 1 | [displaay.net](https://displaay.net/typeface/season/) |
| Self Modern | contemporary editorial serif | Bretagne | paid | 1 | [typewolf.com](https://www.typewolf.com/self-modern) |
| Sentinel | slab/Clarendon serif | Hoefler&Co. | paid | 1 | [typography.com](https://www.typography.com/fonts/sentinel) |
| SF Pro | neo-grotesk | Apple | system | 1 | [developer.apple.com](https://developer.apple.com/fonts/) |
| Sharp Grotesk | grotesque | Sharp Type | paid | 1 | [sharptype.co](https://sharptype.co/typefaces/sharp-grotesk) |
| Slime Box | display/novelty | Heaven Castro (FontSpace) | free-commercial | 1 | [fontspace.com](https://www.fontspace.com/slime-box-font-f29820) |
| Sneak | neo-grotesk | TIGHTYPE | paid | 1 | [typewolf.com](https://www.typewolf.com/sneak) |
| Soleil | geometric sans | TypeTogether | paid | 1 | [type-together.com](https://www.type-together.com/soleil-font) |
| Sora | geometric sans | Barnbrook / Julián Moncada | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Sora) |
| Source Code Pro | grotesk mono | Adobe (Paul D. Hunt) | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Source+Code+Pro) |
| Source Sans | American gothic | Adobe (Paul D. Hunt) | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Source+Sans+3) |
| Space Mono | grotesk mono | Colophon (for Google) | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Space+Mono) |
| Studio Feixen Sans | neo-grotesk | Studio Feixen Fonts | paid | 1 | [fonts.studiofeixen.ch](https://fonts.studiofeixen.ch/wiki) |
| Suisse Int'l Condensed | condensed display sans | Swiss Typefaces | paid | 1 | [swisstypefaces.com](https://www.swisstypefaces.com/fonts/suisse/) |
| Suisse Int'l Mono | grotesk mono | Swiss Typefaces | paid | 1 | [swisstypefaces.com](https://www.swisstypefaces.com/fonts/suisse/) |
| Suisse Works | contemporary editorial serif | Swiss Typefaces | paid | 1 | [swisstypefaces.com](https://www.swisstypefaces.com/fonts/suisse/) |
| Sydonia Atramentiqua | old-style/Garalde serif | Piotr Wardziukiewicz | paid | 1 | [luc.devroye.org](https://luc.devroye.org/fonts-101058.html) |
| Syllabus | old-style/Garalde serif | Matter of Sorts | paid | 1 | [matterofsorts.com](https://matterofsorts.com/) |
| Syne | display/novelty | Bonjour Monde | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Syne) |
| Söhne | grotesque | Klim | paid | 1 | [klim.co.nz](https://klim.co.nz/retail-fonts/sohne/) |
| TASA Orbiter | neo-grotesk | Taiwan Space Agency / Local Remote (probable) | free/open | 1 | [fontsource.org](https://fontsource.org/fonts/tasa-orbiter/about) |
| te-20 | unverified | Teenage Engineering (in-house) (unverified) | custom | 1 | [teenage.engineering](https://teenage.engineering/) |
| TechnoType | unverified | Teenage Engineering (in-house) (unverified) | custom | 1 | [teenage.engineering](https://teenage.engineering/) |
| TeX Gyre Heros | neo-grotesk | GUST (Helvetica-metric clone) | free/open | 1 | [gust.org.pl](https://www.gust.org.pl/projects/e-foundry/tex-gyre/heros) |
| Theinhardt | grotesque | Optimo | paid | 1 | [optimo.ch](https://optimo.ch) |
| TNY | unverified | unknown (unverified) | unknown | 1 | [styles.refero.design](https://styles.refero.design/style/0803e911-23ac-46aa-a770-007674906e73) |
| TWK Continental | grotesque | Weltkern (TWK) | paid | 1 | [studioambre.com](https://www.studioambre.com/style.css) |
| TWK Continental, custom 'Ambre' cut | custom | Weltkern for Studio Ambre | custom | 1 | [studioambre.com](https://www.studioambre.com/style.css) |
| Union | grotesque | RP Digital Type Foundry (Radim Peško) (probable) | paid | 1 | [radimpesko.com](https://radimpesko.com) |
| Untitled Serif | transitional serif | Klim | paid | 1 | [klim.co.nz](https://klim.co.nz/retail-fonts/untitled-serif/) |
| Werklig Sans | neo-grotesk | Werklig (in-house) (probable) | custom | 1 | — |
| Whitney | humanist sans | Hoefler&Co. | paid | 1 | [typography.com](https://www.typography.com/fonts/whitney) |
| Young Serif | old-style/Garalde serif | Bastien Sozeau | free/open | 1 | [fonts.google.com](https://fonts.google.com/specimen/Young+Serif) |
| Zapf Humanist 601 (Optima) | glyphic/incised | Bitstream (after Hermann Zapf's Optima) | paid | 1 | [myfonts.com](https://www.myfonts.com) |

## 7. Sources and caveats

**Where the faces came from**
- **Our CSS census**, 24 Oct 2026: 226 sites opened in a real browser at 1440 × 900; for each, the
  font families the page had actually loaded (`document.fonts` with status `loaded`, up to ten) and the
  computed family and size of its first `h1` (`research/tools/cdp.py`, `capture.py`; data in
  `research/screens/results.jsonl`). Each census row's evidence is its own site, linked in the table.
  Places come from `research/SOURCES.md`.
- **Added and rechecked studios** were verified one by one from Fonts In Use
  (https://fontsinuse.com), Typewolf's Site of the Day (https://www.typewolf.com/site-of-the-day),
  foundry pages, studios' own credits and case studies, press about their identities, and the sites'
  own CSS files where they could be read. Each row links its source.
- **Face identifications** (foundry, classification, licence) come from foundry pages and Fonts In
  Use typeface pages, linked in §6. Where a site uses a renamed, obfuscated or in-house face, the
  table says so rather than guessing.
- Google Fonts popularity ranks are from Google's own metadata
  (https://fonts.google.com/metadata/fonts, saved 23 Oct 2026; 1,950 families, rank 1 = most used).

**Caveats**
- *Display* is the face of the page's `h1` where the browser computed it at 24 px or more. Where the
  `h1` was tiny or hidden, the role is inferred (marked `*`): a family named "Display", or the only
  family. Treat starred roles as approximate. Added rows take their roles from the source; where the
  source doesn't separate roles, the row says so.
- A site that loads a face doesn't necessarily set much in it, and the census can't see fonts drawn
  as images or SVG (wordmarks, many headlines on Squarespace and Wix sites).
- Classification follows one vocabulary (§6). Borderline faces (grotesque vs neo-grotesk, editorial
  vs transitional serif) are judgement calls; the class totals are robust, single assignments less so.
- "Free for personal use" faces (Pangram Pangram's) on a commercial site imply a bought licence; we
  can't see licences, only files.
- Some rows describe a studio's identity rather than its website; the Source column says which.
