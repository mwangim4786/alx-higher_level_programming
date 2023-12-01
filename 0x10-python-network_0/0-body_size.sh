#!/bin/bash
# Display in bytes the size of a HTTP response header for a given URL.
curl -s "$1" | wc -c
