// import React, { useState, useEffect } from 'react';


// const fetchData = async (url) => {
//   const response = await fetch(url);
//   if (!response.ok) {
//     throw new Error(`HTTP error! Status: ${response.status}`);
//   }
//   return response.json();
// };

// const App = () => {
//   const [data, setData] = useState(null);

//   useEffect(() => {
//     const fetchDataFromAPI = async () => {
//       try {
//         const apiUrl = 'http://localhost:8000';  // FastAPI 서버의 주소로 수정
//         const result = await fetchData(`${apiUrl}/api/data`);
//         setData(result);
//       } catch (error) {
//         console.error('Error in component:', error);
//       }
//     };

//     fetchDataFromAPI();
//   }, []);

//   return (
//     <div>
//       <h1>{data !== null ? data : "Loading..."}</h1>
//     </div>
//   );
// };

import Header from "./component/Header";
import Home from "./component/Home";
import Dashboard from "./component/Dashboard";
import Analysis from "./component/Analysis";


import {BrowserRouter as Router, Route, Routes} from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<Home />}/>
          <Route path="/dashboard" element={<Dashboard />}/>
          <Route path="/analysis" element={<Analysis />}/>
        </Routes>
      </div>
    </Router>
  )
}


export default App;