#!/bin/bash
#Makes a POST request to the sever
curl -sd "email=test@gmail.com" "subject=I will always be here for PLD" "$1"
