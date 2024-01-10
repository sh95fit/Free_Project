import React, { useState } from "react";

const Form = ({ onSubmit }) => {
  const [untid, setUntid] = useState("");
  const [ivtid, setIvtid] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const formatDate = (date) => {
    const formattedDate = new Date(date).toISOString().slice(0, 10).replace(/-/g, "");
    return formattedDate;
  };

  const handleStartDateChange = (e) => {
    const formattedDate = formatDate(e.target.value);
    setStartDate(formattedDate);
  };

  const handleEndDateChange = (e) => {
    const formattedDate = formatDate(e.target.value);
    setEndDate(formattedDate);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ untid, ivtid, startDate, endDate });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        UNTID:
        <input type="text" value={untid} onChange={(e) => setUntid(e.target.value)} />
      </label>
      <label>
        IVTID:
        <input type="text" value={ivtid} onChange={(e) => setIvtid(e.target.value)} />
      </label>
      <label>
        Start Date:
        <input type="date" value={startDate} onChange={handleStartDateChange} />
      </label>
      <label>
        End Date:
        <input type="date" value={endDate} onChange={handleEndDateChange} />
      </label>
      <button type="submit">Fetch Data</button>
    </form>
  );
};

export default Form;