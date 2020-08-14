import React, {useState} from 'react';
import { useHistory } from "react-router-dom";
import fetchData from "./fetchData";
import { Form, FormGroup, Label, Input } from 'reactstrap';

function Register() {
    const [state, setState] = useState({
        username: "",
        email: "",
        password: "",
        confirmPassword: ""
    })

    const history = useHistory();

    const handleChange = (e) => {
        const {id , value} = e.target   
        setState(prevState => ({
            ...prevState,
            [id] : value
        }))
    }

    const handleSubmitClick = (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (e.target.checkValidity()) {
            fetchData('https://www.noahtigner.com/auth/api-register', {
                method: 'POST',
                body: JSON.stringify({
                    "username": state.username,
                    // "email": state.email,
                    "password": state.password
                }),
                headers: {"Content-Type": "application/json"}
            }).then(data => {
                console.log("success: ", data);
                history.push("/auth/login");
            }).catch(err => {
                console.log(err);
                alert(err);
            });
        }
        e.target.classList.add('was-validated');
    }

    return(
        <Form className="needs-validation" onSubmit={handleSubmitClick} noValidate>
            <h3>Register</h3>

            <FormGroup>
                <Label>Username</Label>
                <Input 
                    type="text" 
                    className="form-control" 
                    id="username" 
                    placeholder="Enter Username" 
                    value={state.username}
                    onChange={handleChange}
                    required
                />
                {/* <div className="valid-feedback">Valid.</div> */}
                {/* <div className="invalid-feedback">Please fill out this field.</div> */}
            </FormGroup>

            <FormGroup>
                <Label>Email</Label>
                <Input 
                    type="email" 
                    className="form-control" 
                    id="email" 
                    placeholder="Enter Email" 
                    value={state.email}
                    onChange={handleChange}
                    required
                />
            </FormGroup>

            <FormGroup>
                <Label>Password</Label>
                <Input 
                    type="password" 
                    className="form-control" 
                    id="password"
                    placeholder="Enter Password" 
                    value={state.password}
                    onChange={handleChange}
                    required
                />
            </FormGroup>
            
            <FormGroup>
                <Label>Confirm Password</Label>
                <Input 
                    type="password" 
                    className="form-control" 
                    id="confirmPassword" 
                    placeholder="Enter Password" 
                    value={state.confirmPassword}
                    onChange={handleChange}
                    pattern={state.password}
                    required
                />
                <div className="invalid-feedback">Passwords must match</div>
            </FormGroup>

            <br/>
            <button type="submit" className="btn btn-primary btn-block">Submit</button>
        </Form>
    )
}

export default Register;

