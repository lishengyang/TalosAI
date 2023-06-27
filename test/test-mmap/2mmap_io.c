#include <fcntl.h>
#include <pthread.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <unistd.h>
#include <stdio.h>

#define NUM_THREADS 4

typedef struct {
    void *mapped;
    size_t start;
    size_t end;
    char target_char;
    size_t count;
} ThreadData;

void *count_char(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    for (size_t i = data->start; i < data->end; ++i) {
        if (((char *)data->mapped)[i] == data->target_char) {
            data->count++;
        }
    }
    return NULL;
}

double timeval_diff(struct timeval *start, struct timeval *end) {
    return (end->tv_sec - start->tv_sec) + (end->tv_usec - start->tv_usec) / 1e6;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <file>\n", argv[0]);
        return 1;
    }

    int fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        perror("Error opening file for reading");
        return 1;
    }

    struct stat sb;
    fstat(fd, &sb);
    size_t file_size = sb.st_size;

    void *mapped = mmap(NULL, file_size, PROT_READ, MAP_SHARED, fd, 0);
    if (mapped == MAP_FAILED) {
        perror("Error mapping file");
        close(fd);
        return 1;
    }

    pthread_t threads[NUM_THREADS];
    ThreadData thread_data[NUM_THREADS];
    size_t segment_size = file_size / NUM_THREADS;
    char target_char = 'A';

    struct timeval start, end;
    gettimeofday(&start, NULL);

    for (size_t i = 0; i < NUM_THREADS; ++i) {
        thread_data[i].mapped = mapped;
        thread_data[i].start = i * segment_size;
        thread_data[i].end = (i == NUM_THREADS - 1) ? file_size : (i + 1) * segment_size;
        thread_data[i].target_char = target_char;
        thread_data[i].count = 0;
        pthread_create(&threads[i], NULL, count_char, &thread_data[i]);
    }

    size_t total_count = 0;
    for (size_t i = 0; i < NUM_THREADS; ++i) {
        pthread_join(threads[i], NULL);
        total_count += thread_data[i].count;
    }

    gettimeofday(&end, NULL);

    double elapsed_seconds = timeval_diff(&start, &end);
    printf("Occurrences of '%c': %zu\n", target_char, total_count);
    printf("Elapsed time: %.6f seconds\n", elapsed_seconds);

    munmap(mapped, file_size);
    close(fd);
    return 0;
}

