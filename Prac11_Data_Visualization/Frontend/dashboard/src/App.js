import React, { useEffect, useCallback } from 'react';
import './App.css';
import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom';
import ChartDisplay from './pages/ChartDisplayPwr';
import Login from './pages/LoginPage';
import { jwtDecode } from 'jwt-decode';

import axios from 'axios';

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

  const refreshAccessToken = useCallback(async (refreshToken) => {
    try {
      const refreshResponse = await axios.post(
        'http://localhost:8000/auth/refresh-token',
        { refresh_token: refreshToken },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        },
      );

      if (refreshResponse.status !== 200) {
        throw new Error('리프레시 토큰 갱신 실패');
      }

      const refreshResult = await refreshResponse.data;

      if (!refreshResult.access_token) {
        throw new Error('엑세스 토큰 갱신 실패');
      }

      // 새로 받은 엑세스 토큰으로 로컬 스토리지 갱신
      localStorage.setItem('accessToken', refreshResult.access_token);
    } catch (error) {
      console.error('토큰 갱신 에러', error);
      throw error; // 갱신 중 에러가 발생하면 에러를 다시 던져서 처리
    }
  }, []);

  useEffect(() => {
    const checkTokenValidity = async () => {
      const accessToken = localStorage.getItem('accessToken');
      const refreshToken = localStorage.getItem('refreshToken');

      try {
        // 토큰의 만료 시간 확인
        const decodedToken = jwtDecode(accessToken);
        const expirationTimeInSeconds = decodedToken.exp;
        const currentTimeInSeconds = Math.floor(Date.now() / 1000);

        if (expirationTimeInSeconds < currentTimeInSeconds && refreshToken) {
          // 토큰이 만료되었으면 리프레시 토큰으로 엑세스 토큰 갱신
          await refreshAccessToken(refreshToken);
        } else {
          // 토큰이 만료되지 않았거나 리프레시 토큰이 없으면 /chart 페이지로 이동
          navigate('/chart');
        }
      } catch (error) {
        console.error('토큰 검증 에러', error);
        // 검증 중 에러가 발생하면 로그인 페이지로 이동
        localStorage.removeItem('accessToken');
        navigate('/');
      }

      if (!accessToken) {
        // 토큰이 없으면 로그인 페이지로 이동
        localStorage.removeItem('accessToken');
        navigate('/');
        return;
      }
    };

    checkTokenValidity();
  }, [navigate, refreshAccessToken]);

  return <ChartDisplay />;
};

export default App;