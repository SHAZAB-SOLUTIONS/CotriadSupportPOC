import logging
import os
import time


def process1():
    process1_logger = logging.getLogger('process1')
    process1_logger.info(f"Pid:{os.getpid()}")
    fifo = '/tmp/process_fifo.txt'

    # Create a fifo, os.mkfifo will block until there is a reader (process2)
    os.mkfifo(fifo)

    # Open fifo for writing
    file = open(fifo, 'w')

    # Write 10 entries
    # for i in range(1,11):

    # Attempt to write to our fifo until succession
    myName = 'Fuzail'
    while True:
        try:
            process1_logger.info(f"Writing {myName}")
            file.write(f"{myName}\n")
            file.flush()
            break
        except:
            pass

    # Clean up fifo
    file.close()

    # Grace for the read process to complete
    # process1_logger.info("Sleeping for 2")
    # time.sleep(2)

    # Log completion
    process1_logger.info("Finished process 1")