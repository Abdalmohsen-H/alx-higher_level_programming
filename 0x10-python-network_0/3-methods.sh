#!/bin/bash
#Show all HTTP methods allowed on a URL; -2f- extract second field and all fields till end of line, -I to get headers only; no need for"-X options"
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
