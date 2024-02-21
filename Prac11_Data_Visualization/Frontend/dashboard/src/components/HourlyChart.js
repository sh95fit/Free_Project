// Chart.js
import React from "react";
// import "chart.js/auto";
import {
  ArcElement,
  BarElement,
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  Tooltip,
  registerables,
} from "chart.js";
import { Chart } from "react-chartjs-2";


ChartJS.register(
  ...registerables,
  LinearScale,
  CategoryScale,
  BarElement,
  PointElement,
  LineElement,
  Legend,
  Tooltip,
  ArcElement
);

const MixedChart = ({ data }) => {
  // 차트에 사용할 데이터 포맷
  const chartData = {
    labels: data.map((entry) => entry.UPDDATIME),
    datasets: [
      {
        type: "line",
        label: "IVT1",
        data: data.map((entry) => entry.TPG),
        backgroundColor: "rgba(75,192,192,0.2)",
        borderColor: "rgba(75,192,192,1)",
        borderWidth: 1,
      },
      {
        type: "bar",
        label: "Total",
        data: data.map((entry) => entry.TPG),
        backgroundColor: "#ddd",
        borderColor: "#ddd",
        borderWidth: 2,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend:{
          position: 'top',
        },
      title:{
          display: true,
          text: "Daily Inverter Chart"
        },
    },
  };

  return (
    <div>
      <Chart type="bar" data={chartData} options={chartOptions} />
    </div>
  );
};

export default MixedChart;