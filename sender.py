# udp_client.py
import socket
import time
import random

IP = "127.0.0.1"
PORT = 9999
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)  # 1 second timeout for ACK

# Congestion control parameters
window_size = 1
max_window = 50
timeout_limit = 3
increase_step = 1
decrease_factor = 0.5

packet_id = 0

while packet_id < 100:
    success_count = 0

    for _ in range(window_size):
        msg = f"Packet {packet_id}"
        try:
            sock.sendto(msg.encode(), (IP, PORT))
            ack = sock.recvfrom(BUFFER_SIZE)
            print(f"ACK received for: {msg}")
            success_count += 1
        except socket.timeout:
            print(f"Timeout: No ACK for {msg}")

        packet_id += 1
        time.sleep(0.01)

    # Simple congestion control logic
    if success_count == window_size:
        window_size = min(window_size + increase_step, max_window)
    else:
        window_size = max(1, int(window_size * decrease_factor))
    
    print(f"Updated window size: {window_size}")

sock.close()
