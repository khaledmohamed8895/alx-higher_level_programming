#!/usr/bin/python3
""" Print the status_code if it's > 400 """

if __name__ == "__main__":
    import requests
    import sys
    from urllib.error import HTTPError
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
