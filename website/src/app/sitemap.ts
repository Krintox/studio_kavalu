import { siteUrl } from "@/lib/site-url";
import type { MetadataRoute } from "next";
import { projects } from "@/content/projects";

const url = siteUrl;

export default function sitemap(): MetadataRoute.Sitemap {
  const pages = ["", "/work", "/studio", "/start"].map((p) => ({
    url: `${url}${p}`,
    changeFrequency: "monthly" as const,
    priority: p === "" ? 1 : 0.8,
  }));
  const work = projects.map((p) => ({
    url: `${url}/work/${p.slug}`,
    changeFrequency: "yearly" as const,
    priority: p.kind === "case-study" ? 0.7 : 0.4,
  }));
  return [...pages, ...work];
}
