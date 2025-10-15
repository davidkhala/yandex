from typing import Literal

from davidkhala.http_request import Request


class API(Request):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key

    def request(self, url, method: str, params=None, data=None, json=None) -> dict:
        params['apikey'] = self.api_key
        return super().request(url, method, params, data, json)

    def suggest(self, query):
        """
        :param query:
        :return: No lng,lat in return
        """
        r = self.request('https://suggest-maps.yandex.ru/v1/suggest', "GET", {
            'text': query
        })
        return [{
            'name': result['title']['text'],
            'subtitle': result['subtitle']['text'],
            'tags': result['tags'],
            'distance': result['distance']['value']
        } for result in r['results']]

    def search(self, query, _type: Literal['geo', 'biz']):
        """
        commercial api that commitment start from $2000
        :param query:
        :param _type: geo for address. biz for entity
        :return:
        """
        r = self.request('https://search-maps.yandex.ru/v1/', 'GET', {
            'text': query,
            'type': _type
        })
        return r

    def encode(self, address: str):
        r = self.request('https://geocode-maps.yandex.ru/v1/', 'GET', {
            'geocode': address,
            'format': 'json'  # mandatory
        })
        _ = r['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']

        longitude, latitude = _['Point']['pos'].split(' ')

        return {
            'name': _['name'],
            'longitude': longitude,
            'latitude': latitude,
            'uri': _['uri'],
        }
