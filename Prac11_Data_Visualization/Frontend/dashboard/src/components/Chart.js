// Chart.js
import React from "react";
// import "chart.js/auto";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from "react-chartjs-2";


ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const Chart = ({ data }) => {
  // 차트에 사용할 데이터 포맷
  const chartData = {
    labels: data.map((entry) => entry.UPDDATIME),
    datasets: [
      {
        label: "TPG",
        data: data.map((entry) => entry.TPG),
        backgroundColor: "rgba(75,192,192,0.2)",
        borderColor: "rgba(75,192,192,1)",
        borderWidth: 1,
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
      <Line data={chartData} options={chartOptions} />
    </div>
  );
};

export default Chart;