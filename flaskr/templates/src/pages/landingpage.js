import React, { } from "react";
import {Link} from 'react-router-dom';

export default function LandingPage(){

    return (
        <header>
            <div>
                <h1>Los Pits Crew</h1>
            </div>
            <div>
                <p><Link to="/login" className="btn-signin">Iniciar sesión</Link> | <Link to="/signup" className="btn-signup" >Registrarse</Link></p>
            </div>
        </header>
    );
}