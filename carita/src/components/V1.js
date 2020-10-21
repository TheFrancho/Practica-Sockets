import React, {useEffect, useState} from 'react'; //Cosas de React
import "./V1.css" //Se importa el css de la página
import io from "socket.io-client"; //Se importan los web sockets del cliente

let socket;

export default function V1() { //Función que se exporta que contiene todo el contendido js y html del front
    const [cadena,setCadena]=useState("") //Variable de React que se encarga de obtener y cambiar el valor de la cadena a traducir
    const [cambia,setCambia]=useState(true) //Variable de React que se encarga de cambiar el lenguaje a traducir
    const [salida, setSalida]=useState("") //Variable de react que se encarga de obtener y dar el valor de la traducción
    const ENDPOINT = "localhost:5000" //Variable de javascript que contiene la dirección de conexión al servidor

    useEffect(()=>{ //Hook de React que se encarga de conectar una única vez con el servidor
        socket = io(ENDPOINT);
    },[])

    useEffect(()=>{ //Hook de React que se encarga de recibir las salidas del servidor y darlas al html 
        socket.on("respuesta", (msg)=>{
            setSalida(msg)
        })
    }, [salida])

    const q = (e)=>{ //Función flecha que se encarga de enviar en tiempo real el trxto a traducir al servidor
        setCadena(e.target.value)
        socket.emit("mensaje", JSON.stringify({
            lenguaje : cambia,
            contenido : e.target.value
        }));
     }

     const b = (e)=>{ //Función flecha que se encarga de limpiar el texto al orpimir el botón de cambiar lenguaje
        setCambia(!cambia)
        setCadena("")
        socket.emit("mensaje", JSON.stringify({
            lenguaje : cambia,
            contenido : ""
        }));
     }

    return ( //Se retorna el contendio html para renderizar en la página
        <div id="V1"> 
           <div id = "Op">
                <div>
                    <div>{cambia?"Español":"Binario"}</div>
                        <input type="text" id="Cajita1" name="Cajita1" placeholder="Ingrese un texto a traducir" 
                        value={cadena} onChange={q}/>
                    </div>
                <div>
                    <div>{cambia?"Binario":"Español"}</div>
                    <input type="text" id="Cajita2" name="Cajita2" placeholder="Mire el resultado de la traducción" readOnly
                    value={salida}/>
                </div>
            </div>  
            <div><button onClick={b}>Cambiar lenguaje</button></div>
        </div>
    )
}