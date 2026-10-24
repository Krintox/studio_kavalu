import Link from "next/link";
import { ground } from "@/lib/surfaces";

export default function NotFound() {
  return (
    <section
      {...ground("notFound")}
      style={{ minHeight: "80vh", display: "grid", alignContent: "center", padding: "calc(var(--nav-h) + 3rem) 0 4rem" }}
    >
      <div className="container" style={{ display: "grid", gap: "1.4rem", maxWidth: "52rem" }}>
        <p className="eyebrow">404 · off the map</p>
        <h1 className="display" style={{ fontSize: "var(--t-1)" }}>
          This road <em>isn&apos;t on the map.</em>
        </h1>
        <p style={{ color: "var(--on-soft)", maxWidth: "30rem" }}>
          The page you were after has moved, or never existed. Every road from here leads somewhere good:
        </p>
        <p style={{ display: "flex", gap: "1.25rem", flexWrap: "wrap", fontSize: "1.05rem" }}>
          <Link href="/" style={{ borderBottom: "1px solid currentColor", color: "var(--on-strong)" }}>
            Back to the crossroads
          </Link>
          <Link href="/work" style={{ borderBottom: "1px solid currentColor", color: "var(--on-strong)" }}>
            See the work
          </Link>
          <Link href="/start" style={{ borderBottom: "1px solid currentColor", color: "var(--on-strong)" }}>
            Start a project
          </Link>
        </p>
      </div>
    </section>
  );
}
