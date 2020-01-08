from threading import Thread
import os
import socket
import random
import string
from time import sleep

class KeyException(Exception):
    def __init__(self):
        super().__init__('Not valid key')

def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length)).encode('utf-8')

def send(s, data):
    byte = bytearray([5, 1])
    byte += len(data).to_bytes(4, 'big')
    byte += data
    s.send(byte)

def recv(s):
    key = int.from_bytes(s.recv(1), byteorder='little')
    if key != 5:
        raise KeyException

    id = int.from_bytes(s.recv(1), byteorder='little')  
    size = int.from_bytes(s.recv(4), byteorder='big')

    if id == 1:
        ip_bin = s.recv(4)
        ip = socket.inet_ntoa(ip_bin[::-1])
        body_size = size - 4
    else:
        ip = ''
        body_size = size

    return id, ip, s.recv(body_size).decode('utf-8')

def recv_loop(s):
    while True:
        id, ip, data = recv(s)
        sender = ip if id == 1 else 'system'
        print(f"{sender} : recv from server id is {id}\ndata is {data}\n")

if __name__ == '__main__':
    with socket.socket() as s:
        data = bytearray([5, 1])
        s.connect(('127.0.0.1', 5555))
        Thread(target=recv_loop, args=[s]).start()

        while True:
            sleep(10)
            data = random_string(random.randrange(2, 10))
            send(s, data)
            print(f"data is {data}")