import { useNavigate } from "react-router-dom";

const navigate = useNavigate();

const logout = () =>{
    localStorage.removeItem("token");
    navigate("/login")
}

function Dashboard() {
    const logout = () => {
        localStorage.removeItem(
            "token"
        );
        window.location.href = "login";
    };
    return(
        <div>
            <h1>Dashboard</h1>
            
            
            
            <p>Protected Page</p>

            <button onClick={logout}>Logout</button>
        </div>
    );
}

export default Dashboard;