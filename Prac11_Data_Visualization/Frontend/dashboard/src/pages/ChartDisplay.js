import React, { useState } from "react";
import './ChartDisplay.css'

import axios from "axios";

//import DailyChart from '../components/DailyChart'
import HourlyChart from '../components/HourlyChart'
import ErrorBoundary from '../components/ErrorBoundary'
import Navbar from '../components/Navbar'

export default function ChartDisplay() {
  const [solarData, setData] = useState([]);

  const fetchData = async ({ untId, ivtList, startDate, endDate }) => {
    try {
      // const response = await axios.get(
        // `http://localhost:8000/more/daily/${untid}/${ivtid}?start_date=${startDate}&end_date=${endDate}`
      const response = await axios.post(
        "http://localhost:8000/more/hour/post",
        {
          "UNTID": untId,
          "IVTID": ivtList,
          "start_date": startDate,
          "end_date": endDate,
        }
      );

      setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div>
      <Navbar onSubmit={fetchData} />
      <ErrorBoundary>
        <div className="container">
          <HourlyChart className="chart" data={solarData} />
          <HourlyChart className="chart" data={solarData} />
          <HourlyChart className="chart" data={solarData} />
          <HourlyChart className="chart" data={solarData} />
        </div>
      </ErrorBoundary>
    </div>
  )
}