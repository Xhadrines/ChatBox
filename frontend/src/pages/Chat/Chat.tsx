import React, { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../../components/Header/Header";
import "./Chat.css";

type Message = {
  sender: "user" | "bot";
  text: string;
  fileUrl?: string;
  llmUsed?: string;
};

const Chat: React.FC = () => {
  const navigate = useNavigate();

  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [gptOssRemaining, setGptOssRemaining] = useState<number>(0);

  const [showUpgradeModal, setShowUpgradeModal] = useState(false);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [inputText, setInputText] = useState("");

  const [modalType, setModalType] = useState<"chat" | "file" | null>(null);

  const logActivity = async (messagesSent = 0, filesUploaded = 0) => {
    const currentUser = JSON.parse(localStorage.getItem("user") || "{}");
    const userId = currentUser.id;
    if (!userId) return;

    try {
      const apiUrl = import.meta.env.VITE_CHAT_API;

      if (messagesSent > 0 || filesUploaded > 0) {
        await fetch(`${apiUrl}/api/user-usage/log-user-activity/${userId}/`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          credentials: "include",
          body: JSON.stringify({
            messages_sent: messagesSent,
            files_uploaded: filesUploaded,
          }),
        });
      } else {
        console.log(`Would log ${messagesSent} messages for user ${userId}`);
      }
    } catch (err) {
      console.error("Error logging activity:", err);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("user");
    navigate("/login", { replace: true });
  };

  const sendMessage = async () => {
    if (inputText.trim() === "" || isLoading) return;

    const userMessage = inputText;
    setMessages((prev) => [...prev, { sender: "user", text: userMessage }]);
    setInputText("");
    setIsLoading(true);

    const currentUser = JSON.parse(localStorage.getItem("user") || "{}");
    const userId = currentUser.id;
    if (!userId) return;

    setMessages((prev) => [
      ...prev,
      { sender: "bot", text: "Se generează răspunsul..." },
    ]);

    try {
      const apiUrl = import.meta.env.VITE_CHAT_API;

      const response = await fetch(`${apiUrl}/api/chat/${userId}/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          model: "gpt-oss",
          prompt: userMessage,
        }),
      });

      const data = await response.json();

      if (data.gpt_oss_remaining !== null && data.gpt_oss_remaining === 0) {
        showModalOncePerDay(data.active_plan_id, "chat");
      }

      setGptOssRemaining(data.gpt_oss_remaining);

      setMessages((prev) =>
        prev.map((msg, i) =>
          i === prev.length - 1 && msg.sender === "bot"
            ? { sender: "bot", text: data.response, llmUsed: data.llm_used }
            : msg
        )
      );
      await logActivity(1, 0);
    } catch (error) {
      console.error("Error sending message:", error);
      setMessages((prev) =>
        prev.map((msg, i) =>
          i === prev.length - 1 && msg.sender === "bot"
            ? { sender: "bot", text: "Eroare de conexiune." }
            : msg
        )
      );
    } finally {
      setIsLoading(false);
    }
  };

  const handleAttach = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files) return;
    const file = e.target.files[0];

    const allowedExtensions = ["pdf", "txt"];
    const fileExt = file.name.split(".").pop()?.toLowerCase();
    if (!fileExt || !allowedExtensions.includes(fileExt)) {
      alert("Doar fișiere PDF și TXT sunt acceptate!");
      return;
    }

    const currentUser = JSON.parse(localStorage.getItem("user") || "{}");
    const userId = currentUser.id;
    if (!userId) return;

    const formData = new FormData();
    formData.append("file", file);
    formData.append("user", userId.toString());

    try {
      const apiUrl = import.meta.env.VITE_CHAT_API;
      const response = await fetch(`${apiUrl}/api/files/upload-file/`, {
        method: "POST",
        body: formData,
        credentials: "include",
      });

      let data: any = {};
      try {
        data = await response.json();
      } catch (err) {
        console.warn("Nu s-a putut parsa JSON-ul:", err);
      }

      const reachedLimit =
        data.daily_file_limit !== null &&
        data.uploaded_today >= data.daily_file_limit;

      if (!response.ok || reachedLimit) {
        showModalOncePerDay(data.active_plan_id || "unknown", "file");
        if (!response.ok) {
          console.error("Upload failed:", data);
        }
        return;
      }

      await logActivity(0, 1);

      const fileUrl = `${apiUrl}${data.file_url}`;
      console.log("fileUrl generat:", fileUrl);

      if (fileExt === "txt") {
        try {
          const txtResp = await fetch(
            `${apiUrl}/api/files/read-txt/${data.id}/`,
            { credentials: "include" }
          );
          const txtData = await txtResp.json();
          setMessages((prev) => [
            ...prev,
            { sender: "user", text: txtData.content },
          ]);
        } catch (err) {
          console.error("Error reading txt file:", err);
        }
      } else {
        setMessages((prev) => [
          ...prev,
          { sender: "user", text: data.file_name, fileUrl },
        ]);
      }
    } catch (err) {
      console.error(err);
      showModalOncePerDay("unknown", "file");
    }
  };

  useEffect(() => {
    const fetchMessages = async () => {
      const currentUser = JSON.parse(localStorage.getItem("user") || "{}");
      const userId = currentUser.id;
      if (!userId) return;

      try {
        const apiUrl = import.meta.env.VITE_CHAT_API;
        const response = await fetch(`${apiUrl}/api/chat/events/${userId}/`, {
          method: "GET",
          headers: { "Content-Type": "application/json" },
          credentials: "include",
        });

        if (!response.ok) return;

        const data = await response.json();
        console.log("Mesaje GET API:", data);
        const formattedMessages: Message[] = [];

        data.forEach((event: any) => {
          if (event.type === "message") {
            formattedMessages.push({ sender: "user", text: event.text });
            if (event.llm_resp) {
              formattedMessages.push({
                sender: "bot",
                text: event.llm_resp,
                llmUsed: event.llm_used,
              });
            }
          } else if (event.type === "file") {
            formattedMessages.push({
              sender: "user",
              text: event.file_name,
              fileUrl: `${import.meta.env.VITE_CHAT_API}${event.file_url}`,
            });
          }
        });

        setMessages(formattedMessages);
      } catch (err) {
        console.error("Error fetching messages:", err);
      }
    };

    fetchMessages();
  }, []);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const showModalOncePerDay = (planId: string, type: "chat" | "file") => {
    const today = new Date().toISOString().split("T")[0];
    const modalData = localStorage.getItem("upgrade_modal_data");

    let lastShown = null;
    let lastPlanId = null;

    if (modalData) {
      try {
        const parsed = JSON.parse(modalData);
        lastShown = parsed.date;
        lastPlanId = parsed.planId;
      } catch {}
    }

    if (lastShown !== today || lastPlanId !== planId) {
      setShowUpgradeModal(true);
      setModalType(type);
      localStorage.setItem(
        "upgrade_modal_data",
        JSON.stringify({ date: today, planId })
      );
    }
  };

  return (
    <div className="chat-page">
      <Header
        title="ChatBox"
        dropdownItems={[
          {
            label: "Profil",
            value: "profile",
            icon: "/user.png",
            onClick: () => navigate("/profile"),
          },
          {
            label: "Logout",
            value: "logout",
            icon: "/logout.png",
            onClick: handleLogout,
          },
          {
            label: "Dashboard",
            value: "dashboard",
            icon: "/dashboard.png",
            onClick: () => navigate("/admin-dashboard"),
          },
        ]}
      />

      <div className="chat-body">
        <div className="messages">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.sender === "user" ? "user" : "bot"}`}
            >
              {msg.fileUrl ? (
                <a href={msg.fileUrl} target="_blank" rel="noopener noreferrer">
                  {msg.text}
                </a>
              ) : (
                <>
                  <span>{msg.text}</span>
                  {msg.sender === "bot" && msg.llmUsed && (
                    <small className="llm-label">{msg.llmUsed}</small>
                  )}
                </>
              )}
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        <div className="chat-input-container">
          <div className="input-wrapper">
            <textarea
              placeholder="Scrie un mesaj..."
              disabled={isLoading}
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyDown={handleKeyDown}
              rows={1}
            />
            <div className="chat-buttons">
              <button className="attach-button">
                <label htmlFor="file-input">
                  <img src="/attach.png" alt="Attach" />
                </label>
                <input
                  id="file-input"
                  type="file"
                  style={{ display: "none" }}
                  onChange={handleAttach}
                />
              </button>
              <button className="send-button" onClick={sendMessage}>
                <img src="/send.png" alt="Send" />
              </button>
            </div>
          </div>
        </div>
      </div>

      {showUpgradeModal && (
        <div className="modal-backdrop">
          <div className="modal-content">
            <p>
              {modalType === "chat"
                ? "Ai terminat mesajele premium GPT-OSS. Pentru a trimite mai multe, upgradează abonamentul."
                : modalType === "file"
                ? "Ai atins limita zilnică de fișiere. Pentru a încărca mai multe, upgradează abonamentul."
                : ""}
            </p>
            <div className="modal-buttons">
              <button
                className="modal-btn-close"
                onClick={() => setShowUpgradeModal(false)}
              >
                Închide
              </button>
              <button
                className="modal-btn-upgrade"
                onClick={() => {
                  setShowUpgradeModal(false);
                  navigate("/profile");
                }}
              >
                Upgrade
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chat;
