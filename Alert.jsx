// src/components/Alert.jsx
import React from 'react';
import { Box, Typography } from '@mui/material';

const Alert = ({ title, message, type }) => {
  return (
    <Box sx={{ padding: '10px', backgroundColor: type === 'error' ? 'red' : 'green' }}>
      <Typography variant="h6" color="white">{title}</Typography>
      <Typography color="white">{message}</Typography>
    </Box>
  );
};

export default Alert;