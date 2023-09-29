#!/usr/bin/python3
"""task 3:  Py script that do get request using urllib
package, then print body of the response (decoded in utf-8)
otherwise print error code
url is passed from user as arguments to py script"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
