
"""HERE WE ARE PRACTISING DATA MANIPULATION OF THE DATA WE GET FROM THE POKEMON API:

-LIST COMPREHENSION

-MAPPING

"""
import requests



###EXAMPLE 1###

### Filtering list data W/ LIST COMPREHENSION ###

pokemon_name = input("Enter a pokemon name:")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)   # pokemon by id number
response = requests.get(url)

pokemon = response.json()  # returns as a python dictionary object, extracting the API result

pokemonAbilities = [skill['ability']['name'] for skill in pokemon['abilities']]   # The name of all the skills the pokemon has

pokemonWeight = pokemon['weight']

print("{} has all of the following abilities: {}, it weighs {}.\n".format(pokemon_name.capitalize(), pokemonAbilities, pokemonWeight))





### EXAMPLE 2 ###

### REMAPPING or NORMALISING Data with MAP ### # Remember map is used on a function and a list #
url20AllPoke = "https://pokeapi.co/api/v2/pokemon/"    # all 20 pokemon at this url
response2 = requests.get(url20AllPoke)
all20Poke = response2.json()

infoOf20Pokemons = all20Poke['results'] #access the list of results for all 20 pokemon

#This funtion grabs just the 'name' of the pokemon in the dictionary that describes it
def justName(p):
    name = p['name']
    return name

simpleData = map(justName, infoOf20Pokemons)   # every item in 'infoOf20Pokemons is ran through the 'justName' function
                                               # simpleDate is a list of the return values of every map iteration == the names
print("Names of 20 Pokemon: ", list(simpleData))