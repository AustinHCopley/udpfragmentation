import socket
import cv2
import pickle
#import numpy as np
from sys import getsizeof

class Fragment():
    """fragment an opencv image into smaller datagrams, and send them via udp port"""
    def __init__(self, ip="127.0.0.1", port=5005, packsize=100000):
        self.ip = ip
        self.port = port
        self.packsize = packsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.packsize)

    def fragment(self, data):
        framesize = getsizeof(data)
        # split the frame into datagrams
        for x in range( framesize // self.packsize + 1 ):
            self.sock.sendto(data[x*self.packsize : x*self.packsize+self.packsize], (self.ip, self.port))


def main():
    frag = Fragment()

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    while ret:
        ret, frame = cap.read()

        ret2, buff = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
        #string_data = buff.tobytes()
        string_data = pickle.dumps(buff)
        frag.fragment(string_data)


if __name__ == "__main__":
    main()