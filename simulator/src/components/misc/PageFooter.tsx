import React from "react";
import { FaGithub } from "react-icons/fa";

export const PageFooter = () => {
  return (
    <footer className="flex justify-center gap-2">
      <div>&copy; AY23/24 Sem 2 Group XI</div>
      <div>|</div>
      <a
        href="https://github.com/xJQx/SC2079-MDP-Group11-Algorithms"
        target="_blank"
        rel="noopener noreferrer"
        className="hover:text-black cursor-pointer"
      >
        <FaGithub className="w-[24px] h-[24px]" />
      </a>
    </footer>
  );
};
