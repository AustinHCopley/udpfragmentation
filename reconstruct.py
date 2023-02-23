import socket
IP = "127.0.0.1"
PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

def reconstruct(packets):
    message = "".join(packets)
    return message

if __name__ == "__main__":
    received = []
    while True:
        data, addr = sock.recvfrom(6000)
        packet = data.decode()
        received.append(packet)
        print(packet)

    reconstructed = reconstruct(received)
    print(reconstructed)