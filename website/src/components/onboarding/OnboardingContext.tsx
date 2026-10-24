"use client";

import { createContext, useCallback, useContext, useMemo, useState, type MouseEvent, type ReactNode } from "react";
import type { RoadKey } from "@/content/onboarding";

type State = { open: boolean; roads: RoadKey[]; step: number; ref: string; session: number };
type Ctx = State & { start: (road?: RoadKey | RoadKey[], opts?: { step?: number; ref?: string }) => void; close: () => void };

const OnboardingContext = createContext<Ctx>({
  open: false,
  roads: [],
  step: 0,
  ref: "",
  session: 0,
  start: () => {},
  close: () => {},
});
export const useOnboarding = () => useContext(OnboardingContext);

export function OnboardingProvider({ children, drawer }: { children: ReactNode; drawer: ReactNode }) {
  const [state, setState] = useState<State>({ open: false, roads: [], step: 0, ref: "", session: 0 });
  const start = useCallback((road?: RoadKey | RoadKey[], opts?: { step?: number; ref?: string }) => {
    const roads = road === undefined ? [] : Array.isArray(road) ? road : [road];
    setState((s) => ({ open: true, roads, step: opts?.step ?? 0, ref: opts?.ref ?? "", session: s.session + 1 }));
  }, []);
  const close = useCallback(() => setState((s) => ({ ...s, open: false })), []);
  const value = useMemo(() => ({ ...state, start, close }), [state, start, close]);
  return (
    <OnboardingContext.Provider value={value}>
      {children}
      {drawer}
    </OnboardingContext.Provider>
  );
}

/**
 * A real link to /start (so it works without JavaScript and can be opened in a new tab)
 * that opens the onboarding drawer in place when clicked normally.
 */
export function StartLink({
  road,
  from,
  className,
  children,
  "aria-label": ariaLabel,
}: {
  road?: RoadKey;
  /** where the visitor started from, e.g. a case study slug */
  from?: string;
  className?: string;
  children: ReactNode;
  "aria-label"?: string;
}) {
  const { start } = useOnboarding();
  const params = new URLSearchParams();
  if (road) params.set("road", road);
  if (from) params.set("ref", from);
  const href = params.size ? `/start?${params}` : "/start";
  const onClick = (e: MouseEvent<HTMLAnchorElement>) => {
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
    e.preventDefault();
    start(road, { ref: from });
  };
  return (
    <a href={href} className={className} onClick={onClick} aria-label={ariaLabel}>
      {children}
    </a>
  );
}
