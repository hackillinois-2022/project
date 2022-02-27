import React, { useState } from 'react'

import {
    BrowserRouter as Router,
    Link
  } from "react-router-dom";

function Welcome({ username }) {
    return (
    <div className="container mx-auto flex flex-col md:flex-row items-center my-12 md:my-24">
		<div className="flex flex-col w-full lg:w-1/2 justify-center items-start pt-12 pb-24 px-6">
			<p className="font-bold text-3xl mb-2">Maximize Your Profits</p>
			<p className="leading-normal mb-4">AgroGen is a system for farmers to improve their profits by predicting the future prices of their produce. </p>
			<Link to="/register" className="bg-transparent hover:bg-black text-black hover:text-white rounded shadow hover:shadow-lg py-2 px-4 border border-black hover:border-transparent">Register</Link>
		</div>
		<div className="w-full lg:w-1/2 lg:py-6 text-center">
            <img className="rounded-2xl" src="https://static.agriculture.com/styles/node_article_image_full_large/s3/s3fs-public/image/2018/11/01/VBaleha-470186603%5B1%5D.jpg"></img>
		</div>
	</div>
    )
}

export default Welcome;