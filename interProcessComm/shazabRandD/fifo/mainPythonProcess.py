import logging
import os
import time
from multiprocessing import Process

from process1 import process1
from process2 import process2


def main():

    # Setup parent logger and log pid
    parent_logger = logging.getLogger('parent')
    parent_logger.info(f"Pid:{os.getpid()}")

    # Setup processes
    processOne = Process(target=process1)
    processTwo = Process(target=process2)
    # procs = [Process(target=process1), Process(target=process2)]

    processOne.start()
    parent_logger.info(f"Process One started")

    time.sleep(2)

    processTwo.start()
    parent_logger.info(f"Process Two started")

    processOne.join()
    processTwo.join()

    # # Start processes
    # for proc in procs:
    #     proc.start()

    # # Run to completion
    # for proc in procs:
    #     proc.join()

# Setup simple logging
logging.basicConfig(level=logging.INFO)

# Execute main
if __name__ == '__main__':
    main()
    if os.path.exists('/tmp/process_fifo.txt'):
        os.remove('/tmp/process_fifo.txt')