#!/bin/bash
# cURL only methods
curl -sI  0.0.0.0:5000/route_4 | sed -n '/Allow: /s/Allow: //p'
