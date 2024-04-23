#!/usr/bin/node

// Import the 'request' module.
const request = require('request');

// Construct the URL for the specific Star Wars film by appending argv[2].
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Perform HTTP GET request to the constructed URL using request.
request(url, function (error, response, body) {
  // print to console the title if successful, error if not.
  console.log(error || JSON.parse(body).title);
});
