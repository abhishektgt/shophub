import './App.css';
import HomePage from './homepage.js';
import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Signup from './signup.js';
import Login from './login.js';
import Homepage from './homepage.js';





function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<Signup />} />
          <Route path= "/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/homepage" element={<Homepage />} /> 
        </Routes>

      </Router>
  );
}

export default App;
