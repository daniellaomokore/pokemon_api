### EXERCISE 5 ###

"""
This API is called 'Pokeapi'
It gives access to data about Pokemons
This API is free and does not require any authentication!

Each Pokemon has a number that identifies it

You can retrieve information about different Pokemon from urls

https://pokeapi.co/api/v2/pokemon/6/

"""

"""
import json
import requests
from pprint import pprint

pokemon_number = input("What is he Pokemon's ID?")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(response)"""

### EXERCISE 6 ###

"""
Get the height and weight of a specific Pokemon and print the output

!!! Extension !!! Print the names of all a specific Pokemon's moves

"""


"""
NOTE:
-json.loads() method converts a JSON string into a Python Dictionary:deserializing 
-json.dumps() method converts a Python object and into a JSON string : serializing

"""
import requests
import json
import logging
from config import api_auth_key
from pprint import pprint

logging.basicConfig(filemode='example.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.WARNING)



try:
    pokemon_number = input("What is he Pokemon's ID?")
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.ConnectionError as cerr:
    print("Sorry a Connection error has been found")
    logging.warning(cerr)
except requests.exceptions.HTTPError as err:
    print("Bad Status Code", response.status_code)
else:
    print("Status code:", response.status_code)



#print(type(response))   ## prints the data type : 'request.models.Response''

pokemon = response.json()  # returns as a python dictionary object
#print(type(pokemon))     # prints the data type : python dict
#print(pprint(pokemon)) # prints entire python dictionary for the chosen pokemon

nameOfPoke = pokemon['name']
weightOfPoke = pokemon['weight']

print("Name: ", nameOfPoke)      # in python object form
print(json.dumps(nameOfPoke))    # in json string form
print("Weight: ", weightOfPoke)


# INITIALISING THE BODY AND HEADERS FOR REQUESTS
# YOU would probably have a different body depending on the request you want to do
body = {"Name": {nameOfPoke}, "Weight": {weightOfPoke}}

headers = {'content-type': 'application/json',
           'Authorization': '{key}'.format(key=api_auth_key)}


# POST REQUEST W/headers and body
result = requests.post(
    'http://httpbin.org/post', headers=headers,
    data=body
)


# GET REQUEST with headers and query string (using 'params')
result1 = requests.get(
    'http://httpbin.org/get', params=body, headers=headers,
)


print(result.text)
print(result1.text)


# serializing- turning python dictionary into json string
print("Json string, name:", json.dumps(pokemon['name'], indent=4))
print("Json string, weight:", json.dumps(pokemon['weight'], indent=4))
print("Json string, height:", json.dumps(pokemon['height'], indent=4))
#print("Json string- everything:", json.dumps(pokemon, indent=4))




"""

print("Name: {}".format(pokemon['name']))
print("Height: {}".format(pokemon['height']))
print("Weight: {}".format(pokemon['weight']))
print("All Abilities: {}".format(pokemon['abilities']))  # All of it's abilities
print("1st Ability: {}".format(pokemon['abilities'][0]))  # It's first ability
print("2nd Ability: {}".format(pokemon['abilities'][1]))  # It's second ability
"""