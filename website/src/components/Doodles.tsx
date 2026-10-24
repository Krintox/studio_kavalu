import type { ServiceKey } from "@/content/types";

// Line doodles for the four roads, after the icons on the studio's first site:
// a clipboard (branding), the pen tool (identity), a film canister (social), a camera (film & photo).
const common = {
  fill: "none",
  stroke: "currentColor",
  strokeWidth: 1.6,
  strokeLinecap: "round" as const,
  strokeLinejoin: "round" as const,
};

export function Doodle({ name, className }: { name: ServiceKey; className?: string }) {
  return (
    <svg viewBox="0 0 64 64" className={className} aria-hidden="true">
      {name === "branding" && (
        <g {...common}>
          <rect x="14" y="12" width="36" height="44" rx="3" />
          <path d="M25 12v-3h14v3" />
          <rect x="23" y="8" width="18" height="7" rx="2" fill="var(--doodle-fill, transparent)" />
          <path d="M21 26h22M21 33h22M21 40h14" />
          <path d="M40 44l3 3 6-7" />
        </g>
      )}
      {name === "identity" && (
        <g {...common}>
          <path d="M32 10l10 14-10 22-10-22z" />
          <circle cx="32" cy="27" r="3" />
          <path d="M32 30v16" />
          <path d="M26 46h12v6H26z" />
          <path d="M8 30c8-10 16-14 24-14M56 30c-8-10-16-14-24-14" strokeDasharray="2 3" />
          <rect x="5" y="28" width="5" height="5" />
          <rect x="54" y="28" width="5" height="5" />
        </g>
      )}
      {name === "social" && (
        <g {...common}>
          <rect x="10" y="18" width="24" height="32" rx="4" />
          <path d="M10 26h24M10 42h24" />
          <path d="M34 28h14a6 6 0 0 1 0 12H34" />
          <path d="M40 28v12M46 28v12" strokeDasharray="1.5 3" />
          <path d="M18 12h8v6h-8z" />
        </g>
      )}
      {name === "film" && (
        <g {...common}>
          <rect x="8" y="22" width="48" height="30" rx="4" />
          <path d="M22 22l4-7h12l4 7" />
          <circle cx="32" cy="37" r="9" />
          <circle cx="32" cy="37" r="4" />
          <path d="M14 28h5" />
          <path d="M46 13l2 3 3-1-1 3 3 2-3 1 1 3-3-1-2 3" />
        </g>
      )}
    </svg>
  );
}
