import socket
import asyncio
import numpy as np
# import threading

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

async def listener():
    global msgList
    msgList = []
    while True:
        data, addr = await loop.sock_recv(sock, 6000)
        msgList.append(data.decode())

async def reconstruct():
    print(msgList)


loop = asyncio.get_event_loop()
msg = ""
tasks = asyncio.gather(listener(), reconstruct())
loop.run_until_complete(tasks)
"""while True:
    data, addr = sock.recvfrom(6000)
    print("Received from", addr)
    msg += data.decode()
    print(len(msg))"""
    
