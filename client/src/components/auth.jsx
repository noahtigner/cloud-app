import React from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import Login from "./login.jsx";
import Register from "./register.jsx";

const Auth = () => {
    return (
        <Router>
            
            <div className="auth-wrapper">
                <div className="auth-inner">
                    <Switch>
                        <Route exact path='/auth' component={Login} />
                        <Route exact path="/auth/login" component={Login} />
                        <Route exact path="/auth/register" component={Register} />
                    </Switch>
                </div>
            </div>
        </Router>
    )
}

export default Auth;
