import React from "react";

interface ButtonProps
  extends React.DetailedHTMLProps<
    React.HTMLAttributes<HTMLDivElement>,
    HTMLDivElement
  > {
  children: React.ReactNode;
}

export const Button = (props: ButtonProps) => {
  const { children, ...divProps } = props;
  return (
    <div
      className="w-max flex items-center gap-2 px-2 py-1 bg-orange-900 rounded font-bold text-white text-[14px] shadow-lg hover:text-orange-300 cursor-pointer"
      {...divProps}
    >
      {children}
    </div>
  );
};
