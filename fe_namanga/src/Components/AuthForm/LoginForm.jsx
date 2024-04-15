/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './LoginForm.css';
import { FaUserAlt, FaLock } from "react-icons/fa";
import Home from './Home'; // Import Home component

const LoginForm = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isLoggedIn, setIsLoggedIn] = useState(false); // State để kiểm tra trạng thái đăng nhập

    const isValidEmail = (email) => /\S+@\S+\.\S+/.test(email);

    useEffect(() => {
        const accessToken = localStorage.getItem('accessToken');
        if (accessToken) {
            setIsLoggedIn(true);
        }
    }, []); // Effect này chỉ chạy một lần sau khi component được render lần đầu tiên

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!isValidEmail(email)) {
          alert("Please enter a valid email address.");
          setEmail('');
          return;
        }

        if (password.length < 8) {
          alert("Password must be at least 8 characters long.");
          setPassword('');
          return;
        }

        try {
          const response = await axios.post('http://localhost:8000/api/auth/login/', {
            email,
            password
          });

          if (response.data.access) {
            alert("Login Success!");
            localStorage.setItem('accessToken', response.data.access);
            setIsLoggedIn(true); // Đặt trạng thái đăng nhập thành true
          } else {
            alert("Login failed: Email or Password invaid");
            setEmail('');
            setPassword('');
          }
        } catch (error) {
          alert("Login failed: Email or Password invaid");
          setEmail('');
          setPassword('');
        }
    }

    // Nếu đã đăng nhập thành công, chuyển đến trang Home
    if (isLoggedIn) {
      return <Home />;
    }

    return (
        <div className='wrapper'>
            <form onSubmit={handleSubmit}>
                <h1>Login</h1>
                <div className='input-box'>
                    <input type='text' placeholder='Email' required value={email} onChange={e => setEmail(e.target.value)} />
                    <FaUserAlt className='icon' />
                </div>
                <div className='input-box'>
                    <input type='password' placeholder='Password' required value={password} onChange={e => setPassword(e.target.value)} />
                    <FaLock className='icon' />
                </div>

                <div className='remember-forgot'>
                    <label><input type='checkbox'/>Remember me</label>
                    <a href='#'>Forgot password?</a>
                </div>

                <button type='submit'>Login</button>
                
                <div className='register-link'>
                    <p>Don't have an account? <a href="#" onClick={props.toggleForm}>Register</a></p>
                </div>
            </form>
        </div>
    )
}

export default LoginForm;


