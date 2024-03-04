import React, { useEffect } from 'react';
import './App.css';
import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom';
import ChartDisplay from './pages/ChartDisplayPwr';
import Login from './pages/LoginPage';

const App = () => {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
          {/* ChartDisplay 페이지에서만 토큰 유효성 검증을 수행 */}
          <Route path="/chart/*" element={<ProtectedChartDisplay />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
};

const ProtectedChartDisplay = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const checkTokenValidity = async () => {
      const accessToken = localStorage.getItem('accessToken');
      if (!accessToken) {
        // 토큰이 없으면 로그인 페이지로 이동
        navigate('/');
        return;
      }

      try {
        const response = await fetch('http://localhost:8000/auth/validate-token', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`,
          },
          body: JSON.stringify({ token: accessToken }),
        });

        if (!response.ok) {
          // 토큰이 유효하지 않으면 로그인 페이지로 이동
          navigate('/');
        }
      } catch (error) {
        console.error('토큰 검증 에러', error);
        // 검증 중 에러가 발생하면 로그인 페이지로 이동
        navigate('/');
      }
    };

    checkTokenValidity();
  }, [navigate]);

  return <ChartDisplay />;
};

export default App;