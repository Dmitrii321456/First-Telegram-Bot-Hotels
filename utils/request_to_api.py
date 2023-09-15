from loguru import logger
from logs.logers import func_loggers

import requests


@func_loggers
def request_to_api(method, headers, url, **kwargs):
    """Функция выполняет запрос на API"""

    try:
        response = requests.request(method=method, headers=headers, url=url, timeout=10, **kwargs)
        if response.status_code == requests.codes.ok:
            return response.text

    except Exception as er:
        logger.error(str(er))
        return None

