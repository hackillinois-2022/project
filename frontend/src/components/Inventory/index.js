import React, { useState, useEffect } from 'react'
import axios from 'axios'
import InventoryModal from '../InventoryModal'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBasketShopping, faMinus, faLocationPin } from '@fortawesome/free-solid-svg-icons'

function Inventory({ username }) {

    const getData = async () => {
        const response = await axios.get(`http://localhost:8080/api/inventory`, { params: { username }})
        return response.data
    }

    const removeItem = async (item) => {
        await axios.delete(`http://localhost:8080/api/inventory`, { data : { username: username, produceName: item }}).then((res) => {
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
            // console.log(res.success, res.data)
            if (res.success) {
                console.log('setting item list')
                if (res.data == undefined) {
                    setItemList([])
                } else {
                    setItemList(res.data)
                }
            }
            // done updating...
            // toggleUpdate(false)
        })
    }, [update])

    const itemElements = itemList.map((item) => {
        return (
            <li key={item.name} className="p-3 flex flex-row text-center justify-between items-center">
                <div className="flex flex-col">
                    <div>
                    {item.produce_name}
                    </div>
                    <div>
                        <FontAwesomeIcon className="pr-2" icon={faLocationPin} />
                        {item.location == 'LOS ANGELES' ? 'CHAMPAIGN' : item.location}
                    </div>
                </div>
                <button onClick={() => removeItem(item.produce_name)} className="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-red-100 hover:bg-red-700 sm:mx-0 sm:h-10 sm:w-10">
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
                <FontAwesomeIcon icon={faBasketShopping} className="mr-2" /> Add Produce 
            </button>
        </div>
        {modalShown && <InventoryModal setModalShown={setModalShown} update={update} toggleUpdate={toggleUpdate} username={username} />}
        <div className="grid grid-cols-2 gap-2">
            {produceList}
            <div className="">
            </div>
        </div>
    </div>

}

export default Inventory;