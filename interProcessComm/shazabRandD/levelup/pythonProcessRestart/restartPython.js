const { execSync } = require('child_process');
const fs = require('fs')

let pythonProcess = 'hello.py';
console.log(`Stopping Python process: ${pythonProcess}`);
const pidValue = execSync(`ps aux | grep ${pythonProcess} | grep -v grep | awk '{ print $2 }'`)

if (pidValue){
    execSync(`kill ${pidValue}`);
}

if (fs.existsSync('/home/fuzail/Desktop/interProcessComm/levelup/pipe_a')) {
    execSync('sudo rm /home/fuzail/Desktop/interProcessComm/levelup/pipe_a');
}

console.log(`Starting Python process: ${pythonProcess}`);


// execSync('sudo rm /home/fuzail/Desktop/interProcessComm/levelup/pipe_a')
execSync(`python3 /home/fuzail/Desktop/interProcessComm/levelup/${pythonProcess}`);