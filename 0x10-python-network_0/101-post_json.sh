#!/bin/bash
# cURL a JSON fil3
curl -sX POST -H "Content-Type: application/json" -d "$2" "$1"
