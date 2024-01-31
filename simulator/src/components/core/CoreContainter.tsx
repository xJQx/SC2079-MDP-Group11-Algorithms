import React from "react";

interface CoreContainterProps {
  title: string;
  children: React.ReactNode;
}

export const CoreContainter = (props: CoreContainterProps) => {
  const { title, children } = props;

  return (
    <div className="flex flex-col justify-center items-center my-6">
      <div className="font-bold text-[24px] mb-2">- {title} -</div>
      <div>{children}</div>
    </div>
  );
};
