#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print(f"Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.content.decode()}")
