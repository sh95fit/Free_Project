// import React, { Component } from 'react';

// class ErrorBoundary extends Component {
//   constructor(props) {
//     super(props);
//     this.state = { hasError: false };
//   }

//   static getDerivedStateFromError(error) {
//     return { hasError: true };
//   }

//   componentDidCatch(error, errorInfo) {
//     console.error('Error caught by ErrorBoundary:', error, errorInfo);
//     // 에러를 로깅하거나 다른 처리를 수행할 수 있습니다.
//   }

//   render() {
//     if (this.state.hasError) {
//       return <div>Something went wrong. Please refresh the page.</div>;
//     }

//     return this.props.children;
//   }
// }

// export default ErrorBoundary;


import React, { useState, useEffect } from 'react';

function ErrorBoundary({ children }) {
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    const errorHandler = (error, errorInfo) => {
      console.error('Error caught by ErrorBoundary:', error, errorInfo);
      // 에러를 로깅하거나 다른 처리를 수행할 수 있습니다.
      setHasError(true);
    };

    const cleanup = () => {
      // Clean up any resources or perform actions when the component unmounts
    };

    window.addEventListener('error', errorHandler);

    return () => {
      window.removeEventListener('error', errorHandler);
      cleanup();
    };
  }, []);

  if (hasError) {
    return <div>Something went wrong. Please refresh the page.</div>;
  }

  return children;
}

export default ErrorBoundary;