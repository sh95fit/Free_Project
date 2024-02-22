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


const MixedChart = ({ data }) => {

  // 날짜와 시간대를 기준으로 정렬하는 함수
  const sortByDateTime = (a, b) => {
    // const dateTimeA = new Date(`${a.EVTDATE}T${a.EVTHH}`);
    // const dateTimeB = new Date(`${b.EVTDATE}T${b.EVTHH}`);
    // return dateTimeA - dateTimeB;
    const dateTimeA = new Date(`${a.EVTDATE}T${a.EVTHH}`).getTime();
    const dateTimeB = new Date(`${b.EVTDATE}T${b.EVTHH}`).getTime();
    return dateTimeA - dateTimeB || parseInt(a.EVTHH, 10) - parseInt(b.EVTHH, 10);
  };

  const sortedData = data.slice().sort(sortByDateTime);

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


  // 중복된 항목을 제거하고 IVTID 별로 데이터를 가져오는 함수
  const getIVTData = (data) => {

    // IVTID 별로 데이터를 가져오기
    const ivtData = {};

    for (const entry of Object.values(sortedData)) {
      const ivtid = entry.IVTID;
      if (!ivtData[ivtid]) {
        ivtData[ivtid] = [];
      }
      ivtData[ivtid].push(entry);
    }

    return ivtData;
  };

  // IVTID 별로 데이터셋 생성하는 함수
  const getIVTDatasets = (ivtData) => {
    // 모든 IVTID에 대한 전체 EVTDATE+EVTHH 기준 값을 가져옴
    const allDates = Array.from(
      new Set(
        Object.values(ivtData)
          .flatMap((values) => values.map((entry) => entry.EVTDATE + entry.EVTHH))
      )
    );

    return Object.entries(ivtData).map(([ivtid, values]) => {
      const randomColor = `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 1)`;
      const dataWithZeros = fillMissingValues(values, allDates);
      return {
        type: "line",
        label: `${ivtid}'s TPG`,
        data: dataWithZeros.map((entry) => entry.TPG),
        borderColor: randomColor,
        backgroundColor: randomColor,
        borderWidth: 1,
        fill: false,
      };
    });
  };

  // 값이 없으면 0으로 채우는 함수
  const fillMissingValues = (values, allDates) => {
    // 모든 EVTDATE+EVTHH 기준 값에 대해 IVTID에 해당하는 값을 가져옴
    const completeSet = allDates.map((datetime) => {
      const existingEntry = values.find((entry) => entry.EVTDATE + entry.EVTHH === datetime);
      return existingEntry ? existingEntry : { EVTDATE: datetime.substring(0, 8), EVTHH: datetime.substring(8), TPG: 0 };
    });

    return completeSet;
  };


  // 중복된 항목을 제거하고 합산된 데이터를 가져옴
  const reducedData = Object.values(reduceAndSortDataByDateTime(data));


  const ivtData = getIVTData(data);
  const ivtDatasets = getIVTDatasets(ivtData);


  // 차트에 사용할 데이터 포맷
  const chartData = {
    labels: reducedData.map((entry) => entry.EVTDATE + " " + entry.EVTHH),
    datasets: [
      ...ivtDatasets,
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
    // <div>
    //   <Chart type="bar" data={chartData} options={chartOptions} />
    // </div>
    <div key={JSON.stringify({ data })}>
      <Chart type="bar" data= {chartData} options={chartOptions} />
    </div>
  );
};

export default MixedChart;



