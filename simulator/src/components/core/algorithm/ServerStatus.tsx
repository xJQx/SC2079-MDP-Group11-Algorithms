import React, { useState } from "react";
import { Button } from "../../common";
import { HiOutlineStatusOnline, HiOutlineStatusOffline } from "react-icons/hi";
import toast from "react-hot-toast";

export const ServerStatus = () => {
  const [isServerOnline, setIsServerOnline] = useState(false);

  const checkServerOnlineStatus = () => {
    // TODO: Connect to backend to see if backend is running
    if (isServerOnline) {
      toast.error("Server offline!");
    } else {
      toast.success("Server online!");
    }
    setIsServerOnline((prev) => !prev);
  };

  return (
    <div className="mt-2 mb-4 flex justify-center items-center">
      <Button
        title="Check Server Status"
        className={`${
          isServerOnline
            ? "text-green-500 hover:text-green-600"
            : "text-rose-500 hover:text-rose-600"
        }`}
        onClick={checkServerOnlineStatus}
      >
        <span>Server Status - {isServerOnline ? "Online" : "Offline"}</span>
        {isServerOnline ? (
          <HiOutlineStatusOnline className="text-[18px] animate-pulse" />
        ) : (
          <HiOutlineStatusOffline className="text-[18px]" />
        )}
      </Button>
    </div>
  );
};
