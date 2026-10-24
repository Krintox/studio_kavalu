# Choose your road
### Start-a-project research and recommended onboarding flow for Studio Kavalu by Ananya

Prepared on 23 October 2026 for the lead designer. It goes with `design_direction.md` (homepage section 8, "Choose your road", and the `/start` page).

**How this was researched.** On 23 October 2026 I read 41 studio contact pages using WebFetch and curl. That meant raw HTML, the field definitions behind embedded HubSpot forms, and the text on each page. No browser automation was used.
- Forms that only render in JavaScript are marked "fields not readable".
- Locomotive sits behind a Cloudflare bot check, so it could not be read.
- Tool and price figures come from each vendor's own page on the same day. Vendors change these often, so re-check before buying.
- Where a figure could only be confirmed through secondary sources, the text says so.

---

## Contents
1. The short version
2. Survey: 41 studio pages
3. What the evidence says
4. Tools that make onboarding feel instant
5. Backend options for a Next.js App Router site
6. Recommended flow: "Choose your road"
7. What the founder must set up
8. Sources
9. Appendix: what could not be verified

---

## 1. The short version

1. **The best-known studios barely have a form.** Pentagram, Collins, Koto, Porto Rocha, Basic/Dept, Mother, Ragged Edge, Buck and Studio Dumbar offer a new-business email, often with a named person. 21 of the 40 readable pages have no project form at all. That restraint reads as premium. But it relies on fame and a business-development team, which a founder-led studio does not have.
2. **Studios that want a quick start use a short brief with set choices, then a call.** Halo Lab, Cuberto, FableSquare, Identity Makers, NOW Media, Jess Creatives and Designjoy all do this. The brief has service chips, budget bands, a timeline and a promise of when they will reply. Most then offer a call the visitor can book straight away.
3. **Indian studios add WhatsApp, a phone number, budgets in rupees (in lakh), and quick-reply promises.** Tenet promises a reply "in under 2 hours". FableSquare in Bengaluru says "< 1 day" and is the closest model for Kavalu.
4. **The evidence supports a short form split over several screens:**
   - one to three questions per screen;
   - an easy, interesting first question, with contact details last;
   - answers given by tapping rather than typing;
   - budget as ranges, with a "Not sure yet" choice;
   - checking each field when the visitor moves on from it;
   - chips built from standard checkboxes and radio buttons;
   - spam blocked by hidden checks, not by a puzzle CAPTCHA.
5. **Replying quickly is what wins after the form.** In an HBR study (2011), businesses that contacted an enquiry within an hour were about 7 times as likely to turn it into a real conversation as those that waited an hour. They were about 60 times as likely as those that waited a day. So: an automatic reply within seconds, a personal reply within one working day, and the call booking on the thank-you screen.
6. **Keep the "letter" from the design direction, but make it the result rather than the form.** Forms written as a sentence with blanks to fill in have a well-known 25 to 40% lift (Vast.com, 2010). But other things changed in that test too. And this style has well-documented accessibility problems (Roselli, 2021). The better route: the letter writes itself from ordinary, labelled questions. Then it folds into an envelope and is stamped with the brief's reference number.
7. **Recommended setup:**
   - The site's own server code (a Next.js Route Handler) sends two emails through **Resend**. One goes to connect@ with the client set as reply-to. The other is a branded automatic reply to the client.
   - Spam is blocked by **Cloudflare Turnstile**, a hidden decoy field, and a check on how fast the form was filled.
   - Each brief is also logged to a **Google Sheet**.
   - **Cal.com** (free) is embedded on the thank-you screen, with the client's details already filled in.
   - A **wa.me** WhatsApp link.
   - Later, **Razorpay** Payment Links for the advance. Stripe only takes new Indian businesses by invitation. HoneyBook is not available in India.

---

## 2. Survey: 41 studio pages

### 2.1 Big, well-known studios (mostly email only)

| Studio | URL | How enquiries come in | Notes |
|---|---|---|---|
| Basic/Dept (US and global) | https://www.basicagency.com/contact | Email only: biz@basicagency.com | "We collaborate with ambitious brands and people. Let's build." Offices listed with their local time |
| Collins (NY, SF, London) | https://www.wearecollins.com/contact | "Work with us" with info@wearecollins.com and a copy button | Nothing else near it |
| Koto (global) | https://koto.com/contact/ | Email and phone for each office, with the office's named heads, and a "Say Hello" button | Heading: "Work with us. Wherever you are." |
| Porto Rocha (NY, London) | https://www.portorocha.com/about | "New Business": business@portorocha.com | No form |
| Mother Design (London, NY, LA) | https://www.motherdesign.com/contact | New-business email for each office; a phone link labelled "Call your Mother" | Playful tone, no form |
| Ragged Edge (London) | https://www.raggededge.com/contact | "Time to commit?" with workwithus@raggededge.com and a phone number | Newsletter sign-up uses reCAPTCHA |
| Pentagram | https://www.pentagram.com/contact | "New Business Inquiries": email and phone for each office | No guidance on what to send, no reply-time promise |
| Studio Dumbar/DEPT (Rotterdam) | https://studiodumbar.com/contact | "For new business inquiries contact Wouter", with his email and mobile | One named person is the whole approach |
| Buck (5 offices) | https://buck.co/contact | A newbiz email and phone number for each office | |
| JKR (London, NY) | https://www.jkrglobal.com/contact | Phone and a "New Biz" link | |
| Manual (SF, Amsterdam) | https://manual.studio/contact | "Work enquiry" email | |
| Clay (SF) | https://clay.global/contact | "Become a Client": hey@clay.global and phone | |
| Unseen Studio (Bristol, London) | https://unseen.co/contact/ | projects@unseen.co and phone | |
| Dogstudio/DEPT | https://dogstudio.co/contact | biz@dogstudio.be under a rotating series of jokes ("If you want to make good shit, drop us a line") | The tone does all the work |
| 14islands (Stockholm, Reykjavik) | https://www.14islands.com/contact | "Want to talk?" with hello@ | |
| Rejouice (San Diego, Paris) | https://www.rejouice.com/contact | "New Business." hello@rejouice.com | |
| Hey Studio (Barcelona) | https://heystudio.es/contact/ | "Start a new project · Say hey" with hey@, and the team listed with their roles | |
| Ueno (relaunched in 2025 as a small studio) | https://www.ueno.co/contact | Email (hidden from scrapers) and social links | Its old "project planner" could not be checked because the Wayback Machine blocked requests |
| Hoodzpah (US boutique) | https://hoodzpahdesign.com/contact/ | "Let's talk about your project", leading to an email | Promises to recommend other studios if it is not the right fit or is booked up; lists office hours |
| Locomotive (Montreal) | https://locomotive.ca/en/contact | **Not verified** | Cloudflare's bot check refused both WebFetch and curl (403) |

### 2.2 Studios with a form or a guided enquiry

