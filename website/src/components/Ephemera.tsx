import type { CSSProperties, ReactNode } from "react";

/** A steel paper clip, drawn as one stroke so it reads at any size. */
export function PaperClip({ className, style }: { className?: string; style?: CSSProperties }) {
  return (
    <svg className={className} style={style} viewBox="0 0 24 64" fill="none" aria-hidden="true">
      <path
        d="M8 20v28a6 6 0 0 0 12 0V12a8.5 8.5 0 0 0-17 0v36a10 10 0 0 0 20 0V22"
        style={{ stroke: "var(--steel)" }}
        strokeWidth="2.2"
        strokeLinecap="round"
      />
      <path d="M8 20v28a6 6 0 0 0 12 0V12" style={{ stroke: "var(--steel-light)" }} strokeWidth="0.8" strokeLinecap="round" opacity="0.8" />
    </svg>
  );
}

/** A round sticker with text running around its edge. */
export function Sticker({
  text,
  children,
  size = 132,
  className,
  style,
  tone = "plum",
}: {
  text: string;
  children?: ReactNode;
  size?: number;
  className?: string;
  style?: CSSProperties;
  tone?: "plum" | "blue" | "cream";
}) {
  const colors = {
    plum: { bg: "var(--plum)", fg: "var(--cream)" },
    // a blue sticker on a blue ground turns plum, so it never disappears into its page (styles/surfaces.css)
    blue: { bg: "var(--blue-object, var(--blue))", fg: "var(--blue-object-ink, var(--plum))" },
    cream: { bg: "var(--cream)", fg: "var(--plum)" },
  }[tone];
  // one ring path per sticker: two stickers on a page must not share an id
  const ring = `ring-${tone}-${size}`;
  return (
    <span
      className={className}
      style={{ display: "block", width: size, height: size, ...style }}
      role="img"
      aria-label={text.replace(/·/g, ",")}
    >
      <svg viewBox="0 0 200 200" width="100%" height="100%" aria-hidden="true" style={{ overflow: "visible" }}>
        <defs>
          <path id={ring} d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0" />
        </defs>
        <circle cx="100" cy="100" r="98" style={{ fill: colors.bg, filter: "drop-shadow(0 6px 10px rgb(39 6 23 / .25))" }} />
        <circle cx="100" cy="100" r="88" fill="none" style={{ stroke: colors.fg }} strokeOpacity="0.35" strokeWidth="1" />
        {/* sized to the ring: the studio line runs 461 of its 465 units in Courier Prime, so the closing
            "·" lands just before the start (browsers ignore textLength on textPath) */}
        <text style={{ fill: colors.fg, fontFamily: "var(--f-mono)", fontSize: 14.5, letterSpacing: 2, textTransform: "uppercase" }}>
          <textPath href={`#${ring}`} startOffset="0">
            {text}
          </textPath>
        </text>
        <foreignObject x="45" y="45" width="110" height="110">
          <div
            style={{
              width: "100%",
              height: "100%",
              display: "grid",
              placeItems: "center",
              color: colors.fg,
              textAlign: "center",
            }}
          >
            {children}
          </div>
        </foreignObject>
      </svg>
    </span>
  );
}
