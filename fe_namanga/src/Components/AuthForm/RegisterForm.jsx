/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState } from 'react';
import axios from 'axios';
import './LoginForm.css';
import './RegisterForm.css'
import { FaUserAlt, FaLock } from "react-icons/fa";
import { IoMail } from "react-icons/io5";

const RegisterForm = (props) => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [showPopup, setShowPopup] = useState(false);
    const [verificationCode, setVerificationCode] = useState('');
    const [registrationSuccess, setRegistrationSuccess] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

    const isValidEmail = (email) => /\S+@\S+\.\S+/.test(email);

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            setConfirmPassword('');
        } else if (password.length < 8) {
            alert("Password must be at least 8 characters long.");
            setPassword('');
            setConfirmPassword('');
        } else if (!isValidEmail(email)) {
            alert("Please enter a valid email address.");
            setEmail('');
        } else {
            setIsLoading(true); // Hiển thị popup "loading"
            try {
                const response = await axios.post('http://localhost:8000/api/auth/register/', {
                    username,
                    email,
                    password
                });
                if (response.data.code === "200") {
                    setShowPopup(true); // Show popup for verification code
                } else {
                    alert("Registration failed: username or email already exist");
                    setUsername('');
                    setEmail('');
                    setPassword('');
                    setConfirmPassword('');
                }
            } catch (error) {
                alert("Registration failed: " + error.message);
            } finally {
                setIsLoading(false);
            }
        }
    }

    const handleVerificationSubmit = async () => {
        try {
            setIsLoading(true); // Hiển thị popup "loading"
            const response = await axios.post('http://localhost:8000/api/auth/verify-code/', {
                email,
                verify_code: verificationCode
            });
            if (response.data.code === "200") {
                setRegistrationSuccess(true);
            }
        } catch (error) {
            alert("Verification failed: " + error.message);
        } finally {
            setIsLoading(false);
        }
    }

    return (
        <div className='wrapper'>
            {!registrationSuccess && !isLoading ? (
                <form onSubmit={handleSubmit}>
                    <h1>Register</h1>
                    <div className='input-box'>
                        <input type='text' placeholder='Username' required value={username} onChange={e => setUsername(e.target.value)} />
                        <FaUserAlt className='icon' />
                    </div>
                    <div className='input-box'>
                        <input type='text' placeholder='Gmail' required value={email} onChange={e => setEmail(e.target.value)} />
                        <IoMail className='icon' />
                    </div>
                    <div className='input-box'>
                        <input type='password' placeholder='Password' required value={password} onChange={e => setPassword(e.target.value)} />
                        <FaLock className='icon' />
                    </div>
                    <div className='input-box'>
                        <input type='password' placeholder='Re-enter password' required value={confirmPassword} onChange={e => setConfirmPassword(e.target.value)} />
                        <FaLock className='icon' />
                    </div>

                    <button type='submit'>Register</button>
                </form>
            ) : (
                <div className="popup">
                    {isLoading ? (
                        <p>Loading...</p>
                    ) : (
                        <>
                            <p>Register Successfully!</p>
                            <button onClick={props.toggleForm}>Login</button>
                        </>
                    )}
                </div>
            )}

            {showPopup && !registrationSuccess && !isLoading && (
                <div className="popup">
                    <input type="text" placeholder="Enter verification code" value={verificationCode} onChange={(e) => setVerificationCode(e.target.value)} />
                    <button onClick={handleVerificationSubmit}>Verify</button>
                </div>
            )}

            {!registrationSuccess && !isLoading && (
                <div className='register-link'>
                    <p>Already have an account? <a href="#" onClick={props.toggleForm}>Login</a></p>
                </div>
            )}
        </div>
    );
}

export default RegisterForm;
