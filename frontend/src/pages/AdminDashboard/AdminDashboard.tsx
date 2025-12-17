import React, { useEffect, useState } from "react";
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
import "./AdminDashboard.css";

const apiUrl = import.meta.env.VITE_CHAT_API;

interface TableConfig {
  name: string;
  endpoint: string;
  columns: string[];
  fks?: { [key: string]: string };
}

const tables: TableConfig[] = [
  {
    name: "User Roles",
    endpoint: "user-roles",
    columns: ["id", "name", "description", "created_at", "updated_at"],
  },
  {
    name: "User Status",
    endpoint: "user-status",
    columns: ["id", "name", "description", "created_at", "updated_at"],
  },
  {
    name: "Users",
    endpoint: "users",
    columns: [
      "id",
      "username",
      "email",
      "password",
      "role",
      "role_name",
      "status",
      "status_name",
    ],
    fks: { role: "user-roles", status: "user-status" },
  },
  {
    name: "User Token",
    endpoint: "user-token",
    columns: ["user", "key", "created"],
    fks: { user: "users" },
  },
  {
    name: "Plan Types",
    endpoint: "plan-types",
    columns: ["id", "name", "description", "created_at", "updated_at"],
  },
  {
    name: "Plans",
    endpoint: "plans",
    columns: [
      "id",
      "name",
      "price",
      "type",
      "type_name",
      "duration_days",
      "name_llm_prm",
      "daily_prm_msg",
      "name_llm_std",
      "daily_std_msg",
      "daily_file_limit",
    ],
    fks: { type: "plan-types" },
  },
  {
    name: "User Plans",
    endpoint: "user-plans",
    columns: ["id", "user", "plan", "plan_name", "start_date", "end_date"],
    fks: { user: "users", plan: "plans" },
  },
  {
    name: "Messages",
    endpoint: "messages",
    columns: ["id", "user", "user_msg", "llm_resp", "llm_used", "uploaded_at"],
    fks: { user: "users" },
  },
  {
    name: "Files",
    endpoint: "files",
    columns: ["id", "user", "file_name", "file_path", "uploaded_at"],
    fks: { user: "users" },
  },
  {
    name: "User Usage",
    endpoint: "user-usage",
    columns: ["id", "user", "date", "messages_sent", "files_uploaded", "date"],
    fks: { user: "users" },
  },
];

