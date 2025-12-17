import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Header from "../../components/Header/Header";
import "./Login.css";

const Login: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [messageType, setMessageType] = useState<"error" | "success" | "info">(
    "info"
  );
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setMessage("");

    const apiUrl = import.meta.env.VITE_CHAT_API;

    try {
      const response = await fetch(`${apiUrl}/api/login/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.error || "Eroare la login");
        setMessageType("error");
        return;
      }

      localStorage.setItem("user", JSON.stringify(data.user));
      localStorage.setItem("token", data.token);

      try {
        const planResponse = await fetch(
          `${apiUrl}/api/user-plans/user-active-plan/${data.user.id}/`
        );
        const planData = await planResponse.json();

        if (planResponse.ok && planData.active_plan) {
          localStorage.setItem(
            "activePlan",
            JSON.stringify(planData.active_plan)
          );
          setMessage("Login reușit! Plan activ încărcat.");
          setMessageType("success");
        } else {
          console.warn("Nu există plan activ");
          localStorage.removeItem("activePlan");
          setMessage("Login reușit! Nu există plan activ.");
          setMessageType("info");
        }
      } catch (err) {
        console.error("Eroare la fetch plan activ:", err);
        localStorage.removeItem("activePlan");
        setMessage("Login reușit! Nu s-a putut încărca planul activ.");
        setMessageType("info");
      }

      setTimeout(() => navigate("/chat"), 1200);
    } catch (err) {
      console.error("Eroare la conectarea cu serverul:", err);
      setMessage("Eroare la conectarea cu serverul");
      setMessageType("error");
    }
  };

  return (
    <div className="page-container">
      <Header title="ChatBox" />
      <div className="body-container">
        <form className="login-form" onSubmit={handleLogin}>
          <h2>Login</h2>

          {message && <div className={`message ${messageType}`}>{message}</div>}

          <div className="form-row">
            <label>Email:</label>
            <input
              type="email"
              placeholder="Introduce email-ul"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div className="form-row">
            <label>Password:</label>
            <input
              type="password"
              placeholder="Introduce parola"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <div className="form-row">
            <button type="submit" className="login-button">
              Login
            </button>
          </div>

          <p style={{ textAlign: "center", marginTop: "12px" }}>
            Nu ai cont?{" "}
            <Link to="/register" className="signup-link">
              Crează unul
            </Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Login;
