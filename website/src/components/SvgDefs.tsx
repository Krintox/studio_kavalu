/** Shared SVG filters, referenced from CSS as filter: url("#duo-plum") etc. */
export function SvgDefs() {
  return (
    <svg width="0" height="0" aria-hidden="true" focusable="false" style={{ position: "absolute" }}>
      <defs>
        {/* deep plum shadows -> powder blue highlights */}
        <filter id="duo-plum" colorInterpolationFilters="sRGB">
          <feColorMatrix
            type="matrix"
            values="0.30 0.59 0.11 0 0  0.30 0.59 0.11 0 0  0.30 0.59 0.11 0 0  0 0 0 1 0"
          />
          <feComponentTransfer>
            <feFuncR type="table" tableValues="0.153 0.671" />
            <feFuncG type="table" tableValues="0.024 0.804" />
            <feFuncB type="table" tableValues="0.090 0.839" />
          </feComponentTransfer>
        </filter>
        {/* the intro's fast frames: a plum duotone held between deep plum (relative luminance 0.006) and
            #7A4A5E (0.098). No change between two frames can reach WCAG 2.3.1's 10% "general flash", at any
            size or speed, and nothing in it is a saturated red. */}
        <filter id="kv-reel" colorInterpolationFilters="sRGB">
          <feColorMatrix
            type="matrix"
            values="0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 1 0"
          />
          <feComponentTransfer>
            <feFuncR type="table" tableValues="0.153 0.478" />
            <feFuncG type="table" tableValues="0.024 0.290" />
            <feFuncB type="table" tableValues="0.090 0.369" />
          </feComponentTransfer>
        </filter>
      </defs>
    </svg>
  );
}
