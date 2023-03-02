import socket
import threading
import time
import numpy as np
import cv2

class Reconstruct():
    """listen for messages over udp port and reconstruct them back into the original images"""
    def __init__(self, ip="127.0.0.1", port=5005, packsize=6000):
        self.msgList = []
        self.ip = ip
        self.port = port
        self.packsize = packsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))
        self.listen = threading.Thread(target=self.listener)

    def listener(self):
        msgList = []
        start = time.time()
        while (time.time() - start) < 12:
            data, addr = self.sock.recvfrom(self.packsize)
            # delimit between frames
            """if data.decode() == "xxx":
                #print("new frame")
                pass"""
            self.msgList.append(np.frombuffer(data, dtype=np.uint8))

    def reconstruct(self):
        if self.msgList:
            print(len(self.msgList))
            data = np.concatenate(self.msgList)
            data = np.frombuffer(data, dtype=np.uint8)
            image = cv2.imdecode(data, flags=cv2.IMREAD_COLOR)
            cv2.imshow("image test", image)
            cv2.waitKey(0)


def main():
    recon = Reconstruct()
    recon.listen.start()
    time.sleep(12)
    recon.reconstruct()


if __name__ == "__main__":
    main()
