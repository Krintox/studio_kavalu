import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ViewTransition } from "react";
import { CaseStudy } from "@/components/work/CaseStudy";
import { getProject, projects } from "@/content/projects";
import { site } from "@/content/site";

export const dynamicParams = false;

export function generateStaticParams() {
  return projects.map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const p = getProject(slug);
  if (!p) return {};
  // A shared link shows the project's own cover when it is sharp and wide enough for the 1.91:1 frame social
  // sites crop to; a portrait or a placeholder would be cut badly, so those show the site's card
  // (app/opengraph-image.jpg, made by research/tools/og_card.py). Named here because a page that sets
  // its own openGraph no longer inherits the card from the root.
  const wide = !p.cover.placeholder && p.cover.w / p.cover.h >= 1.6;
  const images = wide
    ? [{ url: p.cover.src, width: p.cover.w, height: p.cover.h, alt: p.cover.alt }]
    : [{ url: "/opengraph-image.jpg", width: 1200, height: 630, alt: site.cardAlt }];
  return {
    title: p.title,
    description: p.summary,
    openGraph: { title: `${p.title} · Studio Kavalu`, description: p.summary, images },
    twitter: { card: "summary_large_image", images },
  };
}

export default async function ProjectPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const project = getProject(slug);
  if (!project) notFound();
  const i = projects.indexOf(project);
  const next = projects[(i + 1) % projects.length];
  return (
    <ViewTransition enter="page-in" exit="page-out" default="none">
      <div>
        <CaseStudy project={project} next={next} />
      </div>
    </ViewTransition>
  );
}
