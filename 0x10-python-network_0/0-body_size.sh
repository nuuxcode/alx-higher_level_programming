#!/bin/bash
# cURL b0dy siz3
curl -sw '%{size_download}\n' -o /dev/null "$1"