const AdminDashboard: React.FC = () => {
  const [activeTable, setActiveTable] = useState<TableConfig>(tables[0]);
  const [data, setData] = useState<any[]>([]);
  const [editRow, setEditRow] = useState<any | null>(null);
  const [formData, setFormData] = useState<any>({});
  const [viewRow, setViewRow] = useState<any | null>(null);
  const [fkOptions, setFkOptions] = useState<{ [key: string]: any[] }>({});
  const [usageData, setUsageData] = useState<any[]>([]);
  const [viewUsageData, setViewUsageData] = useState<any[]>([]);

  useEffect(() => {
    fetchTableData();
    fetchUsageData();
    if (activeTable.fks) fetchFkOptions();
  }, [activeTable]);

  useEffect(() => {
    if (viewRow && activeTable.name === "Users") {
      const fetchUserUsage = async () => {
        try {
          const res = await fetch(
            `${apiUrl}/api/user-usage/user/${viewRow.id}/`,
            { credentials: "include" }
          );
          if (!res.ok) return;
          const userData = await res.json();
          const chartData = userData
            .map((u: any) => ({
              date: u.date,
              messages: u.messages_sent,
              files: u.files_uploaded,
            }))
            .sort((a: any, b: any) => (a.date > b.date ? 1 : -1));
          setViewUsageData(chartData);
        } catch (err) {
          console.error(err);
        }
      };
      fetchUserUsage();
    } else setViewUsageData([]);
  }, [viewRow, activeTable]);

  const fetchTableData = async () => {
    try {
      const token = localStorage.getItem("token");

      const res = await fetch(`${apiUrl}/api/admin/${activeTable.endpoint}/`, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
      });
      if (res.ok) setData(await res.json());
    } catch (err) {
      console.error(err);
    }
  };

  const fetchUsageData = async () => {
    if (activeTable.name !== "User Usage") return;
    try {
      const res = await fetch(`${apiUrl}/api/admin/user-usage/`, {
        credentials: "include",
      });
      if (!res.ok) return;
      const data = await res.json();
      const aggregated: {
        [date: string]: { messages: number; files: number };
      } = {};
      data.forEach((u: any) => {
        if (!aggregated[u.date]) aggregated[u.date] = { messages: 0, files: 0 };
        aggregated[u.date].messages += u.messages_sent;
        aggregated[u.date].files += u.files_uploaded;
      });
      const chartData = Object.entries(aggregated)
        .map(([date, val]) => ({
          date,
          messages: val.messages,
          files: val.files,
        }))
        .sort(
          (a, b) => new Date(a.date).getTime() - new Date(b.date).getTime()
        );
      setUsageData(chartData);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchFkOptions = async () => {
    if (!activeTable.fks) return;
    const newOptions: { [key: string]: any[] } = {};
    for (const [fkField, fkEndpoint] of Object.entries(activeTable.fks)) {
      try {
        const token = localStorage.getItem("token");

        const res = await fetch(`${apiUrl}/api/admin/${fkEndpoint}/`, {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`,
          },
        });

        if (res.ok) newOptions[fkField] = await res.json();
      } catch (err) {
        console.error(err);
      }
    }
    setFkOptions(newOptions);
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm("Sigur vrei să ștergi acest rând?")) return;
    try {
      const token = localStorage.getItem("token");

      const res = await fetch(
        `${apiUrl}/api/admin/${activeTable.endpoint}/${id}/`,
        {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`,
          },
        }
      );
      if (res.status === 204) fetchTableData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleEdit = (row: any) => {
    const newFormData = { ...row };

    if ("password" in newFormData) {
      newFormData.password = "";
    }

    setEditRow(row);
    setFormData(newFormData);
  };

  const handleView = (row: any) => setViewRow(row);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSave = async () => {
    try {
      const method = editRow && editRow.id ? "PATCH" : "POST";
      const url =
        editRow && editRow.id
          ? `${apiUrl}/api/admin/${activeTable.endpoint}/${editRow.id}/`
          : `${apiUrl}/api/admin/${activeTable.endpoint}/`;

      const bodyData = { ...formData };
      if (bodyData.password === "") delete bodyData.password;

      if (!bodyData.password) {
        delete bodyData.password;
      }

      const token = localStorage.getItem("token");

      const res = await fetch(url, {
        method,
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
        body: JSON.stringify(bodyData),
      });
      if (res.ok) {
        setEditRow(null);
        setFormData({});
        fetchTableData();
      } else {
        const errorData = await res.json();
        console.error("Error saving:", errorData);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleCancel = () => {
    setEditRow(null);
    setFormData({});
  };

  const closeViewRow = () => setViewRow(null);

  return (
    <div className="dashboard-container">
      <Header title="ChatBox" showBackButton={true} backUrl="/chat" />

      <div className="table-wrapper">
        <div className="tabs">
          {tables.map((t) => (
            <button
              key={t.name}
              className={t.name === activeTable.name ? "active-tab" : ""}
              onClick={() => setActiveTable(t)}
            >
              {t.name}
            </button>
          ))}
        </div>

        <button className="add-button" onClick={() => setEditRow({})}>
          Adaugă rând nou
        </button>

        <div className="table-container">
          {activeTable.name === "User Usage" && usageData.length > 0 && (
            <div className="chart-container">
              <h3>Grafic total mesaje și fișiere</h3>
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
          )}

          <table>
            <thead>
              <tr>
                {activeTable.columns.map((col) => (
                  <th key={col}>{col}</th>
                ))}
                <th>Acțiuni</th>
              </tr>
            </thead>
            <tbody>
              {data.map((row: any) => (
                <tr key={row.id || row.key || row.user}>
                  {activeTable.columns.map((col) => (
                    <td key={col}>{row[col]}</td>
                  ))}
                  <td>
                    <button
                      className="view-btn"
                      onClick={() => handleView(row)}
                    >
                      Vizualizare
                    </button>
                    <button
                      className="edit-btn"
                      onClick={() => handleEdit(row)}
                    >
                      Edit
                    </button>
                    <button
                      className="delete-btn"
                      onClick={() => handleDelete(row.id || row.pk || row.user)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {viewRow && (
          <div className="modal">
            <div className="modal-content1 large-modal">
              <h3>
                Detalii {activeTable.name}:{" "}
                {viewRow.username || viewRow.name || viewRow.id}
              </h3>
              {activeTable.columns.map((col) => (
                <p
                  key={col}
                  className={col === "password" ? "password-text" : ""}
                >
                  <strong>{col}:</strong> {viewRow[col]}
                </p>
              ))}

              {activeTable.name === "Users" && viewUsageData.length > 0 && (
                <div className="chart-modal-container">
                  <h4>Grafic utilizator</h4>
                  <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={viewUsageData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="date" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line
                        type="monotone"
                        dataKey="messages"
                        stroke="#8884d8"
                      />
                      <Line type="monotone" dataKey="files" stroke="#82ca9d" />
                    </LineChart>
                  </ResponsiveContainer>
                </div>
              )}

              <button className="cancel-btn" onClick={closeViewRow}>
                Închide
              </button>
            </div>
          </div>
        )}

        {editRow && (
          <div className="modal">
            <div className="modal-content1">
              <h3>{editRow.id ? "Editează rând" : "Adaugă rând"}</h3>
              {activeTable.columns.map((col) => {
                if (
                  [
                    "id",
                    "date",
                    "uploaded_at",
                    "created_at",
                    "updated_at",
                    "start_date",
                    "end_date",
                    "key",
                    "created",
                  ].includes(col) ||
                  col.endsWith("_name")
                )
                  return null;

                if (activeTable.fks && activeTable.fks[col]) {
                  const options = fkOptions[col] || [];
                  return (
                    <div key={col} className="form-group">
                      <label>{col}</label>
                      <select
                        name={col}
                        value={formData[col] || ""}
                        onChange={handleChange}
                        className="form-select"
                      >
                        <option value="">-- Selectează --</option>
                        {options.map((opt) => {
                          let displayValue =
                            opt.name || opt.display || opt.username || opt.id;
                          return (
                            <option key={opt.id} value={opt.id}>
                              {displayValue}
                            </option>
                          );
                        })}
                      </select>
                    </div>
                  );
                }

                const inputType = col === "password" ? "password" : "text";

                return (
                  <div key={col} className="form-group">
                    <label>{col}</label>
                    <input
                      type={inputType}
                      name={col}
                      value={formData[col] || ""}
                      onChange={handleChange}
                      className="form-control"
                      placeholder={
                        col === "password"
                          ? "Lăsați gol dacă nu doriți să schimbați"
                          : undefined
                      }
                      autoComplete={
                        col === "password"
                          ? "new-password"
                          : col === "username"
                          ? "off"
                          : col === "email"
                          ? "off"
                          : undefined
                      }
                    />
                  </div>
                );
              })}
              <button className="save-btn" onClick={handleSave}>
                Salvează
              </button>
              <button className="cancel-btn" onClick={handleCancel}>
                Anulează
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default AdminDashboard;
