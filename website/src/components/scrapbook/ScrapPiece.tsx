import Image from "next/image";
import type { CSSProperties } from "react";
import { PaperClip } from "@/components/Ephemera";
import type { ScrapItem } from "@/content/types";
import styles from "./ScrapPiece.module.css";

export function ScrapPiece({
  item,
  width,
  sizes = "280px",
  style,
  className,
}: {
  item: ScrapItem;
  width?: number | string;
  sizes?: string;
  style?: CSSProperties;
  className?: string;
}) {
  const w = typeof width === "number" ? `${width}px` : width;
  const cls = [styles.piece, className].filter(Boolean).join(" ");

  if (item.kind === "image") {
    const fix = item.fix ?? "tape";
    return (
      <figure className={`${cls} ${styles.image} ${styles[`fix_${fix}`]}`} style={{ width: w, ...style }}>
        {fix === "clip" ? <PaperClip className={styles.clip} /> : null}
        {fix === "pin" ? <span className={styles.pin} aria-hidden="true" /> : null}
        <div className={styles.paper}>
          <div className={styles.window} style={{ aspectRatio: `${item.w} / ${item.h}` }}>
            <Image src={item.src} alt={item.alt} width={item.w} height={item.h} sizes={sizes} draggable={false} />
          </div>
        </div>
        {item.caption || item.credit ? (
          <figcaption className={styles.caption}>
            {item.caption}
            {item.credit ? <span className={styles.credit}> · {item.credit}</span> : null}
          </figcaption>
        ) : null}
      </figure>
    );
  }

  if (item.kind === "note") {
    return (
      <blockquote className={`${cls} ${styles.note} ${styles[`paper_${item.paper}`]}`} style={{ width: w, ...style }}>
        <p className="hand" data-written>
          {item.text}
        </p>
        {item.by ? <footer className={styles.by}>— {item.by}</footer> : null}
      </blockquote>
    );
  }

  if (item.kind === "swatch") {
    return (
      <div className={`${cls} ${styles.swatch}`} style={{ width: w, ...style }}>
        <span className={styles.chip} style={{ background: item.hex }} />
        <span className={styles.swatchName}>{item.name}</span>
        <span className={styles.swatchHex}>{item.hex}</span>
      </div>
    );
  }

  return (
    <div className={`${cls} ${styles.word}`} style={style} lang={item.script === "kn" ? "kn" : undefined}>
      <span className={item.script === "kn" ? styles.wordKn : styles.wordEn}>{item.text}</span>
    </div>
  );
}
