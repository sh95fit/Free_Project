import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
// import "./style.css"
import TextField from '@mui/material/TextField'
import Checkbox from "@mui/material/Checkbox"
import Button from '@mui/material/Button'
import FormControlLabel from '@mui/material/FormControlLabel'
import Typography from '@mui/material/Typography'
import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import Link from '@mui/material/Link'
import Grid from '@mui/material/Grid'
import Avatar from '@mui/material/Avatar'
import Box from '@mui/material/Box'
import Container from '@mui/material/Container'

import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

export default function Login() {
  const [loginUsername, setLoginUsername] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await axios.post("http://localhost:8000/auth/login", {
          grant_type: "",
          username: loginUsername,
          password: loginPassword,
          scope: "",
          client_id: "",
          client_secret: "",
        },
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        }
      );

      // const { access_token, username } = response.data;
      const { access_token } = response.data;
      // 토큰 디코딩하여 만료 시간 확인
      const decodedToken = jwtDecode(access_token);

      // 만료 시간 확인
      const expirationTimeInSeconds = decodedToken.exp;
      const currentTimeInSeconds = Math.floor(Date.now() / 1000);

      const handleLogout = () => {
        localStorage.removeItem('accessToken');
        navigate('/');
      }

      if (expirationTimeInSeconds < currentTimeInSeconds) {
        // 토큰 만료
        console.log("토큰이 만료되었습니다");
        alert('로그인 실패');
        handleLogout();
      } else {
        // 토큰이 유효함
        localStorage.setItem('accessToken', access_token);
        navigate('/chart');
      }
    } catch(error) {
      console.error('Login failed', error);
      alert('로그인 실패');
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Avatar sx={{m:1, bgcolor:'secondary.main'}}><LockOutlinedIcon /></Avatar>
        <Typography component="h1" variant="h5">Login</Typography>
        <TextField label="ID" value={loginUsername} onChange={(e) => setLoginUsername(e.target.value)} required fullWidth name="username" autoComplete='id' autoFocus margin="normal"/>
        <TextField type="password" label="Password"  value={loginPassword} onChange={(e) => setLoginPassword(e.target.value)}  required fullWidth name="password" autoComplete='current-password'/>
        <FormControlLabel control={<Checkbox value="remember" color="primary" />} label="Remember me"/>
        <Button onClick={handleLogin} fullWidth variant="contained" sx={{mt:3, mb:2}}>Login</Button>
        <Grid container>
          <Grid item xs>
            <Link>
              Forgot password?
            </Link>
          </Grid>
          <Grid item>
            <Link>
              Sign Up
            </Link>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
}