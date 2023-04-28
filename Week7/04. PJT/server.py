import asyncio
import threading
from time import sleep
from websockets.server import serve


server = "192.168.110.135"
PORT = "8765"

unread1 = False
buf1 = ""

unread2 = False
buf2 = ""

async def echo(websocket):
    global unread1
    global unread2
    global buf1
    global buf2

    async for message in websocket:
        
        ID, remains = message.split(sep=':')
        cmd, msg = remains.split(sep=',')

        print(f"remains: {remains}")
        print(f"ID: {ID}, command: {cmd}, message: {msg}")

        if int(ID) == 1:
            if cmd == "read":
                if unread1 == True:
                    unread1 = False
                    await websocket.send(buf1)
                else:
                    await websocket.send("no message")

            elif cmd == "write":
                if unread2 == True:
                    await websocket.send("Fail")
                else:
                    unread2 = True
                    buf2 = msg
                    await websocket.send("Suc")


        elif int(ID) == 2:
            if cmd == "read":
                if unread2 == True:
                    unread2 = False
                    await websocket.send(buf2)
                else:
                    await websocket.send("no message")

            elif cmd == "write":
                if unread1 == True:
                    await websocket.send("Fail")
                else:
                    unread1 = True
                    buf1 = msg
                    await websocket.send("Suc")




async def main():
    portnum = int(PORT)
    async with serve(echo, server, portnum):
        await asyncio.Future()

asyncio.run(main())