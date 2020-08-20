import React from 'react';
// import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css'; 
import { HashRouter as Router, Switch, Route } from "react-router-dom";


// import Login from "./components/login.jsx";
// import Register from "./components/register.jsx";
import Header from "./components/header.jsx";
import Auth from "./components/auth.jsx";
import Portfolio from "./components/portfolio.jsx";


function App() {
    return (
       <React.Fragment>
            <Header/>
            <Router>
                <Switch>
                    <Route path='/auth' component={Auth} />
                    <Route exact path='/' component={Portfolio} />
                </Switch>
            </Router>
        </React.Fragment>
    );
}

export default App;
