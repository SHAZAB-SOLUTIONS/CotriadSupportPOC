# Initial Setup
(As of 12 Jun 2023, 6:30 pm, using OS: Windows 10)

After cloning this repository, navigate to the IPC directory:

    cd hawk/IPC

Create the 'node' and 'python virtual' environments usiing following commands:

    a. For node:

        npm install

    b. For python

        python -m venv ipc
        ipc/Scripts/activate
        pip install pywin32 opencv-python

# USAGE 
The open two Command line interfaces and navigate to 'node-python-ipc\src\python-agent' in one of them and 'node-python-ipc\src\node-agent' in other.

Run 'python pythonAgent.py' in the python-agent directory and 'ts-node agent.ts' in the node-agent directory. 