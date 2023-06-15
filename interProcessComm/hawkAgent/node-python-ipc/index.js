const net = require("net");


class IpcServer {
    constructor() {
        this.server = null;
        this.chunk = "";
    }

    init() {
        this.server = net.createServer((socket) => {
            socket.on("data", (data) => {
                this.chunk = this.chunk + data.toString();
                console.log('data is: ', data.toString());
            });

            socket.on("end", function () {
                console.log('message: ', this.chunk);
                this.server.close();
            });
        });
    }

    listen(pipePath, handler) {
        this.server.listen(pipePath, handler);
    }
}

class IpcSender {
    init(remotePipePath) { }

    send(msgObject) { }
}

module.exports = { IpcSender, IpcServer };
