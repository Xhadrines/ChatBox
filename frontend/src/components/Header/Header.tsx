import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Header.css";

interface DropdownItem {
  label: string;
  value: string;
  icon: string;
  onClick?: () => void;
}

interface HeaderProps {
  title: string;
  showBackButton?: boolean;
  backUrl?: string;
  dropdownItems?: DropdownItem[];
}

const Header: React.FC<HeaderProps> = ({
  title,
  showBackButton = false,
  backUrl,
  dropdownItems = [],
}) => {
  const navigate = useNavigate();
  const [openDropdown, setOpenDropdown] = useState(false);
  const [userRoleName, setUserRoleName] = useState<string | null>(null);

  // const [user] = useState(() => {
  //   const stored = localStorage.getItem("user");
  //   return stored ? JSON.parse(stored) : null;
  // });

  useEffect(() => {
    const stored = localStorage.getItem("user");
    const userObj = stored ? JSON.parse(stored) : null;

    if (!userObj || !userObj.role) {
      queueMicrotask(() => setUserRoleName(null));
      return;
    }

    fetch(`${import.meta.env.VITE_CHAT_API}/api/user-roles/${userObj.role}/`)
      .then((res) => res.json())
      .then((data) => setUserRoleName(data.name))
      .catch(() => setUserRoleName(null));
  }, []);

  const filteredItems = dropdownItems.filter((item) => {
    if (
      item.value === "dashboard" &&
      userRoleName?.toLowerCase() !== "administrator"
    ) {
      return false;
    }
    return true;
  });

  const handleBack = () => {
    if (backUrl) {
      navigate(backUrl);
    } else {
      navigate(-1);
    }
  };

  const toggleDropdown = () => setOpenDropdown(!openDropdown);

  return (
    <header className="header">
      <div className="header-left">
        {showBackButton && (
          <button className="back-button" onClick={handleBack}>
            <img src="/back.png" alt="Back" className="back-icon" />
          </button>
        )}
      </div>

      <h1 className="header-title">{title}</h1>

      <div className="header-right">
        {filteredItems.length > 0 && (
          <div className="dropdown-container">
            <button className="dropdown-button" onClick={toggleDropdown}>
              <img src="/settings.png" alt="Settings" className="header-icon" />
            </button>

            {openDropdown && (
              <div className="dropdown-menu">
                {filteredItems.map((item) => (
                  <div
                    key={item.value}
                    className="dropdown-item"
                    onClick={() => {
                      item.onClick?.();
                      setOpenDropdown(false);
                    }}
                  >
                    <img
                      src={item.icon}
                      alt={item.label}
                      className="dropdown-icon"
                    />
                    <span>{item.label}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;
