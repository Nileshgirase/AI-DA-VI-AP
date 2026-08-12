import { useNavigate } from "react-router-dom";

import  { useEffect, useState } from "react";

import api from "../services/api";

function Dashboard() {

    const [user, setUser] = useState(null);
    
    const navigate = useNavigate();

    const logout = () =>{

        localStorage.removeItem("token");
        navigate("/login");
    }

    useEffect(() => {
        getCurrentUser();
    }, []);

    const getCurrentUser = async () => {

        try{

            const token = localStorage.getItem("token");

            const response = await api.get("/me", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            console.log(response.data);
        } catch (error) {
            console.log(error.response);
        }
    };
    return(
        <div>
            <h1>Dashboard</h1>
            
            {user && (
            <>
                <p>Email: {user.sub}</p>
                <p>Expiry: {user.exp}</p>
            </>
         )}
            
            <p>Protected Page</p>

            <button onClick={logout}>Logout</button>
        </div>
    );
}

export default Dashboard;