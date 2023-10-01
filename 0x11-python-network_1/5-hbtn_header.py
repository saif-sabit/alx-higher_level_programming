#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the variable
X-Request-Id in the response header
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: {} <URL>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)

    request_id = response.headers.get("X-Request-Id")
    if request_id:
        print(request_id)
