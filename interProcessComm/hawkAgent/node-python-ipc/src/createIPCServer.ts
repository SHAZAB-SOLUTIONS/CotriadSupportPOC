import net from "net";

export function createIPCServer(callbacks: {
    onClientSocketEnd?: (data: string) => void;
}) {
    const { onClientSocketEnd } = callbacks;
    let chunk = "";
    const server = net.createServer((socket) => {
        socket.on("data", (data) => {
            chunk = data.toString();
            console.log('createIPCServer.ts: chunk is: ' + chunk); // .slice(-35));
        });
        socket.on("end", function () {
            onClientSocketEnd?.(chunk);
            // server.close();
        });
    });
    return server;
}