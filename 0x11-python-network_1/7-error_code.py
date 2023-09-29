#!/usr/bin/python3
""" module doc """
import requests
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        res = requests.get(url)
        print(res.text)
    except requests.exceptions.RequestException as e:
        print(f"Error code: {e}")
