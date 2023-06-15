import { generateSocketFilename } from "../generateSocketFilename";
import { generatePipePath } from "../generatePipePath";
import { createIPCServer } from "../createIPCServer";
import { listenOnServer } from "../listenOnServer";
import { writeToPipe } from "../writeToPipe";

import requestObj from "./requestObj.json"

import * as fs from 'fs';


// const IPC_PATH_1 = requestObj.pipe

const IPC_PATH_1 = generateSocketFilename({ prefix: 'fuzail', suffix: '2' });

const server_2 = createIPCServer({
    onClientSocketEnd: (data: string) => {
        const messageFromServer: string = 'nodeAgentForSnapshot.ts: createIPCServer: onClientSocketEnd: Message from Server is: ' + data.slice();
        console.log(messageFromServer);
    }
})

console.log('nodeAgentForSnapshot: IPC Server created!: Server_2!!!');

const IPC_PATH_2 =
    process.platform === "win32"
        ? generatePipePath({
            prefix: 'fuzail',
            suffix: '2'
        })
        : generateSocketFilename({
            prefix: 'fuzail',
            suffix: '2'
        });

console.log('nodeAgentForSnapshot: Pipe created is: ' + IPC_PATH_2);

const fileName_2: string = `../2_pipePath.txt`;
fs.writeFile(fileName_2, IPC_PATH_2, { flag: 'w' }, (err) => {
    if (err) {
        console.error('nodeAgentForSnapshot.ts: An error occurred while writing to the file:', err);
    } else {
        console.log('nodeAgentForSnapshot.ts: Successfully wrote pipe path to the file: ' + fileName_2);
    }
})

// Main
listenOnServer(IPC_PATH_2, server_2)
writeToPipe(IPC_PATH_1, JSON.stringify(requestObj))