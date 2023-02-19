import socket
import numpy as np

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

def main():
    while True:
        data, addr = sock.recvfrom(6000)
        print("Received from", addr)
        print(data)

if __name__ == "__main__":
    main()