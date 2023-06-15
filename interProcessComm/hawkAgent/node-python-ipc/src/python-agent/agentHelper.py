import os
import json
import platform
from getSnapShotPath import getSnapshotPath


def getSnapShot(cameraLink, name):
    import cv2
    print(f"getSnapShot: Opening camera: {name}")

    try:
        print("getSnapShot: Getting snapshot...")
        cap = cv2.VideoCapture()
        cap.open(cameraLink)  # Opening connection to camera

        ret, frame = cap.read()  # Reading frames
        if not ret:
            status = 'Failed to read frame from the camera.'
            snapShotPath = 'NIL'
            return snapShotPath, status

        snapShotPath = getSnapshotPath()  # Getting the path where snapshot will be stored

        cv2.imwrite(snapShotPath, frame)  # Getting the snapshot

        if os.path.exists(snapShotPath):
            status = "Snapshot taken!"
        else:
            status = "Snapshot not taken."

        cap.release()

        return snapShotPath, status

    except cv2.error as e:
        status = f"OpenCV ERROR: {str(e)}"
        snapShotPath = 'NIL'

        return snapShotPath, status


def commandExecutor(message):
    msg_dict = json.loads(message)
    command = msg_dict["command"]

    if command == 'Get Snapshot':
        print(f"commandExecutor: Command is: {command}")
        print("commandExecutor: Parsing Request Object...")
        request = {
            'rtspLink': msg_dict["camera"]["rtspLink"],
            'camName': msg_dict["camera"]["name"],
            'pipe': msg_dict["pipe"],
            'command': msg_dict["command"]
        }
        snapShotPath, status = getSnapShot(
            request["rtspLink"], request["camName"])
        print('commandExecutor: Status is: ' + status)
        print('commandExecutor: Snapshot path is: ' + snapShotPath)
        response = {
            'snapShotPath': snapShotPath,
            'status': status
        }
    return request, response


def listenOnPipe(pipe):
    if platform.system() == 'Windows':
        import win32pipe
        import win32file

        handle = win32pipe.CreateNamedPipe(
            pipe,
            win32pipe.PIPE_ACCESS_DUPLEX,
            win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_READMODE_BYTE | win32pipe.PIPE_WAIT,
            1,  # Number of instances
            65536,  # Output buffer size in bytes
            65536,  # Input buffer size in bytes
            0,  # Default timeout in milliseconds
            None  # Security attributes
        )

        win32pipe.ConnectNamedPipe(handle, None)  # Connecting to pipe
        buffer_size = 4096  # Adjust the buffer size as needed
        data = win32file.ReadFile(handle, buffer_size)
        receivedMessage = data[1].decode()

        # Processing the message and running commands as per the message
        request, response = commandExecutor(receivedMessage)

        # Closing the read handle
        win32file.CloseHandle(handle)

        return receivedMessage, request, response

    else:
        import socket
        import os

        os.mkfifo(pipe)
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(pipe)

        data = s.recv(4096)
        receivedMessage = data.decode()

        # Processing the message and running commands as per the message
        request, response = commandExecutor(receivedMessage)

        # Closing the read handle
        s.close()

        return receivedMessage, request, response


def writeToPipe(pipe, response):
    if platform.system() == 'Windows':
        import win32file

        handle = win32file.CreateFile(
            pipe,
            win32file.GENERIC_WRITE,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None
        )

        # Writing to pipe
        win32file.WriteFile(handle, str(response).encode())

        # Closing the write handle
        win32file.CloseHandle(pipe)

    else:
        import socket
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # Connecting to pipe
        s.connect(pipe)
        # Writing to pipe
        s.send(response)
        # Closing connection to pipe
        s.close()
