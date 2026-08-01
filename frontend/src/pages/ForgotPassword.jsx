import { useState } from 'react';
import { Link } from 'react-router-dom';
import api from "../services/api";

function ForgotPassword(){
    const [email, setEmail] = useState('');

    const handleSubmit = async () => {
        try {
            const response = 
            await api.post('/forgotpassword',
                {
                    email
                }
                
            );
            localStorage.setItem(
                "token",
                response.data.access_token 
            );

            alert("Sent Successful");
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
    
    return (
        <div className="forgot-password-container">
            <h2>Reset Password</h2>
            <form onSubmit={handleSubmit}>
                <input type="email" placeholder="Enter your email"
                    value={email} onChange={(e) => setEmail(e.target.value)}
                    required
                />

                <button type="submit">Send Reset Link</button>
            </form>

            <div className="back-to-login">
                <Link to="/login">Back to Login</Link>
            </div>
        </div>
    );
}

export default ForgotPassword;