#!/usr/bin/python3
"""task 4:  Py script to show how to fetche urls
using requests package"""
import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print(f"\t- type: {type(res.text)}")  # str
    # print(f"\t- type: {type(res.content)}")  # bytes
    print("\t- content: {}".format(res.text))
