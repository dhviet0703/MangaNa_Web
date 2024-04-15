// import './App.css';
// import LoginForm from './Components/AuthForm/LoginForm';
// import RegisterForm from './Components/AuthForm/RegisterForm'

// function App() {
//   return (
//     <div>
//       <LoginForm />
//     </div>
//   );
// }

// export default App;

import React, { useState } from 'react';
import './App.css';
import LoginForm from './Components/AuthForm/LoginForm';
import RegisterForm from './Components/AuthForm/RegisterForm';

function App() {
  const [isLogin, setIsLogin] = useState(true);

  const toggleForm = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div>
      {isLogin ? <LoginForm toggleForm={toggleForm} /> : <RegisterForm toggleForm={toggleForm} />}
    </div>
  );
}

export default App;