| Studio | URL | What the visitor fills in | Budget, call, WhatsApp | Promises, prices, availability, other content |
|---|---|---|---|---|
| Instrument (Portland, NY) | https://www.instrument.com/contact/start-a-project | One-page HubSpot form with 9 fields, 3 of them required: first and last name, "How about your email address?", "What's the business name?", "How can we help you?", "Is there a defined budget for this project?" (a number), "Attach a project brief if you'd like!" (file), how they heard, anything else. CAPTCHA switched on | Budget optional, typed as a number. No call | "Tell us about your project in the form below, and we'll put you in touch with the right team." Email alternative: partnerships@ |
| Metalab | https://www.metalab.com/contact | One page: name\*, email\*, "How did you hear of us?"\*, company stage (early, mid or late-stage startup, or enterprise), message\*, newsletter | No budget | "Or reach out directly at contact@metalab.com. We read every message." |
| Cuberto (US, Prague) | https://cuberto.com/contacts/ | "Hey! Tell us all the things": 8 services as tappable chips (real checkboxes), name, email (set as plain text, so phones show the wrong keyboard), message, attachment. reCAPTCHA | Budget chips in US dollars: 10-20k, 20-30k, 30-50k, 50-100k, 100k+ | After sending: "We'll contact you shortly!" |
| Halo Lab | https://growth.halo-lab.com/contacts | **Two steps, marked 1/2 and 2/2.** Step 1: name\*, company email\*, phone. Step 2: about the project\*, budget\* | Budget required, from a US-dollar list running $10–20k up to $100–200k. A separate "Book a call" form | "We respond to inquiries within 24 hours and can usually begin the project within 3–7 business days". Will sign an NDA on request. Five FAQs and nine testimonials on the same page |
| basement.studio | https://basement.studio/contact | Five fields: name, company, email, "Budget (optional)" as free text, message | Optional | Very short |
| Fueled (NY) | https://fueled.com/contact/ | First asks what you want (work on a project, speak at an event, or a media interview). Then name\*, email\*, company\*, phone, website, city, short overview\* | None | Two hidden spam checks: a decoy field and a timestamp |
| Ramotion (SF) | https://www.ramotion.com/contact/ | A form that insists on a company email ("Make sure you use your company email address") | | If sending fails, it offers "Send again" and "Send email" |
| Fantasy (NY) | https://fantasy.co/contact | A form (fields not readable), privacy consent and phone | | |
| Saffron Avenue (US boutique) | https://saffronavenue.com/contact | **14 fields, 6 required**: name, email, business, website or social, years in business, phone, design needs, budget\* (free text with the hint "$5-10k, $10-15k, $15-30k"), ideal launch date\*, about you\*, how they found you\*, "What makes you excited to work with us?", past experience with designers, "What book are you currently reading?" | Budget required, in US dollars | "If you believe we would be a great fit…"; "You can expect to hear back from us within 24 hours!"; office hours; link to the FAQ |
| Davey & Krista (US) | https://daveyandkrista.com/custom-design | "INQUIRE NOW" goes to the contact page. Offers a free brand questionnaire to download | | 25% deposit to start; brand and website take "8–12 weeks"; 8-step process in the FAQ |
| Jess Creatives (US, solo designer) | https://jesscreatives.com/hire-me | Enquiry form in Dubsado; a free "Brainstorm call" booked through TidyCal | Call: yes | Packages at $6,000 and $8,000, each with a timeline. "I typically book out 3-5 months in advance". "I'll reply within 1-2 business days with a quote and next steps". Process, testimonials beside the button, FAQ |
| Paige Brunton (Squarespace studio) | https://www.paigebrunton.com/squarespace-website-designer | "Inquire Now" button | | "$5,600" for a semi-custom site. Custom "starting at $9,000+ … typically range from $9,000 to $15,000". "My team and I take on a handful of projects a year" |
| Designjoy (fixed monthly subscription) | https://www.designjoy.co/ | Either pay straight away through Stripe, or "Book a 15-min intro call" (Cal.com is embedded) | Call: yes | $4,995 a month; "a limited roster of clients"; setup "usually takes about an hour" |

### 2.3 Indian studios

| Studio | URL | What the visitor fills in | Budget, call, WhatsApp | Promises, prices, availability, other content |
|---|---|---|---|---|
| **FableSquare (Bengaluru)** | https://fablesquare.com/contact/ | Name\*, work email\*, company, phone, current website, service (dropdown), approximate budget, timeline (ASAP, 1-2 months, 3-6 months, 6+ months, just exploring), "Tell us more"\*. A hidden decoy field labelled "Leave this field empty". Button: "Send the brief" | **₹50K–₹1L, ₹1L–₹2L, ₹2L–₹5L, ₹5L–₹10L, ₹10L–₹25L, ₹25L+, Not sure yet.** "Prefer a call? Pick a slot directly — we keep 30 minutes free every weekday". Phone | "Typical reply time < 1 day". **"The first 10 days": Day 0 you write, Day 2 a 20-minute intro call, Day 5 a working session, Day 10 the proposal and kick-off.** "A one-line brief is fine." "Tell us the budget band." The FAQ says projects run ₹5L–₹50L, retainers about ₹3L a month, and a paid discovery phase ₹1–3L |
| NOW Media (Bengaluru) | https://nowmedia.in/ | "Plan my project" estimator: pick services, see a rough budget, then book a scoping call. Also an AI chat | Ranges in rupees and dollars (branding ₹5L–₹25L, or $6K–$30K). 20-minute call slots | "Get onboarded in under 5 days". A "Discovery Blueprint" questionnaire of 15 to 45 minutes. Testimonials |
| Confetti Design (Mumbai and Dubai; has a Bengaluru page) | https://confetti.design/contact-us | Full name, email, company, phone, "Tell us about the project, scope of work, timelines, budget, etc.", and service checkboxes (branding, packaging, website, quick-commerce, photography, other). reCAPTCHA | "Book a call directly with our founders"; "Whatsapp Us" link | "Get Instant Response". "Strategy to final packaging in 6 weeks". Client quotes beside the buttons |
| Identity Makers (India) | https://identitymakers.co/ | **Several steps** ("Step 1: What are you looking for?"): service, country (India first), budget, company stage. Small budgets are pointed to free guides | **Under Rs 24,000; Rs 24,000 to 90,000; above Rs 90,000.** WhatsApp link with the message "Hi, Please help me in building my brand." already typed | "Starting at" price tables in rupees (+18% GST) and in dollars. "By taking on fewer projects monthly…". Review ratings |
| Tenet (Noida, Dubai, London) | https://www.wearetenet.com/contact-us | A form (fields not readable), plus "Don't want to fill the form? Cool. Some more options for you." | Phone numbers for the UAE, India and the UK | **"Get a Response in Under 2 Hours — Guaranteed!"** |
| Chlorophyll (Mumbai) | https://www.chlorophyll.in/contact-us/ | One page: full name\*, company, email\*, phone\*, enquiry type\* (business or job), industry, how they heard of you, message, privacy consent\*. CAPTCHA | None | |
| Kahani Designworks (Mumbai) | https://www.kahanidesignworks.com/contact | Email and phone ("Talk to us") | | |
| Yellow Slice (Mumbai, Pune, UK) | https://www.yellowslice.in/contact | A business-enquiry email and phone number for each city | | |

### 2.4 Website templates (Framer)

| Template | URL | What it does |
|---|---|---|
| Booked Call (free) | https://www.framer.com/marketplace/templates/booked-call/ | "A native Cal.com embed sits at the center of the page, so booking happens right there". Has a simple form for people not ready to book |
| Consultant (free) | https://framer.com/templates/consultants | A working Cal.com calendar, a written enquiry form "for people who would rather type", a three-step "how this works", and a starting price |
| FluxForm component ($18) | https://www.framer.com/community/marketplace/components/fluxform/ | Budget and multi-service choices; submissions go through Formspark |

### 2.5 How often each approach appears
Counted across the 40 readable studio pages (templates not counted).

| Approach | Count | Who |
|---|---|---|
| No project form (email or phone only) | 21 of 40 | Everyone in 2.1, plus Kahani and Yellow Slice |
| A form or guided enquiry | 19 of 40 | Sections 2.2 and most of 2.3 |
| Asks for a budget | 9 of 19 | Instrument, Cuberto, Halo Lab, basement, Saffron Avenue, FableSquare, Identity Makers, NOW Media (in its estimator), Confetti (as a prompt in its message box) |
| Makes the budget compulsory | 2 of 19 | Halo Lab, Saffron Avenue |
| Spread over several steps | 3 of 19 | Halo Lab, Identity Makers, NOW Media |
| Lets you upload a file | 2 of 19 | Instrument, Cuberto |
| Lets you book a call | 6 of 19 | Halo Lab, FableSquare, NOW Media, Confetti, Jess Creatives, Designjoy |
| WhatsApp link | 2, plus thinkB in Bengaluru | Indian studios only |
| Says when they will reply | 5 | Tenet (under 2 hours), FableSquare (under a day), Halo Lab (24 hours), Saffron Avenue (24 hours), Jess Creatives (1–2 business days) |
| Shows prices or ranges | 7 | Jess Creatives, Paige Brunton, Designjoy, Identity Makers, FableSquare, NOW Media, Davey & Krista (the deposit) |
| Says how booked up they are | 4 | Jess Creatives, Paige Brunton, Designjoy, Identity Makers |
| Explains the process next to the form | 6 | FableSquare, Jess Creatives, Davey & Krista, NOW Media, Halo Lab, Confetti |
| Visible CAPTCHA | 4 | Instrument (through HubSpot), Cuberto, Confetti, Chlorophyll |
| Hidden decoy field | 2 | FableSquare, Fueled |

