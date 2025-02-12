import { TextField, Button, Box, Typography, FormControlLabel, Checkbox, Grid } from "@mui/material";

const Signup = () => {
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
       Admin Signup
      </Typography>

      <Grid container spacing={2} sx={{ width: "100%", mb: 2 }}>
        <Grid item xs={6}>
          <TextField 
            placeholder="First Name" 
            variant="outlined" 
            fullWidth 
            InputProps={{ sx: { backgroundColor: "white", borderRadius: 1, color: "#1B3948" } }} 
            sx={{ input: { color: "#1B3948" } }}
          />
        </Grid>
        <Grid item xs={6}>
          <TextField 
            placeholder="Last Name" 
            variant="outlined" 
            fullWidth 
            InputProps={{ sx: { backgroundColor: "white", borderRadius: 1, color: "#1B3948" } }} 
            sx={{ input: { color: "#1B3948" } }}
          />
        </Grid>
      </Grid>

      <TextField 
        placeholder="Email Address" 
        variant="outlined" 
        fullWidth 
        InputProps={{ sx: { backgroundColor: "white", borderRadius: 1, color: "#1B3948" } }} 
        sx={{ mb: 2, input: { color: "#1B3948" } }}
      />

      <TextField 
        placeholder="Confirm Email" 
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

      <TextField 
        placeholder="Confirm Password" 
        type="password" 
        variant="outlined" 
        fullWidth 
        InputProps={{ sx: { backgroundColor: "white", borderRadius: 1, color: "#1B3948" } }} 
        sx={{ mb: 2, input: { color: "#1B3948" } }}
      />

      <FormControlLabel 
        control={<Checkbox sx={{ color: "white" }} />} 
        label={<Typography sx={{ color: "white" }}>Accept Terms and Conditions</Typography>} 
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
         Signup
      </Button>
    </Box>
  );
};

export default Signup;