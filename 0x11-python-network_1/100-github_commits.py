#!/usr/bin/python3
# task 10(file100): github API challange A.Hesham
# get last 10 commits from a repo
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    res = requests.get(url)
    res_json = res.json()
    try:
        for idx in range(0, 10):
            print("{}: {}".format(
                res_json[idx].get('sha'),
                res_json[idx]['commit']['author'].get('name')
                )
                )
    except IndexError:
        pass
