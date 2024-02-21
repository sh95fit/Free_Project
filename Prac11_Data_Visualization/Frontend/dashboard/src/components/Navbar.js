import React from 'react';
import Form from './Form';

import './Navbar.css';

const Navbar = ({ onSubmit }) => {
  return (
    <div className = "navbar">
      <Form onSubmit={ onSubmit } />
    </div>
  )
}

export default Navbar;