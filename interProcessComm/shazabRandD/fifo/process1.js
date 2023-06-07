const fs = require('fs');
// const { logger } = require('./utils');

console.log(`Pid:${process.pid}`);

const fifo = '/tmp/process_fifo.txt';

// Create a fifo, fs.mkfifoSync will block until there is a reader (process2)
fs.mkfifo(fifo);

// Open fifo for writing
const file = fs.createWriteStream(fifo);

// Attempt to write to our fifo
const myName = 'Fuzail';
while (true) {
  try {
    console.log(`Writing ${myName}`);
    file.write(`${myName}\n`);
    break;
  } catch (error) {}
}

// Clean up fifo
file.close();

// Log completion
console.log('Finished process 1');
