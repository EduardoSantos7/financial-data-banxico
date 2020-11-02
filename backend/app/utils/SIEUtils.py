import os

import requests


class SIEUtils:
    SIE_TOKEN = os.getenv('SIE_TOKEN')
    BASE_URL = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/'

    @staticmethod
    def get_data(serie, start_date, end_date):
        url = f'{SIEUtils.BASE_URL}{serie}/datos/{start_date}/{end_date}'
        headers = {
            'Bmx-Token': SIEUtils.SIE_TOKEN,
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json().get('bmx', {}).get('series', [])[0].get('datos', [])

        return []


class SIESeries:
    UDIS = 'SP68257'
    Dollars = 'SF63528'
