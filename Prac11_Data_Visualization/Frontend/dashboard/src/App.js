import React, { useEffect } from 'react';
import './App.css';
import {BrowserRouter, Route, Routes } from 'react-router-dom';


// import ChartDisplay from "./pages/ChartDisplay";
import ChartDisplay from "./pages/ChartDisplayPwr";
import Login from "./pages/LoginPage";


const App = () => {

  useEffect(() => {
    const checkTokenValidity = async () => {
      const accessToken = localStorage.getItem('accessToken');
      if (accessToken) {
        const response = await validateToken(accessToken);
        if (!response.valid){
          logout();
        }
      }
    };

    checkTokenValidity();
  }, []);

  const validateToken = async (token) => {
    try {
      const response = await fetch('http://localhost:8000/auth/validate-token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({token})
      });

      if (response.ok) {
        return response.json();
      } else {
        throw new Error('토큰 검증 실패');
      }
    } catch (error) {
      console.error('토큰 검증 에러', error);
      return {valid:false};
    }
  };

  const logout = () => {
    localStorage.removeItem('accessToken');
    // 로그아웃 후 리다이렉트 처리
  }

  return (
        <div>
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<Login />} />
              <Route path="/chart" element={<ChartDisplay />} />
            </Routes>
          </BrowserRouter>
        </div>
  );
};

export default App;