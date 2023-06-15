import { Socket } from "net";

export function writeToPipe(
    IPC_PATH: any,
    message: any
) {
    return new Promise<string>((resolve, reject) => {
        const socket = new Socket();
        console.log('writeToPipe: Connecting to path: ' + IPC_PATH);
        socket.connect(IPC_PATH, () => {
            console.log('writeToPipe: Connected to pipe to write! ');
            console.log('writeToPipe: Writing to pipe: ' + message);
            socket.write(message, (err) => {
                if (err) {
                    console.log('writeToPipe: Error is: ' + err);
                    reject(err);
                }
                console.log('writeToPipe: Successfully wrote!!');
                resolve(message)
            });
        });
    });
}