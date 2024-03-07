import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
// import "./style.css"

import "./LoginPage.css"
import ModalForgotPw from './ModalForgotPw';
import ModalSignIn from './ModalSignIn';

import TextField from '@mui/material/TextField'
import Checkbox from "@mui/material/Checkbox"
import Button from '@mui/material/Button'
import FormControlLabel from '@mui/material/FormControlLabel'
import Typography from '@mui/material/Typography'
// import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
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
  const [rememberMe, setRememberMe] = useState(false);
  const [modalPw, setModalPw] = useState(false);
  const [modalSignIn, setModalSignIn] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    // 페이지 진입 시 localStorage에서 저장된 정보를 읽어와서 상태에 설정
    const storedUsername = localStorage.getItem('rememberedUsername');
    const storedRememberMe = localStorage.getItem('rememberMe') === 'true';

    if (storedUsername) {
      setLoginUsername(storedUsername);

      if (storedRememberMe){
        setRememberMe(storedRememberMe);

        document.getElementById('password-input').focus();
      }
    }
  }, []);

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

      // 로그인 성공 시 rememberMe가 체크된 경우 localStorage에 아이디 저장
      if (rememberMe){
        localStorage.setItem('rememberedUsername', loginUsername);
        localStorage.setItem('rememberMe', 'true');
      } else {
        // 체크되지 않은 경우 저장된 정보 삭제
        localStorage.removeItem('rememberedUsername');
        localStorage.removeItem('rememberMe');
      }

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

  const handleOpenModalPw = () => {
    setModalPw(true);
  }

  const handleCloseModalPw = () => {
    setModalPw(false);
  }

  const handleOpenModalSignIn = () => {
    setModalSignIn(true);
  }

  const handleCloseModalSignIn = () => {
    setModalSignIn(false);
  }

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: '30px',
          top: '50%',
          left: '50%',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Avatar sx={{m:1,
          bgcolor:'white',
          width: '400px',
          height: '400px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          marginBottom: '-50px',
        }}>
          <img src="./assets/logo.jpg" alt="MORE" style={{ width: '100%', height: '100%' }} />
        </Avatar>
        {/* <Typography component="h1" variant="h5" marginBottom={'30px'} fontWeight={'600'} fontSize={'24px'} style={{ textAlign: 'center'}}>Login</Typography> */}
        <TextField label="ID" value={loginUsername} onChange={(e) => setLoginUsername(e.target.value)} required fullWidth name="username" autoComplete='id' autoFocus margin="normal"/>
        <TextField id='password-input' type="password" label="Password"  value={loginPassword} onChange={(e) => setLoginPassword(e.target.value)}  required fullWidth name="password" autoComplete='current-password'/>
        <FormControlLabel control={<Checkbox value="remember" color="primary" checked={rememberMe} onChange={(e) => setRememberMe(e.target.checked)} />} label="Remember me"/>
        <Button onClick={handleLogin} fullWidth variant="contained" sx={{mt:3, mb:2}}>Login</Button>
        <Grid container>
          <Grid item xs>
            <Link onClick={handleOpenModalPw} className="login-option">
              Forgot password?
            </Link>
            <ModalForgotPw open={modalPw} handleClose={handleCloseModalPw} />
          </Grid>
          <Grid item>
            <Link onClick={handleOpenModalSignIn} className="login-option">
              Sign Up
            </Link>
            <ModalSignIn open={modalSignIn} handleClose={handleCloseModalSignIn} />
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
}