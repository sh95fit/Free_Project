import React from 'react';
import {Link} from "react-router-dom";

function Header() {
  return <div className="header">
    <h1>
      <Link to="/">Hun's Dashboard</Link>
    </h1>
    <div className="menu">
      <Link to="/dashboard" className='link'>
        데이터 시각화
      </Link>
      <Link to="/analysis" className='link'>
        데이터 분석
      </Link>
    </div>
  </div>
}

export default Header;