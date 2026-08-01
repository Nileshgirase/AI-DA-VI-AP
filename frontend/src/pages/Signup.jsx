import { useState } from "react";
import api from "../services/api";
import { Link } from "react-router-dom";

function Signup(){
    const [username,  setUsername] = useState("");

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const handleSignup = async () => {
        
        try{

            const response = 
            await api.post (
                "/register",
                {
                    username, email, password,
                }
            );
            alert(response.data.message);
        }
        catch (error){
            console.log(error);
            console.log(error.response);

            if (error.response){
                alert(error.response.data.detail);
            } else{
                alert(error.message);
            }
        }
    };
    return(
        <div>
            <h1>Signup</h1>

            <input placeholder="Enter UserName"
                onChange={(e) =>
                    setUsername(e.target.value)
                }
            />

            <input placeholder="Enter Email"
                onChange={(e)=>
                    setEmail(e.target.value)
                }
            />

            <input type="password"
                placeholder="Enter Password"
                onChange={(e)=>
                    setPassword(e.target.value)
                }
            />

            <button onClick={handleSignup}>Signup</button>

            <p>
                Already have an account?
                <Link to="/login">Login</Link>
            </p>
        </div>
    );
}

export default Signup;