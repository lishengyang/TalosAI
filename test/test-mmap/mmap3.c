#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/resource.h>
#include <unistd.h>
#include <stdio.h>

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

    struct rusage start_usage, end_usage;
    getrusage(RUSAGE_SELF, &start_usage);

    // Perform I/O operation here: count occurrences of the target character.
    char target_char = 'A';
    size_t count = 0;
    for (size_t i = 0; i < file_size; ++i) {
        if (((char *)mapped)[i] == target_char) {
            count++;
        }
    }

    getrusage(RUSAGE_SELF, &end_usage);

    double user_time = timeval_diff(&start_usage.ru_utime, &end_usage.ru_utime);
    double system_time = timeval_diff(&start_usage.ru_stime, &end_usage.ru_stime);

    printf("Occurrences of '%c': %zu\n", target_char, count);
    printf("User CPU time: %.6f seconds\n", user_time);
    printf("System CPU time: %.6f seconds\n", system_time);

    munmap(mapped, file_size);
    close(fd);
    return 0;
}

