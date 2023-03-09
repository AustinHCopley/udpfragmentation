import socket
import threading
import cv2
from pickle import loads

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
        self.data = None

    def listener(self):
        while True:
            self.data, addr = self.sock.recvfrom(self.packsize)

    def reconstruct(self):
        while True:
            if self.data is not None:
                data = loads(self.data)
                image = cv2.imdecode(data, flags=cv2.IMREAD_COLOR)
                cv2.imshow("image test", image)
                cv2.waitKey(30)
        cv2.destroyAllWindows()


def main():
    recon = Reconstruct()
    recon.listen.start()
    recon.reconstruct()


if __name__ == "__main__":
    main()
