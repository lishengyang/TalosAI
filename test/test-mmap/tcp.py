import socket
import time

# Define the server address and port
server_address = ('10.0.0.3', 8080)

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(server_address)

# Start the timer
start_time = time.time()

# Send a simple request to the server
client_socket.sendall(b'Hello, server!')

# Receive data from the server
response = client_socket.recv(1024)

# Stop the timer
end_time = time.time()

# Calculate the latency
latency = (end_time - start_time) * 1000  # Convert to milliseconds

# Close the socket
client_socket.close()

# Print the latency
print(f'Latency: {latency} ms')

