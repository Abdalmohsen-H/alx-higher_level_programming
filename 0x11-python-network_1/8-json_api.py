#!/usr/bin/python3
"""task 7:  Py script that do post request using requests
package, then print body of the response if it's a valid json
, otherwise just return error msg
query_param is passed from user as arguments to py script
query_param is a letter , if no param just send q='' """

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:  # no argument passed to py script
        letter = ""
    else:
        letter = argv[1]
    data = {'q': letter}
    res = requests.post("http://0.0.0.0:5000/search_user", data)

    try:
        res_json = res.json()
        if res_json == {}:  # JSON is empty
            print("No result")
        else:
            print(f"[{res_json.get('id')}] {res_json.get('name')}")

    except ValueError:
        print("Not a valid JSON")
