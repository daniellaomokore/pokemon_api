### EXERCISE 5 ###

"""
This API is called 'Pokeapi'
It gives access to data about Pokemons
This API is free and does not require any authentication!

Each Pokemon has a number that identifies it

You can retrieve information about different Pokemon from urls

https://pokeapi.co/api/v2/pokemon/6/

"""
import json

import endpoint

"""import requests
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

import requests
from pprint import pprint


pokemon_number = input("What is he Pokemon's ID?")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response.status_code)

pokemon = response.json() # returns the JSON as python dictionary object (if the result was written in JSON format, if not it raises an error).
#print(pprint(pokemon))
data = json.loads()

nameOfPoke = pokemon['name']
weightOfPoke = pokemon['weight']
print("Name: ", nameOfPoke)
print("Weight:", weightOfPoke)

headers = {'content-type': 'application/json',
           'Authorization': '[your API key]'}
result = requests.post(
    'http://httpbin.org/post', headers=headers,
    data=json.dumps("Name: {} , Weight: {}".format(nameOfPoke, weightOfPoke)),
)

print(result.status_code)
print(result.text)


"""

print("Name: {}".format(pokemon['name']))
print("Height: {}".format(pokemon['height']))
print("Weight: {}".format(pokemon['weight']))
print("All Abilities: {}".format(pokemon['abilities']))  # All of it's abilities
print("1st Ability: {}".format(pokemon['abilities'][0]))  # It's first ability
print("2nd Ability: {}".format(pokemon['abilities'][1]))  # It's second ability
"""