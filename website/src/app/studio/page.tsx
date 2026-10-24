import type { Metadata } from "next";
import { ViewTransition } from "react";
import { Doodle } from "@/components/Doodles";
import { ChooseRoad } from "@/components/home/ChooseRoad";
import { Founder } from "@/components/home/Founder";
import { StartLink } from "@/components/onboarding/OnboardingContext";
import { Process } from "@/components/studio/Process";
import { ground, sheet } from "@/lib/surfaces";
import styles from "@/components/studio/Studio.module.css";
import { services, site } from "@/content/site";

export const metadata: Metadata = {
  title: "Studio",
  description: `${site.about} Founded by Ananya in ${site.city}.`,
};

// confirm: proposed answers, to be checked and completed by Ananya.
const faq = [
  {
    q: "Where are you based?",
    a: `In ${site.city}. We work with brands across India and further away; most of a project happens over calls, shared boards and, when the work needs it, a shoot day.`,
  },
  {
    q: "Do you only take on full rebrands?",
    a: "No. Some projects need all four roads, some need one. Many start with a brand audit or a social direction and grow from there.",
  },
  {
    q: "Do you work with brands that are just an idea?",
    a: "Yes. The first conversation is about where you are standing today, whether that is a name and a notebook or a business that has outgrown its look.",
  },
  {
    q: "How do we start?",
    a: "Choose your road: five short steps, about three minutes. Ananya reads every brief herself and replies personally.",
  },
];

export default function StudioPage() {
  return (
    <ViewTransition enter="page-in" exit="page-out" default="none">
      <div>
        <section className={styles.hero} {...ground("studioHero")}>
          <div className="container" {...sheet("studioHero")}>
            <p className="eyebrow">The studio</p>
            <div className={styles.word}>
              <span lang="kn" className={styles.kn}>
                {site.word}
              </span>
              <span className={styles.say}>/{site.say}/ · Kannada · noun</span>
            </div>
            <p className={styles.definition}>{site.definition[0].toUpperCase() + site.definition.slice(1)}</p>
            <div className={styles.intro}>
              <p className={styles.lead}>{site.manifesto}</p>
              <div className={styles.introBody}>
                <p>{site.about}</p>
                <p>{site.aim}</p>
              </div>
            </div>
          </div>
        </section>

        <section className={styles.roads} {...ground("studioRoads")} aria-labelledby="studio-roads">
          <div className="container">
            <p className="eyebrow">What we do</p>
            <h2 id="studio-roads" className={styles.h2}>
              The four <em>roads.</em>
            </h2>
            <ol className={styles.roadList}>
              {services.map((s, k) => (
                <li key={s.key} className={styles.road}>
                  <div className={styles.roadHead}>
                    <span className={styles.roadNo}>{String(k + 1).padStart(2, "0")}</span>
                    <Doodle name={s.key} className={styles.roadDoodle} />
                  </div>
                  <div>
                    <p className={styles.roadChoice}>{s.choice}</p>
                    <h3 className={styles.roadTitle}>{s.title}</h3>
                    <p className={styles.roadLine}>{s.line}</p>
                  </div>
                  <ul className={styles.roadItems}>
                    {s.items.map((it) => (
                      <li key={it}>{it}</li>
                    ))}
                  </ul>
                  <StartLink road={s.key} className={styles.roadStart}>
                    Start here →
                  </StartLink>
                </li>
              ))}
            </ol>
          </div>
        </section>

        <Process />

        <Founder link={false} />

        <section className={styles.faq} {...ground("faq")} aria-labelledby="faq-title">
          <div className="container" {...sheet("faq")}>
            <p className="eyebrow">Questions</p>
            <h2 id="faq-title" className={styles.h2}>
              Before you <em>ask.</em>
            </h2>
            <div className={styles.faqList}>
              {faq.map((f) => (
                <details key={f.q} className={styles.qa}>
                  <summary>{f.q}</summary>
                  <p>{f.a}</p>
                </details>
              ))}
            </div>
          </div>
        </section>

        <ChooseRoad />
      </div>
    </ViewTransition>
  );
}
