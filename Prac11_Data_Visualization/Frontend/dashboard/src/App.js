import React from 'react';
import './App.css';
import {BrowserRouter, Route, Routes } from 'react-router-dom';


// import ChartDisplay from "./pages/ChartDisplay";
import ChartDisplay from "./pages/ChartDisplayPwr";
import Login from "./pages/LoginPage";


const App = () => {
  return (
        <div>
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<Login />} />
              {/* <Route path="/chart" element={<ChartDisplay />} /> */}
              <Route path="/chart" element={<ChartDisplay />} />
            </Routes>
          </BrowserRouter>
        </div>
  );
};

export default App;