import { useEffect } from 'react';
import './App.css';

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
      Test
    </div>
  );
}

export default App;
