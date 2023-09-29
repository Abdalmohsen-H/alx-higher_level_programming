#!/usr/bin/python3
"""task 6:  Py script that do post request using requests
package, then print body of the response
url + email are passed from user as arguments to py script"""
import requests
from sys import argv


if __name__ == "__main__":
    data = {
            "email": argv[2],
            }

    response = requests.post(argv[1], data)

    print(response.text)
