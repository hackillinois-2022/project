import React, { useState } from 'react';

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

import Notifications from './components/Notifications';
import Predictions from './components/Predictions';
import Welcome from './components/Welcome';
import Inventory from './components/Inventory';
import SignIn from './components/SignIn';
import Registration from './components/Registration';
import MenuBar from './components/MenuBar';

function App() {
  // cheese cuz authentication isn't actually real
  const [username, setUsername] = useState('bob');
  // how do i modify menu bar based on signed in

  return (
    <Router>
      <MenuBar username={username} setUsername={setUsername} />
      <Routes>
        {(username !== null) &&
        (
          <>
            <Route path="/notifications" element= {<Notifications username={username} />} />
            <Route path="/inventory" element={<Inventory username={username} />} />
          </>
        )
      }
      <Route path="/" element = {<Welcome username={username} />} />
      <Route path="/register" element={<Registration setUsername={setUsername}/>} />
      <Route path="/signin" element={<SignIn setUsername={setUsername}/>} />
        {/* <Route
          path="*"
          element={<Navigate to="/" />}
        /> */}
      </Routes>
    </Router>
  )

}

export default App;
