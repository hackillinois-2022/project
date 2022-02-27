import React, { useState, useEffect } from 'react'
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js';
  import { Line } from 'react-chartjs-2';

import axios from 'axios';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );

function Predictions({ username }) {
    const getPredictions = async () => {
        const response = await axios.get(`http://localhost:8080/api/predictions`, { params: { username } })
        return response.data
    }

    const options = {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: false,
            text: 'Chart.js Line Chart',
          },
        },
      };

    const [predictions, setPredictions] = useState({ 'loading...': { 'location': 'new york' , 'predictions': [{'high_price': 0, 'low_price': 0},{'high_price': 0, 'low_price': 0},{'high_price': 0, 'low_price': 0},{'high_price': 'loading...', 'low_price': 'loading...'}]} })
    const tableRows = Object.entries(predictions).map(([item, { location, predictions }]) => {



        let dataObj = null
        let highData = predictions.map(p => p['high_price'])
        let lowData = predictions.map(p => p['low_price'])
        let labels = predictions.map(p => p['date'])

        if (item !== 'loading...') {
            dataObj = {
                labels,
                datasets: [
                    {
                    label: 'High Prediction',
                    data: highData,
                    borderColor: 'rgb(255, 99, 132)',
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    },
                    {
                    label: 'Low Prediction',
                    data: lowData,
                    borderColor: 'rgb(53, 162, 235)',
                    backgroundColor: 'rgba(53, 162, 235, 0.5)',
                    },
                ],
            }
        }
        

        return (
            <tr class="even:bg-gray-100 odd:bg-gray-200 border-b">

                <td class="py-4 px-6 text-sm font-medium text-gray-900 whitespace-nowrap dark:text-black">
                    {item}
                </td>
                <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                    {location}
                </td>
                <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                    {predictions[3]['high_price']}
                </td>
                <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                    {predictions[3]['low_price']}
                </td>
                {item !== 'loading...' ? (<td>
                    <Line options={options} data={dataObj} />;
                </td>) : <td></td>}
            </tr>
        )
    })

    useEffect(() => {
        getPredictions().then(res => {
            // setLoading(false)
            // console.log(res.success, res.data)
            if (res.success) {
                console.log('setting item list')
                setPredictions(res.data)
            }
            // done updating...
            // toggleUpdate(false)
        })
    }, [])

    return (

        <div class="container flex flex-col">

            <div className="text-2xl mb-2 w-full mt-4 flex justify-center align-center">
                <div>Prediction Values
                </div> 
            </div>
            <div class="flex flex-col w-full min-w-full">
                <div class="overflow-x-auto sm:-mx-6">
                    <div class="py-2 min-w-full sm:px-6 lg:px-8 flex align-center justify-center">
                        <div class="overflow-hidden shadow-md sm:rounded-lg lg:w-1/2">
                            <table class="min-w-full">
                                <thead class="bg-slate-100 border-b">
                                    <tr>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Produce
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Location
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Upper Price Prediction
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Lower Price Prediction
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Chart
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {tableRows}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Predictions;