import logging
import os
from multiprocessing import Process

from process2 import process2


def process1():
    os.system('node process1.js')

def main():

    # Setup parent logger and log pid
    parent_logger = logging.getLogger('parent')
    parent_logger.info(f"Pid:{os.getpid()}")

    # Setup processes
    procs = [Process(target=process1), Process(target=process2)]

    # Start processes
    for proc in procs:
        proc.start()


    # Run to completion
    for proc in procs:
        proc.join()

# Setup simple logging
logging.basicConfig(level=logging.INFO)

# Execute main
if __name__ == '__main__':
    main()
