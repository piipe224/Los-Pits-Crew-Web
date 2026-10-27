import logo from './logo.svg';
import React, { } from 'react';
import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import LandingPage from "./pages/landingpage";
import Login from './pages/auth/login';
import SignUp from './pages/Auth/signup';

function App() {
  return (
    <div className="App">
      <header className="App-header">
          <h1>Los Pits Crew</h1>  
      </header>

      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
