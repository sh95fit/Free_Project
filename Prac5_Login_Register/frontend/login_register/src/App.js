import { useEffect } from 'react';
import './App.css';
import {Routes, Route, Link} from "react-router-dom";
import Find from "./pages/auth_pages/Find";
import Login from "./pages/auth_pages/Login";
import SignUp from "./pages/auth_pages/SignUp";
import Withdrawal from "./pages/auth_pages/Withdrawal";


function App() {

  useEffect(() => {
      fetch("/auth/test").then(
        res => res.json()
      ).then(
        data => {
          console.log(data);
        }
      );
    }, [])

  return (
    <div className="App">
      <Link to="/signup">Sign Up</Link> | <Link to="/Login">Login</Link> | <Link to="/find">Find ID/PW</Link> |  <Link to="/withdrawal">Withdrawal</Link>
      <Routes>
        <Route path="/signup" element={<SignUp/>} />
        <Route path="/Login" element={<Login/>} />
        <Route path="/find" element={<Find/>} />
        <Route path="/withdrawal" element={<Withdrawal/>} />
      </Routes>
    </div>
  );
}

export default App;