### 2.6 What to borrow and what to avoid

**Borrow:**
- **From the big studios:** restraint, a named person and short, confident copy.
- **From FableSquare:**
  - budget ranges in rupees, with "Not sure yet";
  - "a one-line brief is fine";
  - call slots kept free every weekday;
  - a typical reply time;
  - the day-by-day "first 10 days".
- **From Halo Lab:** split the form so the easy part comes first. State the reply time and how soon work can start. Keep the FAQ and testimonials next to the form.
- **From Jess Creatives and Paige Brunton:** honest starting prices, and honest notes on how far ahead they are booked.
- **From Identity Makers:** a kind route for small budgets (a smaller offer rather than a dead end), and a WhatsApp message that is already typed.
- **From Hoodzpah:** "if we're not the right fit, we'll point you to someone who is". It is selective without being cold.
- **From Instrument:** questions written the way you would ask them out loud, and an optional place to attach a brief.

**Avoid:**
- Saffron Avenue's 14 fields. Too much for a visitor who should be able to start straight away.
- Insisting on a company email, as Ramotion does. Many Indian founders and direct-to-consumer brands use Gmail.
- Email fields set as plain text, as at Cuberto. Phones then show the wrong keyboard.
- Visible CAPTCHAs.
- The current site's single "Message" box. It gives no structure, sets no expectations and offers no next step.

---

## 3. What the evidence says

### 3.1 One page or several steps
- **Nielsen Norman Group (NN/g)** says step-by-step forms suit tasks people are doing for the first time [1]. Briefing a studio is exactly that.
  - Benefits: they feel less overwhelming, and they can branch so each person only sees the questions that apply.
  - Costs: more clicks, and it is harder to stop and pick up later.
  - Advice: show all the steps and which one you are on, name each step clearly, offer a Back button, and let people leave and come back.
- **GOV.UK** advises: "Start by asking one question per page". It "helps users understand what you're asking them to do" [2].
- **Venture Harbour** reports big gains from switching its own lead forms to several steps [3]. Its consulting enquiry form went from 0.96% to 8.1% of visitors, and a finance site from 11% to 46%. Its explanation: start with an easy question and ask for contact details last. No method is published, so treat these as indicative.
- **Baymard** (research on online checkouts) finds that the number of fields matters far more than the number of steps [4]. The average checkout has 11.3 fields; most only need about 8.
- **For Kavalu:** five short screens of one to three questions, about 8 required answers, most of them taps.

### 3.2 How many fields, and which ones
- **HubSpot** analysed about 40,000 landing pages (Dan Zarrella) [5]. Asking for age, phone number or location went with fewer sign-ups. Extra large text boxes and dropdowns cost more than extra one-line fields.
- **CXL** [6] shows the count is not the whole story. Michael Aagaard removed three fields and sign-ups fell 14%, because he had cut the questions people actually wanted to answer. Rewriting the field labels instead raised sign-ups by 19.2%. The much-quoted Imagescape case (11 fields cut to 4, sign-ups up 120%) dates from 2007–08.
- **MarketingExperiments** [7]: a shorter form cut the cost of each lead by $10.66 in one test.
- **For Kavalu:**
  - Require only:
    - which services;
    - where the brand is today;
    - the brand's name;
    - a short brief;
    - the timeline;
    - a budget range;
    - the client's name and email.
  - Make the phone number optional, offered as a WhatsApp contact.
  - Accept any email address, not only company ones.
  - Write every label as a plain question.

### 3.3 Showing only the questions that apply
Show only what is relevant [8] and let the form branch [1]. For Kavalu:
- Step 2 only shows the follow-up questions for the services the visitor picked.
- Choosing packaging adds a question about how many products.
- Choosing ongoing social media switches the budget to monthly amounts.
- The thank-you screen changes with the budget and timeline.

### 3.4 Progress bars
- **A review of 32 experiments** (Villar, Callegaro and Yang, 2013) found that a progress bar moving at a steady rate did not significantly reduce drop-off [9]. A bar that moved fast at first and then slowed did reduce it. One that started slow and sped up made drop-off worse.
- **GOV.UK** advises testing without a progress bar first [2]. Several of its services removed theirs "without any negative effects". The Carer's Allowance form dropped a 12-step bar "with no effect on completion rates or times".
- **For Kavalu:** a quiet line of named steps ("Road · Details · Brand · Timing · You") drawn as the plum road, with no percentage. Put the quickest questions first so it feels fast early on.

### 3.5 Asking about budget
**For:**
- It shows early whether the project fits.
- It lets Ananya reply with a suitable option and saves a wasted call.
- Premium peers talk about money openly (FableSquare: "Tell us the budget band").

**Against:**
- It is a known reason people abandon forms. Zuko lists "qualification questions (e.g. company size, budget, job title)" among them [10].
- Many clients genuinely do not know their budget.
- A budget figure can set expectations too low.
- One set of ranges fits a film shoot and a monthly social retainer badly.

**What we don't know:** no solid public test isolates the effect of a budget question. In the survey, 9 of the 19 forms ask for budget and only 2 insist on it.

**For Kavalu:**
- Ask late, at step 4.
- Show ranges in the visitor's currency, using lakh for India.
- Include "Not sure yet — guide me".
- Make the question required, but with that one-tap way out.
- Put a "projects usually start at…" line beside it.
- Use monthly ranges for retainers.
- Use the answer to choose the thank-you message, never to reject anyone automatically.

### 3.6 Checking answers and showing errors
- **A study by Etre and Luke Wroblewski** (22 people, six versions of a form) compared the best version that checked fields as you went with one that only checked on submit [11]. With checking as you go:
  - success went up 22%;
  - errors went down 22%;
  - satisfaction went up 31%;
  - time to finish went down 42%;
  - eye movements went down 47%.
- **When to check:** after the person leaves a field worked better than while they were still typing [11].
- **NN/g's advice** [12]:
  - check once the answer is complete;
  - put the message right next to the field;
  - don't rely on colour alone;
  - don't let a list at the top be the only sign of an error.
- **GOV.UK** puts a summary of errors at the top when the form is submitted, linking to each field [13].
- **Labels:** keep them visible above the field, because grey example text inside the box is not a label [14]. Mark required fields, and optional ones too [15].

### 3.7 Phones
- Set each field's type (email, phone) and its autofill hint correctly. Do not ask people to type their email twice [16].
- Baymard found 54% of mobile sites did not show the right keyboard for phone, postcode or card fields [17]. Cuberto's email field shows this mistake.
- iPhones zoom into any field whose text is smaller than 16px [18]. Use 16px or more rather than switching zoom off.
- People finished single-column forms about 15.4 seconds faster than two-column ones (CXL Institute, about 700 people) [19].
- Anything tappable should be at least 24×24 pixels (accessibility standard WCAG 2.2, level AA, rule 2.5.8) [20]. Aim for chips 44–48px tall.
- **For Kavalu:**
  - a Back/Continue bar fixed at the bottom that stays above the keyboard;
  - chips that wrap onto new lines rather than scrolling sideways;
  - answers saved on the device in case the visitor leaves;
  - one column throughout.

### 3.8 Making chips accessible
- **Grouping:** put each question in a `fieldset`, with the question as its `legend` [21].
- **Build each chip from a real checkbox or radio button:**
  - Hide the real control with `opacity: 0`, placed over the custom design. Never use `display:none` or `visibility:hidden`, which hide it from screen readers too [22][23].
  - Style the chip using `:checked +` and `:focus-visible`.
  - Test it in Windows high-contrast mode.
- **Keyboard:** real controls bring the expected behaviour for free [24]. Tab moves into the group, the arrow keys move between radio options, and Space ticks a checkbox.
- **Showing what is selected:**
  - Show it with more than colour, for example a tick plus bolder text.
  - Borders and selected states need at least 3:1 contrast.
  - The keyboard focus must be visible.
- **Personal details:** add the standard autofill hints to name, email and phone fields [25].
- **Which control:**
  - Radio buttons where only one answer is allowed (stage, timeline, budget).
  - Checkboxes where several are allowed (services, details).
  - Do not fake chips out of plain buttons for form answers.

