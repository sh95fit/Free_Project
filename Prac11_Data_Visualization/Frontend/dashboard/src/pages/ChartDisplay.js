import React, { useState } from "react";
import './ChartDisplay.css'

import axios from "axios";

import DailyChart from '../components/DailyChart'
import ErrorBoundary from '../components/ErrorBoundary'
import Navbar from '../components/Navbar'

export default function ChartDisplay() {
  const [dailyData, setData] = useState([]);

  const fetchData = async ({ untid, ivtid, startDate, endDate }) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/more/daily/${untid}/${ivtid}?start_date=${startDate}&end_date=${endDate}`
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
          <DailyChart className="chart" data={dailyData} />
          <DailyChart className="chart" data={dailyData} />
          <DailyChart className="chart" data={dailyData} />
          <DailyChart className="chart" data={dailyData} />
        </div>
      </ErrorBoundary>
    </div>
  )
}