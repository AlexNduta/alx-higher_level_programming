#!/bin/bash
#make a GET request an adds specific headers to be sent
curl -sH "X-School-User-Id":98 "$1"
