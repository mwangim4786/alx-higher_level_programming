#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    # with urllib.request.urlopen(req) as response:
    # body = response.read()
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    else:
        body = response.read()
        print("{}".format(body.decode("utf-8")))
