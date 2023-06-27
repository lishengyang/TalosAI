#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int server_sock, client_sock, c, read_size;
    struct sockaddr_in server, client;
    char client_message[2000];

    // create a TCP socket
    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock == -1) {
        printf("Could not create socket");
    }

    // set up the server address and port
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(80); // replace with the server port number

    // bind the socket to the server address and port
    if (bind(server_sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("bind failed");
        return 1;
    }

    // listen for incoming connections
    listen(server_sock, 3);

    printf("Waiting for incoming connections...\n");

    c = sizeof(struct sockaddr_in);

    // accept incoming connections
    while ((client_sock = accept(server_sock, (struct sockaddr *)&client, (socklen_t *)&c))) {
        printf("Connection accepted from %s:%d\n", inet_ntoa(client.sin_addr), ntohs(client.sin_port));

        // receive a message from the client
        while ((read_size = recv(client_sock, client_message, 2000, 0)) > 0) {
            // send a response back to the client
            write(client_sock, client_message, strlen(client_message));
        }

        if (read_size == 0) {
            printf("Client disconnected\n");
        } else if (read_size == -1) {
            perror("recv failed");
        }

        // close the client socket
        close(client_sock);
    }

    if (client_sock < 0) {
        perror("accept failed");
        return 1;
    }

    // close the server socket
    close(server_sock);

    return 0;
}

