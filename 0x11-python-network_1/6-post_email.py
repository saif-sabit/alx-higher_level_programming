#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: {} <URL> <email>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    dect_email = {'email': email}
    response = requests.post(url, data=dect_email)
    print(response.text)
