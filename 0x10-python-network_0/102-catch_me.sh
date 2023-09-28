#!/bin/bash
# find the right method and body and header to get "you got me response from specific URL", also the right url is theris is a redirection
curl -s -L -X PUT -H "Origin:School" -d "user_id=98" "0.0.0.0:5000/catch_me_2"
