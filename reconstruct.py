import socket
import threading
import time
import numpy as np
import cv2
import pickle

class Reconstruct():
    """listen for messages over udp port and reconstruct them back into the original images"""
    def __init__(self, ip="127.0.0.1", port=5005, packsize=100000):
        self.msgList = []
        self.ip = ip
        self.port = port
        self.packsize = packsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))
        self.listen = threading.Thread(target=self.listener)

    def listener(self):
        #msgList = []
        #start = time.time()
        while True:
            self.data, addr = self.sock.recvfrom(self.packsize)
            # data = data[0]
            # data = pickle.loads(data)
            # data = cv2.imdecode(data, cv2.IMREAD_COLOR)
            # cv2.imshow("image", data)
            # cv2.waitKey(30)
            # self.msgList = data
            # self.msgList.append(np.frombuffer(data, dtype=np.uint8))

    def reconstruct(self):
        while True:
            # print(len(self.msgList))
            # data = np.concatenate(self.msgList)
            # data = self.msgList
            # data = np.frombuffer(self.data, dtype=np.uint8)
            data = pickle.loads(self.data)
            image = cv2.imdecode(data, flags=cv2.IMREAD_COLOR)
            cv2.imshow("image test", image)
            cv2.waitKey(30)
            # self.msgList = []


def main():
    recon = Reconstruct()
    recon.listen.start()
    #time.sleep(12)
    recon.reconstruct()


if __name__ == "__main__":
    main()
