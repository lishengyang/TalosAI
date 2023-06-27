#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

#define BLOCK_SIZE (4 * 1024)
#define FILE_SIZE (1 * 1024 * 1024 * 1024)

double get_time_ms() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (double)tv.tv_sec * 1000.0 + (double)tv.tv_usec / 1000.0;
}

void sequential_read_test(const char* filename) {
    char buf[BLOCK_SIZE];
    double start_time, end_time;
    FILE* fp = fopen(filename, "rb");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }
    start_time = get_time_ms();
    while (fread(buf, 1, BLOCK_SIZE, fp) > 0) {}
    end_time = get_time_ms();
    fclose(fp);
    double elapsed_time = end_time - start_time;
    double throughput = (double)FILE_SIZE / (1024.0 * 1024.0) / (elapsed_time / 1000.0);
    printf("Sequential read test: %.2f MB/s\n", throughput);
}

void sequential_write_test(const char* filename) {
    char buf[BLOCK_SIZE];
    memset(buf, 'A', BLOCK_SIZE);
    double start_time, end_time;
    FILE* fp = fopen(filename, "wb");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }
    start_time = get_time_ms();
    for (off_t off = 0; off < FILE_SIZE; off += BLOCK_SIZE) {
        if (fwrite(buf, 1, BLOCK_SIZE, fp) != BLOCK_SIZE) {
            perror("fwrite");
            exit(1);
        }
    }
    end_time = get_time_ms();
    fclose(fp);
    double elapsed_time = end_time - start_time;
    double throughput = (double)FILE_SIZE / (1024.0 * 1024.0) / (elapsed_time / 1000.0);
    printf("Sequential write test: %.2f MB/s\n", throughput);
}

void random_write_test(const char* filename) {
    char buf[BLOCK_SIZE];
    memset(buf, 'A', BLOCK_SIZE);
    double start_time, end_time;
    FILE* fp = fopen(filename, "wb");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }
    start_time = get_time_ms();
    for (int i = 0; i < FILE_SIZE / BLOCK_SIZE; i++) {
        off_t off = rand() % (FILE_SIZE / BLOCK_SIZE) * BLOCK_SIZE;
        if (fseek(fp, off, SEEK_SET) < 0) {
            perror("fseek");
            exit(1);
        }
        if (fwrite(buf, 1, BLOCK_SIZE, fp) != BLOCK_SIZE) {
            perror("fwrite");
            exit(1);
        }
    }
    end_time = get_time_ms();
    fclose(fp);
    double elapsed_time = end_time - start_time;
    double throughput = (double)FILE_SIZE / (1024.0 * 1024.0) / (elapsed_time / 1000.0);
    printf("Random write test: %.2f MB/s\n", throughput);
}

void random_read_test(const char* filename) {
    char buf[BLOCK_SIZE];
    double start_time, end_time;
    FILE* fp = fopen(filename, "rb");
    if (fp == NULL)
    {
        perror("fopen");
        exit(1);
    }
    start_time = get_time_ms();
    for (int i = 0; i < FILE_SIZE / BLOCK_SIZE; i++) {
        off_t off = rand() % (FILE_SIZE / BLOCK_SIZE) * BLOCK_SIZE;
        if (fseek(fp, off, SEEK_SET) < 0) {
            perror("fseek");
            exit(1);
        }
        if (fread(buf, 1, BLOCK_SIZE, fp) != BLOCK_SIZE) {
            perror("fread");
            exit(1);
        }
    }
    end_time = get_time_ms();
    fclose(fp);
    double elapsed_time = end_time - start_time;
    double throughput = (double)FILE_SIZE / (1024.0 * 1024.0) / (elapsed_time / 1000.0);
    printf("Random read test: %.2f MB/s\n", throughput);
}

void io_latency_test(const char* filename) {
    char buf[BLOCK_SIZE];
    double start_time, end_time;
    FILE* fp = fopen(filename, "r+b");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }
    start_time = get_time_ms();
    for (off_t off = 0; off < FILE_SIZE; off += BLOCK_SIZE) {
        if (fseek(fp, off, SEEK_SET) < 0) {
            perror("fseek");
            exit(1);
        }
        if (fread(buf, 1, BLOCK_SIZE, fp) != BLOCK_SIZE) {
            perror("fread");
            exit(1);
        }
        if (fwrite(buf, 1, BLOCK_SIZE, fp) != BLOCK_SIZE) {
            perror("fwrite");
            exit(1);
        }
    }
    end_time = get_time_ms();
    fclose(fp);
    double elapsed_time = end_time - start_time;
    double latency = elapsed_time / (double)(FILE_SIZE / BLOCK_SIZE);
    printf("I/O latency test: %.2f ms\n", latency);
}

int main(int argc, char** argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(1);
    }
    srand(0);
    sequential_read_test(argv[1]);
    sequential_write_test(argv[1]);
    random_write_test(argv[1]);
    random_read_test(argv[1]);
    io_latency_test(argv[1]);
    return 0;
}

