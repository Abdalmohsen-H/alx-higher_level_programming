#!/bin/bash
# task 0: Bash script to take a URL from user as argument -> "$1", Then
# send a request to this URL -> curl -s "$1" # s option means silent
# then show size of response body in bites -> | wc -c
curl -s "$1" | wc -c
