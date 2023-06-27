#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/time.h>

#define PORT 12345

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char *hello = "Hello, server!";
    char buffer[1024] = {0};

    // Create a socket file descriptor
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    // Connect to the server
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }

    // Send a request to the server
    struct timeval start, end;
    gettimeofday(&start, NULL);
    send(sock, hello, strlen(hello), 0);
    recv(sock, buffer, sizeof(buffer), 0);
    gettimeofday(&end, NULL);

    // Calculate and print the latency
    double latency = (end.tv_sec - start.tv_sec) * 1000.0 + (end.tv_usec - start.tv_usec) / 1000.0;
    printf("TCP Latency: %.2f ms\n", latency);

    // Close the socket
    close(sock);

    return 0;
}

