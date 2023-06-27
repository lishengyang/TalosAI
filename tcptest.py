import socket

# Set the server IP address and port
server_ip = '10.0.0.4'  # Update with the IP address of the TCP server
server_port = 12345     # Update with the port number of the TCP server

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((server_ip, server_port))
print(f"Connected to server {server_ip}:{server_port}")

while True:
    # Accept user input for the message to send
    message = input("Enter the message to send (or 'quit' to exit): ")

    if message == 'quit':
        # Exit the loop if user enters 'quit'
        print("Exiting...")
        break

    # Encode the message to bytes
    message_bytes = message.encode('utf-8')

    # Send the message to the server
    sock.sendall(message_bytes)

    # Wait for response from the server
    response = sock.recv(1024)

    # Decode the response and display it
    print("Response from server:", response.decode('utf-8'))

# Close the socket
sock.close()

