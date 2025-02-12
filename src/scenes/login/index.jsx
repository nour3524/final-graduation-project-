import { TextField, Button, Box, Typography, FormControlLabel, Checkbox } from "@mui/material";

const Login = () => {
  return (
    <Box 
      display="flex" 
      flexDirection="column" 
      alignItems="center" 
      justifyContent="center" 
      height="100vh"
      width="50%"
      mx="auto"
    >
      <Typography variant="h4" sx={{ fontWeight: "bold", mb: 3, color: "white" }}>
         Admin Login
      </Typography>

      <TextField 
        placeholder="Email Address" 
        variant="outlined" 
        fullWidth 
        InputProps={{ sx: { backgroundColor: "white", borderRadius: 1, color: "#1B3948" } }} 
        sx={{ mb: 2, input: { color: "#1B3948" } }}
      />

      <TextField 
        placeholder="Password" 
        type="password" 
        variant="outlined" 
        fullWidth 
        InputProps={{ sx: { backgroundColor: "white", borderRadius: 1, color: "#1B3948" } }} 
        sx={{ mb: 2, input: { color: "#1B3948" } }}
      />

      <FormControlLabel 
        control={<Checkbox sx={{ color: "white" }} />} 
        label={<Typography sx={{ color: "white" }}>Remember Me</Typography>} 
        sx={{ alignSelf: "flex-start", mb: 2 }} 
      />

      <Button 
        variant="contained" 
        sx={{
          backgroundColor: "#2D5265", 
          color: "white", 
          padding: "12px 20px", 
          borderRadius: 1, 
          width: "100%",
          "&:hover": { backgroundColor: "#1B3948" }
        }}
      >
        SIGN IN
      </Button>
    </Box>
  );
};

export default Login;