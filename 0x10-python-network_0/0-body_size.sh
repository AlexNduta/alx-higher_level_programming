#!/bin/bash
#calvulates the total bytes of a http header give. how to use /0-boody_size.sh 
curl -sI "$1" | grep 'Content-Length:' | wc -c
