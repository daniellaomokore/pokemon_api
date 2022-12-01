

"""
Get the height and weight of a specific Pokemon and print the output

!!! Extension !!! Print the names of all a specific Pokemon's moves

NOTE:
-json.loads() method converts a JSON string into a Python Dictionary:deserializing
-json.dumps() method converts a Python object and into a JSON string : serializing

"""
import requests
import json
import logging
from pprint import pprint

logging.basicConfig(filemode='example.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.WARNING)





def getPokeName(pokemon):
    nameOfPoke = pokemon['name']
    return nameOfPoke

def getPokeWeight(pokemon):
    weightOfPoke = pokemon['weight']
    return weightOfPoke

def getPokeNameWeight(pokemon):
    name = getPokeName(pokemon)
    weight = getPokeWeight(pokemon)
    nameWeightString = {"Name":{name}, "Weight":{weight}}
    print(nameWeightString)
    return nameWeightString

# POST REQUEST W/headers and body - NAME AND WEIGHT
def postNameWeight(pokemon):
    headers = {'content-type': 'application/json',
           'Authorization': '[your API key]'}

    result = requests.post(
    'http://httpbin.org/post', headers=headers,
    data=json.dumps(getPokeNameWeight(pokemon))
    )

    print(result)
    return result




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
    pokemon = response.json()  # returns as a python dictionary object of entire api
    getPokeNameWeight(pokemon)
    postNameWeight(pokemon)

"""
# GET REQUEST with querystring (using 'params')
result1 = requests.get(
    'http://httpbin.org/get', params=stringling, headers=headers,
)


print(result.text)
print(result1.text)

# serializing- turning python dictionary into jon string

print("Json string, name:", json.dumps(pokemon['name'], indent=4))
print("Json string, weight:", json.dumps(pokemon['weight'], indent=4))
print("Json string, height:", json.dumps(pokemon['height'], indent=4))
#print("Json string- everything:", json.dumps(pokemon, indent=4))



"""
"""

print("Name: {}".format(pokemon['name']))
print("Height: {}".format(pokemon['height']))
print("Weight: {}".format(pokemon['weight']))
print("All Abilities: {}".format(pokemon['abilities']))  # All of it's abilities
print("1st Ability: {}".format(pokemon['abilities'][0]))  # It's first ability
print("2nd Ability: {}".format(pokemon['abilities'][1]))  # It's second ability
"""