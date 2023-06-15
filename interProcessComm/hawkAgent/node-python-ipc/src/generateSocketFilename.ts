import os from "os";
import path from "path";
// import crypto from "crypto";

export function generateSocketFilename(options: {
    prefix?: string;
    suffix?: string;
    tmpdir?: string;
}) {
    console.log('generateSocketFilename.ts: Generating socket name!');
    let { prefix, suffix, tmpdir } = options;
    prefix = prefix !== undefined ? prefix : "atri";
    suffix = suffix !== undefined ? suffix : "";
    tmpdir = tmpdir !== undefined ? tmpdir : os.tmpdir();
    return path.join(
        tmpdir,
        prefix + suffix
        // prefix + crypto.randomBytes(16).toString("hex") + suffix
    );
}

// const options = {
//   prefix: 'Atri',
//   suffix: 'fuzail',
// }
// const pathOf: unknown = generateSocketFilename(options)

// console.log(pathOf);


// const options = {
//     prefix: 'fuzail',
//     suffix: 'rockzzz'
// }

// const pipeName: unknown = generateSocketFilename(options);

// console.log(pipeName);

