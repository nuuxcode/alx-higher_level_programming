#!/usr/bin/python3
""" module """

def append_after(filename="", search_string="", new_string=""):
    ip=1
    with open(filename ,'r') as f:
        lines = f.readlines()
        new_list=lines[:]
        for i, string in enumerate(lines):
                print(search_string+str(i))
                new_list.insert(i+ip, new_string)
                ip+=1
                continue

    with open(filename, 'w') as f:
        f.writelines(new_list)
