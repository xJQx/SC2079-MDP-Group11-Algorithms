import React, { useState } from "react";
import { Button } from "../../common";
import { HiOutlineStatusOnline, HiOutlineStatusOffline } from "react-icons/hi";
import toast from "react-hot-toast";
import useFetch from "../../../hooks/useFetch";

export const ServerStatus = () => {
  const [isServerOnline, setIsServerOnline] = useState(false);
  const fetch = useFetch();

  const checkServerOnlineStatus = async () => {
    // TODO: Fetch from backend to see if backend is running
    try {
      const isServerOnline: boolean = await fetch.get("/is-server-online");

      if (isServerOnline) {
        setIsServerOnline(true);
        toast.success("Server online!");
      }
    } catch (e) {
    } finally {
      setIsServerOnline(false);
      toast.error("Server offline!");
    }
  };

  return (
    <div className="mt-2 mb-4 flex justify-center items-center">
      <Button
        title="Check Server Status"
        className={`${
          isServerOnline
            ? "!text-green-500 hover:!text-green-600"
            : "!text-rose-500 hover:!text-rose-600"
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
