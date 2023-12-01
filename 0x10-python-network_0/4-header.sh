#!/bin/bash
#make a GET request an adds specific headers to be met
curl -sH "X-School-User-Id" "$1"
