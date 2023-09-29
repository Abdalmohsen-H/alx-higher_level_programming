#!/usr/bin/python3
"""task 0:  Py script to show how to fetche urls
using urllib package"""
import urllib.request


if __name__ == "__main__":
    get_url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(get_url) as response:
        res = response.read()
        print("Body response:")
        print(f"\t- type: {type(res)}")
        print("\t- content: {}".format(res))
        print(f"\t- utf8 content: {res.decode('utf-8')}")
