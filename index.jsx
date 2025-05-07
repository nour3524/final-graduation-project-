import { Box, Button, IconButton, Typography, useTheme } from "@mui/material";
import { tokens } from "../../theme";
import { mockTransactions } from "../../data/mockData";
import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import EmailIcon from "@mui/icons-material/Email";
import PointOfSaleIcon from "@mui/icons-material/PointOfSale";
import PersonAddIcon from "@mui/icons-material/PersonAdd";
import TrafficIcon from "@mui/icons-material/Traffic";
import Header from "../../components/Header";
import LineChart from "../../components/LineChart";
import GeographyChart from "../../components/GeographyChart";
import BarChart from "../../components/BarChart";
import StatBox from "../../components/StatBox";
import ProgressCircle from "../../components/ProgressCircle";
import PieChart from "../../components/PieChart";
import Alert from "../../components/Alert";
import RiskyUsersList from "../../components/RiskyUsersList";

const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box m="20px">
      {/* HEADER */}
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Header title="DASHBOARD" subtitle="Welcome to your dashboard" />

        <Box>
          <Button
            sx={{
              backgroundColor: colors.blueAccent[700],
              color: colors.grey[100],
              fontSize: "14px",
              fontWeight: "bold",
              padding: "10px 20px",
            }}
          >
            <DownloadOutlinedIcon sx={{ mr: "10px" }} />
            Download Reports
          </Button>
        </Box>
      </Box>

      {/* ALERTS SECTION */}
      <Box mb="20px">
        <Alert title="High Priority Alert" message="Suspicious activity detected on IP 192.168.1.10" type="error" />
      </Box>

      {/* GRID LAYOUT FOR STATISTICS AND CHARTS */}
      <Box
        display="grid"
        gridTemplateColumns="repeat(12, 1fr)"
        gridAutoRows="140px"
        gap="20px"
      >
        {/* ROW 1: STATBOXES */}
        <Box gridColumn="span 3" backgroundColor={colors.primary[400]} display="flex" alignItems="center" justifyContent="center">
          <StatBox
            title="97"
            subtitle="Anomalous User Activities"
            progress="0.75"
            increase="+14%"
            icon={<EmailIcon sx={{ color: colors.greenAccent[600], fontSize: "26px" }} />}
          />
        </Box>
        <Box gridColumn="span 3" backgroundColor={colors.primary[400]} display="flex" alignItems="center" justifyContent="center">
          <StatBox
            title="85"
            subtitle="File and data access anomalies"
            progress="0.50"
            increase="+21%"
            icon={<PointOfSaleIcon sx={{ color: colors.greenAccent[600], fontSize: "26px" }} />}
          />
        </Box>
        <Box gridColumn="span 3" backgroundColor={colors.primary[400]} display="flex" alignItems="center" justifyContent="center">
          <StatBox
            title="45"
            subtitle="Network and communication"
            progress="0.30"
            increase="+5%"
            icon={<PersonAddIcon sx={{ color: colors.greenAccent[600], fontSize: "26px" }} />}
          />
        </Box>
        <Box gridColumn="span 3" backgroundColor={colors.primary[400]} display="flex" alignItems="center" justifyContent="center">
          <StatBox
            title="159"
            subtitle="Unauthorized access & login"
            progress="0.80"
            increase="+43%"
            icon={<TrafficIcon sx={{ color: colors.greenAccent[600], fontSize: "26px" }} />}
          />
        </Box>

        {/* ROW 2: CHARTS */}
        <Box gridColumn="span 8" gridRow="span 2" backgroundColor={colors.primary[400]}>
          <Box mt="25px" p="0 30px" display="flex" justifyContent="space-between" alignItems="center">
            <Box>
              <Typography variant="h5" fontWeight="600" color={colors.grey[100]}>
                SECURITY THREATS ANALYZED
              </Typography>
            </Box>
            <Box>
              <IconButton>
                <DownloadOutlinedIcon sx={{ fontSize: "26px", color: colors.greenAccent[500] }} />
              </IconButton>
            </Box>
          </Box>
          <Box height="250px" m="-20px 0 0 0">
            <LineChart isDashboard={true} />
          </Box>
        </Box>

        <Box gridColumn="span 4" gridRow="span 2" backgroundColor={colors.primary[400]} overflow="auto">
          <Box display="flex" justifyContent="space-between" alignItems="center" borderBottom={`4px solid ${colors.primary[500]}`} colors={colors.grey[100]} p="15px">
            <Typography color={theme.palette.mode === 'dark' ? colors.blueAccent[700] : colors.blueAccent[500]} variant="h5" fontWeight="600">
              Recent Security Events
            </Typography>
          </Box>
          {mockTransactions.map((transaction, i) => (
            <Box key={i} display="flex" justifyContent="space-between" alignItems="center" borderBottom={`4px solid ${colors.primary[500]}`} p="15px">
              <Box>
                <Typography color={colors.greenAccent[500]} variant="h5" fontWeight="600">{transaction.txId}</Typography>
                <Typography color={colors.grey[100]}>{transaction.user}</Typography>
              </Box>
              <Box color={colors.grey[100]}>{transaction.date}</Box>
            </Box>
          ))}
        </Box>

        {/* PIE CHART */}
        <Box gridColumn="span 8" gridRow="span 2" backgroundColor={colors.primary[400]} display="flex" flexDirection="column" alignItems="flex-start" p="10px">
          <Typography variant="h5" fontWeight="600" align="left" mb={2}>
            Threat Distribution
          </Typography>
          <PieChart data={[{ category: 'Malicious', value: 40 }, { category: 'Suspicious', value: 30 }, { category: 'Safe', value: 30 }]} />
        </Box>

        {/* RISKY USERS LIST */}
        <Box gridColumn="span 4" gridRow="span 2" backgroundColor={colors.primary[400]} p="10px">
          <Typography variant="h6" color={colors.grey[100]} fontWeight="600">
            Top Risky Users
          </Typography>
          <RiskyUsersList />
        </Box>

      </Box>
    </Box>
  );
};

export default Dashboard;