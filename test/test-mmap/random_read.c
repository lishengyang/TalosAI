#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

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
    // 分配内存
    struct Data* data = (struct Data*)malloc(MEMORY_SIZE);
    if (data == NULL) {
        printf("Failed to allocate memory.\n");
        return 1;
    }

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

    free(data); // 释放内存

    return 0;
}

