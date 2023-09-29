#!/usr/bin/python3
"""task 5:  Py script to show how to fetche urls
using requests package and get header value
url is passed from user as argument to the py script"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get("X-Request-Id"))
