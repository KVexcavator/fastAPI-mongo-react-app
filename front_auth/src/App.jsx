import { useState } from 'react';
import { AuthProvider } from "./AuthContext";
import Register from './Register';
import Login from './Login';
import Users from './Users';
import Message from './Message';

function App() {
  const [showLogin, setShowLogin] = useState(true)
  return (
    <div className="bg-blue-200 flex flex-col justify-center items-center min-h-screen">
      <AuthProvider>
        <h1 className="text-2xl text-blue-800">
          Simple Auth App
        </h1>
        <Message />
        {showLogin ? <Login /> : <Register />}
        <button
          onClick={() => setShowLogin(!showLogin)}
        >
          {showLogin ? "Register" : "Login"}
        </button>
        <hr />
        <Users />
      </AuthProvider>
    </div>
  )
}

export default App
