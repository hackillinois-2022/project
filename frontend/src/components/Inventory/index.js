import React, { useState, useEffect } from 'react'
import axios from 'axios'

function Inventory({ username }) {

    const getData = async () => {
        const response = await axios.get(`http://localhost:5000/api/inventory/${username}`)
        return response.data
    }

    const [loading, setLoading] = useState(true);

    const loadingPage = <div>loading</div>
    const [itemList, setItemList] = useState([]);

    useEffect(() => {
        let mounted = true;
        getData().then(res => {
            // setLoading(false)
            console.log(res.success, res.data)
            if (res.success) {
                if(mounted) {
                    console.log('setting item list')
                    setItemList(res.data)
                }
            }
            return () => mounted = false
        })
    }, [])
    
    return <div className="bg-white rounded-lg shadow lg:w-1/3">
        <ul className="divide-y divide-gray-100">
            {itemList.map((item) => {
            <li className="p-3 hover:bg-blue-600 hover:text-blue-200">
                {item.name}
            </li>
            })}
        </ul>
    </div>

}

export default Inventory;