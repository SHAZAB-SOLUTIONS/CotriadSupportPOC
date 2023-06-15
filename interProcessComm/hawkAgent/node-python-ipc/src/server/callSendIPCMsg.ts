import { sendIPCMsg } from "./sendIPCMsg";
import { EXAMPLE_MSG } from "../consts";
import * as fs from 'fs';

fs.readFile('./1_pipepath.txt', 'utf-8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    console.log('File content:', data);
    const ATRI_IPC_PATH = data;
    console.log("callSendIPCMsg.ts: Ran callSendIPCMsg", ATRI_IPC_PATH);
    sendIPCMsg(EXAMPLE_MSG, ATRI_IPC_PATH)
        .then((data) => {
            console.log('callSendIPCMsg.ts: data is: ' + data);
            console.log('callSendIPCMsg.ts: Type of data is: ' + typeof data);
            console.log("callSendIPCMsg.ts: message sent: " + EXAMPLE_MSG);
        })
        .catch(console.log);

})


// declare global {
//     namespace NodeJS {
//         interface ProcessEnv {
//             ATRI_IPC_PATH: string;
//         }
//     }
// }

// sendIPCMsg(EXAMPLE_MSG, ATRI_IPC_PATH)
//     .then((data) => {
//         console.log('callSendIPCMsg.ts: data is: ' + data);
//         console.log('callSendIPCMsg.ts: Type of data is: ' + typeof data);
//         console.log("callSendIPCMsg.ts: message sent: " + EXAMPLE_MSG);
//     })
//     .catch(console.log);
