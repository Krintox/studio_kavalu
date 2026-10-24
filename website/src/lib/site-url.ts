/*
 * The site's public address, used for absolute links (social previews, sitemap, robots).
 * Order: NEXT_PUBLIC_SITE_URL (set it when the real domain is live), then the address Vercel serves this
 * project from (so previews work before the domain exists), then the intended domain.
 */
const vercel = process.env.VERCEL_PROJECT_PRODUCTION_URL;

export const siteUrl = process.env.NEXT_PUBLIC_SITE_URL ?? (vercel ? `https://${vercel}` : "https://studiokavalu.com");
