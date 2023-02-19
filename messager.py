import socket
import cv2
import numpy as np

IP = "127.0.0.1"
PORT = 5005

def main():
    cap = cv2.VideoCapture(0)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ret, frame = cap.read()

    while ret:

        ret, frame = cap.read()
        data = np.array(frame)
        string_data = data.tobytes()

        sock.sendto(string_data[:5000], (IP, PORT))

if __name__ == "__main__":
    main()