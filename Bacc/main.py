from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json
import traductor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def test_connect():
    print ("conectado")
    # emit('my response', {'data': 'Connected'})

@socketio.on('message')
def handleMessage(msg):
    dic = json.loads(msg)
    if dic["lenguaje"]:
        out=traductor.espa_bin(dic["contenido"])
    else:
        out=traductor.bin_espa(dic["contenido"])
    print(out)
    emit('response', out)

if __name__ == '__main__':
    socketio.run(app)