import requests
import sys
import json
#code to take only one user input
if len(sys.argv) != 2:
    sys.exit()
#code to connet to the apple url 

response= requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
o= response.json() #grabbing from server the json object
for result in o["results"]:
    print(result["trackName"])
