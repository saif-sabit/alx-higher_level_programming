#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: {} <URL> <email>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data)

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except Exception as e:
        sys.stderr.write("Error: {}".format(str(e)))
        sys.exit(1)
