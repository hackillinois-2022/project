import axios from 'axios';
import React, { useState } from 'react'

function SignIn() {

    const [username, setUsername] = useState();
    const [password, setPassword] = useState();

    const signIn = async () => {
        console.log('signing in')
        const response = await axios.post('http://localhost:5000/api/signin', {username, password})
        console.log(response.data)
    }
    return (
    <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
        <div className="mb-4">
            <label className="block text-grey-darker text-sm font-bold mb-2" for="username">
                Username
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" value={username} onChange={(e) => setUsername(e.target.value)} id="username" type="text" placeholder="Username"></input>
        </div>
        <div className="mb-6">
            <label className="block text-grey-darker text-sm font-bold mb-2" for="password">
                Password
            </label>
            <input className="shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3" value={password} onChange={(e) => setPassword(e.target.value)} id="password" type="password" placeholder="******************">
                </input>
        </div>
        <div className="flex items-center justify-between">
            <button onClick={signIn} className="bg-black hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="button">
                Sign In
            </button>
            <a className="inline-block align-baseline font-bold text-sm text-blue hover:text-blue-darker" href="#">
                Forgot Password?
            </a>
        </div>
    </div>
  )
}

export default SignIn