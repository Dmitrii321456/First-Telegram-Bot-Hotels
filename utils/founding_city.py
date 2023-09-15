import json
import re
from pprint import pprint
from typing import List, Dict
from logs.logers import func_loggers
from config import API_KEY
from loguru import logger
import requests

@func_loggers
def check_connection(method, url, headers, **kwargs):
    try:
        response = requests.request(method=method, url=url, headers=headers, **kwargs)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        logger.error(f'Connection is not found, error: {e}')

@func_loggers
def find_cities(city: str):
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {"q": city, "locale": "en_US", "langid": "1033", "siteid": "300000001"}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    response = check_connection(method='GET', url=url,  headers=headers, params=querystring)
    if response:
        pattern = r'"@type":.*"gaiaRegionResult"'
        find_result = re.search(pattern, response)
        date = json.loads(response)
        if find_result:
            cities = dict()
            for sr in date['sr']:
                if sr['@type'] == 'gaiaRegionResult':
                    city = sr['regionNames']['shortName']
                    city_id = sr['gaiaId']
                    cities[city_id] = city
            return cities
    else:
        logger.error('Ошибка в поиске json')


@func_loggers
def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None





