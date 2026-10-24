import type { ServiceKey } from "./types";

/*
 * "Choose your road": the start-a-project flow. Everything Ananya may want to change lives here.
 * Values marked DECIDE are placeholders that only she can set (prices, promises, ranges).
 * Flow and copy follow research/onboarding_research.md, section 6.
 */

export type RoadKey = ServiceKey | "unsure";

export const settings = {
  /** DECIDE: show "Now booking projects from {month}." Leave empty to hide. */
  bookingFrom: "",
  /** DECIDE: "Identity projects usually start at {x}". Leave empty to hide. */
  identityFrom: "",
  /** DECIDE: "social media partnerships at {y} a month". Leave empty to hide. */
  socialFrom: "",
  /** DECIDE: working days to send a proposal after the call. */
  proposalDays: 3,
  /** DECIDE: advance taken at kick-off, in %. */
  advance: 50,
  /** Promise shown after sending. */
  replyPromise: "within one working day",
};

export const roads: { key: RoadKey; title: string; help: string }[] = [
  { key: "branding", title: "Branding", help: "Strategy, research, audits; what the brand says" },
  { key: "identity", title: "Visual identity", help: "Logo, systems, packaging, print; how it looks" },
  { key: "social", title: "Social media", help: "Audits, direction, content; where it shows up" },
  { key: "film", title: "Film & photography", help: "Shoots, ad films, art direction; who it speaks to" },
  { key: "unsure", title: "Not sure yet", help: "Help me choose" },
];

export const stages = [
  { key: "idea", label: "Just an idea", phrase: "and right now we're just an idea" },
  { key: "launch", label: "Getting ready to launch", phrase: "and we're getting ready to launch" },
  { key: "running", label: "Up and running, ready to grow", phrase: "already up and running, and ready to grow" },
  { key: "rebrand", label: "Due for a rebrand", phrase: "and we're ready for a rebrand" },
] as const;

export const needs: Record<ServiceKey, string[]> = {
  branding: ["Brand strategy", "Competitor & market research", "Brand audit", "Not sure yet"],
  identity: ["Full identity", "Logo", "Visual system & design language", "Rebranding", "Packaging", "Print & collateral"],
  social: ["Social media audit", "Social direction & content archetypes", "Strategy & content"],
  film: ["Ad film / brand shoot", "Creative direction & photography", "Editing", "Set design", "Campaign & art direction"],
};

export const skuCounts = ["1–3", "4–10", "More than 10", "Not sure"];
export const platforms = ["Instagram", "LinkedIn", "YouTube", "Pinterest", "Other"];
export const socialModes = [
  { key: "oneoff", label: "A one-off project" },
  { key: "ongoing", label: "Ongoing, month to month" },
  { key: "unsure", label: "Not sure" },
];
export const shootLocations = ["Bengaluru", "Elsewhere in India", "Outside India", "Not sure yet"];

export const timelines = [
  { key: "asap", label: "As soon as possible", phrase: "as soon as we can" },
  { key: "1-3", label: "In 1–3 months", phrase: "in the next one to three months" },
  { key: "3-6", label: "In 3–6 months", phrase: "in three to six months" },
  { key: "flexible", label: "Flexible, just exploring", phrase: "whenever the time is right" },
] as const;

export type Currency = "INR" | "USD";

/** DECIDE: set the lowest range just below the studio's minimum project size. */
export const budgets: Record<"project" | "monthly", Record<Currency, string[]>> = {
  project: {
    INR: ["Under ₹1 lakh", "₹1–2.5 lakh", "₹2.5–5 lakh", "₹5–10 lakh", "₹10 lakh+"],
    USD: ["Under $1,500", "$1,500–3,000", "$3,000–6,000", "$6,000–12,000", "$12,000+"],
  },
  monthly: {
    INR: ["Under ₹50k a month", "₹50k–1 lakh a month", "₹1–2 lakh a month", "₹2 lakh+ a month"],
    USD: ["Under $750 a month", "$750–1,500 a month", "$1,500–3,000 a month", "$3,000+ a month"],
  },
};
export const BUDGET_UNSURE = "Not sure yet, guide me";

export const replyVia = ["Email", "WhatsApp", "A quick call"];
export const heardFrom = ["Instagram", "A friend or client", "Behance", "Google", "Saw your work out in the world", "Other"];

export const steps = [
  { key: "road", label: "Road" },
  { key: "details", label: "Details" },
  { key: "brand", label: "Brand" },
  { key: "timing", label: "Timing & budget" },
  { key: "you", label: "You" },
] as const;

export type Answers = {
  roads: RoadKey[];
  stage: string;
  needs: Partial<Record<ServiceKey, string[]>>;
  skuCount: string;
  platforms: string[];
  socialMode: string;
  shootLocation: string;
  brandName: string;
  brandLink: string;
  brief: string;
  references: string;
  timeline: string;
  deadline: string;
  currency: Currency;
  budget: string;
  name: string;
  email: string;
  phone: string;
  replyVia: string;
  heardFrom: string;
  /** honeypot: must stay empty */
  website: string;
  /** which page or case study they came from */
  ref: string;
};

export const emptyAnswers = (road?: RoadKey, currency: Currency = "INR"): Answers => ({
  roads: road ? [road] : [],
  stage: "",
  needs: {},
  skuCount: "",
  platforms: [],
  socialMode: "",
  shootLocation: "",
  brandName: "",
  brandLink: "",
  brief: "",
  references: "",
  timeline: "",
  deadline: "",
  currency,
  budget: "",
  name: "",
  email: "",
  phone: "",
  replyVia: "Email",
  heardFrom: "",
  website: "",
  ref: "",
});

export const isMonthly = (a: Pick<Answers, "roads" | "socialMode">) =>
  a.roads.length === 1 && a.roads[0] === "social" && a.socialMode === "ongoing";

export function roadsPhrase(keys: RoadKey[]) {
  const names = keys.filter((k) => k !== "unsure").map((k) => roads.find((r) => r.key === k)!.title.toLowerCase());
  if (!names.length) return "finding the right road";
  if (names.length === 1) return names[0];
  return `${names.slice(0, -1).join(", ")} and ${names[names.length - 1]}`;
}
