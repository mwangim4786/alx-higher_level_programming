#!/usr/bin/python3
"""Python script that sends a POST request a passed URL an email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    email = urllib.parse.urlencode(email)
    email = email.encode("ascii")

    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
