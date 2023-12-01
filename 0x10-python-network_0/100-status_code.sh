#!/bin/bash
# Sends a GET request to a URL passed as an argument, and display the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
