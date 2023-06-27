#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {
  // Create a TCP server socket.
  int server_socket = socket(AF_INET, SOCK_STREAM, 0);
  if (server_socket < 0) {
    perror("socket");
    exit(1);
  }

  // Bind the socket to a port.
  struct sockaddr_in server_address;
  server_address.sin_family = AF_INET;
  server_address.sin_port = htons(8080);
  server_address.sin_addr.s_addr = INADDR_ANY;
  if (bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address)) < 0) {
    perror("bind");
    exit(1);
  }

  // Listen for incoming connections.
  listen(server_socket, 5);

  while (1) {
    // Accept an incoming connection.
    int client_socket = accept(server_socket, NULL, NULL);
    if (client_socket < 0) {
      perror("accept");
      exit(1);
    }

    // Read the HTTP request from the client.
    char request[1024];
    int bytes_read = recv(client_socket, request, sizeof(request), 0);
    if (bytes_read < 0) {
      perror("recv");
      exit(1);
    }

    // Parse the HTTP request and determine what the client is asking for.
    char *method = strtok(request, " ");
    char *path = strtok(NULL, " ");

    // Generate the HTTP response.
    char response[1024];
    sprintf(response, "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>Hello, world!</body></html>");

    // Write the HTTP response to the client.
    int bytes_written = send(client_socket, response, strlen(response), 0);
    if (bytes_written < 0) {
      perror("send");
      exit(1);
    }

    // Close the socket.
    close(client_socket);
  }

  return 0;
}

