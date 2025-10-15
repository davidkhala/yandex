import os
import unittest

from davidkhala.yandex.map import API


class SuggestTestCase(unittest.TestCase):
    def test_school(self):
        api_key = os.environ.get('SUGGEST_KEY')
        api = API(api_key)
        school = 'XXI Century Integration International Secondary School'
        r = api.suggest(school)
        self.assertEqual('International Ib School 21st Century Integration', r[0]['name'])

    def test_search(self):
        school = 'XXI Century Integration International Secondary School'
        api_key = os.environ.get('PLACE_KEY')
        api = API(api_key)
        r = api.search(school, 'biz')

        print(r)
    def test_geocode(self):
        api_key = os.environ.get('GEOCODE_KEY')
        address = 'International Ib School 21st Century Integration'
        api = API(api_key)
        r = api.encode(address)
        self.assertEqual('21st Century Tower, Трейд Сентер Секонд', r['name']) # error match


if __name__ == '__main__':
    unittest.main()
