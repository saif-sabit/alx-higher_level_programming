#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: {} <URL>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.getheader("X-Request-Id")
            if request_id:
                print(request_id)
    except Exception as e:
        sys.stderr.write("Error: {}\n".format(str(e)))
        sys.exit(1)
