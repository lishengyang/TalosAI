#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define BLOCK_SIZE (4 * 1024)
#define FILE_SIZE (64 * 1024 * 1024  * 10)

double get_time_ms() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (double)tv.tv_sec * 1000.0 + (double)tv.tv_usec / 1000.0;
}

int get_block_size(const char *filename) {
    struct stat sb;
    if (stat(filename, &sb) == -1) {
        perror("stat");
        exit(1);
    }
    return sb.st_blksize;
}

void random_write_test(const char *filename, int block_size) {
    char *buf;
    posix_memalign((void **)&buf, block_size, BLOCK_SIZE);
    memset(buf, 'A', BLOCK_SIZE);
    double start_time, end_time;
    int fd = open(filename, O_WRONLY | O_CREAT | O_TRUNC | O_DIRECT, 0644);
    if (fd < 0) {
        perror("open");
        exit(1);
    }
    start_time = get_time_ms();
    for (off_t off = 0; off < FILE_SIZE; off += BLOCK_SIZE) {
        if (pwrite(fd, buf, BLOCK_SIZE, off) != BLOCK_SIZE) {
            perror("pwrite");
            exit(1);
        }
    }
    end_time = get_time_ms();
    close(fd);
    double elapsed_time = end_time - start_time;
    double throughput = (double)FILE_SIZE / (1024.0 * 1024.0) / (elapsed_time / 1000.0);
    printf("Random write test: %.2f MB/s\n", throughput);
    free(buf);
}

void random_read_test(const char *filename, int block_size) {
    char *buf;
    posix_memalign((void **)&buf, block_size, BLOCK_SIZE);
    double start_time, end_time;
    int fd = open(filename, O_RDONLY | O_DIRECT);
    if (fd < 0) {
        perror("open");
        exit(1);
    }
    start_time = get_time_ms();
    for (off_t off = 0; off < FILE_SIZE; off += BLOCK_SIZE) {
        if (pread(fd, buf, BLOCK_SIZE, off) != BLOCK_SIZE) {
            perror("pread");
            exit(1);
        }
    }
    end_time = get_time_ms();
    close(fd);
    double elapsed_time = end_time - start_time;
    double throughput = (double)FILE_SIZE / (1024.0 * 1024.0) / (elapsed_time / 1000.0);
    printf("Random read test: %.2f MB/s\n", throughput);
    free(buf);
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    const char *filename = argv[1];
    int block_size = get_block_size(filename);

    random_write_test(filename, block_size);
    random_read_test(filename, block_size);

    return 0;
}

