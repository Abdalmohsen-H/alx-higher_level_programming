#!/usr/bin/python3
"""task 1:  Py script to show how to fetche urls
using urllib package and get header value
url is passed from user as argument to the py script"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    get_url = urllib.request.Request(argv[1])
    with urllib.request.urlopen(get_url) as response:
        print(response.getheader("X-Request-Id"))
