import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import { Link } from "react-router-dom";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";

export default class HomePage2 extends Component {
  default_var = "500";
  
  constructor(props) {
    super(props);
    this.state = {
      variable: this.default_var,
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleButtonClick = this.handleButtonClick.bind(this);
  }

  handleChange(e){
    this.setState({
     variable: e.target.value,
    });
  }

  handleButtonClick(){
    console.log(this.state);

    const requestOptions = {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        date_time: "2018-11-20T15:58:44.767594-06:00",
      })
    };
    fetch("/api/routes/", requestOptions)
    .then((response) => response.json())
    .then((data) => console.log(data));
  } 

  render() {
    
    

    return <Grid container spacing={1}>
      <Grid item xs={12} align="center">
        <Typography component="h4" variant="h4">
          Nova Pocetna {this.state.variable}
        </Typography>
      </Grid>

      <Grid item xs={12} align="center">
      <FormControl>
            <FormHelperText>
              Explanation text {this.state.variable}
            </FormHelperText>
            <TextField
              required={true}
              type="number"        
              onChange={this.handleChange}   
              defaultValue={this.default_var}
              inputProps={{
                min: 1,
                style: { textAlign: "center" },
              }}
            />       
            <TextField  
              value={this.state.variable}      
              
              inputProps={{
                style: { textAlign: "center" },
              }}
            />        
          </FormControl>         
        </Grid>

      <Grid item xs={12} align="center">
        <Button 
          color="secondary" 
          variant="contained" 
          onClick={this.handleButtonClick}> 
          Create new route
        </Button>
        <Button color="primary" variant="contained" to="/" component={Link}>
          Back
        </Button>        
      </Grid>
    </Grid>;
  }
}