### 3.9 Stopping spam without a CAPTCHA
- **The W3C** (the web standards body) says CAPTCHAs remain a barrier for many people [26]. It prefers approaches the visitor never has to interact with, and lists hidden decoy fields and behaviour checks as alternatives.
- **Stanford** (Bursztein and others, 2010) tested 318,000 CAPTCHAs [27]. People found them hard, and the audio ones hardest. Non-native English speakers were slower and less accurate, which matters for an Indian and international audience.
- **SEOmoz** (2009) found a CAPTCHA cut spam by 88% but stopped 159 real submissions, about 3.2% of the total [28]. These figures are reported second-hand.
- **Cloudflare Turnstile** is a free spam check that can run invisibly [29]. The free plan allows up to 20 widgets.
  - Each check has to be confirmed by the site's server.
  - Each token lasts 300 seconds and can only be used once. A step-by-step brief can take longer than 5 minutes, so run the check on the final step.
- **Time checks:** common tools reject forms filled faster than 2 seconds (Convert Forms) or 5 seconds (the Drupal Honeypot module) [30].
- **For Kavalu:**
  - A hidden decoy field that only bots fill in.
  - A signed record of when the visitor started, so forms finished in under about 4 seconds are flagged.
  - Turnstile running invisibly.
  - The automatic reply never repeats anything the visitor typed. Otherwise the form could be used to send spam to strangers.
  - Submissions caught by the decoy or the timer are flagged rather than deleted, and get no automatic reply. A small studio cannot afford to lose a real client to a false alarm.

### 3.10 Building trust around the form
- **Speed:** HBR (Oldroyd, McElheran and Elkington, 2011) tested 2,241 US companies [31]. Those that replied to an enquiry within an hour were nearly 7 times as likely to reach a real conversation as those that waited an hour. They were more than 60 times as likely as those that waited a day or more. So:
  - send the automatic reply within seconds;
  - reply personally within one working day;
  - put the call booking on the thank-you screen.
- **Showing prices:**
  - NN/g finds price is the first thing most people look for [32]. Custom services should show what typical projects cost.
  - Gartner (June 2025) found 61% of business buyers prefer to buy without talking to a salesperson [33].
  - So: "Identity projects usually start at ₹[X]."
- **Being booked up:**
  - Things in short supply are valued more (Worchel, Lee and Adewole, 1975) [34].
  - Peers say honestly how far ahead they are booked. Jess Creatives: "book out 3-5 months in advance".
  - Only say it when it is true, and update it every month.
- **Testimonials:**
  - The Spiegel Research Center found that showing reviews raised sales by 190% for cheaper products and 380% for more expensive ones [35]. That is online-shop data, so it only suggests the effect for services.
  - So: one short client quote beside the form, not a slider.
- **What happens next:** the thank-you page should say what happens next, and when [36].

---

## 4. Tools that make onboarding feel instant

### 4.1 Booking a call

| | Cal.com (recommended) | Calendly |
|---|---|---|
| Free plan | One person, **unlimited types of meeting**, email and SMS reminders, payments by Stripe and PayPal [37] | **One type of meeting**, no payments or reminders [39] |
| Putting it on the site | On the page, as a pop-up when something is clicked, or as a floating button [38] | Can be embedded |
| Filling in the client's details | Yes. Name, email, notes, any booking question and the brief's reference number can be passed in [38] | Yes, through the link |
| Knowing when a call is booked | The embed reports each booking, so the page can confirm it and you can count bookings [38] | |
| Sending people to different meetings by their answers | Paid (Teams plan at $12 per person a month, paid yearly; another Cal.com page quotes $37). Not needed, because Kavalu's own form does this [37][38] | Teams plan at $16 per person a month [39] |
| Charging for a call | Stripe and PayPal add-ons. Cal.com's own payment option (run by Whop) is built for the US: fees in dollars and payouts by US bank transfer, PayPal or Cash App [38] | From the Standard plan, $10 per person a month [39] |

### 4.2 Form builders, if the form isn't built by hand
- **Tally's free plan** covers unlimited forms and submissions (within fair use), questions that branch, sending data to other tools, Google Sheets and Notion [40]. Uploads are capped at 10 MB per file. Automatic emails to the person who filled it in, saving half-finished forms, your own web address and removing Tally's branding all need Pro at $24 a month.
- **Typeform** starts at $28 a month paid yearly, or $39 monthly, for 100 responses a month [41]. Removing its branding starts on the Plus plan.
- **Verdict:** build the form into the Next.js site. It is a key brand moment. Tally Pro is a fallback that can be live the same day.

### 4.3 Managing clients and client portals
- **HoneyBook** works in the US, Canada, the UK and Australia (the UK and Australia since May 2026), but not in India [42].
- **Dubsado** costs $335 a year (Starter) or $525 a year (Premier) [43]. It covers enquiry forms, client portals and invoices, with scheduling and automation on Premier. Its payments run through US-based processors, which is less useful while Stripe India is invitation-only.
- **Bonsai's** Essentials plan costs $19 per person a month paid yearly, or $25 monthly [44]. It covers proposals, contracts, invoices, a client portal, scheduling and forms. Payments go through Stripe.
- **For Kavalu now:** a free Notion page for each client, copied from a template, with the brief, timeline, files, feedback and invoices. For GST invoices, use Razorpay Invoices or whatever the accountant uses.

### 4.4 Taking payments
- **Razorpay** [45]:
  - No setup fee and no annual fee.
  - 2% per payment on Indian cards, UPI, net banking and wallets; up to 3% on international cards. GST of 18% is charged on the fee.
  - Payment Links can be sent on WhatsApp, by text or by email. They accept part-payments and advances, in about 100 currencies.
  - The pricing page also mentions a 0.2% fee for Payment Pages and Payment Buttons, and contradicts itself on this. Confirm before using them.
- **Stripe** only takes new Indian businesses by invitation [46].
- **When to take money:**
  - Not at first contact for custom work. Premium studios do not take money before a conversation.
  - For the advance once the proposal is accepted: a Razorpay Payment Link set to take part of the fee.
  - Optionally, a fixed-price starter service such as a Brand Audit or Social Media Audit, bought and booked in one go. The client pays on a Razorpay Payment Page, then lands on the Cal.com booking.

### 4.5 Automatic reply and welcome guide
- The automatic reply goes out within seconds from the studio's own address (sent through Resend), with the brief's reference number. A personal reply follows within one working day.
- A welcome guide, "Working with Studio Kavalu", as a Notion page or a one-page PDF. It covers:
  - how we work: Listen, Map, Make, Launch, from the design direction;
  - what we need from you;
  - typical timelines;
  - fees and the advance;
  - rounds of changes;
  - how we keep in touch;
  - an FAQ.

### 4.6 WhatsApp
- **The link:** `https://wa.me/91XXXXXXXXXX?text=<message>`, where the message is web-encoded (spaces as %20 and so on). Write the full international number with no plus sign, leading zeros, brackets or dashes [47].
- **Message already typed:**
  - On the thank-you screen: "Hi Ananya, I just sent brief KAV-7Q2MD through your website."
  - On the first screen: "Hi Ananya, I found Studio Kavalu online and would love to talk about a project."
- **App:** use the free WhatsApp Business app on the studio's number, for a business profile and automatic greeting and away messages.
- **Look:** show it as a text link ("Prefer WhatsApp?") rather than a floating green bubble, to keep the premium feel.

### 4.7 What is normal for Indian studios (from the survey)
- WhatsApp links (Confetti, Identity Makers, thinkB) and a visible phone number.
- Budgets shown in lakh (FableSquare, Identity Makers), with rupees and dollars side by side for international clients (Identity Makers, NOW Media).
- "Talk to the founders" (Confetti).
- Quick-reply promises (Tenet, FableSquare).
- Prices shown "+18% GST" (Identity Makers).
- 20- to 30-minute introductory calls (FableSquare, NOW Media).
- Payment by Razorpay, UPI or bank transfer against a GST invoice.

---

## 5. Backend options for a Next.js App Router site

### 5.1 Comparison (prices as published on 23 October 2026)

