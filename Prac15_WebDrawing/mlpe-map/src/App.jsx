import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginForm from './components/Login/LoginForm';
import DashboardForm from './components/Login/DashboardForm';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/main" element={<DashboardForm />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
