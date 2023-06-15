const { IpcServer } = require('./index')

const server = new IpcServer();

server.init()

server.listen('\\\\.\\pipe\\fuzail2', (data) => {
    console.log('Listening...')
    console.log('server.chunk is: ', server.chunk);
    console.log('data is: ', data);
})