#!/bin/bash

python decipher.py > edges_sample_python.json

cat edges_sample_python.json | go run testToCoords.go -ep2i > img.png
cp img.png static/img.png