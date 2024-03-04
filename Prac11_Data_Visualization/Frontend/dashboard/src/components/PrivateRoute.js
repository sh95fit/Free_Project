import React from 'react';
import { Route, useNavigate } from 'react-router-dom';

const PrivateRoute = ({ element, authenticated, ...rest }) => {
  const navigate = useNavigate();

  if (!authenticated) {
    // 사용자가 인증되지 않은 경우 로그인 페이지로 이동
    navigate('/');
    return null;
  }

  return <Route {...rest} element={element} />;
};

export default PrivateRoute;