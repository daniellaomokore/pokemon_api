"""

HERE WE ARE PRACTISING DATA MANIPULATION OF THE DATA WE GET FROM THE POKEMON API:

-LIST COMPREHENSION

-MAPPING

"""
import requests



### EXAMPLE 1 ###

print("EXAMPLE 1")


### Filtering list data W/ LIST COMPREHENSION ###

pokemon_name = input("Enter a pokemon name:")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)   # Pokemon by id number
response = requests.get(url)

pokemon = response.json()  # returns as a python dictionary object, extracting the API result

pokemon_abilities = [skill['ability']['name'] for skill in pokemon['abilities']]   # The name of all the skills the pokemon has

pokemon_weight = pokemon['weight']

print("{} has all of the following abilities: {}, it weighs {}.\n".format(pokemon_name.capitalize(), pokemon_abilities, pokemon_weight))





### EXAMPLE 2 ###

print("EXAMPLE 2")

### REMAPPING or NORMALISING Data with MAP ### # Remember map is used on a function and a list #
url_20_all_poke = "https://pokeapi.co/api/v2/pokemon/"    # all 20 pokemon at this url
response_2 = requests.get(url_20_all_poke)
all_20_poke = response_2.json()

info_of_20_pokemons = all_20_poke['results'] #access the list of results for all 20 pokemon

#This funtion grabs just the 'name' of the pokemon in the dictionary that describes it
def justName(p):
    name = p['name']
    return name

simple_data = map(justName, info_of_20_pokemons)   # every item in 'infoOf20Pokemons is ran through the 'justName' function
                                               # simpleDate is a list of the return values of every map iteration == the names
print("Names of 20 Pokemon: ", list(simple_data))