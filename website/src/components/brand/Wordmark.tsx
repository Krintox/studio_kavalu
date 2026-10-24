import type { CSSProperties, SVGProps } from "react";
import { KAVALU, MARK, STUDIO, type Glyph } from "./wordmark-paths";

/*
 * Studio Kavalu's logotype, redrawn from Ananya's own lettering (see research/brand/wordmark_fit).
 * Proportions of the lockup are measured from her site's header: mark = 2.91 caps tall, words start
 * 0.46 caps after it and 0.35 caps down, line gap 0.19 caps, KAVALU indented 0.30 caps, and the words
 * set about 3.5% narrower than the stretched footer version.
 */

const WORDS = { STUDIO, KAVALU };

type WordProps = Omit<SVGProps<SVGSVGElement>, "viewBox"> & {
  word: keyof typeof WORDS;
  /** Class put on every letter's <path>, e.g. for per-letter motion. */
  glyphClassName?: string;
};

/** One word of the logotype, letters as separate paths (data-glyph="S"...). Colour = currentColor. */
export function Word({ word, glyphClassName, ...rest }: WordProps) {
  const w = WORDS[word];
  return (
    <svg viewBox={`0 0 ${w.width} ${w.height}`} fill="currentColor" aria-hidden="true" focusable="false" {...rest}>
      {w.glyphs.map((g: Glyph, i: number) => (
        <path key={i} d={g.d} fillRule="evenodd" data-glyph={g.letter} className={glyphClassName} />
      ))}
    </svg>
  );
}

/** The K mark: a rounded square whose cream negative spaces draw the K. */
export function LogoMark(props: Omit<SVGProps<SVGSVGElement>, "viewBox">) {
  return (
    <svg viewBox={`0 0 ${MARK.width} ${MARK.height}`} fill="currentColor" aria-hidden="true" focusable="false" {...props}>
      <path d={MARK.d} fillRule="evenodd" />
    </svg>
  );
}

// lockup geometry, cap height = 100
const CAP = 100;
const MARK_H = 2.91 * CAP;
const MARK_W = (MARK.width / MARK.height) * MARK_H;
const SX = 0.965;
const WX = MARK_W + 0.46 * CAP;
const STUDIO_Y = 0.35 * CAP;
const KAVALU_Y = STUDIO_Y + CAP + 0.19 * CAP;
const KAVALU_X = WX + 0.3 * CAP;
const LOCKUP_W = Math.max(WX + STUDIO.width * SX, KAVALU_X + KAVALU.width * SX);

/** Horizontal lockup: mark + STUDIO / KAVALU stacked, as on her current site. */
export function LogoLockup({ className, style, title = "Studio Kavalu" }: { className?: string; style?: CSSProperties; title?: string }) {
  const m = MARK_H / MARK.height;
  return (
    <svg
      viewBox={`0 0 ${LOCKUP_W.toFixed(1)} ${MARK_H.toFixed(1)}`}
      fill="currentColor"
      role="img"
      aria-label={title}
      className={className}
      style={style}
    >
      <path d={MARK.d} fillRule="evenodd" transform={`scale(${m.toFixed(4)})`} />
      <g transform={`translate(${WX.toFixed(1)} ${STUDIO_Y}) scale(${SX} 1)`}>
        {STUDIO.glyphs.map((g, i) => (
          <path key={i} d={g.d} fillRule="evenodd" />
        ))}
      </g>
      <g transform={`translate(${KAVALU_X.toFixed(1)} ${KAVALU_Y}) scale(${SX} 1)`}>
        {KAVALU.glyphs.map((g, i) => (
          <path key={i} d={g.d} fillRule="evenodd" />
        ))}
      </g>
    </svg>
  );
}

export const LOCKUP_ASPECT = LOCKUP_W / MARK_H;
