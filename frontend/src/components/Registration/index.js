import React, { useState } from 'react'

import axios from 'axios';

function Registration({ setUsername }) {

    const [username, setLocalUsername] = useState();
    const [email, setEmail] = useState();
    const [password, setPassword] = useState('');
    const [first, setFirst] = useState();
    const [last, setLast] = useState();

    const [errorMessage, setErrorMessage] = useState('')
    const register = async () => {
        console.log('registering...')
        const payload = {username: username, email, firstName: first, lastName: last,  password_val: password}
        const response = (await axios.post('http://localhost:8080/api/register', payload)).data
        if (response.success) {
            setUsername(username);
        } else {
            setErrorMessage(response.message)
        }
    }

    return (
    <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
        <div className="mb-4">
            <label className="block text-grey-darker text-sm font-bold mb-2" htmlFor="username">
                Username
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" value={username} onChange={(e) => setLocalUsername(e.target.value)} id="username" type="text" placeholder="Username"></input>
        </div>
        <div className="mb-4">
            <label className="block text-grey-darker text-sm font-bold mb-2" htmlFor="first">
                First Name
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" value={first} onChange={(e) => setFirst(e.target.value)} id="first" type="text" placeholder="John"></input>
        </div>
        <div className="mb-4">
            <label className="block text-grey-darker text-sm font-bold mb-2" htmlFor="last">
                Last Name
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" value={last} onChange={(e) => setLast(e.target.value)} id="last" type="text" placeholder="Smith"></input>
        </div>
        <div className="mb-4">
            <label className="block text-grey-darker text-sm font-bold mb-2" htmlFor="email">
                Email
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" value={email} onChange={(e) => setEmail(e.target.value)} id="number" type="text" placeholder="abc@def.com"></input>
        </div>
        <div className="mb-6">
            <label className="block text-grey-darker text-sm font-bold mb-2" htmlFor="password">
                Password
            </label>
            <input className="shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3" value={password} onChange={(e) => setPassword(e.target.value)} id="password" type="password" placeholder="******************">
                </input>
            <p className="text-red text-xs italic">{errorMessage}</p>
        </div>
        <div className="flex items-center justify-between">
            <button onClick={register} className="bg-black hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="button">
                Register
            </button>
        </div>
    </div>
  )
}

export default Registration;