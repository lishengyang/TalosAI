python
import smbus
import time

# Define I2C address and register of the sensor
I2C_ADDRESS = 0x48
TEMP_REG_ADDR = 0x00

# Initialize the I2C bus
bus = smbus.SMBus(1)

while True:
  # Read temperature register from the sensor
  temp_raw = bus.read_byte_data(I2C_ADDRESS, TEMP_REG_ADDR)

  # Convert the raw temperature value to Celsius
  temp_celsius = temp_raw * 0.0625

  # Print the temperature
  print("Temperature: {:.2f} °C".format(temp_celsius))

  # Wait for some time before reading again
  time.sleep(1)