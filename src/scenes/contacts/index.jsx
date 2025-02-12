import { Box } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import Header from "../../components/Header";
import { useTheme } from "@mui/material";
import { useState } from "react";

const Users = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  // Columns for the data grid without Added By and Deleted By
  const columns = [
    { field: "username", headerName: "Username", flex: 1 },
    { field: "registrarId", headerName: "Registrar ID" },
    { field: "role", headerName: "Role", flex: 1 },
    { field: "status", headerName: "Status", flex: 1 },
    { field: "lastLogin", headerName: "Last Login", flex: 1 },
    { field: "createdAt", headerName: "Created At", flex: 1 },
    { field: "updatedAt", headerName: "Updated At", flex: 1 },
    {
      field: "actions",
      headerName: "Actions",
      flex: 1,
      renderCell: (params) => (
        <Box display="flex" justifyContent="space-around">
          <button onClick={() => handleAdd(params)}>Add</button>
          <button onClick={() => handleDelete(params)}>Delete</button>
        </Box>
      ),
    },
  ];

  // Mock data for admins
  const [mockDatausers, setMockDatausers] = useState([
    { id: 1, username: "salmaelkholy", registrarId: "R1", role: "Admin", status: "Active", lastLogin: "2025-02-09", createdAt: "2024-10-12", updatedAt: "2025-01-01" },
    { id: 2, username: "safeyaiyad", registrarId: "R2", role: "Admin", status: "Inactive", lastLogin: "2025-01-20", createdAt: "2024-08-22", updatedAt: "2025-01-05" },
    // Add more mock data as needed
  ]);

  // Function to handle Add action
  const handleAdd = (params) => {
    const newUser = {
      id: mockDatausers.length + 1,
      username: `newUser${mockDatausers.length + 1}`,
      registrarId: `R${mockDatausers.length + 1}`,
      role: "Admin",
      status: "Active",
      lastLogin: "2025-02-10",
      createdAt: new Date().toISOString().split("T")[0],
      updatedAt: new Date().toISOString().split("T")[0],
    };
    setMockDatausers((prevData) => [...prevData, newUser]);
  };

  // Function to handle Delete action
  const handleDelete = (params) => {
    setMockDatausers((prevData) =>
      prevData.map((user) =>
        user.id === params.row.id ? { ...user, status: "Deleted" } : user
      )
    );
  };

  return (
    <Box m="20px">
      <Header
        title="Admins"
        subtitle="Admins Info"
      />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
          "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
            color: `${colors.grey[100]} !important`,
          },
        }}
      >
        <DataGrid
          rows={mockDatausers}
          columns={columns}
          components={{ Toolbar: GridToolbar }}
        />
      </Box>
    </Box>
  );
};

export default Users;