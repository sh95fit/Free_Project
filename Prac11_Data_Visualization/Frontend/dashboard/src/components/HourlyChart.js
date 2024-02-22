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

  // 날짜와 시간대를 기준으로 정렬하는 함수
  const sortByDateTime = (a, b) => {
    const dateTimeA = parseInt(a.EVTDATE + a.EVTHH);
    const dateTimeB = parseInt(b.EVTDATE + b.EVTHH);
    return dateTimeA - dateTimeB;
  };



  // 날짜와 시간대를 기준으로 데이터 합산 및 정렬하는 함수
  const reduceAndSortDataByDateTime = (data) => {
    const sortedData = data.slice().sort(sortByDateTime);

    return sortedData.reduce((acc, entry) => {
      const key = entry.EVTDATE + " " + entry.EVTHH;

      if (!acc[key]) {
        acc[key] = { ...entry };
      } else {
        // 여기에서 TPG를 합산하거나 다른 로직을 수행할 수 있습니다.
        acc[key].TPG += entry.TPG;
      }

      return acc;
    }, {});
  };

  // 중복된 항목을 제거하고 합산된 데이터를 가져옴
  const reducedData = Object.values(reduceAndSortDataByDateTime(data));


  // 차트에 사용할 데이터 포맷
  const chartData = {
    labels: reducedData.map((entry) => entry.EVTDATE + " " + entry.EVTHH),
    datasets: [
      {
        type: "bar",
        label: "Total",
        data: reducedData.map((entry) => entry.TPG),
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
          text: "Hourly Inverter Chart",
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





