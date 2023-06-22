import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // StrictMode로 설정되어 있는 경우 디버그 모드에서 UseEffect가 2회 실행되는 이슈가 발생
  // <React.StrictMode>
    // react-router-dom 사용을 위해 앱을 BrowserRouter로 감싸줘야 한다!
    <BrowserRouter>
      <App />
    </BrowserRouter>
  // </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
