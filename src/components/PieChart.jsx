import { ResponsivePie } from "@nivo/pie";
import { tokens } from "../theme";
import { useTheme } from "@mui/material";

// Updated mock data for UEBA (User and Entity Behavior Analytics)
const mockPieData = [
  {
    id: "Normal Behavior",
    label: "Normal",
    value: 75,
    color: "hsl(207, 70%, 50%)",
  },
  {
    id: "Anomalous Behavior",
    label: "Anomalous",
    value: 15,
    color: "hsl(348, 70%, 50%)",
  },
  {
    id: "High Risk",
    label: "High Risk",
    value: 5,
    color: "hsl(0, 70%, 50%)",
  },
  {
    id: "Medium Risk",
    label: "Medium Risk",
    value: 5,
    color: "hsl(50, 70%, 50%)",
  },
];

const PieChart = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <ResponsivePie
      data={mockPieData} // Updated data here
      theme={{
        axis: {
          domain: {
            line: {
              stroke: colors.grey[100],
            },
          },
          legend: {
            text: {
              fill: colors.grey[100],
            },
          },
          ticks: {
            line: {
              stroke: colors.grey[100],
              strokeWidth: 1,
            },
            text: {
              fill: colors.grey[100],
            },
          },
        },
        legends: {
          text: {
            fill: colors.grey[100],
          },
        },
      }}
      margin={{ top: 40, right: 80, bottom: 80, left: 80 }}
      innerRadius={0.5}
      padAngle={0.7}
      cornerRadius={3}
      activeOuterRadiusOffset={8}
      borderColor={{
        from: "color",
        modifiers: [["darker", 0.2]],
      }}
      arcLinkLabelsSkipAngle={10}
      arcLinkLabelsTextColor={colors.grey[100]}
      arcLinkLabelsThickness={2}
      arcLinkLabelsColor={{ from: "color" }}
      enableArcLabels={false}
      arcLabelsRadiusOffset={0.4}
      arcLabelsSkipAngle={7}
      arcLabelsTextColor={{
        from: "color",
        modifiers: [["darker", 2]],
      }}
      defs={[
        {
          id: "dots",
          type: "patternDots",
          background: "inherit",
          color: "rgba(255, 255, 255, 0.3)",
          size: 4,
          padding: 1,
          stagger: true,
        },
        {
          id: "lines",
          type: "patternLines",
          background: "inherit",
          color: "rgba(255, 255, 255, 0.3)",
          rotation: -45,
          lineWidth: 6,
          spacing: 10,
        },
      ]}
      legends={[
        {
          anchor: "bottom",
          direction: "row",
          justify: false,
          translateX: 0,
          translateY: 56,
          itemsSpacing: 0,
          itemWidth: 100,
          itemHeight: 18,
          itemTextColor: "#999",
          itemDirection: "left-to-right",
          itemOpacity: 1,
          symbolSize: 18,
          symbolShape: "circle",
          effects: [
            {
              on: "hover",
              style: {
                itemTextColor: "#000",
              },
            },
          ],
        },
      ]}
    />
  );
};

export default PieChart;