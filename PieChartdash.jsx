// src/components/PieChart.jsx
import React from "react";
import { Pie } from "react-chartjs-2";
import { Box } from "@mui/material";

const PieChart = ({ data }) => {
  const chartData = {
    labels: data.map(item => item.category),
    datasets: [
      {
        data: data.map(item => item.value),
        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
      },
    ],
  };

  return (
    <Box sx={{ width: "100%", height: "300px" }}>
      <Pie data={chartData} />
    </Box>
  );
};

export default PieChart;