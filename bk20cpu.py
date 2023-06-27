import multiprocessing
import time

def cpu_bound_process():
    while True:
        x = 1
        time.sleep(0.01) # sleep for 10 milliseconds


if __name__ == '__main__':
    processes = []
    num_processes = multiprocessing.cpu_count()

    for i in range(num_processes):
        processes.append(multiprocessing.Process(target=cpu_bound_process))

    for process in processes:
        process.start()

    time.sleep(60)

    for process in processes:
        process.terminate()
