#!/usr/bin/node

// Import 'fs' module
const fs = require('fs');

// Import 'request' module
const request = require('request');

// Use 'request' module to perform an HTTP GET request to the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
