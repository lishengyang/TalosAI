import socket

# Set the local IP address and port to listen on
local_ip = '0.0.0.0'    # Listen on all available network interfaces
local_port = 12345     # Choose a port number to listen on

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the local IP address and port
sock.bind((local_ip, local_port))

print(f"UDP server listening on {local_ip}:{local_port}")

# Loop to continuously receive incoming messages
while True:
    # Receive data and address from the client
    data, addr = sock.recvfrom(1024)  # Buffer size is set to 1024 bytes, adjust as needed
    
    # Decode the received data from bytes to string
    message = data.decode('utf-8')
    
    # Print the received message and client address
    print(f"Received message: '{message}' from {addr[0]}:{addr[1]}")

