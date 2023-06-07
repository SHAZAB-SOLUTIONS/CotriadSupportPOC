const fs              = require('fs');
const { spawn, fork } = require('child_process');

const path_a = 'pipe_a';
const path_b = 'pipe_b';
let fifo_b   = spawn('mkfifo', [path_b]);  // Create Pipe B

fifo_b.on('exit', function(status) {
    console.log('Created Pipe B');

    const fd   = fs.openSync(path_b, 'r+');
    let fifoRs = fs.createReadStream(null, { fd });
    let fifoWs = fs.createWriteStream(path_a);

    console.log('Ready to write')

    const message = {
        camera : {
            rtspLink: "rtsp://admin:Shazabadmin123@172.16.1.6:554",
            name : "Office Room 2"
        },
        command: "Get Snaphot"
    }
    
    console.log(message);
    console.log(JSON.stringify(message));
    console.log('-----   Send packet   -----');
    fifoWs.write(JSON.stringify(message))


    fifoRs.on('data', data => {
        console.log('----- Received packet -----');
        console.log('    Snapshot Path   : ' + data.toString());
    });
});