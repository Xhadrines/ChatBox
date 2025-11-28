import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../../components/Header/Header";
import "./Register.css";

const Register: React.FC = () => {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    if (password !== confirmPassword) {
      setError("Parolele nu coincid");
      return;
    }

    const apiUrl = import.meta.env.VITE_CHAT_API;

    try {
      const response = await fetch(`${apiUrl}/api/register/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email, password }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.error || "Eroare la înregistrare");
      } else {
        setSuccess("Cont creat cu succes! Redirecționare la login...");

        setTimeout(() => navigate("/login", { replace: true }), 1000);
      }
    } catch (err) {
      console.error("Eroare la conectarea cu serverul:", err);
      setError("Eroare la conectarea cu serverul");
    }
  };

  return (
    <div className="page-container">
      <Header title="ChatBox" showBackButton={true} backUrl="/" />
      <div className="body-container">
        <form className="register-form" onSubmit={handleRegister}>
          <h2>Register</h2>

          {error && <p className="error-message">{error}</p>}
          {success && <p className="success-message">{success}</p>}

          <div className="form-row">
            <label>Username:</label>
            <input
              type="text"
              placeholder="Introduce username-ul"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="form-row">
            <label>Email:</label>
            <input
              type="email"
              placeholder="Introduce email-ul"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="form-row">
            <label>Password:</label>
            <input
              type="password"
              placeholder="Introduce parola"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <div className="form-row">
            <label>Confirm Password:</label>
            <input
              type="password"
              placeholder="Confirmă parola"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </div>

          <div className="form-row">
            <button type="submit" className="register-button">
              Register
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Register;
