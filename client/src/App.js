import React from 'react';
// import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css'; 
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";


// import Login from "./components/login.jsx";
// import Register from "./components/register.jsx";
import Topper from "./components/topper.jsx";
import Auth from "./components/auth.jsx";
import Portfolio from "./components/portfolio.jsx";


function App() {
    return (
       <React.Fragment>
            <Topper/>
            {/* <Router>
                
                <div className="auth-wrapper">
                    <div className="auth-inner">
                        <Switch>
                            <Route exact path='/auth' component={Login} />
                            <Route path="/auth/login" component={Login} />
                            <Route path="/auth/register" component={Register} />
                        </Switch>
                    </div>
                </div>
            </Router> */}
            <Router>
                <Switch>
                    <Route path='/auth' component={Auth} />
                    <Route path='/' component={Portfolio} />
                </Switch>
            </Router>
        </React.Fragment>
    );
}

export default App;
