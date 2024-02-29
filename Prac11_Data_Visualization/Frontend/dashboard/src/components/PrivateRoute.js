import React from 'react';
import { Route, useNavigate } from 'react-router-dom';

const PrivateRoute = ({ element, authenticated, ...rest }) => {

  const navigate = useNavigate();

  return authenticated ? (
    <Route {...rest} element={element} />
  ) : (
    navigate('/chart')
  );
};

export default PrivateRoute;