import React, { useState } from "react";
import axios from "axios";

import Chart from '../components/Chart'
import ErrorBoundary from '../components/ErrorBoundary'
import Form from '../components/Form'

export default function ChartDisplay() {
  const [data, setData] = useState([]);

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
      <Form onSubmit={fetchData} />
      <ErrorBoundary>
        <Chart data={data} />
      </ErrorBoundary>
    </div>
  )
}