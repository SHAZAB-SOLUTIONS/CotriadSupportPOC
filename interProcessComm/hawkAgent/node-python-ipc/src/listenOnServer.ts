export function listenOnServer(
    IPC_PATH: any,
    server: any
) {
    return new Promise<string>((resolve) => {
        console.log('listenOnServer: Connecting to path: ' + IPC_PATH);
        console.log('listenOnServer: Listening on pipe: ' + IPC_PATH);
        server.listen(IPC_PATH, () => { })
        server.onClientSocketEnd = (data: string) => {
            const messageFromServer = 'listenOnServer: Message from Server is: ' + data;
            console.log(messageFromServer);
            resolve(messageFromServer);
        };
    });
}