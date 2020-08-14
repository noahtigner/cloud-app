import React from 'react';
// import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    Container,
    Row,
    Col,
    Jumbotron,
    Button
} from 'reactstrap';

import Login from "./components/login.jsx";
import Register from "./components/register.jsx";


function App() {
    return (
        <Router>
            {/* <nav className="navbar navbar-expand-lg navbar-light fixed-top">
                <div className="container">
                    <Link className="navbar-brand" to={"/auth/login"}>noahtigner.com</Link>
                    <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
                        <ul className="navbar-nav active">
                            <li className="nav-item">
                                <Link className="nav-link" to={"/auth/login"}>Login</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to={"/auth/register"}>Register</Link>
                            </li>
                        </ul>
                    </div> 
                </div>
            </nav> */}
            <Navbar color="inverse" light expand="md">
                <NavbarBrand href={"/auth/login"}>noahtigner.com</NavbarBrand>
                
                <Collapse isOpen={true} navbar>
                    <Nav className="ml-auto" navbar>
                        <NavItem>
                            <NavLink href={"/auth/login"}>Login</NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href={"/auth/register"}>Register</NavLink>
                        </NavItem>
                    </Nav>
                </Collapse>
            </Navbar>

            <div className="auth-wrapper">
                <div className="auth-inner">
                    <Switch>
                        <Route exact path='/auth' component={Login} />
                        <Route path="/auth/login" component={Login} />
                        <Route path="/auth/register" component={Register} />
                    </Switch>
                </div>
            </div>
        </Router>

    );
}

export default App;
