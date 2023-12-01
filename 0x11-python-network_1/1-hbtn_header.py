#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import sys
import urllib.request

url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.headers['X-Request-Id'])
