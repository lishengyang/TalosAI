import serial

# Initialize serial UART communication with a baud rate of 9600
ser = serial.Serial('/dev/ttyS0', 9600)

# Send data over the UART
ser.write(b'Hello, UART!')

# Read data from the UART
data = ser.read()

# Print out the received data
print(data)

# Close the serial connection
ser.close()