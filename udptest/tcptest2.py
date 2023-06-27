import socket

# Server details
HOST = '10.0.0.4'   # Server IP address
PORT = 12345        # Port used for communication

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the host and port
    s.bind((HOST, PORT))
    print(f"Server bound to {HOST}:{PORT}")

    # Listen for incoming connections
    s.listen(1)
    print("Server is listening for incoming connections...")

    while True:
        # Accept a client connection
        conn, addr = s.accept()
        print("Connected by", addr)

        # Receive data from the client
        data = conn.recv(1024).decode()
        print("Message received:", data)

        # Prompt for a response
        response = input("Enter a response to send: ")

        # Send the response back to the client
        conn.sendall(response.encode())
        print("Response sent:", response)

        # Close the connection
        conn.close()
        print("Connection closed.")

        # Go back to listening for more connections

