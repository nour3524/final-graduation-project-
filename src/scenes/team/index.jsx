import { Box, Typography, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import { mockDataTeam } from "../../data/mockData";
import AdminPanelSettingsOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import LockOpenOutlinedIcon from "@mui/icons-material/LockOpenOutlined";
import SecurityOutlinedIcon from "@mui/icons-material/SecurityOutlined";
import Header from "../../components/Header";

const Team = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const columns = [
    { field: "user_id", headerName: "User ID", flex: 1 },
    { field: "name", headerName: "Name", flex: 1, cellClassName: "name-column--cell" },
    { field: "username", headerName: "Username", flex: 1 },
    { field: "email", headerName: "Email", flex: 1 },
    { field: "department", headerName: "Department", flex: 1 },
    { field: "device_id", headerName: "Device ID", flex: 1 },
    { field: "join_date", headerName: "Join Date", type: "date", flex: 1 },
    { field: "risk_score", headerName: "Risk Score", type: "number", flex: 1 },
    { field: "risk_reason", headerName: "Risk Reason", flex: 1 },
    { field: "status", headerName: "Status", flex: 1 },
  ];

  return (
    <Box m="20px">
      <Header title="Employee profile" subtitle="Managing the employee info" />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": { border: "none" },
          "& .MuiDataGrid-cell": { borderBottom: "none" },
          "& .name-column--cell": { color: colors.greenAccent[300] },
          "& .MuiDataGrid-columnHeaders": { backgroundColor: colors.blueAccent[700], borderBottom: "none" },
          "& .MuiDataGrid-virtualScroller": { backgroundColor: colors.primary[400] },
          "& .MuiDataGrid-footerContainer": { borderTop: "none", backgroundColor: colors.blueAccent[700] },
          "& .MuiCheckbox-root": { color: `${colors.greenAccent[200]} !important` },
        }}
      >
        <DataGrid checkboxSelection rows={mockDataTeam} columns={columns} />
      </Box>
    </Box>
  );
};

export default Team;
