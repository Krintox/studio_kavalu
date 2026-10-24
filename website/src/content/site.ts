import type { Service } from "./types";

// Copy marked "confirm" is proposed wording, not something Ananya has said or signed off.
export const site = {
  name: "Studio Kavalu",
  byline: "by Ananya",
  kannada: "ಸ್ಟುಡಿಯೋ ಕವಲು",
  word: "ಕವಲು",
  say: "ka·va·lu",
  definition: "a crossroads; a point where paths meet, split, and become something new.",
  headline: ["Every brand hits a", "crossroads.", "We help you choose the", "road."],
  manifesto: "A brand is a set of choices; what it says, how it looks, where it shows up, who it speaks to.",
  about:
    "Studio Kavalu is a branding and content house that makes these choices with you. We shape brands, feeds and persona through a design lens backed with strategy.",
  aim: "The aim: work with a point of view clear enough that people recognise it, and others follow it.",
  founder: {
    name: "Ananya",
    role: "Founder",
    // [before, the emphasised word, after]: the quote is set with one italic word
    quote: ["I don’t design things. I design the", "story", "that holds them together."],
    // confirm: placeholder bio until Ananya sends hers.
    bio: [
      "Ananya started Studio Kavalu to give growing brands one place where strategy, identity, social and the camera are decided together.",
    ],
  },
  email: "connect@studiokavalu.com",
  city: "Bengaluru",
  country: "India",
  timeZone: "Asia/Kolkata",
  // Leave empty to hide. Fill in when known.
  instagram: "",
  whatsapp: "", // digits only with country code, e.g. 919800000000
  booking: "", // e.g. https://cal.com/studiokavalu/intro
};

export const services: Service[] = [
  {
    key: "branding",
    choice: "What it says",
    title: "Branding",
    line: "Who you are, who you are for, and the reasons people should care.", // confirm
    items: ["Brand strategy", "Competitor and market research", "Brand audit", "Visual identity"],
    tone: "cream",
  },
  {
    key: "identity",
    choice: "How it looks",
    title: "Visual identity",
    line: "One visual language, from the logo down to the last label.", // confirm
    items: [
      "Full identity design",
      "Logo design",
      "Visual systems and design language",
      "Rebranding",
      "Packaging",
      "Print and physical collaterals",
    ],
    tone: "blue",
  },
  {
    key: "social",
    choice: "Where it shows up",
    title: "Social media",
    line: "Feeds with a point of view, built on archetypes rather than trends.", // confirm
    items: ["Social media audit", "Socials direction and content archetype", "Strategy and social content"],
    tone: "cream",
  },
  {
    key: "film",
    choice: "Who it speaks to",
    title: "Film & photography",
    line: "Shoots and films directed end to end, from the set to the final cut.", // confirm
    items: [
      "Ad films / brand shoots",
      "Creative direction and photography",
      "Editing and captions",
      "Set design",
      "Campaigns and art direction",
    ],
    tone: "blue",
  },
];

// confirm: a proposed way of describing the studio's process.
export const process = [
  { step: "Listen", text: "A first conversation, an audit of where the brand stands, and the people it needs to reach." },
  { step: "Map", text: "Strategy and direction: we lay out the possible roads and choose one together." },
  { step: "Make", text: "Identity, packaging, content and shoots, designed as one system." },
  { step: "Launch", text: "Guidelines, files and a plan for the feed, so the brand keeps its point of view." },
];
