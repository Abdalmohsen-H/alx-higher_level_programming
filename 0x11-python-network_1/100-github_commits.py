#!/usr/bin/python3
# task 10(file100): github API challange A.Hesham
# get last 10 commits from a repo
import requests
from sys import argv

repo = argv[1]
owner = argv[2]
url = f"https://api.github.com/repos/{repo}/{owner}/commits"
res = requests.get(url)
res = res.json()
for idx in range(0, 10):
    print(f"{res[idx].get('sha')}: {res[idx]['commit']['author'].get('name')}")
