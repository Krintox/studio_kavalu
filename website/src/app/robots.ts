import { siteUrl } from "@/lib/site-url";
import type { MetadataRoute } from "next";

const url = siteUrl;

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [{ userAgent: "*", allow: "/", disallow: ["/api/"] }],
    sitemap: `${url}/sitemap.xml`,
  };
}
