import { Box, IconButton, useTheme, Tooltip, Popover, Typography, Divider, List, ListItem, ListItemText } from "@mui/material";
import { useContext, useState } from "react";
import { ColorModeContext, tokens } from "../../theme";
import InputBase from "@mui/material/InputBase";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import NotificationsOutlinedIcon from "@mui/icons-material/NotificationsOutlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import SearchIcon from "@mui/icons-material/Search";
import ExitToAppIcon from "@mui/icons-material/ExitToApp";
import useMediaQuery from "@mui/material/useMediaQuery";
import EditIcon from '@mui/icons-material/Edit';

const Topbar = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const colorMode = useContext(ColorModeContext);
  const [searchTerm, setSearchTerm] = useState("");
  const [anchorEl, setAnchorEl] = useState(null);
  const [popupType, setPopupType] = useState(null);
  const isMobile = useMediaQuery(theme.breakpoints.down("sm"));

  const handleSearch = () => {
    console.log("Searching for:", searchTerm);
  };

  const handlePopupOpen = (event, type) => {
    if (popupType === type) {
      setPopupType(null);
      setAnchorEl(null);
    } else {
      setPopupType(type);
      setAnchorEl(event.currentTarget);
    }
  };

  const handlePopupClose = () => {
    setPopupType(null);
    setAnchorEl(null);
  };

  const handleLogout = () => {
    console.log("Logging out...");
    window.location.href = "/login";
  };

  return (
    <Box display="flex" justifyContent="space-between" p={2}>
      {/* SEARCH BAR */}
      <Box display="flex" backgroundColor={colors.primary[400]} borderRadius="3px">
        <InputBase sx={{ ml: 2, flex: 1 }} placeholder="Search" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} />
        <IconButton type="button" sx={{ p: 1 }} onClick={handleSearch}>
          <SearchIcon />
        </IconButton>
      </Box>

      {/* ICONS */}
      <Box display="flex">
        <Tooltip title="Toggle Light/Dark Mode">
          <IconButton onClick={colorMode.toggleColorMode}>
            {theme.palette.mode === "dark" ? <DarkModeOutlinedIcon /> : <LightModeOutlinedIcon />}
          </IconButton>
        </Tooltip>

        <Tooltip title="View Notifications">
          <IconButton onClick={(e) => handlePopupOpen(e, "notifications")}>
            <NotificationsOutlinedIcon />
          </IconButton>
        </Tooltip>

        <Tooltip title="Open Settings">
          <IconButton onClick={(e) => handlePopupOpen(e, "settings")}>
            <SettingsOutlinedIcon />
          </IconButton>
        </Tooltip>

        <Tooltip title="Open Profile Menu">
          <IconButton onClick={(e) => handlePopupOpen(e, "profile")}>
            <PersonOutlinedIcon />
          </IconButton>
        </Tooltip>

        <Tooltip title="Log Out">
          <IconButton onClick={handleLogout}>
            <ExitToAppIcon />
          </IconButton>
        </Tooltip>
      </Box>

      {/* POPUP COMPONENT */}
      <Popover
        open={Boolean(anchorEl)}
        anchorEl={anchorEl}
        onClose={handlePopupClose}
        anchorOrigin={{ vertical: "bottom", horizontal: "right" }}
        transformOrigin={{ vertical: "top", horizontal: "right" }}
        sx={{ mt: 1 }}
      >
        <Box p={3} width="400px" minHeight="300px" display="flex" flexDirection="column">
          {popupType === "notifications" && (
            <>
              <Typography variant="h6" sx={{ marginBottom: 2 }}>User Behavior Alerts</Typography>
              <Divider />
              <List>
                <ListItem>
                  <ListItemText
                    primary="User: John Doe"
                    secondary="Multiple failed login attempts"
                  />
                </ListItem>
                <ListItem>
                  <ListItemText
                    primary="User: Jane Smith"
                    secondary="Suspicious activity detected"
                  />
                </ListItem>
              </List>
            </>
          )}
          {popupType === "settings" && (
            <>
              <Typography variant="h6" sx={{ marginBottom: 2 }}>Settings</Typography>
              <Divider />
              <List>
                <ListItem button>
                  <ListItemText primary="Account Settings" />
                  <EditIcon />
                </ListItem>
                <ListItem button>
                  <ListItemText primary="Privacy Settings" />
                  <EditIcon />
                </ListItem>
                <ListItem button>
                  <ListItemText primary="Notification Preferences" />
                  <EditIcon />
                </ListItem>
              </List>
            </>
          )}
          {popupType === "profile" && (
            <Box display="flex" flexDirection="column" justifyContent="space-between" height="100%">
              <Box>
                <Box display="flex" alignItems="center" mb={2}>
                  <img src="/path-to-profile-pic.jpg" alt="Profile" style={{ width: 50, height: 50, borderRadius: "50%" }} />
                  <Typography variant="h6" ml={2} sx={{ color: colors.grey[900] }}>User Name</Typography>
                </Box>
                <Typography
                  variant="body2"
                  sx={{ cursor: "pointer", color: theme.palette.primary.main, mb: 2 }}
                  onClick={() => window.location.href = "/admin-info"}
                >
                  Manage My Account
                </Typography>
              </Box>
              <Typography
                variant="body2"
                sx={{ cursor: "pointer", color: "red", textAlign: "center", p: 2, borderTop: `1px solid ${colors.grey[300]}` }}
                onClick={handleLogout}
              >
                Log Out
              </Typography>
            </Box>
          )}
        </Box>
      </Popover>
    </Box>
  );
};

export default Topbar;