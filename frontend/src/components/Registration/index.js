import React, { useState } from 'react'

function Registration() {

    const [username, setUsername] = useState();
    const [number, setNumber] = useState();
    const [password, setPassword] = useState();
    return (
    <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
        <div className="mb-4">
            <label className="block text-grey-darker text-sm font-bold mb-2" for="username">
                Username
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" value={username} onChange={(e) => setUsername(e.target.value)} id="username" type="text" placeholder="Username"></input>
        </div>
        <div className="mb-4">
            <label className="block text-grey-darker text-sm font-bold mb-2" for="username">
                Phone Number
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" value={number} onChange={(e) => setNumber(e.target.value)} id="username" type="text" placeholder="XXX-XXX-XXXX"></input>
        </div>
        <div className="mb-6">
            <label className="block text-grey-darker text-sm font-bold mb-2" for="password">
                Password
            </label>
            <input className="shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3" value={password} onChange={(e) => setPassword(e.target.value)} id="password" type="password" placeholder="******************">
                </input>
            <p className="text-red text-xs italic">Please choose a password.</p>
        </div>
        <div className="flex items-center justify-between">
            <button className="bg-black hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="button">
                Register
            </button>
        </div>
    </div>
  )
}

export default Registration;