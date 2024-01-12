import React from 'react';
import {BrowserRouter, Route, Routes } from 'react-router-dom';

import ChartDisplay from "./pages/ChartDisplay";
import Login from "./pages/LoginPage";


const App = () => {
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