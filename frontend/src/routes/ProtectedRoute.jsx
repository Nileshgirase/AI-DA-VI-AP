import { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import api from "../services/api";

function ProtectedRoute({ children }) {

   const [loading, setLoading] = useState(true);

   const [authenticated, setAuthenticated]= useState(false);

   useEffect(() => {

      const checkUser = async () => {
         const token = localStorage.getItem("token");

         if (!token) {
            setAuthenticated(false);
            setLoading(false);
            return;
         }
         try{
            const response = await api.get("/me",{
               headers: {
                  Authorization:`Bearer ${token}`,
               },
            });
         
            console.log("User:",response.data);
            setAuthenticated(true);
         
         }catch(error) {
            console.log("Authentication request failed::",error);

            localStorage.removeItem("token");
            setAuthenticated(false);
         }
         finally{
            setLoading(false);
         }
      };
      checkUser(); 
         
   }, []);

   if (loading) {
      return <h2>Checking Authentication....</h2>;
   }
   return authenticated
      ? children
      : <Navigate to="/Login" replace/>;
}

export default ProtectedRoute;