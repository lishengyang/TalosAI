#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_READS 1000000
#define FILE_SIZE 4096

int main() {
  int fd = open("example.txt", O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
  ftruncate(fd, FILE_SIZE);

  char *data = mmap(NULL, FILE_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

  srand(time(NULL));
  struct timeval start, end;
  gettimeofday(&start, NULL);

  for (int i = 0; i < NUM_READS; i++) {
    int index = rand() % FILE_SIZE;
    volatile char c = data[index];
  }

  gettimeofday(&end, NULL);
  long elapsed = (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_usec - start.tv_usec);
  printf("mmap: %ld microseconds\n", elapsed);

  munmap(data, FILE_SIZE);
  close(fd);
  return 0;
}

