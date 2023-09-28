#!/bin/bash
# return response body for a request on a given URL only if status code == 200; also follow redirects with option L
curl -s -o /dev/null -w "%{http_code}\n" -L "$1" | ( read -r status; [ "$status" -eq 200 ] && curl -s -L "$1" )
