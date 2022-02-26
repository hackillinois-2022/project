import React, { useState, useEffect } from 'react'
import axios from 'axios'
import InventoryModal from '../InventoryModal'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee, faMinus } from '@fortawesome/free-solid-svg-icons'

function Inventory({ username }) {

    const getData = async () => {
        const response = await axios.get(`http://localhost:8080/api/inventory/${username}`)
        return response.data
    }

    const removeItem = async (item) => {
        await axios.post(`http://localhost:8080/api/inventory/${username}`, { username, item }).then((res) => {
            console.log('Removing item...')
            // force re-render
            toggleUpdate(!update)
        })
    }

    const [update, toggleUpdate] = useState(false);
    const [modalShown, setModalShown] = useState(false);
    const [itemList, setItemList] = useState([]);

    useEffect(() => {
        getData().then(res => {
            // setLoading(false)
            console.log(res.success, res.data)
            if (res.success) {
                console.log('setting item list')
                setItemList(res.data)
            }
            // done updating...
            // toggleUpdate(false)
        })
    }, [update])

    const itemElements = itemList.map((item) => {
        return (
            <li key={item.name} className="p-3 flex flex-row text-center justify-between items-center">
                <div className="">
                    {item.name}
                </div>
                <button onClick={() => removeItem(item.name)} className="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-red-100 hover:bg-red-700 sm:mx-0 sm:h-10 sm:w-10">
                    <FontAwesomeIcon icon={faMinus} /> 
                </button>
            </li>
        )
    })
    const produceList = <div className="bg-white rounded-lg shadow">
        <ul className="divide-y divide-gray-100">
            {itemElements}
        </ul>
    </div>
    return <div className="container w-full md:max-w-3xl mx-auto pt-20">
        <div className="w-full flex flex-row justify-between">
            <div className="font-sans">
                <h1 className="font-bold font-sans text-gray-900 pt-6 pb-2 text-3xl md:text-4xl">My Produce</h1>
            </div>
            <button onClick={() => setModalShown(true)} className="bg-blue-500 hover:bg-blue-700 text-white font-bold my-3 px-4 rounded">
                <FontAwesomeIcon icon={faCoffee} /> Add Produce 
            </button>
        </div>
        {modalShown && <InventoryModal setModalShown={setModalShown} username={username} />}
        <div className="grid grid-cols-2 gap-2">
            {produceList}
            <div className="">
            </div>
        </div>
    </div>

}

export default Inventory;