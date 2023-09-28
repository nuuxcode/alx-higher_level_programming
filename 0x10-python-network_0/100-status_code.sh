#!/bin/bash
# Only status cod3
curl -sw '%{http_code}\n' -o /dev/null 0.0.0.0:5000
