
import {BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";

import Signup from "./pages/Signup";

import Dashboard from "./pages/Dashboard";

import ForgotPassword from "./pages/ForgotPassword";

import ProtectedRoute from "./routes/ProtectedRoute";

import UploadDataset from "./pages/UploadDataset";

import DatasetAnalysis from "./pages/DatasetAnalysis";

function App() {
  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/login" element={<Login/>}/>

        <Route path="/signup" element={<Signup/>}/>
        
        <Route path="/dashboard" element={
          <ProtectedRoute>
            <Dashboard/>
          </ProtectedRoute>
            }/>

        <Route path="/forgotpassword" element={<ForgotPassword/>}/>

        <Route
          path="/upload"
          element={
            <ProtectedRoute>
              <UploadDataset />
            </ProtectedRoute>
          }
        />

        <Route path="/datasets/:datasetId/analysis"
          element={<DatasetAnalysis/>}>
        </Route>

      </Routes>


    </BrowserRouter>
  );
  
}

export default App;