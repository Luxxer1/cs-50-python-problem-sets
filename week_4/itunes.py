import requests
import sys
import json

if len(sys.argv) == 2:
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]).json()
    for x in response["results"]:
        print(x["trackName"])
