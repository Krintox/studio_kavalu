import type { Metadata } from "next";
import { ViewTransition } from "react";
import { WorkIndex } from "@/components/work/WorkIndex";
import { projects } from "@/content/projects";
import { ground } from "@/lib/surfaces";
import styles from "./work.module.css";

export const metadata: Metadata = {
  title: "Work",
  description: "Identity, packaging, social and shoots by Studio Kavalu: every project, as stamps or as an index.",
};

export default function WorkPage() {
  return (
    <ViewTransition enter="page-in" exit="page-out" default="none">
      <section className={styles.page} {...ground("work")}>
        <div className="container">
          <header className={styles.head}>
            <p className="eyebrow">The album · {String(projects.length).padStart(2, "0")} projects</p>
            <h1 className={styles.title}>
              Work, <em>stamped</em> and filed.
            </h1>
            <p className={styles.lede}>
              Identities, packaging, feeds and shoots. Filter by the road a project took, or switch to the index for a quicker
              read.
            </p>
          </header>
          <WorkIndex projects={projects} />
        </div>
      </section>
    </ViewTransition>
  );
}
