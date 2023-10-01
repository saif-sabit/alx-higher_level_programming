#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: {} <URL>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('ascii')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
