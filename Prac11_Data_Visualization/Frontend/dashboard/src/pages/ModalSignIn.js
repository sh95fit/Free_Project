import React from 'react';
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

const ModalForgotPw = ({ open, handleClose }) => {
  return (
    <Modal open={open} onClose={handleClose}>
      <Box
        sx={{
          position: 'absolute',
          width: 400,
          bgcolor: 'background.paper',
          border: '2px solid transparent',
          borderRadius: '5px',
          boxShadow: 24,
          p: 2,
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          textAlign: 'left',
        }}
      >
        <Typography style={{fontSize: '16px'}} component="div" mb={2}>
          ICT사업부 개발팀으로 문의 바랍니다.
        </Typography>
        <div style={{ textAlign: 'right' }}>
        <Button variant="contained" onClick={handleClose}>
          Close
        </Button>
        </div>
      </Box>
    </Modal>
  );
};

export default ModalForgotPw;