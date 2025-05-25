# udp_server.py
import socket

IP = "127.0.0.1"
PORT = 9999
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print(f"UDP Server started on {IP}:{PORT}")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Received: {data.decode()} from {addr}")
    
    # Simulate ACK
    sock.sendto(b"ACK", addr)
