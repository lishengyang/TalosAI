import socket

# Server details
HOST = '10.0.0.4'   # Server IP address
PORT = 12345        # Port used for communication

while True:
    # Prompt for message to send
    message = input("Enter a message to send (or 'q' to quit): ")

    # Check if user wants to quit
    if message.lower() == 'q':
        print("Quitting...")
        break

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        # Send the message
        s.sendall(message.encode())
        print("Message sent:", message)

        # Receive response from the server
        response = s.recv(1024).decode()
        print("Response received:", response)

    # Connection is automatically closed after each message is sent and response is received
    # Client will return to the prompt for sending another message

