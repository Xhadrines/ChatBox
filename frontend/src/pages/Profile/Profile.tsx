import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import Header from "../../components/Header/Header";
import "./Profile.css";

interface User {
  id: number;
  username: string;
  email: string;
  role: string;
  role_name: string;
  status: string;
  status_name: string;
  created_at: string;
  updated_at: string;
  last_login: string | null;
}

interface UserPlans {
  id: number;
  plan: string;
  plan_name: string;
  start_date: string;
  end_date: string | null;
}

interface Plan {
  id: number;
  name: string;
  price: string;
  type: number;
  type_name: string;
  duration_days: number | null;
  name_llm_prm: string;
  daily_prm_msg: number | null;
  name_llm_std: string;
  daily_std_msg: number | null;
  daily_file_limit: number | null;
  created_at: string;
  updated_at: string;
}

const Profile: React.FC = () => {
  const [user, setUser] = useState<User | null>(null);
  const [plan, setPlan] = useState<UserPlans | null>(null);
  const [plansList, setPlansList] = useState<Plan[]>([]);
  const [showModal, setShowModal] = useState(false);
  const [message, setMessage] = useState<string>("");
  const [messageType, setMessageType] = useState<"error" | "success" | "info">(
    "info"
  );
  const [usageData, setUsageData] = useState<any[]>([]);

  const navigate = useNavigate();
  const apiUrl = import.meta.env.VITE_CHAT_API;

  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    const storedPlan = localStorage.getItem("activePlan");

    if (!storedUser) {
      navigate("/login");
      return;
    }

    const parsedUser = JSON.parse(storedUser);
    setUser(parsedUser);
    if (storedPlan) setPlan(JSON.parse(storedPlan));

    fetchActivePlan(parsedUser.id).then((activePlan) => {
      if (activePlan) {
        console.log("Plan activ încărcat:", activePlan.plan_name);
      }
    });

    fetchUserUsage(parsedUser.id);
  }, [navigate]);

  const fetchUserUsage = async (userId: number) => {
    try {
      const res = await fetch(`${apiUrl}/api/user-usage/user/${userId}/`);
      if (!res.ok) return;
      const data = await res.json();

      const chartData = data
        .map((u: any) => ({
          date: u.date,
          messages: u.messages_sent,
          files: u.files_uploaded,
        }))
        .sort(
          (a: any, b: any) =>
            new Date(a.date).getTime() - new Date(b.date).getTime()
        );

      setUsageData(chartData);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchPlans = async () => {
    try {
      const response = await fetch(`${apiUrl}/api/plans/`);
      const data = await response.json();
      if (response.ok) setPlansList(data);
      else console.error("Nu s-au putut încărca planurile");
    } catch (err) {
      console.error("Eroare la fetch planuri:", err);
    }
  };

  const handleChangePlanClick = () => {
    fetchPlans();
    setShowModal(true);
  };

  const handleSelectPlan = async (selectedPlanId: number) => {
    if (!user) return;

    try {
      const response = await fetch(
        `${apiUrl}/api/user-plans/change-user-plan/${user.id}/`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ plan_id: selectedPlanId }),
        }
      );
      const data = await response.json();

      if (response.ok && data.active_plan) {
        setPlan(data.active_plan);
        localStorage.setItem("activePlan", JSON.stringify(data.active_plan));

        fetchActivePlan(user.id);
        setMessage("Planul a fost schimbat cu succes!");
        setMessageType("success");
        setShowModal(false);
      } else {
        setMessage("Nu s-a putut schimba planul.");
        setMessageType("error");
      }
    } catch (err) {
      console.error("Eroare la schimbarea planului:", err);
      setMessage("Eroare la schimbarea planului");
      setMessageType("error");
    }
  };

  const fetchActivePlan = async (userId: number) => {
    try {
      const res = await fetch(
        `${apiUrl}/api/user-plans/user-active-plan/${userId}/`
      );
      console.log(res);
      if (!res.ok) return null;
      const data = await res.json();
      if (data.active_plan) {
        setPlan(data.active_plan);
        localStorage.setItem("activePlan", JSON.stringify(data.active_plan));
        return data.active_plan;
      }
      return null;
    } catch (err) {
      console.error("Eroare la fetch plan activ:", err);
      return null;
    }
  };

  return (
    <div className="page-container">
      <Header title="ChatBox" showBackButton={true} backUrl="/chat" />
      <div className="body-container">
        <div className="profile-card">
          <h2>Profilul tău</h2>

          {message && <div className={`message ${messageType}`}>{message}</div>}

          {user && (
            <div className="profile-info">
              <p>
                <strong>Nume utilizator:</strong> {user.username}
              </p>
              <p>
                <strong>Email:</strong> {user.email}
              </p>
              <p>
                <strong>Rol:</strong> {user.role_name}
              </p>
              <p>
                <strong>Status:</strong> {user.status_name}
              </p>
              <p>
                <strong>Ultima logare:</strong>{" "}
                {user.last_login
                  ? new Date(user.last_login).toLocaleString("ro-RO")
                  : "Nu există"}
              </p>
              <p>
                <strong>Creat la:</strong>{" "}
                {new Date(user.created_at).toLocaleString("ro-RO")}
              </p>
              <p>
                <strong>Actualizat la:</strong>{" "}
                {new Date(user.updated_at).toLocaleString("ro-RO")}
              </p>
              <hr />
              {plan ? (
                <>
                  <p>
                    <strong>Plan activ:</strong> {plan.plan_name}
                  </p>
                  <p>
                    <strong>Început:</strong>{" "}
                    {new Date(plan.start_date).toLocaleDateString("ro-RO")}
                  </p>
                  <p>
                    <strong>Expiră:</strong>{" "}
                    {plan.end_date
                      ? new Date(plan.end_date).toLocaleDateString("ro-RO")
                      : "Nelimitat"}
                  </p>
                  <div className="button-bottom-center">
                    <button
                      onClick={handleChangePlanClick}
                      className="change-plan-button"
                    >
                      Schimbă planul
                    </button>
                  </div>
                </>
              ) : (
                <p>Nu există plan activ</p>
              )}
            </div>
          )}
        </div>

        {usageData.length > 0 && (
          <div className="chart-card">
            <h3>Mesaje și fișiere încărcate</h3>
            <div className="chart-container">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={usageData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="date" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="messages" stroke="#8884d8" />
                  <Line type="monotone" dataKey="files" stroke="#82ca9d" />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>
        )}
      </div>

      {showModal && (
        <div className="modal-overlay" onClick={() => setShowModal(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <h3>Selectează un plan</h3>
            <ul className="plans-grid">
              {plansList.map((p) => (
                <li key={p.id} className="plan-card">
                  <h4>{p.name}</h4>
                  <p className="price">{p.price} EUR</p>
                  <div className="plan-details">
                    <p>
                      <strong>Tip:</strong> {p.type_name}
                    </p>
                    {p.duration_days && (
                      <p>
                        <strong>Durată:</strong> {p.duration_days} zile
                      </p>
                    )}
                    <p>
                      <strong>LLM Premium:</strong> {p.name_llm_prm}
                    </p>
                    <p>
                      <strong>Mesaje premium/zi:</strong>{" "}
                      {p.daily_prm_msg ?? "Nelimitat"}
                    </p>
                    <p>
                      <strong>LLM Standard:</strong> {p.name_llm_std}
                    </p>
                    <p>
                      <strong>Mesaje standard/zi:</strong>{" "}
                      {p.daily_std_msg ?? "Nelimitat"}
                    </p>
                    <p>
                      <strong>Fișiere/zi:</strong>{" "}
                      {p.daily_file_limit ?? "Nelimitat"}
                    </p>
                  </div>
                  <button
                    className="select-plan-card-btn"
                    onClick={() => handleSelectPlan(p.id)}
                  >
                    Activează
                  </button>
                </li>
              ))}
            </ul>
            <button className="close-modal" onClick={() => setShowModal(false)}>
              Închide
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Profile;
