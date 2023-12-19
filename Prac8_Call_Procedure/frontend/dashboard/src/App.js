import React, { useState, useEffect } from 'react';


const fetchData = async (url) => {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
  return response.json();
};

const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchDataFromAPI = async () => {
      try {
        const apiUrl = 'http://localhost:8000';  // FastAPI 서버의 주소로 수정
        const result = await fetchData(`${apiUrl}/api/data`);
        setData(result);
      } catch (error) {
        console.error('Error in component:', error);
      }
    };

    fetchDataFromAPI();
  }, []);

  return (
    <div>
      <h1>{data !== null ? data : "Loading..."}</h1>
    </div>
  );
};

export default App;