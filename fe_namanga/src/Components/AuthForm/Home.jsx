/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState } from 'react';
import './LoginForm.css';

const Home = () => {
    const [showConfirmation, setShowConfirmation] = useState(false); // State để kiểm tra hiển thị của popup

    const handleLogout = () => {
        setShowConfirmation(true); // Hiển thị popup xác nhận khi người dùng ấn nút "Đăng xuất"
    };

    const confirmLogout = () => {
        localStorage.removeItem('accessToken'); // Xóa thông tin đăng nhập từ localStorage
        setShowConfirmation(false); // Ẩn popup xác nhận
        window.location.reload(); // Làm mới trang để quay lại trang login
    };

    const cancelLogout = () => {
        setShowConfirmation(false); // Ẩn popup xác nhận
    };

    return (
        <div className='wrapper'>
            <p>Login Successfully!</p>
            <button onClick={handleLogout}>Logout</button>

            {/* Popup xác nhận */}
            {showConfirmation && (
                <div className="confirmation-popup">
                    <p>Are you sure you want to logout?</p>
                    <button onClick={confirmLogout}>Yes</button>
                    <button onClick={cancelLogout}>No</button>
                </div>
            )}
        </div>
    );
}

export default Home;

