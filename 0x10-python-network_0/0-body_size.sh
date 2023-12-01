#!/usr/bin/bash
#calculates the total bytes of a http header give. how to use /0-boody_size.sh 
curl -sI "$1" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r\n'