| Option | Free plan | First paid plan | Automatic reply to the client | Attachments | Spam tools | Setup | Watch out for |
|---|---|---|---|---|---|---|---|
| **The site's own server code plus Resend** [48] | 3,000 emails a month (100 a day), 3 domains, 30 days of logs | Pro, $20 a month for 50,000 | Yes, any template, styled to the brand | Up to 40 MB per email, but the files must first reach the site's server code (see 5.2) | You build them (5.3) | Half a day, including the domain's email settings | You handle spam and keeping a record yourself. The domain's email settings (SPF and DKIM) must be set up |
| Formspree [49] | 50 submissions a month, kept 30 days, no uploads | Personal, $10 a month paid yearly (200 submissions, 1 GB of files). Professional, $20 a month paid yearly (2,000, 5 GB) | Professional and above | Personal and above | Its own spam filter and reCAPTCHA. A custom decoy field only on Business | 30 minutes | Low free limit. The page shows two different sets of monthly prices |
| Web3Forms [50] | 250 a month, unlimited forms, hCaptcha, decoy field | Pro, $12 a month paid yearly ($149): 10,000, files (5 GB), Turnstile, automatic replies, sending data to other tools | Pro | Pro | Free: hCaptcha and a decoy field. Pro: Turnstile and reCAPTCHA | 30 minutes | Its access key sits in the page code. Limiting it to your own domain needs Pro |
| Basin [51] | 50 a month, 1 form, 100 MB of storage | Starter, $12.50 a month paid yearly. Growth, $24.17 a month paid yearly (automatic replies, sending data to other tools) | Growth and above | Yes | Decoy field, reCAPTCHA, hCaptcha, Turnstile | 30 minutes | Low free limit |
| Supabase [52] | 500 MB database, 1 GB storage, 5 GB of downloads, 50 MB per file, 2 projects. **Paused after a week with no activity** | Pro, $25 a month | No (use it with Resend) | Yes, uploaded straight from the browser | | 1–2 hours | The pausing is a real risk for a form that is used rarely. Add a scheduled task to keep it awake, or pay |
| Google Sheets with Apps Script [53] | Free. A personal Google account can send emails to 100 people a day, run a script for up to 6 minutes, and make 20,000 web requests a day. Google Workspace allows 1,500 emails a day | | Possible, sent from Gmail | Awkward | | 1 hour | Easy for the founder to read. Google can change the limits without notice |
| Tally (no code) [40] | Unlimited (within fair use), 10 MB files, sends data to other tools | Pro, $24 a month | Pro | Yes | Blocks duplicate submissions | 1 hour | Hard to make it look like the brand |

### 5.2 Hosting limits that shape the build
- **Size limits:** Vercel (the usual host for Next.js) refuses anything over **4.5 MB** sent to the site's server code [54]. A Next.js Server Action only accepts **1 MB** unless the setting is raised [55]. So files must never go through that code.
  - Version 1: take links to references only.
  - If uploads are wanted later: send files from the browser straight to storage (Vercel Blob, or a one-off upload link from Supabase), and email the links [54][52].
- **Vercel's free Hobby plan is for non-commercial use only.** It counts "advertising the sale of a product or service" as commercial, so the studio site needs Pro at $20 a month [54]. The alternative is Netlify, whose staff have said several times that its free plan can be used commercially [56]. Check its current terms.
- **Supabase's free plan** pauses after 7 days without activity [52].

### 5.3 Recommendation
**The site's own server code, plus Resend, Turnstile, the decoy field and timer, a Google Sheet log, Cal.com and a WhatsApp link.**

Why:
- Automatic replies cost extra with every ready-made form service (Formspree Professional, Web3Forms Pro, Basin Growth). Resend's free plan includes them, fully branded.
- 3,000 free emails a month, against 50 to 250 free submissions elsewhere.
- Passwords and keys stay on the server, no other company's branding appears, and the briefs land in a sheet the founder owns.
- The cost is about half a day of code and email settings, and you handle spam yourself (section 3.9).

If there is no development time: Web3Forms Pro ($12 a month) or Tally Pro ($24 a month), plus Cal.com.

How it fits together:
- **In the browser** ("Choose your road", five steps, answers saved on the device):
  - "Let's begin" asks the server for a signed start time. This must come from the server at that moment, because the page itself may be built in advance.
  - On step 5, Turnstile runs invisibly when the visitor presses Send.
  - The answers go to `/api/brief`, with the decoy field, the start time and the Turnstile result.
- **On the server:**
  1. Check every answer, trim spaces, cap lengths, and reject web addresses typed into the name or brand fields.
  2. Confirm the Turnstile check with Cloudflare. If it fails, refuse the submission.
  3. If the decoy field is filled or the form was too fast, mark it as flagged rather than refusing it.
  4. Create a reference number, `KAV-XXXXX`.
  5. At the same time, email connect@ through Resend (with the client as reply-to) and add a row to the Google Sheet.
  6. If either worked, tell the browser it succeeded, then send the automatic reply to the client (unless flagged).
  7. If both failed, report an error. The browser keeps the answers and offers the email address and a "Copy my answers" button.
- **The thank-you screen:** the letter folds into an envelope stamped with the reference number, then "What happens next", the Cal.com booking with details filled in, and the WhatsApp link.

Code outline for the developer. Check the names against the current versions of each tool's documentation before using it.

```ts
// app/api/brief/route.ts
import { after } from "next/server";
import { Resend } from "resend";
import { createHmac, timingSafeEqual, randomBytes } from "node:crypto";
import { BriefSchema, labels } from "@/lib/brief";          // zod schema + fixed option labels (section 6)
import { InternalBrief, ClientWelcome } from "@/emails";     // React Email templates

export const runtime = "nodejs";
const resend = new Resend(process.env.RESEND_API_KEY);

function startedLongEnoughAgo(token = "") {
  const [t = "", sig = ""] = token.split(".");
  const good = createHmac("sha256", process.env.FORM_SIGNING_SECRET!).update(t).digest("hex");
  if (sig.length !== good.length || !timingSafeEqual(Buffer.from(sig), Buffer.from(good))) return false;
  const age = Date.now() - Number(t);
  return age > 4_000 && age < 24 * 60 * 60 * 1000;     // longer than 4 s, younger than a day
}

export async function POST(req: Request) {
  const parsed = BriefSchema.safeParse(await req.json());
  if (!parsed.success) return Response.json({ error: "invalid" }, { status: 400 });
  const b = parsed.data;

  // 1. Turnstile: hard fail
  const verify = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
    method: "POST",
    body: new URLSearchParams({ secret: process.env.TURNSTILE_SECRET_KEY!, response: b.turnstileToken }),
  }).then((r) => r.json());
  if (!verify.success) return Response.json({ error: "verify" }, { status: 403 });

  // 2. Honeypot + time trap: soft fail (flag, keep, no auto-reply)
  const flagged = Boolean(b.website) || !startedLongEnoughAgo(b.startToken);
  const id = "KAV-" + randomBytes(3).toString("hex").toUpperCase().slice(0, 5);
  const l = labels(b);                                    // only fixed option labels + sanitised first name

  // 3. Notify the studio and log the brief, in parallel
  const [mail, sheet] = await Promise.allSettled([
    resend.emails.send({
      from: process.env.BRIEF_FROM_EMAIL!,
      to: [process.env.BRIEF_TO_EMAIL!],
      replyTo: b.email,                                   // `reply_to` in older SDK versions
      subject: `${flagged ? "[check] " : ""}New brief · ${b.brandName} · ${l.roads} · ${l.budget} · ${l.timeline}`,
      react: InternalBrief({ id, b, l, flagged }),
    }),
    fetch(process.env.SHEETS_WEBHOOK_URL!, {
      method: "POST",
      body: JSON.stringify({ secret: process.env.SHEETS_WEBHOOK_SECRET, id, flagged, ...b }),
    }),
  ]);
  const mailOk = mail.status === "fulfilled" && !mail.value.error;   // Resend returns { data, error }
  const sheetOk = sheet.status === "fulfilled" && sheet.value.ok;
  if (!mailOk && !sheetOk) return Response.json({ error: "send" }, { status: 500 });

  // 4. Auto-reply after the response is sent (never echo free text)
  if (!flagged) {
    after(() =>
      resend.emails.send({
        from: process.env.BRIEF_FROM_EMAIL!,
        to: [b.email],
        replyTo: process.env.BRIEF_TO_EMAIL!,
        subject: `Your brief is with us, ${l.firstName}`,
        react: ClientWelcome({ id, l }),
      }),
    );
  }
  return Response.json({ id });
}
```

