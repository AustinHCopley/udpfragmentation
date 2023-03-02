import socket
import cv2
import numpy as np
from sys import getsizeof

class Fragment():
    """fragment an opencv image into smaller datagrams, and send them via udp port"""
    def __init__(self, ip="127.0.0.1", port=5005, packsize=6000):
        self.ip = ip
        self.port = port
        self.packsize = packsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def fragment(self, data):
        framesize = getsizeof(data)
        # split the frame into 6KB datagrams
        for x in range( framesize // self.packsize + 1 ):
            self.sock.sendto(data[x*self.packsize : x*self.packsize+self.packsize], (self.ip, self.port))
        self.sock.sendto("xxx".encode(), (self.ip, self.port))


def main():
    frag = Fragment()

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    ret, buff = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
    string_data = buff.tobytes()
    print(getsizeof(string_data))
    frag.fragment(string_data)


if __name__ == "__main__":
    main()