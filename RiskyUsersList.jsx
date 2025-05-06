import React from "react";
import { Box, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Chip } from "@mui/material";

// Sample risky users data
const riskyUsers = [
  { name: "Eman", riskScore: 95, lastThreat: "Multiple Failed Logins" },
  { name: "Alaa", riskScore: 88, lastThreat: "Unusual Network Activity" },
  { name: "Sarah", riskScore: 82, lastThreat: "Unauthorized File Access" },
  { name: "Mark", riskScore: 78, lastThreat: "Abnormal Login Time" },
  { name: "John", riskScore: 74, lastThreat: "Multiple Device Logins" },
];

const getRiskLevelColor = (score) => {
  if (score >= 90) return "error"; // High Risk (Red)
  if (score >= 80) return "warning"; // Medium Risk (Orange)
  return "info"; // Low Risk (Blue)
};

const RiskyUsersList = () => {
  return (
    <Box sx={{ display: "flex", flexDirection: "row", alignItems: "center", gap: 3, overflowX: "auto", padding: "4px", maxWidth: "160%", scrollbarWidth: "thick", "&::-webkit-scrollbar": { height: "px" }, "&::-webkit-scrollbar-thumb": { backgroundColor: "#888", borderRadius: "1px" }, "&::-webkit-scrollbar-track": { backgroundColor: "#f1f1f1" } }}>
      <Typography variant="h5" sx={{ fontWeight: "bold", color: "#ff6666", whiteSpace: "nowrap" }}>
      </Typography>
      <TableContainer component={Paper} sx={{ maxWidth: "100%", overflowY: "auto", maxHeight: "260px" }}>
        <Table stickyHeader>
          <TableHead>
            <TableRow>
              <TableCell sx={{ fontWeight: "bold", color: (theme) => theme.palette.mode === 'dark' ? "#fff" : "inherit" }}>User</TableCell>
              <TableCell sx={{ fontWeight: "bold", color: (theme) => theme.palette.mode === 'dark' ? "#fff" : "inherit" }}>Risk Score</TableCell>
              <TableCell sx={{ fontWeight: "bold", color: (theme) => theme.palette.mode === 'dark' ? "#fff" : "inherit" }}>Last Detected Threat</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {riskyUsers.map((user, index) => (
              <TableRow key={index}>
                <TableCell sx={{ color: (theme) => theme.palette.mode === 'dark' ? "#fff" : "inherit" }}>{user.name}</TableCell>
                <TableCell>
                  <Chip label={user.riskScore} color={getRiskLevelColor(user.riskScore)} />
                </TableCell>
                <TableCell sx={{ color: (theme) => theme.palette.mode === 'dark' ? "#fff" : "inherit" }}>{user.lastThreat}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default RiskyUsersList;
