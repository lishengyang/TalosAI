#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#define BLOCK_SIZE (4 * 1024)
#define FILE_SIZE (1 * 1024 * 1024 * 10)

double get_time_ms() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (double)tv.tv_sec * 1000.0 + (double)tv.tv_usec / 1000.0;
}

void random_write_test(const char* filename) {
    char buf[BLOCK_SIZE];
    memset(buf, 'A', BLOCK_SIZE);
    double start_time, end_time;
    int fd = open(filename, O_WRONLY | O_CREAT | O_TRUNC | O_DIRECT, 0644);
    if (fd < 0) {
        perror("open");
        exit(1);
    }
    start_time = get_time_ms();
    for (int i = 0; i < FILE_SIZE / BLOCK_SIZE; i++) {
        off_t off = rand() % (FILE_SIZE / BLOCK_SIZE) * BLOCK_SIZE;
        if (lseek(fd, off, SEEK_SET) < 0) {
            perror("lseek");
            exit(1);
        }
        if (write(fd, buf, BLOCK_SIZE) < 0) {
            perror("write");
            exit(1);
        }
    }
    end_time = get_time_ms();
    close(fd);
    double elapsed_time = end_time - start_time;
    double throughput = (double)FILE_SIZE / (1024.0 * 1024.0) / (elapsed_time / 1000.0);
    printf("Random write test: %.2f MB/s\n", throughput);
}

void random_read_test(const char* filename) {
    char buf[BLOCK_SIZE];
    double start_time, end_time;
    int fd = open(filename, O_RDONLY | O_DIRECT);
    if (fd < 0) {
        perror("open");
        exit(1);
    }
    start_time = get_time_ms();
    for (int i = 0; i < FILE_SIZE / BLOCK_SIZE; i++) {
        off_t off = rand() % (FILE_SIZE / BLOCK_SIZE) * BLOCK_SIZE;
        if (lseek(fd, off, SEEK_SET) < 0) {
            perror("lseek");
            exit(1);
        }
        if (read(fd, buf, BLOCK_SIZE) < 0) {
            perror("read");
            exit(1);
        }
    }
    end_time = get_time_ms();
    close(fd);
    double elapsed_time = end_time - start_time;
    double throughput = (double)FILE_SIZE / (1024.0 * 1024.0) / (elapsed_time / 1000.0);
    printf("Random read test: %.2f MB/s\n", throughput);
}

int main(int argc, char** argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(1);
    }
    srand(0);
    random_write_test(argv[1]);
    random_read_test(argv[1]);
    return 0;
}

