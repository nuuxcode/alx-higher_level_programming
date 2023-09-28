#!/bin/bash
# cURL b0dy siz3
curl -s -w '%{size_download}\n' -o /dev/null "$1"
