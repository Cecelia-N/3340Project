import * as React from "react";
import "./Components.css";
import Logo from '../images/Logo1.png';

// importing material UI components
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Button from "@mui/material/Button";


export default function Header() {
  return (
    <AppBar position="static">
      <Toolbar class="Header">
        <div>
          <Button href="./">
            <Logo1 src={Logo} />
          </Button>
          <div display="flex" justify-content="flex-end">
          <Button justify="right" class="GenerateNowRectangle" href="./GenerationPage">
            <div class="GenerateNowText">Shop now</div>
          </Button>
          </div>
        </div>        
      </Toolbar>
    </AppBar>
  );
}
