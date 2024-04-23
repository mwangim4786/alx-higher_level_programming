#!/usr/bin/node
const request = require('request');
// Import the request module.

request.get(process.argv[2]).on('response', function (response){
// Use request module to perform HTTP request to the url.
// event listener for the response event.

  console.log('code: ${response.statusCode}');
  // print the HTTP status code to the console.
});
