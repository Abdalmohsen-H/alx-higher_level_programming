#!/usr/bin/python3
# task 10(file100): github API challange A.Hesham
# get last 10 commits from a repo
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    res = requests.get(url)
    res_json = res.json()
    try:
        for idx in range(0, 10):
            print("{}: {}".format(
                res_json[idx].get('sha'),
                res_json[idx].get('commit').get('author').get('name')
                ))
    except IndexError:
        pass
    except KeyError:
        pass
    except Exception as e:
        pass
