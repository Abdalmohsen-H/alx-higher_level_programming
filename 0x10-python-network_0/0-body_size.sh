#!/bin/bash
# task 0: Bash script to take a URL from user "$1", Then send a request, s option means silent;then show size of response body in bites |wc -c
curl -s "$1" | wc -c
