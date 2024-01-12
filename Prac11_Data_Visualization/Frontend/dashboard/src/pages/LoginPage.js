import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
// import "./style.css"
import TextField from '@mui/material/TextField'
import Checkbox from "@mui/material/Checkbox"
import Button from '@mui/material/Button'
import FormControlLabel from '@mui/material/FormControlLabel'
import Typography from '@mui/material/Typography'
// import LockOutlineIcon from '@mui/icon-material/LockOutlineIcon'

export default function Loginin() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    if (username === 'admin' && password === '1234') {
      navigate('/chart');
    } else {
      alert('로그인 실패');
    }
  }

  return (

    <div>
      <Typography component="h1" variant="h5">Login</Typography>
      <TextField label="ID" value={username} onChange={(e) => setUsername(e.target.value)} required fullWidth name="email" autoComplete='email' autoFocus/>
      <TextField type="password" label="Password"  value={password} onChange={(e) => setPassword(e.target.value)}  required fullWidth name="password" autoComplete='current-password'/>
      <FormControlLabel control={<Checkbox value="remember" color="primary" />} label="Remember me"/>
      <Button onClick={handleLogin} fullWidth variant="contained" sx={{mt:3, mb:2}}>Login</Button>
    </div>
  );
}