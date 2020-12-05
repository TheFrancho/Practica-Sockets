from flask import Flask #Se importa del gestionador de servidores Flask la clase Flask
from flask_socketio import SocketIO, emit #Se importan de los WebSockets de Flask los métodos socketIO y emit 
import json #Se importa el módulo json para traducir las entradas de javascript en diccionarios de python
import traductor #Se importa el código de traductor que realiza el proceso de traducción

app = Flask(__name__) #Se inicializa el servidor de Flask
app.config['SECRET_KEY'] = 'secret!' #Se configura una clave por defecto por necesidad de Flask
socketio = SocketIO(app, cors_allowed_origins="*") #Se inicializan los sockets con base al servidor de Flask

@socketio.on('connect') #Si la conexión recibe un "connect"
def conectado(): #Imprime 
    print ("Cliente conectado al servidor")

@socketio.on('mensaje') #Si la conexión recibe un "mensaje"
def Proceso_Traduccion(msg): #Se realiza el proceso de traducción según el contenido del json de entrada
    dic = json.loads(msg)
    if dic["lenguaje"]:
        out=traductor.espa_bin(dic["contenido"])
    else:
        out=traductor.bin_espa(dic["contenido"])
    emit('respuesta', out)

if __name__ == '__main__': #Se inicializa el programa
    socketio.run(app, debug=True)
    