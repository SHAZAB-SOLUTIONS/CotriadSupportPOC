import os
import select
import json
import cv2

IPC_FIFO_NAME_A = "pipe_a"
IPC_FIFO_NAME_B = "pipe_b"

def get_message(fifo):
    '''Read n bytes from pipe. Note: n=24 is an example'''
    return os.read(fifo, 150)

def process_msg(msg):
    '''Process message read from pipe'''
    msg_dict = json.loads(msg.decode())
    # if msg_dict['command'] == "Get Snapshot":
    directory, status = getSnapshot(msg_dict['camera']['rtspLink'], msg_dict['camera']['name'])
    print(status)
    return directory.encode(), status.encode()

    # else:
    #     directory = ''
    #     status = 'Decoding message error'
    #     return directory.encode(), status.encode()

    
def getSnapshot(cameraLink, name):
    print(f"Opening camera of : {name}")
    
    cap = cv2.VideoCapture()
    cap.open(cameraLink)

    if not cap.isOpened():
        status = "Failed to open camera"
        snapShotPath = ''
        return snapShotPath, status


    ret, frame = cap.read()
    if not ret:
        status = 'Failed to read frame ftom the camera.'
        snapShotPath = ''
        return snapShotPath, status
    
    # os.mkdir("/home/fuzail/Desktop/interProcessComm/shazabRandD/levelup/getCameraSnapshot/snapShots")
    snapShotPath = "/home/fuzail/Desktop/ShazabInternal/interProcessComm/shazabRandD/levelup/getCameraSnapshot/snapShots/snapshot.png"
    cv2.imwrite(snapShotPath, frame)

    if os.path.exists(snapShotPath):
        status = "OK"
    else:
        status = "Snapshot not taken."

    cap.release()

    return snapShotPath, status


if __name__ == "__main__":
    os.mkfifo(IPC_FIFO_NAME_A)  # Create Pipe A

    try:
        fifo_a = os.open(IPC_FIFO_NAME_A, os.O_RDONLY | os.O_NONBLOCK)  # pipe is opened as read only and in a non-blocking mode
        print('Pipe A ready')

        while True:
            try:
                fifo_b = os.open(IPC_FIFO_NAME_B, os.O_WRONLY)
                print("Pipe B ready")
                break
            except:
                # Wait until Pipe B has been initialized
                pass

        try:
            poll = select.poll()
            poll.register(fifo_a, select.POLLIN)

            try:
                while True:
                    print('OKAYYYYYYYYYY')
                    if (fifo_a, select.POLLIN) in poll.poll(1000):  # Poll every 1 sec
                        msg = get_message(fifo_a)                   # Read from Pipe A
                        snapShotPath, status = process_msg(msg)                      # Process Message
                        os.write(fifo_b, snapShotPath)
                        os.write(fifo_b, status)                       # Write to Pipe B

                        print("Status is " + status.decode("utf-8"))
                        print('----- Sending to Agent -----')
                        print("    " + snapShotPath.decode("utf-8"))
            finally:
                poll.unregister(fifo_a)
        finally:
            os.close(fifo_a)
    finally:
        os.remove(IPC_FIFO_NAME_A)
        os.remove(IPC_FIFO_NAME_B)