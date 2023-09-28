#!/bin/bash
#task8: send post rquest with JSON file data; Json file path is 2nd arg to bash script, URL is 1st arg, you could use "cat"$2"", -X POST not req here
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