The Google Sheet side. In the sheet, open Extensions → Apps Script, paste this, then publish it as a web app that runs as you and that anyone can call.

```js
function doPost(e) {
  const d = JSON.parse(e.postData.contents);
  if (d.secret !== PropertiesService.getScriptProperties().getProperty("SECRET")) {
    return ContentService.createTextOutput("denied");
  }
  SpreadsheetApp.getActive().getSheetByName("Briefs").appendRow([
    new Date(), d.id, d.flagged, d.name, d.email, d.phone, d.brandName, (d.roads || []).join(", "),
    d.stage, d.timeline, d.currency, d.budget, d.brief, d.brandLink, d.references, d.heardFrom, d.ref,
  ]);
  return ContentService.createTextOutput("ok");
}
```

---

## 6. Recommended flow: "Choose your road"

### 6.1 Name and how it fits the design direction
- **Button label:** "Start a project", used everywhere. On a button, clear beats clever.
- **Name of the flow and page title:** "Choose your road", with ಕವಲು (kavalu) as a small mark. Kavalu means crossroads.
- **Progress:** the plum road from the design direction, with five junctions, one per step.
- **Reference number:** `KAV-7Q2MD`, shown as the postmark on the envelope.
- **The letter:** the design direction plans "a letter written as a sentence with inline choices, sent in one click". **Keep the letter, but move the questions out of the sentence.**
  - Sentence-style forms do have a reported 25–40% lift (Vast.com, 2010) [58]. Other changes were tested at the same time, and the author warns they are "unlikely … solely responsible".
  - Accessibility testing of sentence forms found real problems [59]:
    - Screen reader users found it confusing to hear each blank read out one by one.
    - Choices placed inside sentences confused people.
    - Dropdowns annoyed them, because they had to open each one to see the options.
    - People using screen magnifiers lost labels that wrapped onto the next line.
    - Some people with cognitive disabilities found the unfamiliar layout frustrating.
  - **So:** the visitor answers ordinary labelled questions. Beside them on desktop (or tucked into a strip on phones), the letter fills itself in from the answers. On step 5 the finished letter is the review before sending. Press Send, and it folds into an envelope and gets stamped. The visitor gets all the brand feeling with none of the usability cost.

### 6.2 Principles
1. **One conversation in five short steps:** about three minutes, 8 required answers (4 taps, 4 typed).
2. **Premium means restraint:** the founder named, no badges, no counters, honest starting prices.
3. **Instant means no dead ends:** every way out has a next step (a call, WhatsApp, a smaller offer).
4. **Selective means clear, not gatekeeping:** minimums stated, fit explained, other studios recommended when right.
5. **Every answer is used:** services choose the step 2 questions, budget and timeline choose the thank-you message, and everything fills in the call booking.

### 6.3 Ways in
- **Header button**, "Start a project", on every page → `/start`.
- **End of each case study:** "Start a project like Nivritti →" → `/start?road=identity&needs=logo,packaging`.
- **"Four roads" service cards:** "Start here" → `/start?road=<service>`, with that road already selected.
- **Homepage section 8:** step 1 (the four roads, drawn as the index cards) and the start of the letter, inline. "Continue" goes to `/start` at step 2 with the choices carried over. A separate page keeps the homepage light, makes the browser's Back button behave, and makes it easier to see where people drop out.
- **Footer:** the road tabs, connect@studiokavalu.com, the WhatsApp link and Instagram. This replaces the single "Message" box.

### 6.4 Map of the flow
- **The first screen (`/start`)** leads into five steps, then a sent screen:
  1. Road (which services)
  2. Details (follow-up questions for each service)
  3. Brand
  4. Timing and budget
  5. You, with the finished letter shown for review
- **The sent screen:** the envelope is stamped with the reference number, then "What happens next", the Cal.com call booking (details filled in), and a WhatsApp link with the reference. For small budgets it shows the starter offer instead.
- **Ways out from the first screen:**
  - "Rather talk?" opens Cal.com, which asks three booking questions.
  - WhatsApp, with a message already typed.
  - Email to connect@studiokavalu.com.

### 6.5 Each screen: fields and copy
Fields marked \* are required. Every multiple choice is a real radio button or checkbox styled as a chip (section 3.8).

**Screen 0: first screen**
- Small heading above: *Start a project*
- Main heading: **Choose your road.**
- Text: *A brand is a set of choices: what it says, how it looks, where it shows up, who it speaks to. Tell us where you're standing, and we'll make the next ones with you.*
- Small print: *Five short steps · about three minutes · read by Ananya, personally*
- Main button: **Let's begin**
- Second line: *Rather talk first?* [Book a 20-minute call] · [WhatsApp] · [connect@studiokavalu.com]
- Optional lines, filled in by the founder and shown only while true: *Now booking projects from [Month].* · *Identity projects usually start at ₹[X].*
- Beside the form on desktop, below it on phones:
  - one client quote;
  - "How it works": tell us your road (3 minutes) → talk to Ananya (20 minutes) → a proposal within [3] working days.

**Screen 1: Road**

| Field | Question and help text | Type | Options |
|---|---|---|---|
| `roads`\* | **Which road are you on?** *Choose as many as you like. Unsure is a fine place to start.* | Checkbox chips; at least one | **Branding**: strategy, research, audits; what the brand says · **Visual identity**: logo, systems, packaging, print; how it looks · **Social media**: audits, direction, content; where it shows up · **Film & photography**: shoots, ad films, art direction; how it moves · **Not sure yet**: help me choose (choosing this clears the others) |

- Error message: *Choose at least one road, or pick "Not sure yet".*
- Button: **Continue**, with *Next: the details* in small text.

**Screen 2: Details** (only the blocks for the roads chosen)
- Heading: **A little more about that road.** *Tap what fits. Skip what doesn't.*

| Field | Shown when | Question | Type | Options |
|---|---|---|---|---|
| `stage`\* | Always | Where's the brand today? | Radio | Just an idea · Getting ready to launch · Up and running, ready to grow · Due for a rebrand |
| `branding_needs` | Branding chosen | What do you need? | Checkbox | Brand strategy · Competitor & market research · Brand audit · Not sure yet |
| `identity_needs` | Visual identity chosen | What do you need? | Checkbox | Full identity · Logo · Visual system & design language · Rebranding · Packaging · Print & collateral |
| `sku_count` | Packaging ticked | How many products? | Radio | 1–3 · 4–10 · More than 10 · Not sure |
| `social_needs` | Social media chosen | What do you need? | Checkbox | Social media audit · Social direction & content archetypes · Strategy & content |
| `platforms` | Social media chosen | Which platforms? | Checkbox | Instagram · LinkedIn · YouTube · Pinterest · Other |
| `social_mode` | Social media chosen | One-off or ongoing? | Radio | A one-off project · Ongoing, month to month · Not sure |
| `film_needs` | Film & photography chosen | What do you need? | Checkbox | Ad film / brand shoot · Creative direction & photography · Editing · Set design · Campaign & art direction |
| `shoot_location` | Film & photography chosen | Where would we shoot? | Radio | Bengaluru · Elsewhere in India · Outside India · Not sure yet |
| (note) | Only "Not sure yet" chosen | | Text | *No problem. We'll suggest a road on the call.* |

- Error message (stage): *Pick the closest one. You can explain more in a moment.*

**Screen 3: Brand**
- Heading: **Now, the brand.**

| Field | Question and help text | Type | Rules |
|---|---|---|---|
| `brandName`\* | Brand or business name *(A working title is fine.)* | Text, autofill as company name | Up to 80 characters, no web addresses |
| `brandLink` | Where can we see it? *Website or Instagram handle. Skip it if it isn't live yet.* | Text, web-address keyboard | Up to 200 characters |
| `brief`\* | What's the brief? *A few lines is plenty: what you make, who it's for, and what needs to change.* | Text box, 3 lines, grows as you type | Up to 3,000 characters |
| `references` | Anything you love, or don't? *Pinterest boards, brands you admire, a Drive folder. One link per line.* | Text box, 2 lines | Up to 10 links |
| (note) | *Got files? Reply to our email with them, or share a Drive link above.* | Text | Version 1 has no uploads (section 5.2) |

