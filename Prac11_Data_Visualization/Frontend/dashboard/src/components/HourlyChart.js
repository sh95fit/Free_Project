// Chart.js
import React from "react";
// import "chart.js/auto";
import { Chart } from "react-chartjs-2";
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


const MixedChart = ({ data, ivtList }) => {
  // 날짜를 기준으로 정렬하는 함수
  const sortByDate = (a, b) => {
    const dateA = new Date(a.UPDDATIME);
    const dateB = new Date(b.UPDDATIME);
    return dateA - dateB;
  };

  // 기존 데이터를 날짜순으로 정렬
  const sortedData = data.slice().sort(sortByDate);

  // 동적으로 선 그래프 데이터셋 생성
  const generateLineDatasets = (data, ivtList) => {
    return ivtList.flatMap((ivt, index) => {
      return [
        {
          type: "line",
          label: `${ivt}'s TPG`,
          data: data.map((entry) => entry[`${ivt}_TPG`]),
          backgroundColor: `rgba(75, 192, 192, 0.2)`,
          borderColor: `rgba(75, 192, 192, 1)`,
          borderWidth: 1,
        },
      ];
    });
  };


  // 차트에 사용할 데이터 포맷
  const chartData = {
    labels: data.map((entry) => entry.UPDDATIME),
    datasets: [
      // {
      //   type: "line",
      //   label: "IVT1",
      //   data: data.map((entry) => entry.TPG),
      //   backgroundColor: "rgba(75,192,192,0.2)",
      //   borderColor: "rgba(75,192,192,1)",
      //   borderWidth: 1,
      // },
      {
        type: "bar",
        label: "Total",
        data: sortedData.map((entry) => entry.TPG),
        backgroundColor: "#ddd",
        borderColor: "#ddd",
        borderWidth: 2,
      },

      ...(Array.isArray(ivtList) ? generateLineDatasets(data, ivtList) : []),
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