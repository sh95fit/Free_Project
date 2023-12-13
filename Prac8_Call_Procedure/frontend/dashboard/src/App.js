import React, { useEffect, useState } from 'react';

const fetchData = async (url) => {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
  return response.json();
};

const App = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchDataFromAPI = async () => {
      try {
        const apiUrl = 'http://localhost:8000';
        const result = await fetchData(`${apiUrl}/api/data`);
        console.log('API Response:', result); // API 응답을 콘솔에 출력
        setData(result);
      } catch (error) {
        console.error('Error in component:', error);
      }
    };

    fetchDataFromAPI();
  }, []);


  return (
    <div>
      <h1>{JSON.stringify(data)}</h1>
    </div>
  );
};

export default App;