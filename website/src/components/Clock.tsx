"use client";

import { useEffect, useState } from "react";
import { site } from "@/content/site";

/** Bengaluru local time. Renders a neutral placeholder on the server so hydration never mismatches. */
export function Clock({ className, city = true }: { className?: string; city?: boolean }) {
  const [now, setNow] = useState<string | null>(null);

  useEffect(() => {
    const fmt = new Intl.DateTimeFormat("en-GB", { hour: "2-digit", minute: "2-digit", timeZone: site.timeZone });
    const tick = () => setNow(fmt.format(new Date()));
    tick();
    const id = window.setInterval(tick, 15_000);
    return () => window.clearInterval(id);
  }, []);

  return (
    <span className={className}>
      {city ? `${site.city} ` : null}
      <time suppressHydrationWarning>{now ?? "--:--"}</time> IST
    </span>
  );
}
