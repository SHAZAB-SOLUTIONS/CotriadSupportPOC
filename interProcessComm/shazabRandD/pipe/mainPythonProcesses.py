import logging
import os
import multiprocessing
from multiprocessing import Process

from process1 import process1
from process2 import process2

def main():
    parent_logger = logging.getLogger('parent')
    parent_logger.info(f"Pid:{os.getpid()}")

    r, w = multiprocessing.Pipe(False)

    procs = [Process(target=process1, args=(w, )), Process(target=process2, args=(r, ))]

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

def nodeListener(pipe):
    nodeListener_logger = logging.getLogger('nodeListener')
    nodeListener_logger.info(f"Pid:{os.getpid()}")
    file = os.fdopen(pipe.fileno(), 'r')
    nodeListener_logger.info('Open file descriptor')

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    main()
