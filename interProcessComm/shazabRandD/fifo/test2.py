import multiprocessing
import time
import os

# Function to perform the first task


def task1():
    fifo = './fifo.txt'
    os.mkfifo(fifo)
    file = open(fifo, 'w')
    print("Task 1 started")
    for i in range(1, 11):
        print(i)
        data = str(i)
        file.write(data)
        time.sleep(2)
        file.flush()

    file.close()
    # time.sleep(2)  # Simulate a long computation
    print("Task 1 completed")

# Function to perform the second task


def task2():
    print("Task 2 started")
    fifo = "./fifo.txt"
    while True:
        file = open(fifo, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            print(f"Read: {line}")
        file.close()
        break
    print("Task 2 completed")
    if os.path.exists('./fifo.txt'):
        os.remove('./fifo.txt')


if __name__ == '__main__':
    # Create two processes, one for each task
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    # Once both processes have completed, continue with the main process
    print("All tasks completed")