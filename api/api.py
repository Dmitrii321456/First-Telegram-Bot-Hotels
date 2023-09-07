import json
from pprint import pprint

import requests

url = "https://hotels4.p.rapidapi.com/locations/v2/search"

querystring = {"query":"london","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Key": "b20e489dffmsh610ebca1f4e9ff3p1b9accjsn2309ade45d2a",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
json_response = json.loads(response.text)
pprint(json_response['suggestions'])