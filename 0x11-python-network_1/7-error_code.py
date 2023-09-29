#!/usr/bin/python3
"""task 7:  Py script that do get request using requests
package, then print body of the response if status code less
than 400, otherwise just return status code
url + email are passed from user as arguments to py script"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
