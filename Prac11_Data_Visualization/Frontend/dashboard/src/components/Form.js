import React, { useState } from "react";

import './Form.css';

const Form = ({ onSubmit }) => {
  const [untid, setUntid] = useState("");
  const [ivtid, setIvtid] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const formatDate = (date) => {
    const formattedDate = new Date(date).toISOString().slice(0, 10).replace(/-/g, "");
    return formattedDate;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Convert date format before calling onSubmit
    const formattedStartDate = formatDate(startDate);
    const formattedEndDate = formatDate(endDate);

    onSubmit({ untid, ivtid, startDate: formattedStartDate, endDate: formattedEndDate });
  };

  return (
    <form className="form-container" onSubmit={handleSubmit}>
      <label className="form-row">
        UNTID :
        <input type="text" value={untid} onChange={(e) => setUntid(e.target.value)} />
      </label>
      <label className="form-row">
        IVTID :
        <input type="text" value={ivtid} onChange={(e) => setIvtid(e.target.value)} />
      </label>
      <label className="form-row">
        Start Date :
        <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
      </label>
      <label className="form-row">
        End Date :
        <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
      </label>
      <button className="form-data" type="submit">데이터 가져오기</button>
    </form>
  );
};

export default Form;