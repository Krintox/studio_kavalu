import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ViewTransition } from "react";
import { CaseStudy } from "@/components/work/CaseStudy";
import { getProject, projects } from "@/content/projects";

export const dynamicParams = false;

export function generateStaticParams() {
  return projects.map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const p = getProject(slug);
  if (!p) return {};
  return {
    title: p.title,
    description: p.summary,
    openGraph: { title: `${p.title} · Studio Kavalu`, description: p.summary, images: [{ url: p.cover.src }] },
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
