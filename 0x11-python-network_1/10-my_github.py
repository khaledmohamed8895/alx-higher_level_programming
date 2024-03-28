#!/usr/bin/python3
"""
Use Github API to display the id
"""

if __name__ == "__main__":
    import requests
    import sys
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    passwaord = sys.argv[2]
    response = requests.post(url, auth=(username, passwaord))
    try:
        res = response.json()
        id = res.get('id')
        print(id)
    except ValueError:
        print("Not a valid JSON")
