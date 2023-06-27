#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <pthread.h>

void *send_request(void *arg) {
    int sock;
    struct sockaddr_in server;
    char message[] = "Hello, world!";

    // create a TCP socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        printf("Could not create socket");
    }

    // set up the server address and port
    server.sin_addr.s_addr = inet_addr("10.0.0.3"); // replace with the server IP address
    server.sin_family = AF_INET;
    server.sin_port = htons(80); // replace with the server port number

    // connect to the server
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("connect failed");
        return NULL;
    }

    // send a message to the server
    if (send(sock, message, sizeof(message), 0) < 0) {
        puts("send failed");
        return NULL;
    }

    // close the socket
    close(sock);

    return NULL;
}

int main() {
    int i;
    pthread_t tid[10];

    for (i = 0; i < 10; i++) {
        if (pthread_create(&tid[i], NULL, send_request, NULL) != 0) {
            perror("pthread_create failed");
            return 1;
        }
    }

    for (i = 0; i < 10; i++) {
        pthread_join(tid[i], NULL);
    }

    return 0;
}

