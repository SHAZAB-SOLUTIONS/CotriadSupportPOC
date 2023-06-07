const fs = require('fs');

const fd = Number(process.argv[2]);

const stream = fs.createWriteStream(null, {fd: fd});

for (let i = 1;i <=10; i++) {
    while (true) {
        try {
            console.log(`Writing ${i}`);
            stream.write(`${i}\n`);
            stream.flush();
            // if (i % 6 ===0) {
            //     console.log('Intentionally sleeping for 5 seconds...');
            //     await new Promise(resolve => setTimeout(resolve, 5000));
            // }
            break;
        } catch (err) {
            //Handle write errors
        }
    }
}

stream.end();