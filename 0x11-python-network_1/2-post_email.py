#!/usr/bin/python3
"""task 1:  Py script that do post request using urllib
package, then print body of the response (decoded in utf-8)
url + email are passed from user as arguments to py script"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    # post request
    data = parse.urlencode({"email": argv[2]}).encode("ascii")
    fetch_url = request.Request(argv[1], data)
    with request.urlopen(fetch_url) as response:
        print(response.read().decode("utf-8"))
