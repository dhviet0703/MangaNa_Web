/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react';
import './LoginForm.css';
import { FaUserAlt, FaLock,  } from "react-icons/fa";
import { IoMail } from "react-icons/io5";

const RegisterForm = (props) => {
    return (
        <div className='wrapper'>
            <form action='POST'>
                <h1>Register</h1>
                <div className='input-box'>
                    <input type='text' placeholder='Username' required />
                    <FaUserAlt className='icon' />
                </div>
                <div className='input-box'>
                    <input type='text' placeholder='Gmail' required />
                    <IoMail className='icon' />
                </div>
                <div className='input-box'>
                    <input type='password' placeholder='Password' required />
                    <FaLock className='icon' />
                </div>
                <div className='input-box'>
                    <input type='password' placeholder='Repiedre-enter password' required />
                    <FaLock className='icon' />
                </div>

                <button type='submit'>Register</button>

                <div className='register-link'>
                    <p>Already have an account? <a href="#" onClick={props.toggleForm}>Login</a></p>
                </div>

            </form>
        </div>
    )
}

export default RegisterForm