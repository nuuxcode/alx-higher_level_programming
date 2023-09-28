#!/bin/bash
# Only status cod3
curl -sw '%{http_code}' -o /dev/null "$1"
