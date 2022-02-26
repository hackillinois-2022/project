import React, { useState , useEffect } from 'react'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee } from '@fortawesome/free-solid-svg-icons'
import axios from 'axios'
function InventoryModal({ username, setModalShown }) {


    const getProduceList =  async () => {
        const response = await axios.get(`http://localhost:8080/api/list_inventory`)
        return response.data
    }

    const addProduce = async () => {
        await axios.post(`http://localhost:8080/api/inventory/${username}`, { produceSelected, storeCost }).then((res) => {
            console.log('Adding item...')
            // force re-render
            setModalShown(false)
        })
    }

    const [produceList, setProduceList] = useState([]);
    const [storeCost, setStoreCost] = useState(0);
    const [produceSelected, setProduceSelected] = useState('')
    useEffect(() => {
        getProduceList().then(res => {
            // setLoading(false)
            console.log(res.success, res.data)
            if (res.success) {
                setProduceList(res.data)
                setProduceSelected(res.data[0].name)
            }
        })
    }, [])

    const produceListTags = produceList.map((p, i) => {
        // if (i == 0) {
        //     return <option selected value={p.name}>{p.name}</option>
        // }
        return <option key={p.name} value={p.name}>{p.name}</option>
    })

    return (
        <div className="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
            <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                {/* Background overlay, show/hide based on modal state.

                Entering: "ease-out duration-300"
                    From: "opacity-0"
                    To: "opacity-100"
                Leaving: "ease-in duration-200"
                    From: "opacity-100"
                    To: "opacity-0" */}
                <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>

                {/* This element is to trick the browser into centering the modal contents. */}
                <span className="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

                {/* Modal panel, show/hide based on modal state.

                Entering: "ease-out duration-300"
                    From: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                    To: "opacity-100 translate-y-0 sm:scale-100"
                Leaving: "ease-in duration-200"
                    From: "opacity-100 translate-y-0 sm:scale-100"
                    To: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" */}
                <div className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                    <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                        <div className="sm:flex sm:items-start">
                            <div className="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                                <FontAwesomeIcon icon={faCoffee} />
                            </div>
                            <div className="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                                <h3 className="text-lg leading-6 font-medium text-gray-900" id="modal-title">Add produce</h3>
                                <div className="mt-2">
                                    <select value={produceSelected} onChange={(e) => setProduceSelected(e.target.value)} className="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" aria-label="Default select example">
                                        {produceListTags}
                                    </select>
                                    <div className="mb-4">
                                        <label className="block text-grey-darker text-sm font-bold mb-2" htmlFor="store-cost">
                                            Cost to store per KG
                                        </label>
                                        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" value={storeCost} onChange={(e) => setStoreCost(e.target.value)} id="store-cost" type="text" placeholder="Username"></input>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                        <button type="button" onClick={addProduce} className="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">Add</button>
                        <button type="button" onClick={() => setModalShown(false)} className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm">Cancel</button>
                    </div>
                </div>
            </div>
        </div>
    )

}

export default InventoryModal