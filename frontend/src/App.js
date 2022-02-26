import React, { useState } from 'react';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Notifications from './components/Notifications';
import Predictions from './components/Predictions';
import Welcome from './components/Welcome';
import Inventory from './components/Inventory';
import SignIn from './components/SignIn';
import Registration from './components/Registration';

function App() {
  // cheese cuz authentication isn't actually real
  let [username, setUsername] = useState(null);
  // how do i modify menu bar based on signed in

  let signedOut = username === null;
  return (
    <Router>
      <MenuBar username={username} setUserName={setUsername} />
      <Switch>
        <Route path="/notifications">
        {signedOut ? <Redirect to="/" /> : <Notifications />}
        </Route>
        <Route path="/register">
        {signedOut ? <Redirect to="/" /> : <Registration />}
        </Route>
        <Route path="/signin">
        {signedOut ? <Redirect to="/" /> : <SignIn />}
        </Route>
        <Route path="/">
        {signedOut ? <Redirect to="/" /> : <Welcome />}
        </Route>
        <Route path="/inventory">
        {signedOut ? <Redirect to="/" /> : <Inventory />}
        </Route>
      </Switch>
    </Router>
  )

}

export default App;
