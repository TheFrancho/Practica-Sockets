import asyncio
import websockets
import json
import traductor

async def server(websocket, path):
    async for message in websocket:
        print(message)
        dic=json.loads(message)
        print(dic)
        if dic["lenguaje"]:
            out=traductor.espa_bin(dic["contenido"])
        else:
            out=traductor.bin_espa(dic["contenido"])
        print(out)
        await websocket.send(out)

start_server = websockets.serve(server, "localhost", 10000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()