const fs              = require('fs');
const { spawn, fork } = require('child_process');

const path_b = 'pipe_b';

const restartPythonProcess = (pythonProcess) => {
    const pidValue = spawn(`ps aux | grep ${pythonProcess} | grep -v grep | awk '{ print $2 }'`);
    if (pidValue){
        spawn(`kill ${pidValue}`);
    }
    
    console.log('Hello World');
}

const fd   = fs.openSync(path_b, 'r+');
let fifoRs = fs.createReadStream(null, { fd });

fifoRs.on('data', data => {
    for (i=0; i < 5; i++) {
        console.log('----- Received packet -----');
        console.log('    Number   : ' + data.toString());
        if (i == 2) {
            let pyProcess = 'myPythonProcess.py';
            const pidValue = spawn(`ps aux | grep ${pyProcess} | grep -v grep | awk '{ print $2 }'`);
            console.log(pidValue);
            // restartPythonProcess(pyProcess)
        }
        
    }
});

