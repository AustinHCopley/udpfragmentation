import socket
import cv2
import numpy as np
from sys import getsizeof

IP = "127.0.0.1"
PORT = 5005
PACKSIZE = 6000

def main():
    cap = cv2.VideoCapture(0)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ret, frame = cap.read()

    data = np.array(frame)
    string_data = data.tobytes()
    framesize = getsizeof(string_data)
    # split the frame into 6KB datagrams
    for x in range( framesize // PACKSIZE + 1 ):
        sock.sendto(string_data[x*PACKSIZE : x*PACKSIZE+PACKSIZE], (IP, PORT))
    sock.sendto("xxx".encode(), (IP, PORT))


    #sock.sendto(string_data[:6000], (IP, PORT))

if __name__ == "__main__":
    main()