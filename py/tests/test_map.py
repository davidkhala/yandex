import os
import unittest

from davidkhala.yandex.map import API


class SuggestTestCase(unittest.TestCase):
    def test_school(self):
        api_key = os.environ.get('SUGGEST_KEY')
        api = API(api_key)
        school = 'XXI Century Integration International Secondary School'
        r = api.suggest(school)
        print(r[0]['name'])
    def test_search(self):
        school = 'XXI Century Integration International Secondary School'
        api_key = os.environ.get('PLACE_KEY')
        api = API(api_key)
        r = api.search(school, 'biz')

        print(r)

if __name__ == '__main__':
    unittest.main()
