#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
#include <linux/fb.h>
#include <linux/vt.h>
#include <signal.h>
#include <unistd.h>

int fd_tty0, fd_mem;
char *mem;
struct fb_var_screeninfo vinfo;
volatile int data_ready = 0;

void sig_handler(int signo)
{
    if(signo == SIGUSR1)
        data_ready = 1;
}

int main()
{
    int i, j;

    // Open /dev/mem for writing
    fd_mem = open("/dev/mem", O_RDWR | O_SYNC);
    if(fd_mem < 0) {
        perror("open /dev/mem");
        return 1;
    }

    // Get the system's page size
    size_t page_size = getpagesize();

    // Map memory in the disk to the process address space
    size_t buffer_size = 1024 * 1024 * 100; // 100MB
    buffer_size = (buffer_size + page_size - 1) & ~(page_size - 1);
    mem = (char*) mmap(NULL, buffer_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd_mem, 0);
    if(mem == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    // Set up the signal handler for the interrupt
    if(signal(SIGUSR1, sig_handler) == SIG_ERR) {
        perror("signal");
        return 1;
    }

    // Set up the interrupt
    struct sigaction sa;
    sa.sa_flags = SA_SIGINFO;
    sa.sa_sigaction = NULL; // You may need to fill in your own interrupt handler here
    if(sigaction(SIGUSR1, &sa, NULL) < 0) {
        perror("sigaction");
        return 1;
    }

    // Check if the tty0 device file is available
    fd_tty0 = open("/dev/tty0", O_RDONLY);
    if(fd_tty0 >= 0) {
        // Read from tty0 and signal the interrupt handler when data is ready to be saved
        if(ioctl(fd_tty0, VT_GETSTATE, &vinfo) < 0) {
            perror("ioctl VT_GETSTATE");
            return 1;
        }

        if(ioctl(fd_tty0, FBIOGET_VSCREENINFO, &vinfo) < 0) {
            perror("ioctl FBIOGET_VSCREENINFO");
            return 1;
        }

        for(i = 0; i < vinfo.yres; i++) {
            for(j = 0; j < vinfo.xres; j++) {
                char c;
                if(read(fd_tty0, &c, sizeof(char)) < 0) {
                    perror("read tty0");
                    return 1;
                }
                mem[i*vinfo.xres+j] = c;
                if((i*vinfo.xres+j) % (1024*1024) == 0) // Signal the interrupt handler every 1MB of data read
                    kill(getpid(), SIGUSR1);
            }
        }

        close(fd_tty0);
    }

    // Wait for the interrupt handler to finish saving the data
    while(!data_ready) {
        sleep(1);
    }

    // Unmap the memory and close the files
    if(munmap(mem, buffer_size) < 0) {
        perror("munmap");
        return 1;
}

close(fd_mem);

return 0;

}
