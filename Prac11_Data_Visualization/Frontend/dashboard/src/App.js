import React, { useEffect } from 'react';
import './App.css';
import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom';
import ChartDisplay from './pages/ChartDisplayPwr';
import Login from './pages/LoginPage';
import { jwtDecode } from 'jwt-decode';

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
        localStorage.removeItem('accessToken');
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
          localStorage.removeItem('accessToken');
          navigate('/');
          return;
        }

        const result = await response.json();

        if (!result.valid) {
          // 토큰이 유효하지 않으면 로그인 페이지로 이동
          localStorage.removeItem('accessToken');
          navigate('/');
          return;
        }

        // 토큰의 만료 시간 확인
        const decodedToken = jwtDecode(accessToken);
        const expirationTimeInSeconds = decodedToken.exp;
        const currentTimeInSeconds = Math.floor(Date.now() / 1000);

        if (expirationTimeInSeconds < currentTimeInSeconds) {
          // 토큰이 만료되었으면 로그인 페이지로 이동
          localStorage.removeItem('accessToken');
          navigate('/');
          return;
        }

      } catch (error) {
        console.error('토큰 검증 에러', error);
        // 검증 중 에러가 발생하면 로그인 페이지로 이동
        localStorage.removeItem('accessToken');
        navigate('/');
      }
    };

    checkTokenValidity();
  }, [navigate]);

  return <ChartDisplay />;
};

export default App;