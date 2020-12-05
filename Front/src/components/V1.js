import React, {useEffect, useState} from 'react'; //Cosas de React
import "./V1.css" //Se importa el css de la página
import io from "socket.io-client"; //Se importan los web sockets del cliente
import TextareaAutosize from 'react-textarea-autosize';

let socket;

export default function V1() { //Función que se exporta que contiene todo el contendido js y html del front
    const [cadena,setCadena]=useState("") //Variable de React que se encarga de obtener y cambiar el valor de la cadena a traducir
    const [cambia,setCambia]=useState(true) //Variable de React que se encarga de cambiar el lenguaje a traducir
    const [salida, setSalida]=useState("") //Variable de react que se encarga de obtener y dar el valor de la traducción
    //const ENDPOINT = "https://practica-sockets-traductor.herokuapp.com/" //Variable de javascript que contiene la dirección de conexión al servidor
    const ENDPOINT = "localhost:5000"

    useEffect(()=>{ //Hook de React que se encarga de conectar una única vez con el servidor
        socket = io(ENDPOINT);
    },[])

    useEffect(()=>{ //Hook de React que se encarga de recibir las salidas del servidor y darlas al html 
        socket.on("respuesta", (msg)=>{
            setSalida(msg)
        })
    }, [salida])

    const q = (e)=>{ //Función flecha que se encarga de enviar en tiempo real el trxto a traducir al servidor
        if (cambia){
            if (/^([A-Za-zñ:,. /\n/])*$/.test(e.target.value)){
                setCadena(e.target.value)
                socket.emit("mensaje", JSON.stringify({
                    lenguaje : cambia,
                    contenido : e.target.value
                }));
            }
        }
        else {
            if (/^([10])*$/.test(e.target.value)){
                setCadena(e.target.value)
                socket.emit("mensaje", JSON.stringify({
                    lenguaje : cambia,
                    contenido : e.target.value
                }));
            }
        }
     }

     const b = (e)=>{ //Función flecha que se encarga de limpiar el texto al orpimir el botón de cambiar lenguaje
        setCambia(!cambia)
        setCadena("")
        setSalida("")
     }

    return ( //Se retorna el contendio html para renderizar en la página
        <div id="V1"> 
           <div id = "Op">
                <div>
                    <div id="texto">{cambia?"Español":"Binario"}</div>
                        <TextareaAutosize 
                            type="text" id="Cajita1" name="Cajita1" 
                            placeholder="Ingrese un texto a traducir" 
                            cols="40"
                            maxRows={20}
                            minRows={10}
                            value={cadena} onChange={q}/>
                    </div>
                <div>
                    <div id="texto">{cambia?"Binario":"Español"}</div>
                    <TextareaAutosize 
                        type="text" 
                        id="Cajita2" 
                        name="Cajita2" 
                        placeholder="Mire el resultado de la traducción"
                        cols="40"
                        maxRows={20}
                        minRows={10}
                        readOnly
                        value={salida}/>
                </div>
            </div>  
            <div><button id="myButton" onClick={b}>Cambiar lenguaje</button></div>
        </div>
    )
}