import json
from unittest import TestCase
import requests
from pokemonDumpsLoadsinOOPClassesFunctions import useAPI

"""
With more time I would cover all edge cases and test the api when unsuccessful and bad requests are made,
"""


class TestConnectToAPI(TestCase):
    pokemon_number = 1

    def test_successful_connection(self):
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(self.pokemon_number)
        response = requests.get(url)
        data = response.text
        pokemon = json.loads(data)

        self.assertEqual(useAPI.connectToAPI(self), pokemon)

    """def test_unsuccessful_connection(self):
        url = 'https://pokeapi.co/api/v2/pokemonn/{}/'.format(self.pokemon_number)
        response = requests.get(url)
        data = response.text
        pokemon = json.loads(data)

        self.assertNotEqual(useAPI.connectToAPI(self), pokemon)"""


class TestSendPokeInfo(TestCase):

    def test_good_post_request(self):

        self.assertEqual(useAPI.sendPokeInfoToAPI(self,name_of_poke="bulbasaur",weight_of_poke="69"),('POST Request is successful, Status code: 200'))

class TestViewPokeInfo(TestCase):

    def test_good_get_request(self):

        self.assertEqual(useAPI.viewPokeInfoFromAPI(self,name_of_poke="yella", weight_of_poke="2"),("GET Request is successful, Status code: 200" ))

