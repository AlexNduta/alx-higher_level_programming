#!/bin/bash
#Displays all HTTP methods a sever will accept
curl -sI "$1" | grep "Allow:" | cut -f2- -d' '
