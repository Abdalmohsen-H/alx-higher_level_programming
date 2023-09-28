#!/bin/bash
#task 5 post request with multiple params usin -d option (--data option); url is an argument to bash script
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
