// Chart.js
import React from "react";
import { Bar } from "react-chartjs-2";

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
    scales: {
      x: [
        {
          type: "time",
          time: {
            unit: "day",
            tooltipFormat: "YYYY-MM-DD HH:mm:ss",
          },
          title: {
            display: true,
            text: "UPDDATIME",
          },
        },
      ],
      y: [
        {
          title: {
            display: true,
            text: "TPG",
          },
        },
      ],
    },
  };

  return (
    <div>
      <Bar data={chartData} options={chartOptions} />
    </div>
  );
};

export default Chart;