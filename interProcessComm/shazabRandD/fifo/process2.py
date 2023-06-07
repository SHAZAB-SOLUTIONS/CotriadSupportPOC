import logging
import os


def process2():
    process2_logger = logging.getLogger('process2')
    process2_logger.info(f"Pid:{os.getpid()}")
    fifo = '/tmp/process_fifo.txt'

    # Keep attempting to open the fifo, ignore race condition failures
    while True:
        try:
            file = open(fifo, 'r')
            break
        except:
            pass
    try:
        line = file.readline()
        process2_logger.info(f"Read: {line}")
    except:
        pass

    # Clean up fifo
    file.close()
    os.remove(fifo)

    # Log completion
    process2_logger.info("Finished process 2")
