import React, {useEffect, useState} from 'react';
import "./V1.css"

export default function V1() {
    const [sisas,setSisas]=useState("")
    const [cambia,setCambia]=useState(true)
    const [salida, setSalida]=useState("")
    const socket = new WebSocket("ws://localhost:10000")

    useEffect(()=>{
        socket.addEventListener("open",(e)=>{console.log("ChalocaXD")} )
        socket.addEventListener("close", (e)=>{console.log("Bai")})
        
    },[])

    useEffect(()=>{socket.addEventListener('message', function (event) {
        setSalida(event.data)
        console.log('Message from server ');
    });},[socket])

    const q = (e)=>{
        setSisas(e.target.value)
        asin(e)
    }

    async function asin(e) {
        try {
            let server = await socket.send(JSON.stringify({
                lenguaje : cambia,
                contenido : e.target.value
            }))
            // ... use server
        } catch (error) {
            let server = await socket.send(JSON.stringify({
                lenguaje : cambia,
                contenido : e.target.value
            }))
        }
      }

    return (
        <div id="V1">
           <div id = "Op">
                <div>
                    <div>{cambia?"Español":"Binario"}</div>
                        <input type="text" id="Cajita1" name="Cajita1" placeholder="Ingrese un texto a traducir" 
                        value={sisas} onChange={q}/>
                    </div>
                <div>
                    <div>{cambia?"Binario":"Español"}</div>
                    <input type="text" id="Cajita2" name="Cajita2" placeholder="Mire el resultado de la traducción"
                    value={salida}/>
                </div>
            </div>
            <div><button onClick={()=>setCambia(!cambia)}>Sisas</button></div>
        </div>
    )
}