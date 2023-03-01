import socket
import threading
import time
import numpy as np
import cv2
file = open("msg.txt", 'w')

def listener():
    global msgList
    msgList = []
    start = time.time()
    while (time.time() - start) < 12:
        data, addr = sock.recvfrom(6000)
        #print(data)
        """if data.decode() == "xxx":
            #print("new frame")
            pass"""
        msgList.append(np.frombuffer(data, dtype=np.uint8))
        print(len(msgList))
    print('done')
    

def reconstruct():
    if msgList:
        #data = []
        print(msgList)
        data = np.concatenate(msgList)
        image = cv2.imdecode(data, flags=cv2.IMREAD_COLOR)
        cv2.imshow("img", image)
        cv2.waitKey(0)
        print(data)
        #file.write(''.join(msgList))
        

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

# msg = ""
listen = threading.Thread(target=listener)
listen.start()
print("ayo")
time.sleep(12)
print("yuh yuh")
reconstruct()



