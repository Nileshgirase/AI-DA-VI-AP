import { useState } from "react";

import api from "../services/api";

import { Link } from "react-router-dom";

import { useNavigate } from "react-router-dom";




function Login(){

    const [email, setEmail] = 
    useState("");

    const [password, setPassword] = useState("");
    
    const navigate = useNavigate();

    const handleLogin = async () => {
        try {
            const response = 
                await api.post("/login",
                    {
                        email,
                        password,
                    }
                );
            localStorage.setItem(
                "token",
                response.data.access_token 
            );

            alert("Login Successful");

            navigate("/dashboard");
        } 
        catch (error)
        {
            console.log(error);
            console.log(error.response);

            if(error.response){
                alert(error.response.data.detail);
            }else{
                alert(error.message);
            }
        }
    };


    return(
        <div>
            <h1>Login</h1>

            <input placeholder="Enter Email"
                onChange={(e) => 
                    setEmail(e.target.value)
                }   
            />

            <input type="password"
                placeholder="Enter Password"
                onChange={(e)=>
                    setPassword(e.target.value)
                }
            />
           
            <div>
                <Link to="/forgotpassword">Forgot Password?</Link>
            </div>

            

            <button type="button" onClick={handleLogin}>Login</button>
            <div className="go-signup">
                <Link to="/signup">New Register?</Link>
            </div>

            
        </div>
    );
}

export default Login;