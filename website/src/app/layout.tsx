import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";
import { Cursor } from "@/components/Cursor";
import { Footer } from "@/components/Footer";
import { GroundSheet } from "@/components/GroundSheet";
import { SmoothScroll } from "@/components/motion/SmoothScroll";
import { Nav } from "@/components/Nav";
import { OnboardingDrawer } from "@/components/onboarding/OnboardingDrawer";
import { OnboardingProvider } from "@/components/onboarding/OnboardingContext";
import { SvgDefs } from "@/components/SvgDefs";
import { site } from "@/content/site";
import { introScript } from "@/lib/intro";
import { fontVars } from "./fonts";
import "./globals.css";

const url = process.env.NEXT_PUBLIC_SITE_URL ?? "https://studiokavalu.com";

export const metadata: Metadata = {
  metadataBase: new URL(url),
  title: { default: "Studio Kavalu by Ananya · Branding & content house, Bengaluru", template: "%s · Studio Kavalu" },
  description: `${site.manifesto} ${site.about}`,
  openGraph: {
    type: "website",
    siteName: "Studio Kavalu",
    title: "Studio Kavalu by Ananya",
    description: "Every brand hits a crossroads. We help you choose the road.",
    locale: "en_IN",
  },
  twitter: { card: "summary_large_image" },
};

export const viewport: Viewport = {
  themeColor: "#f3f3e7",
  colorScheme: "light",
};

const orgLd = {
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  name: "Studio Kavalu",
  alternateName: "ಸ್ಟುಡಿಯೋ ಕವಲು",
  description: site.about,
  email: site.email,
  url,
  founder: { "@type": "Person", name: site.founder.name },
  address: { "@type": "PostalAddress", addressLocality: site.city, addressCountry: "IN" },
  areaServed: "Worldwide",
  knowsAbout: ["Brand strategy", "Visual identity", "Packaging", "Social media", "Photography", "Brand film"],
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en-IN" className={fontVars} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: introScript }} />
      </head>
      <body>
        <a className="skip-link" href="#main">
          Skip to content
        </a>
        <SvgDefs />
        <SmoothScroll>
          <OnboardingProvider drawer={<OnboardingDrawer />}>
            <Nav />
            <main id="main">{children}</main>
            <Footer />
          </OnboardingProvider>
        </SmoothScroll>
        <Cursor />
        <GroundSheet />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(orgLd) }} />
      </body>
    </html>
  );
}
