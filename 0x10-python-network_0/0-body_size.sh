#!/bin/bash
#calvulates the total bytes of a http header give. how to use /0-boody_size.sh 
curl -s "$1" | wc -c
