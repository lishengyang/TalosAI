#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

#define NUM_READS 1000000
#define FILE_SIZE 4096

int main() {
  int fd = open("example.txt", O_RDONLY);
  char *data = (char *)malloc(FILE_SIZE);
  read(fd, data, FILE_SIZE);

  srand(time(NULL));
  struct timeval start, end;
  gettimeofday(&start, NULL);

  for (int i = 0; i < NUM_READS; i++) {
    int index = rand() % FILE_SIZE;
    volatile char c = data[index];
  }

  gettimeofday(&end, NULL);
  long elapsed = (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_usec - start.tv_usec);
  printf("malloc: %ld microseconds\n", elapsed);

  free(data);
  close(fd);
  return 0;
}

