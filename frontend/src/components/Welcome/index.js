import React, { useState } from 'react'

function Welcome({ username }) {
    let msg = username ? 'welcome back ' + username : username
    return <div>{msg}</div>
}

export default Welcome;