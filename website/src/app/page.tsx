import { Album } from "@/components/home/Album";
import { ChooseRoad } from "@/components/home/ChooseRoad";
import { Founder } from "@/components/home/Founder";
import { Hero } from "@/components/home/Hero";
import { Intro } from "@/components/home/Intro";
import { Manifesto } from "@/components/home/Manifesto";
import { Roads } from "@/components/home/Roads";
import { Spreads } from "@/components/home/Spreads";
import { ViewTransition } from "react";

export default function Home() {
  return (
    <ViewTransition enter="page-in" exit="page-out" default="none">
      <div>
        <Intro />
        <Hero />
        <Spreads />
        <Manifesto />
        <Album />
        <Roads />
        <Founder />
        <ChooseRoad />
      </div>
    </ViewTransition>
  );
}
