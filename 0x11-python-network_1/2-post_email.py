#!/usr/bin/python3
"""Python script that sends a POST request a passed URL an email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
