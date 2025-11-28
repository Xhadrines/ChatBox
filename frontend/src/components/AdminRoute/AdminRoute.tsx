import React from "react";
import { Navigate } from "react-router-dom";

interface AdminRouteProps {
  children: React.ReactNode;
}

const AdminRoute: React.FC<AdminRouteProps> = ({ children }) => {
  const userString = localStorage.getItem("user");

  if (!userString) {
    return <Navigate to="/login" replace />;
  }

  const user = JSON.parse(userString);

  if (user.role_name !== "Administrator") {
    return <Navigate to="/chat" replace />;
  }

  return <>{children}</>;
};

export default AdminRoute;
