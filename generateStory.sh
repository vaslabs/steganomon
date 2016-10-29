#!/bin/bash

cat my_plain_text.txt | go run testToCoords.go -t2e > my_secret_message.dat

python main.py > story.json