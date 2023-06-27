import serial
import time

# Open the serial port with baud rate 9600
ser = serial.Serial('/dev/ttyAMA0', 9600)

try:
    while True:
        # Send data over UART
        ser.write(b'Hello World!')

        # Wait for data to be available
        while ser.inWaiting() == 0:
            pass

        # Read the received data from UART
        data = ser.read(ser.inWaiting())
        print(data)

        # Wait for 1 second before sending more data
        time.sleep(1)

finally:
    # Close the serial port
    ser.close()