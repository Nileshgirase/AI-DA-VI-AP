import { useState } from "react";
import api from "../services/api";

function Login(){

    const [email, setEmail] = 
    useState("");

    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        try {
            const response = 
                await api.post("/login",
                    {
                        email,
                        password
                    }
                );
            localStorage.setItem(
                "token",
                response.data.access_token 
            );

            alert("Login Successful");
        } catch{
            alert("Login Failed");
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
                    e.target.value
                }
            />

            <button onclick={handleLogin}>Login</button>
        </div>
    );
}

export default Login;