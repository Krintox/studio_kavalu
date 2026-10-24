import type { MetadataRoute } from "next";

const url = process.env.NEXT_PUBLIC_SITE_URL ?? "https://studiokavalu.com";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [{ userAgent: "*", allow: "/", disallow: ["/api/"] }],
    sitemap: `${url}/sitemap.xml`,
  };
}
