import React, { Component, useState } from "react";
import ReactMapGL from "react-map-gl";
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
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'



export default class MapPage extends Component {

    constructor(props) {
        super(props);
        this.state = {
            viewport: {
                latitude: 45.794427, 
                longitude: 15.979304,
                zoom: 14,
                bearing: 0,
                pitch: 0
              }
        };        
    }

    

    render() {
        return <Grid container spacing={1}>
        
            <Grid item xs={12} align="center">
                <Typography component="h4" variant="h4">
                    Map page
                </Typography>
            </Grid>

            <Grid item xs={12}>
            <ReactMapGL
                 {...this.state.viewport}
                 width="100vw"
                 height="100vh"
                 mapStyle="mapbox://styles/mapbox/dark-v9"
                 onViewportChange={viewport => this.setState({viewport})}
                 mapboxApiAccessToken="pk.eyJ1IjoidGlzbGphcmljbGVvIiwiYSI6ImNrcGlhaXk0cjBoYmEyb3BjbnIwY3lnc3kifQ.pFnHzkkFObZO7aI-0SFVZQ"
            />
                
            </Grid>

        </Grid>;

    }


}

