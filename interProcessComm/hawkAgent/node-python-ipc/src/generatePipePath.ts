// import crypto from "crypto";

export function generatePipePath(options: {
    prefix?: string;
    suffix?: string;
  }) {
    console.log('generatePipePath.ts: Generating pipe path!');
    let { prefix, suffix } = options;
    prefix = prefix !== undefined ? prefix : "pipe";
    suffix = suffix !== undefined ? suffix : "";
    // const randomString = crypto.randomBytes(16).toString("hex");
    // return `\\\\.\\pipe\\${prefix}${randomString}${suffix}`;
    return `\\\\.\\pipe\\${prefix}${suffix}`;
  }
  
  // const options = {
  //   prefix: 'fuzail',
  //   suffix: 'rockzzz'
  // }
  
  // const pipeName: unknown = generatePipePath(options);
  
  // console.log(pipeName);
  
  