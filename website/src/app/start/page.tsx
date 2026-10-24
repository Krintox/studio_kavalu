import type { Metadata } from "next";
import { RoadForm } from "@/components/onboarding/RoadForm";
import { roads, type RoadKey } from "@/content/onboarding";
import { ground, sheet } from "@/lib/surfaces";

export const metadata: Metadata = {
  title: "Start a project",
  description: "Choose your road: five short steps, about three minutes, read by Ananya personally.",
};

export default async function StartPage({ searchParams }: { searchParams: Promise<Record<string, string | string[] | undefined>> }) {
  const sp = await searchParams;
  const road = typeof sp.road === "string" && roads.some((r) => r.key === sp.road) ? (sp.road as RoadKey) : undefined;
  const from = typeof sp.ref === "string" ? sp.ref.slice(0, 60) : "";
  return (
    <section {...ground("start")} style={{ padding: "calc(var(--nav-h) + clamp(2rem, 6vh, 4rem)) 0 clamp(4rem, 10vh, 7rem)" }}>
      <div className="container" {...sheet("start")}>
        <RoadForm layout="page" initialRoads={road ? [road] : []} from={from} />
      </div>
    </section>
  );
}
