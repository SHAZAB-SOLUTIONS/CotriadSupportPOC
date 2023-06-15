import { Socket } from "net";
// import util from "util";

export function sendIPCMsg(msg: string, IPC_PATH: string) {
  return new Promise<void>((res, rej) => {
    // const ATRI_IPC_PATH = "\\\\.\\pipe\\fuzail949b1d428cc1eec1ee902bdcdec55402rockzzz"
    console.log('sendIPCMsg.ts: ATRI_IPC_PATH is: ', + IPC_PATH);
    // console.log('sendIPCMsg.ts: Type of ATRI_IPC_PATH is: ', + typeof ATRI_IPC_PATH);
    console.log('sendIPCMSG.ts: msg is :' + msg);

    if (typeof IPC_PATH !== "string") {
      rej("ATRI_IPC_PATH environment variable is required.");
      return;
    }
    const socket = new Socket();
    console.log('sendIPCMsg.ts: Connecting to socket: '); // + util.inspect(socket));

    socket.connect(IPC_PATH, () => {
      console.log('sendIPCMsg.ts: Connected to socket: '); // + util.inspect(socket));
      socket.write(msg, (err) => {
        console.log('sendIPCMsg.ts: Writing to socket: ');
        if (err) {
          rej(err);
        } else {
          res();
          socket.destroy();
        }
      });
    });
  });
}
