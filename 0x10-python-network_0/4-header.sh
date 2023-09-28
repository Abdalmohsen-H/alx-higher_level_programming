#!/bin/bash
#task 4 send aheader using curl to user specified url
curl -s -H "X-School-User-Id: 98" "$1"
