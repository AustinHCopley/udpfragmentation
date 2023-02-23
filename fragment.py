import socket
import cv2

IP = "127.0.0.1"
PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MSGSIZE = 5000000

def fragment(message, packsize):
    packets = []
    for i in range(0, len(message), packsize):
        packet = message[i:i+packsize]
        packets.append(packet)
    return packets

def reconstruct(packets):
    message = "".join(packets)
    return message

if __name__ == "__main__":
    msg = "test message iiiiiiiiiiiiiiiiiiiiiiiouiouiouiouiouiouiouiouiouiouiouiouiouiouiouiouiouiouioui"
    packet_size = 10

    # while True:
    packets = fragment(msg, packet_size)
    for packet in packets:
        sock.sendto(packet.encode(), (IP, PORT))
        print("Sent packet: ", packet)
