import socket
import threading

def listener():
    global msgList
    msgList = []
    while True:
        data, addr = sock.recvfrom(6000)
        print(data)
        if data.decode() == "xxx":
            print("new frame")
        msgList.append(data)
        #print(msgList)

def reconstruct():
    if msgList:
        # print(len(msgList))
        pass

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

# msg = ""
listen = threading.Thread(target=listener)
listen.start()
while True:
    reconstruct()
    

    
