#!/usr/bin/python3
""" module doc """
import urllib.request


if __name__ == "__main__":
    try:
        url = "https://alx-intranet.hbtn.io/status"
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
