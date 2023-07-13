#!/usr/bin/python3
""" module """

import sys


counter = 0
data = {"File size": 0, "200": 0, "301": 0, "400": 0,
        "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
globaldata = []


try:
    for line in sys.stdin:
        if counter == 10:
            counter = 0
            for key, value in globaldata[0].items():
                if value == 0:
                    continue
                print(key+": "+str(value))
                sys.stdout.flush()
        counter += 1
        if counter == 1:
            globaldata.insert(0, data.copy())
        line = line.rstrip()
        globaldata[0]["File size"] += int(line.split()[-1])
        globaldata[0][line.split()[-2]] += 1
    if counter > 0:
        for key, value in globaldata[0].items():
            if value == 0:
                continue
            print(key+": "+str(value))
            sys.stdout.flush()
except KeyboardInterrupt as e:
    for key, value in globaldata[0].items():
        if value == 0:
            continue
        print(key+": "+str(value))
        sys.stdout.flush()
    print(e)
