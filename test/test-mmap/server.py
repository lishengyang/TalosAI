import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_address = ('', 12345)  # Use an empty string for the IP address to bind to all available network interfaces
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)  # Maximum number of queued connections

print("Server is ready to receive incoming connections...")

while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()

    # Send a response to the client
    client_socket.sendall(b'Hello, iamserver!')

    # Close the client socket
    client_socket.close()

