import os
import time

IPC_FIFO_NAME_B = "./pipe_b"

if __name__ == "__main__":
    os.mkfifo(IPC_FIFO_NAME_B)
    print("Pipe B ready")
    fifo_b = open(IPC_FIFO_NAME_B, 'w')
    myname = 'Fuzail'
    while True:
        try:
            print(myname)
            fifo_b.write(f"{myname}\n")
            fifo_b.flush()
            time.sleep(3)
        except:
            print('Pipe closed')
            os.remove(IPC_FIFO_NAME_B)
            break
    if os.path.exists(IPC_FIFO_NAME_B):
        os.remove(IPC_FIFO_NAME_B)