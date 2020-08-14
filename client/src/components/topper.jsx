import React from 'react';
import {
    Collapse,
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
} from 'reactstrap';

const Topper = () => {
    return (
        <Navbar light expand="md">
            <NavbarBrand href={"/"}>noahtigner.com</NavbarBrand>

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
    )
}

export default Topper;