#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <time.h>
#include <unistd.h>

#define MEMORY_SIZE (1024 * 1024 * 1024) // 1G内存大小
#define DATA_SIZE 28 // 数据结构大小
#define STRING_SIZE 16 // 字符串大小

// 数据结构
struct Data {
    char str[STRING_SIZE];
    int num1;
    int num2;
    int num3;
};

void random_read(struct Data* data, int index) {
    // 随机读取数据
    // 读取操作，根据需求进行处理
    int value1 = data[index].num1;
    int value2 = data[index].num2;
    int value3 = data[index].num3;
    char* str = data[index].str;
    // 可根据需要使用读取到的数据进行其他操作
}

int main() {
    int fd = open("/dev/zero", O_RDWR); // 打开/dev/zero设备，用于映射匿名内存区域
    if (fd == -1) {
        printf("Failed to open /dev/zero.\n");
        return 1;
    }

    // 分配内存
    struct Data* data = (struct Data*)mmap(NULL, MEMORY_SIZE, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_POPULATE | MAP_ANONYMOUS | MAP_LOCKED, fd, 0);
    if (data == MAP_FAILED) {
        printf("Failed to mmap memory.\n");
        return 1;
    }

    close(fd); // 关闭文件描述符

    srand(time(NULL)); // 随机数种子

    // 随机读取数据，并计算执行时间
    int index;
    clock_t start = clock();
    for (int i = 0; i < 1000000; i++) {
        index = rand() % (MEMORY_SIZE / DATA_SIZE); // 生成随机索引
        random_read(data, index); // 调用随机读取函数
    }
    clock_t end = clock();
    double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC * 1000000; // 计算执行时间，单位为微秒
    printf("Time elapsed: %.2f microseconds\n", elapsed_time);

    munmap(data, MEMORY_SIZE); // 解除内存映射

    return 0;
}

