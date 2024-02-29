import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';

import './Form.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircleXmark } from '@fortawesome/free-solid-svg-icons';

const Form = ({ onSubmit }) => {
  const [untId, setUntid] = useState("");
  const [pwrId, setPwrId] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const navigate = useNavigate();

  const formatDate = (date) => {
    const formattedDate = new Date(date).toISOString().slice(0, 10).replace(/-/g, "");
    return formattedDate;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Convert date format before calling onSubmit
    const formattedStartDate = formatDate(startDate);
    const formattedEndDate = formatDate(endDate);

    // const ivtListArray = ivtList.split(',').map(item => item.trim());

    onSubmit({ untId, pwrId, startDate: formattedStartDate, endDate: formattedEndDate });
  };

  const handleLogout = () => {
    localStorage.removeItem('accessToken');

    navigate('/');
  }

  return (
    <>
      <form className="form-container" onSubmit={handleSubmit}>
        <label className="form-row">
          UNTID :
          <input type="text" value={untId} onChange={(e) => setUntid(e.target.value)} />
        </label>
        <label className="form-row">
          PWRID :
          <input type="text" value={pwrId} onChange={(e) => setPwrId(e.target.value)} />
        </label>
        <label className="form-row">
          Start Date :
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
        </label>
        <label className="form-row">
          End Date :
          <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
        </label>
        <button className="bt-formData" type="submit">데이터 가져오기</button>
      </form>
      <button className="bt-logout" onClick={handleLogout}><FontAwesomeIcon icon={faCircleXmark} /></button>
    </>
  );
};

export default Form;