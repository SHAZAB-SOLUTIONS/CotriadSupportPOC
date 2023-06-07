import os
import logging
import time


def process2(pipe):
    process2_logger = logging.getLogger('process2')
    process2_logger.info(f"Pid:{os.getpid()}")

    # Open the file descriptor
    file = os.fdopen(pipe.fileno(), 'r')
    process2_logger.info("Opened file descriptor")

    # Expect 10 entries
    # count = 0
    # while count < 10:
    while True:
        try:
            line = file.readline()
            if line:
                process2_logger.info(f"Read: {int(line)}")
            else:
                break
            # count += 1
            # break
        except Exception:
            pass

    # Clean up pipe
    pipe.close()

    # Log completion
    process2_logger.info("Finished process 2")
