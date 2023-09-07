import json
from pprint import pprint
from typing import Optional, Dict
from config import API_KEY
from reqest_to_api import request_to_api
import re
import requests
from logs.logers import func_logers


@func_logers
def city_founding(city: str) -> Optional[Dict[str, str]]:
    """Производится поиск городов по названию"""
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {
        "q": city,
        "locale": "en_US",
        "langid": "1033",
        "siteid": "300000001"
    }

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = request_to_api(method='GET', url=url, headers=headers,
                              params=querystring)

    if response:
        pattern = r'"@type":.*"gaiaRegionResult"'
        find_result = re.search(pattern, response)
        if find_result:
            result = json.loads(response)
            cities = dict()
            for sr in result['sr']:
                if sr['@type'] == 'gaiaRegionResult':
                    city = sr['regionNames']['shortName']
                    city_id = sr['gaiaId']
                    cities[city_id] = city
            pprint(cities)
            return cities



city_founding('London')


