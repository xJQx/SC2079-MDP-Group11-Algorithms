import React from "react";
import { PageFooter } from "./PageFooter";
import { PageHeader } from "./PageHeader";

interface LayoutProps {
  children: React.ReactNode;
}

export const Layout = (props: LayoutProps) => {
  const { children } = props;

  return (
    <div className="p-4 min-h-[100vh] bg-gradient-to-b from-orange-100 to-orange-200 text-orange-900 flex flex-col">
      {/* Header */}
      <PageHeader />

      {/* Body */}
      <main className="flex-1">{children}</main>

      {/* Footer */}
      <PageFooter />
    </div>
  );
};
