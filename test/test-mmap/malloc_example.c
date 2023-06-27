#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>

#define ITERATIONS 1000
#define FILE_SIZE (1 * 1024 * 1024) // 1 MB

double get_time() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + tv.tv_usec * 1e-6;
}

int main() {
    char *filename = "temp_file";
    int fd;
    char *data;

    fd = open(filename, O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
    if (fd < 0) {
        perror("open");
        return 1;
    }

    if (ftruncate(fd, FILE_SIZE) < 0) {
        perror("ftruncate");
        close(fd);
        return 1;
    }

    data = (char *)malloc(FILE_SIZE);
    if (data == NULL) {
        perror("malloc");
        close(fd);
        return 1;
    }

    double start = get_time();
    for (int i = 0; i < ITERATIONS; i++) {
        if (pread(fd, data, FILE_SIZE, 0) < 0) {
            perror("pread");
            close(fd);
            free(data);
            return 1;
        }

        // Perform random read and write operations
        for (int j = 0; j < 100; j++) {
            int offset = rand() % FILE_SIZE;
            data[offset] = rand() % 256;
        }

        if (pwrite(fd, data, FILE_SIZE, 0) < 0) {
            perror("pwrite");
            close(fd);
            free(data);
            return 1;
        }
    }
    double end = get_time();
    printf("Elapsed time: %f seconds\n", end - start);

    close(fd);
    free(data);
    unlink(filename);
    return 0;
}

