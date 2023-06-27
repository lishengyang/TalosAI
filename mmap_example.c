#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <sys/time.h>
#include <string.h>

#define FILE_SIZE 1024 * 1024 * 102 // 1 GB

void perform_io_operations(void* addr) {
    // Perform I/O operations on the memory-mapped file
    // For example, writing zeros to the entire file
    memset(addr, 0, FILE_SIZE);
}

void benchmark_mmap_vs_io() {
    // Open a file
    int fd = open("data.bin", O_RDWR | O_CREAT | O_TRUNC, 0666);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    // Resize the file to the desired size
    if (ftruncate(fd, FILE_SIZE) == -1) {
        perror("ftruncate");
        exit(1);
    }

    // Allocate memory for the mmap buffer
    void* addr = mmap(NULL, FILE_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (addr == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }

    // Get the start time
    struct timeval start_time;
    gettimeofday(&start_time, NULL);

    // Perform I/O operations using mmap
    perform_io_operations(addr);

    // Get the end time
    struct timeval end_time;
    gettimeofday(&end_time, NULL);

    // Calculate the time taken for mmap
    double mmap_time = (end_time.tv_sec - start_time.tv_sec) +
                      (end_time.tv_usec - start_time.tv_usec) / 1e6;

    // Close the file
    if (close(fd) == -1) {
        perror("close");
        exit(1);
    }

    // Open the file again for regular I/O
    fd = open("data.bin", O_RDWR);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    // Get the start time
    gettimeofday(&start_time, NULL);

    // Perform I/O operations using regular I/O
    void* io_buf = malloc(FILE_SIZE);
    perform_io_operations(io_buf);
    free(io_buf);

    // Get the end time
    gettimeofday(&end_time, NULL);

    // Calculate the time taken for regular I/O
    double io_time = (end_time.tv_sec - start_time.tv_sec) +
                     (end_time.tv_usec - start_time.tv_usec) / 1e6;

    printf("Time taken for mmap: %f seconds\n", mmap_time);
    printf("Time taken for regular I/O: %f seconds\n", io_time);
    printf("Performance improvement: %.2f times\n", io_time / mmap_time);

    // Close the file
    if (close(fd) == -1) {
        perror("close");
        exit(1);
    }

    // Unmap the memory-mapped file
    if (munmap(addr, FILE_SIZE) == -1) {
        perror("munmap");
        exit(1);
    }
}

int main() {
    benchmark_mmap_vs_io();
    return 0;
}

