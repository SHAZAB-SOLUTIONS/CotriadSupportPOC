import os
import logging
import time


def process1(pipe):
    process1_logger = logging.getLogger('process1')
    process1_logger.info(f"Pid:{os.getpid()}")

    # Open the file descriptor
    file = os.fdopen(pipe.fileno(), 'w')
    process1_logger.info("Opened file descriptor")

    # Write 10 entries
    for i in range(1,5):

        # Attempt to write to our pipe until succession
        while True:
            try:
                process1_logger.info(f"Writing {int(i)}")
                file.write(f"{i}\n")
                
                file.flush()
                time.sleep(2)
                break
            except:
                pass

    # Clean up pipe
    pipe.close()

    # Log completion
    process1_logger.info("Finished process 1")
