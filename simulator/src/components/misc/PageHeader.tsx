import React from "react";
import { TypeAnimation } from "react-type-animation";

export const PageHeader = () => {
  return (
    <div className="flex flex-col items-center justify-center">
      {/* Logo */}
      <img src="/logo.png" alt="logo" />

      {/* Title */}
      <div className="font-rationale font-bold text-[42px] text-center">
        <div>[SC2079]</div>
        <div>Multi-Disciplinary Design Project</div>
      </div>

      {/* Subtitle */}
      <TypeAnimation
        sequence={[
          "A Real-time Robotic Car System...",
          1000, // wait 1s
          "A Real-time Robotic Car System that autonomously tranverse a known area.",
          1000,
          "A Real-time Robotic Car System that detects images with image recognition.",
          1000,
          "A Real-time Robotic Car System that avoids obstacles intelligently.",
          1000,
          "A Real-time Robotic Car System that transmits and receive control signals from a mobile device.",
          1000,
          "A Real-time Robotic Car System that simulates physical robot and algorithms in software.",
          1000,
        ]}
        wrapper="span"
        speed={75}
        className="font-rationale text-[24px] text-center"
        repeat={Infinity}
      />
    </div>
  );
};
