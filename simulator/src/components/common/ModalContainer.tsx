import React from "react";
import { FaTimes } from "react-icons/fa";

interface ModalContainerProps {
  title: string;
  children: React.ReactNode;
  onClose: () => void;
}

export const ModalContainer = (props: ModalContainerProps) => {
  const { title, children, onClose } = props;

  return (
    <div className="fixed inset-0 flex flex-col items-center justify-center z-50">
      {/* Blur Background */}
      <div
        className="fixed inset-0 bg-black opacity-30 z-40"
        onClick={onClose}
      />

      {/* Modal */}
      <div className="relative flex flex-col items-center bg-orange-200 w-full max-w-[350px] p-[24px] rounded-[8px] shadow-card overflow-auto z-50">
        {/* Close Icon */}
        <FaTimes
          className="absolute right-4 top-4 size-5 text-brand-text cursor-pointer"
          onClick={onClose}
        />

        {/* Title */}
        <div className="w-full text-center font-rationale font-bold underline text-[24px] mb-4">
          {title}
        </div>

        {/* Body */}
        <div className="text-brand-text w-full">{children}</div>
      </div>
    </div>
  );
};
