#!/usr/bin/python3
"""task 9:  Py script that do get request using requests
package, then print user ID from the response if it's a valid json
, otherwise just return error msg
auth info is passed from user as arguments to py script
github API with Basic Authentication """
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    if len(argv) < 3:  # missing req arguments
        print('missing req arguments')

    else:
        username = argv[1]  # github uses username or email as username
        passwd = token = argv[2]  # github uses token as passwd

        basic = HTTPBasicAuth(username, passwd)
        res = requests.get('https://api.github.com/user', auth=basic)

        # another way not required in this task
        # headers = {"Authorization" : "Bearer " + token}
        # res = requests.get('https://api.github.com/user', headers=headers)

        try:
            print(res.json().get('id'))

        except ValueError:
            print("Not a valid JSON")
