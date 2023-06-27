#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>

#define SIZE 1024 * 1024 * 1024  // 1GB
#define LOOP_COUNT 1000000       // 100W
#define ELEMENT_SIZE 28

typedef struct {
    char str[16];
    int32_t num1;
    int32_t num2;
    int32_t num3;
} IndexData;

int main() {
    int mmap_flags = MAP_PRIVATE | MAP_ANONYMOUS;
    void *mem = mmap(NULL, SIZE, PROT_READ | PROT_WRITE, mmap_flags, -1, 0);

    if (mem == MAP_FAILED) {
        perror("mmap failed");
        exit(1);
    }

    // Tell the kernel that we will need the memory pages
    if (madvise(mem, SIZE, MADV_WILLNEED) != 0) {
        perror("madvise failed");
        exit(1);
    }

    srand(time(NULL));
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    for (int i = 0; i < LOOP_COUNT; i++) {
        uint64_t idx = rand() % (SIZE / ELEMENT_SIZE);
        IndexData *data = (IndexData *)(mem + idx * ELEMENT_SIZE);

        // Write random data
        snprintf(data->str, 16, "%08x%08x", rand(), rand());
        data->num1 = rand();
        data->num2 = rand();
        data->num3 = rand();

        // Read data
        IndexData read_data;
        memcpy(&read_data, data, sizeof(IndexData));
    }

    clock_gettime(CLOCK_MONOTONIC, &end);
    uint64_t time_taken = (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_nsec - start.tv_nsec) / 1000;

    printf("Time taken: %lu microseconds\n", time_taken);

    munmap(mem, SIZE);
    return 0;
}

