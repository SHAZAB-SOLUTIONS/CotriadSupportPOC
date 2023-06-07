import threading
import os

def main(cameraName, bashScript):
    print(f"Recording {cameraName}")
    os.system(f'bash {bashScript}')

directory = "/home/fuzail/Desktop/ShazabInternal/CameraRecording"
bashScripts = [scripts for scripts in os.listdir(directory) if scripts.endswith('.sh')]
# print(bashScripts)
threads = []

for bashScript in bashScripts:
    cameraName = bashScript[:-3]
    th = threading.Thread(target=main, args=(cameraName, bashScript))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()