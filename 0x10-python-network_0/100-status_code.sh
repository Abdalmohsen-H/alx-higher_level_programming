#!/bin/bash
#task 100 get numeric HTTP status code only, by using -w "%{http_code}\n" and sending body to /dev/null using -o option
curl -s -o /dev/null -w "%{http_code}" "$1"