- Error messages: *Tell us the brand's name, even a working title.* · *A line or two is enough. What would you like to change?*

**Screen 4: Timing and budget**
- Heading: **Timing and budget.**

| Field | Question and help text | Type | Options |
|---|---|---|---|
| `timeline`\* | When would you like to start? | Radio | As soon as possible · In 1–3 months · In 3–6 months · Flexible, just exploring |
| `deadline` | Is there a date we're working towards? *A launch, an event, a festive season.* | Text, short | Up to 60 characters |
| `currency` | | Two-way switch: **₹ INR** / **$ USD** | Rupees if the visitor's time zone is India or their language setting is Indian English; otherwise dollars |
| `budget`\* | What budget are you working with? *A ballpark helps us shape a proposal that fits. It never changes how carefully we read your brief.* | Radio, with a way out | See the ranges below |

Budget ranges. **These are suggestions to adjust:** set the lowest range just below the minimum project size.
- **Project, in rupees:** Under ₹1 lakh · ₹1–2.5 lakh · ₹2.5–5 lakh · ₹5–10 lakh · ₹10 lakh+ · Not sure yet — guide me
- **Project, in dollars:** Under $1,500 · $1,500–3,000 · $3,000–6,000 · $6,000–12,000 · $12,000+ · Not sure yet
- **Monthly, for ongoing social media only:** Under ₹50k a month · ₹50k–1 lakh · ₹1–2 lakh · ₹2 lakh+ · Not sure yet. In dollars: under $750 · $750–1,500 · $1,500–3,000 · $3,000+ · not sure
- **For context, from the survey:**
  - FableSquare's projects start around ₹5L.
  - NOW Media quotes ₹5–25L for branding.
  - Identity Makers sells packages from ₹12k to ₹90k.
  - Kavalu's current clients suggest the lower-middle of that spread.
- **Starting-price line beside the budget question** (founder fills in): *For reference: identity projects usually start at ₹[X], and social media partnerships at ₹[Y] a month.*
- Error message: *Choose the closest range, or "Not sure yet".*

**Screen 5: You, with the finished letter**
- Heading: **Where should we reply?**

| Field | Question | Type | Rules and options |
|---|---|---|---|
| `name`\* | Your name | Text, autofill as name | Up to 60 characters, no web addresses |
| `email`\* | Email | Email field, autofill as email | Must be a valid address |
| `phone` | Phone or WhatsApp *(optional)* | Phone field with a country code (+91 by default), autofill as phone | Up to 20 characters |
| `replyVia` | Best way to reach you? | Radio | Email (default) · WhatsApp · A quick call |
| `heardFrom` | How did you find us? *(optional)* | Dropdown | Instagram · A friend or client · Behance · Google · Saw your work out in the world · Other |
| hidden | | Decoy field `website` labelled "Leave this field empty" and kept out of reach of keyboard and screen readers; signed `startToken`; invisible Turnstile; `ref` (which case study they came from); campaign tags from the link | |

- **The letter appears in full, built from the answers.** This is the review step.

  > Dear Ananya,
  > We're **{brandName}**, {stage phrase}. We'd love your help with **{roads phrase}**.
  > We're hoping to start **{timeline phrase}**{, ahead of {deadline}}, with a budget of **{budget phrase}**.
  > The short version: {first 160 characters of the brief}…
  > Write to me at {email}{, or on WhatsApp at {phone}}.
  > Warmly, {name}

  - Wording for where the brand is today:
    - just an idea → *and right now we're just an idea*
    - getting ready to launch → *and we're getting ready to launch*
    - up and running → *already up and running, and ready to grow*
    - due for a rebrand → *and we're ready for a rebrand*
  - Wording for the timeline:
    - as soon as possible → *as soon as we can*
    - in 1–3 months → *in the next one to three months*
    - in 3–6 months → *in three to six months*
    - flexible → *whenever the time is right*
  - Wording for the budget: a range → *around ₹2.5–5 lakh*; not sure → *that we'd like your advice on*.
  - Blanks not yet answered show as soft underlines.
  - In the page code, the letter comes after the questions so screen readers reach it last. It is not announced as it changes.
  - On phones it is a collapsible strip, *Your letter so far*, that opens in full on step 5.
- Small print: *We use these details only to reply to you about this project.* [Privacy]
- Button: **Send the letter**. While sending: *Sending…*. Repeat clicks are blocked.
- Error messages:
  - *Tell us what to call you.*
  - *That email looks incomplete. Check the @ and the part after it.*
  - If sending fails: *That didn't go through on our side. Your answers are saved. Try again, or email them to connect@studiokavalu.com.* [Copy my answers]

### 6.6 Branching rules

| When | What happens |
|---|---|
| A road is chosen | Its follow-up questions appear on step 2 |
| Only "Not sure yet" is chosen | Step 2 asks only where the brand is today, and the thank-you screen promises a recommendation |
| Packaging is ticked | The product-count question appears |
| Social media is the only road and it's ongoing | Budget switches to monthly ranges |
| The visitor came from a case study (`ref`) | Those roads and details are already selected, with a "Like {project}" note on the letter |
| The budget is below the minimum (lowest range) | Thank-you version B, with the starter offer |
| The timeline is "as soon as possible" | Thank-you version C |
| Film is chosen with a shoot outside India | The email to the studio is marked "travel" |
| The decoy field is filled or the form was too fast | The studio email starts with "[check]" and the client gets no automatic reply |

### 6.7 Thank-you screen
**Version A (default)**
- Envelope folds and is stamped *KAVALU · BENGALURU · 23 OCT 2026 · KAV-7Q2MD*. For visitors who have reduced motion switched on, it simply fades in.
- Heading: **Thank you, {first name}. Your letter is with Ananya.**
- Text: *A copy is on its way to {email}. Your reference is KAV-7Q2MD.*
- **What happens next**
  1. **Today:** Ananya reads your brief herself.
  2. **Within one working day:** a personal reply with first thoughts and a question or two.
  3. **A 20-minute intro call:** to understand the crossroads you're at.
  4. **Within [3] working days of the call:** a proposal with scope, timeline and fee.
  5. **Kick-off:** sign, pay the [50]% advance, and we begin on the agreed date.
- **Skip the back-and-forth: pick a time for the intro call.** The Cal.com booking sits on the page with name, email and notes filled in, and the reference passed along.
- *Prefer WhatsApp?* [Message us with your reference] · *While you wait:* [See how we shaped Nivritti →]
- Once a call is booked, the calendar is replaced by: *You're booked for {day, time}. A calendar invite is on its way.*

**Version B (budget below the minimum)**
- *Thank you for being upfront about budget. Full identity projects usually start at ₹[X].*
- *If that's a stretch right now, a [Brand Audit] is a strong first step. And if we're not the right fit, we'll happily point you to people who are.*
- The starter-offer button replaces the calendar. A smaller link to book a call stays.

**Version C (as soon as possible)**
- Adds: *Tight timeline noted. We'll check the calendar today and tell you honestly whether we can do it well.*

**Version D (not sure which road)**
- Adds: *We'll suggest a road on the call. Bring whatever you have: decks, photos, half-formed ideas.*

### 6.8 Automatic reply to the client
- **From:** Ananya at Studio Kavalu \<hello@mail.studiokavalu.com\> (a sub-address of the domain, set up in Resend)
- **Reply-to:** connect@studiokavalu.com
- **Subject:** Your brief is with us, {first name}. Alternative: *Your letter reached the crossroads, {first name}*
- **Preview line:** *What happens next, and a link to book your intro call.*

> Hi {first name},
>
> Thank you for choosing your road with Studio Kavalu. Your brief has reached me, and I read every one myself.
>
> **What happens next**
> 1. I'll reply within one working day (Monday to Friday, IST) with first thoughts and any questions.
> 2. If you haven't booked yet, pick a time for a 20-minute intro call: **[Book a time]**
> 3. After we talk, you'll get a clear proposal, covering scope, timeline and fee, within [three] working days.
>
> **While you wait**
> - Gather what you already have: logo files, decks, product photos, anything you love or can't stand.
> - See how we work, from first conversation to final files: **[Working with Studio Kavalu]**
> - Prefer WhatsApp? **[Message us]** and mention **KAV-7Q2MD**.
>
> Your brief at a glance: {roads} · {timeline} · {budget range}
>
> Speak soon,
> Ananya
> Founder, Studio Kavalu
> *A brand is a set of choices. We make them with you.*
> studiokavalu.com · Instagram
>
> <small>You're receiving this because a brief was sent from studiokavalu.com with this address. If that wasn't you, please ignore this email.</small>

