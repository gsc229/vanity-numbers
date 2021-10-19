import os
import json
import requests

url = "https://wordsapiv1.p.rapidapi.com/words/"

querystring = {"letterPattern":"^[a-zA-Z]+$", "lettersmin":"2", "lettersMax":"7", "limit":"56000"}

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': os.getenv("RAPID_API_KEY")
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()
data = response["results"]["data"]
print(data)

with open("words.json", 'w') as outfile:
  json.dump(data, outfile)
