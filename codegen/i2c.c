#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>

#define I2C_BUS 1
#define I2C_SLAVE_ADDRESS 0x68

int main(void)
{
    int i2c_fd;
    char buffer[2];

    // Open the I2C bus
    i2c_fd = open("/dev/i2c-1", O_RDWR);

    // Set the I2C slave device address
    if (ioctl(i2c_fd, I2C_SLAVE, I2C_SLAVE_ADDRESS) < 0) {
        perror("ioctl() failed");
        exit(EXIT_FAILURE);
    }

    // Send command to read sensor data
    buffer[0] = 0x00;
    buffer[1] = 0x14;
    if (write(i2c_fd, buffer, 2) < 0) {
        perror("write() failed");
        exit(EXIT_FAILURE);
    }

    // Read sensor data
    if (read(i2c_fd, buffer, 2) < 0) {
        perror("read() failed");
        exit(EXIT_FAILURE);
    }

    printf("Sensor data: %d\n", (int) buffer[0]);

    // Close the I2C bus
    close(i2c_fd);

    return 0;
}