import React, { useState } from "react";
import './ChartDisplay.css'

import axios from "axios";

import DailyChart from '../components/DailyChart'
import HourlyChart from '../components/HourlyChart'
import ErrorBoundary from '../components/ErrorBoundary'
import Navbar from '../components/NavbarPwr'

export default function ChartDisplay() {
  const [solarHourlyData, setHourlyData] = useState([]);
  const [solarDailyData, setDailyData] = useState([]);

  const HourlyData = async ({ untId, pwrId, startDate, endDate, dataSetter }) => {
    try {
      // const response = await axios.get(
        // `http://localhost:8000/more/daily/${untid}/${ivtid}?start_date=${startDate}&end_date=${endDate}`
      const response = await axios.post(
        "http://localhost:8000/more/hourly",
        {
          "UNTID": untId,
          "PWRID": pwrId,
          "start_date": startDate,
          "end_date": endDate,
        }
      );

      dataSetter(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const DailyData = async ({ untId, pwrId, startDate, endDate, dataSetter }) => {
    try {
      // const response = await axios.get(
        // `http://localhost:8000/more/daily/${untid}/${ivtid}?start_date=${startDate}&end_date=${endDate}`
      const response = await axios.post(
        "http://localhost:8000/more/daily",
        {
          "UNTID": untId,
          "PWRID": pwrId,
          "start_date": startDate,
          "end_date": endDate,
        }
      );

      dataSetter(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleFormSubmit = async ({ untId, pwrId, startDate, endDate }) => {
    // fetchData 함수를 이용하여 HourlyData와 DailyData를 동시에 호출
    await HourlyData({
      untId,
      pwrId,
      startDate,
      endDate,
      dataSetter: setHourlyData,
    });

    await DailyData({
      untId,
      pwrId,
      startDate,
      endDate,
      dataSetter: setDailyData,
    });
  };

  return (
    <div>
      <Navbar onSubmit={handleFormSubmit} />
      <ErrorBoundary>
        <div className="container">
          <HourlyChart className="chart" data={solarHourlyData} />
          <DailyChart className="chart" data={solarDailyData} />
          <HourlyChart className="chart" data={solarHourlyData} />
          <DailyChart className="chart" data={solarDailyData} />
        </div>
      </ErrorBoundary>
    </div>
  )
}