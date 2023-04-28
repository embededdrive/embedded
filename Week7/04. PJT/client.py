from websockets.sync.client import connect

ID = "1"
server = "192.168.110.135"
PORT = "8765"

def commu(mod, msg):
    address = "ws://"
    address += server
    address += ":"
    address += PORT
    with connect(address) as websocket:
        while(True):

            websocket.send(ID + ":" + mod + "," + msg)

            message = websocket.recv()

            print(f"Received: {message}")

            return message

def read():
    ret = commu("read", "NULL")
    return ret

def write(send):
    ret = commu("write", send)
    return ret


while(True):
    a, b = input().split(sep="-")
    if a == "read":
        ret = read()
        print(ret)
    elif a == "write":
        ret = write(b)
        print(ret)
