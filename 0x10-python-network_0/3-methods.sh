#!/bin/bash
#Displays all HTTP methods a sever will accept
curl -s "$1" | grep "Allow:" | cut -f2 -d ' '
