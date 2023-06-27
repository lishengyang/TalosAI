import socket
import time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('172.27.68.10', 12345)  # Use the server's IP address and port
client_socket.connect(server_address)

# Send a request to the server
start_time = time.time()
client_socket.sendall(b'Hello, server!')
response = client_socket.recv(1024)
end_time = time.time()

# Calculate and print the latency
latency = end_time - start_time
print(f"Response from server: {response.decode('utf-8')}")
print(f"Latency: {latency:.6f} seconds")

# Close the client socket
client_socket.close()

