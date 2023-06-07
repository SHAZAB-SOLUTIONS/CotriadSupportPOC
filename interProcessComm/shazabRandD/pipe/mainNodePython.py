import logging
import os
import multiprocessing
from multiprocessing import Process, Pipe
import subprocess



def main():

    from interProcessComm.shazabRandD.pipe.process2 import process2

    parent_logger = logging.getLogger('parent')
    parent_logger.info(f"Pid:{os.getpid()}")

    r, w = multiprocessing.Pipe(False)

    process1 = subprocess.Popen(['node', 'process1.js', str(w.fileno())])

    process2 = Process(target=process2, args=(r, ))
    process2.start()

    process1.wait()

    w.close()
    r.close()

    process2.join()

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    main()