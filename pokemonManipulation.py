import requests
import json
import logging

"""HERE WE ARE PRACTISING DATA MANIPULATION OF THE DATA WE GET FROM THE API

-LIST COMPREHENSION

-MAPPING
"""




logging.basicConfig(filemode='example.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.WARNING)

try:
    pokemon_name = input("Enter a pokemon name:")
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)
    response = requests.get(url)
    response.raise_for_status()
    # don't run rest of code
except requests.exceptions.ConnectionError as cerr:
    print("Sorry a Connection error has been found")
    logging.warning(cerr)
    # don't run the rest of the code
except requests.exceptions.HTTPError as err:
    print("Bad Status Code", response.status_code)
    # don't run rest of code
else:
    print("Status code:", response.status_code)

pokemon = response.json()  # returns as a python dictionary object, extracting the API result inJSON format

### Filtering list data W/ LIST COMPREHENSION ###

pokemonAbilities = [skill['ability']['name'] for skill in pokemon['abilities']]   # The name of all the skills the pokemon has

pokemonWeight = pokemon['weight']

print(
    "{} has all of the following abilities: {}.\nThey weigh {}.".format(pokemon_name, pokemonAbilities, pokemonWeight))



""" THIS IS COMPLETELY SEPEARTE FROM THE INOF ABOVE, THIS USES A DIFFERENT URL"""
### REMAPPING or NORMALISING Data with MAP ###

url20AllPoke= "https://pokeapi.co/api/v2/pokemon/"
response2 = requests.get(url20AllPoke)
all20Poke = response2.json()
#print(p)

infoOf20Pokemons = all20Poke['results'] #access the list of results for all 20 pokemon
#print(infoOf20Pokemons)



#This funtion grabs just the name pokemon in the dictionary that describes it
def justName(p):

    name = p['name']

    return name

simpleData = map(justName, infoOf20Pokemons)   # every item in 'infoOf20Pokemons is ran through the 'justName' function
                                               # simpleDate is a list of the return values of every map iteration == the names
print(list(simpleData))