**Rule:** the email only repeats the fixed answer labels and a cleaned-up first name. It never repeats the brief, the brand name or any links the visitor typed.

### 6.9 Notification to the studio (connect@)
- **Subject:** `New brief · {brand} · {roads} · {budget} · {timeline}`, starting with `[check]` if flagged. It can be sorted at a glance in Gmail.
- **Reply-to:** the client, so pressing Reply in Gmail answers them directly.
- **Body:**
  - every answer, in a table;
  - their links;
  - a "WhatsApp {name}" button (`wa.me/{phone}`);
  - when it was sent (IST);
  - where they came from (case study, campaign tags);
  - the currency they chose;
  - the spam checks: Turnstile passed, decoy field empty, time taken.

### 6.10 Welcome guide outline ("Working with Studio Kavalu")
1. **How we work:** Listen → Map → Make → Launch, drawn as a road.
2. **What we need from you:** existing files, access, one person who makes decisions.
3. **Typical timelines** for each service.
4. **Fees and payment:** [50]% advance, the rest before final files. GST applies. International clients are invoiced in dollars.
5. **Feedback and changes:** how many rounds are included.
6. **Keeping in touch:** Ananya is your contact. WhatsApp for quick things, email for approvals.
7. **FAQ**

### 6.11 What sits around the form
- **How it works (three steps):** as on screen 0.
- **FAQ:** six questions.
  - What does a project cost?
  - How long does it take?
  - Do you work with clients outside India? (Yes: invoices in dollars and calls across time zones.)
  - Can you take on a small project?
  - What do you need from me to start?
  - How do payments work?
- **One testimonial** beside the form. Nivritti's or Studio Anokhi's founder would suit.
- **Contact strip:** connect@studiokavalu.com · WhatsApp · Instagram · Bengaluru, with the live local time from the design direction.

### 6.12 Build checklist
- [ ] **Structure:** each step is a section with a heading. Each question is a `fieldset` with a `legend`. Chips are real checkboxes or radio buttons with labels.
- [ ] **Chips:** at least 44px tall, wrap onto new lines, show a tick and bolder text when selected, have at least 3:1 contrast and a visible focus ring, and work in Windows high-contrast mode.
- [ ] **"Not sure yet":** stays a checkbox, but choosing it clears the other roads, and screen readers are told.
- [ ] **Changing steps:**
  - update the web address (`?step=2`) so the browser's Back button works;
  - move focus to the new step's heading;
  - have screen readers announce "Step 2 of 5" politely.
- [ ] **Errors:**
  - check each field when the visitor leaves it, and the whole step on Continue;
  - when a step fails, list the errors at the top, linked to each field, and move focus to the first one;
  - tie each message to its field so screen readers read it.
- [ ] **Fields:**
  - text at least 16px;
  - email and phone fields set as such, with autofill hints for name, email, phone and company;
  - a web-address keyboard for links;
  - no placeholder text used as a label.
- [ ] **Button bar:** fixed at the bottom and kept above the phone keyboard.
- [ ] **Saving and resuming:**
  - answers saved on the device, so a visitor who leaves can resume;
  - the save is written so a blocked or failed save never breaks the page;
  - the saved draft is cleared once the brief is sent.
- [ ] **Turnstile:** set to invisible or managed, loaded on step 5 and run at Send, because its check expires after 300 seconds.
- [ ] **Reduced motion:** for visitors who have it switched on, no drawing road and no folding envelope; a simple fade instead.
- [ ] **Measurement:** track flow started, each step viewed and completed, sent, sending errors, call booked (Cal.com reports bookings), WhatsApp clicks and email clicks. Use privacy-friendly analytics.

---

## 7. What the founder must set up

**Accounts and settings**
1. **Resend (free).**
   - Add the sending address domain, `mail.studiokavalu.com` (or `send.`).
   - Ask whoever manages the domain to add the records Resend shows (SPF and DKIM, plus one for bounced mail).
   - Add a DMARC record to the main domain if it has none.
   - Create an API key.
   - Using a separate sending address leaves connect@'s existing email setup untouched.
2. **Cloudflare (free).** Create a Turnstile widget for studiokavalu.com and the preview addresses (up to 10 per widget). This gives a public site key and a secret key.
3. **Cal.com (free).**
   - Choose a username.
   - Connect Google Calendar and Google Meet.
   - Create "Intro call · 20 min" with:
     - working hours in IST;
     - breaks between calls;
     - at least 24 hours' notice;
     - a daily limit on calls.
   - Add three booking questions for people who skip the brief: brand, road, budget range.
4. **Google Sheet** called "Briefs", with the Apps Script web app published and a shared password (section 5.3).
5. **WhatsApp Business app** on the studio number, with a business profile and greeting and away messages.
6. **Hosting:** Vercel Pro ($20 a month), because Hobby forbids commercial use, or Netlify.
7. **Pages:** a privacy policy, and the welcome guide (a Notion page or PDF).
8. **Later:** Razorpay, which needs PAN, bank details and GST if registered, and takes a few days to approve. Used for Payment Links and an optional starter-offer page. PayPal if international clients need it.

**Settings the developer needs (environment variables)**
```
RESEND_API_KEY=
BRIEF_TO_EMAIL=connect@studiokavalu.com
BRIEF_FROM_EMAIL="Ananya at Studio Kavalu <hello@mail.studiokavalu.com>"
NEXT_PUBLIC_TURNSTILE_SITE_KEY=
TURNSTILE_SECRET_KEY=
FORM_SIGNING_SECRET=            # long random string, signs the start time
SHEETS_WEBHOOK_URL=             # Apps Script web app URL
SHEETS_WEBHOOK_SECRET=          # same value as the script's SECRET property
NEXT_PUBLIC_CAL_LINK=studiokavalu/intro-call
NEXT_PUBLIC_WHATSAPP_NUMBER=91XXXXXXXXXX
# later / optional
NEXT_PUBLIC_RAZORPAY_AUDIT_URL=
BLOB_READ_WRITE_TOKEN=          # only if browser uploads to Vercel Blob are added
```

**Decisions and content only the founder can provide**
- The minimum project size and "starts at" price for each service, and the budget ranges (rupees, dollars, and monthly for retainers).
- The reply promise (one working day?), working days and hours, and an away banner for holidays.
- Whether to show "now booking from [month]", and remembering to update it every month.
- How soon a proposal follows the call, the advance percentage, and how many rounds of changes are included.
- One to three testimonials, with permission. Answers to the six FAQs.
- Whether to offer a starter service (a brand audit or social media audit), and its price.
- The privacy notice. India's data protection rules (the DPDP Act) require notice and consent from around May 2027 [57]. Write it now.

---

## 8. Sources
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

## 9. Appendix: what could not be verified
- **Locomotive:** Cloudflare's bot check refused both WebFetch and curl (403), so it is listed but not described.
- **Ueno's old project planner:** the Wayback Machine blocked requests (too many requests or bot detection). Only the current Ueno contact page was checked.
- **Forms whose fields could not be read** because they only render in JavaScript or sit in a third-party tool: Fantasy, Tenet, Davey & Krista, Paige Brunton, Jess Creatives (Dubsado) and NOW Media's estimator. Their surrounding copy was read.
- **Pricing pages that contradict themselves:**
  - Typeform: the plan cards and comparison table show different monthly prices.
  - Formspree: monthly prices of $15/$30/$90 in the text, $10/$20/$60 in the grids.
  - Razorpay: a 0.2% fee for Payment Pages and Buttons, but also "no extra cost".
  - Cal.com: routing is shown under Teams on the pricing page, but the routing page quotes $37 per person a month.
- **The HBR figures** (about 7 times and 60 times) are as the article is widely summarised. The full text is behind a paywall.
- **The SEOmoz 2009 CAPTCHA test** figures come from secondary write-ups, which disagree on whether it covered one site or 50.
- **WhatsApp user numbers for India** are secondary estimates, so no figure is relied on here.
- **Netlify's commercial use:** confirmed by its support forum, not by its terms page.
