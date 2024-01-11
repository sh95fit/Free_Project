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

  const handleSubmit = (e) => {
    e.preventDefault();

    // Convert date format before calling onSubmit
    const formattedStartDate = formatDate(startDate);
    const formattedEndDate = formatDate(endDate);

    onSubmit({ untid, ivtid, startDate: formattedStartDate, endDate: formattedEndDate });
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
        <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
      </label>
      <label>
        End Date:
        <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
      </label>
      <button type="submit">Fetch Data</button>
    </form>
  );
};

export default Form;