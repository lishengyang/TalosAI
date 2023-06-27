import socket

# Set the local IP address and port to listen on
local_ip = '0.0.0.0'    # Listen on all available network interfaces
local_port = 12345     # Choose a port number to listen on

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the local IP address and port
sock.bind((local_ip, local_port))

# Listen for incoming connections
sock.listen(5)  # Allow up to 5 queued connections

print(f"TCP server listening on {local_ip}:{local_port}")

# Loop to continuously accept incoming connections
while True:
    # Accept a client connection
    client_socket, client_addr = sock.accept()

    # Print the client address
    print(f"Client connected from {client_addr[0]}:{client_addr[1]}")

    # Receive data from the client
    data = client_socket.recv(1024)  # Buffer size is set to 1024 bytes, adjust as needed

    # Decode the received data from bytes to string
    message = data.decode('utf-8')

    # Print the received message
    print(f"Received message: '{message}'")

    # Prompt for a response from the user
    response = input("Enter server response: ")

    # Encode the response message to bytes
    response_bytes = response.encode('utf-8')

    # Send the response back to the client
    client_socket.sendall(response_bytes)

    print("Response sent successfully!")

    # Close the client socket
    client_socket.close()

