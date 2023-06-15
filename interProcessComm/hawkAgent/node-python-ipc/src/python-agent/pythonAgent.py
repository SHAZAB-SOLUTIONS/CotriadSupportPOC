import tempfile
from agentHelper import listenOnPipe, writeToPipe

# For windows
# pipe_name_R = "\\\\.\\pipe\\fuzail1"
# pipe_name_W = "\\\\.\\pipe\\fuzail2"

# For linux
tmpDir = "/mnt/c/Users/LENOVO/AppData/Local/Temp"  # tempfile.gettempdir()
pipe_name_R = f"{tmpDir}/fuzail2"
pipe_name_W = f"{tmpDir}/fuzail1"

# Reading from pipe and generating reposnse
print('pythonAgent: Creating Read pipe handle with IPC: ' + pipe_name_R)

receivedMessage, request, response = listenOnPipe(pipe_name_R)

print(f'Message received is: {receivedMessage}')
print('Request object (processed) is:' + request)
print(f'Response to send is: ', response)

# Writing response to pipe
print('pythonAgent: Creating Write pipe handle with pipe: ' + pipe_name_W)
print(f"pythonAgent: Writing Response:\n{response}\nTo pipe: {pipe_name_W}")
writeToPipe(pipe_name_W)
