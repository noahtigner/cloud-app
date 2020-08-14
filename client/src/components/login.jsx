import React, {useState} from 'react';
import { useHistory } from "react-router-dom";
import fetchData from "./fetchData";
import { Form, FormGroup, Label, Input } from 'reactstrap';

function Login() {
    const [state, setState] = useState({
        username: "",
        password: ""
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
            fetchData('https://www.noahtigner.com/auth/api-login', {
                method: 'POST',
                body: JSON.stringify({
                    "username": state.username,
                    "password": state.password
                }),
                headers: {"Content-Type": "application/json"}
            }).then(data => {
                console.log("success: ", data);
                history.push("/");
            }).catch(err => {
                console.log(err);
                alert(err);
            });

        }
        e.target.classList.add('was-validated');
    }

    return(
        <Form className="needs-validation" onSubmit={handleSubmitClick} noValidate>
            <h3>Login</h3>

            <FormGroup>
                <Label>Username</Label>
                <Input type="text" 
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
                <Label>Password</Label>
                <Input 
                    type="password" 
                    className="form-control" 
                    id="password" 
                    placeholder="Enter password" 
                    value={state.password}
                    onChange={handleChange}
                    required
                />
                {/* <div className="valid-feedback">Valid.</div> */}
                {/* <div className="invalid-feedback">Please fill out this field.</div> */}
            </FormGroup>
            <br/>
            <button type="submit" className="btn btn-primary btn-block">Submit</button>
        </Form>
    )
}

export default Login;