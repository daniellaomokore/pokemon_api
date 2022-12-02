#my attempt to put the code info classes/functions

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
from config import api_auth_key


#this func takes in the enteref id number
def choosePokemon(pokemon_number):
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
        response = requests.get(url)
        response.raise_for_status()
        data = response.text
        pokemon = json.loads(data)  # deserializing - turns json string into python dictionary that can be now accessed

    except requests.exceptions.ConnectionError as cerr:
        print("Sorry a Connection error has been found")
        logging.warning(cerr)
    except requests.exceptions.HTTPError as err:
        print("Bad Status Code", response.status_code)
    else:
        print("Status code:", response.status_code)
        print("Pokemon {} chosen".format(pokemon_number))
        return pokemon

def getPokeName(pokemon):

    nameOfPoke = pokemon['name']
    return nameOfPoke


def getPokeWeight(pokemon):
    weightOfPoke = pokemon['weight']
    return weightOfPoke




def sendPokeInfo(nameOfPoke,weightOfPoke):
    body = {"Name": " {}".format(nameOfPoke),
            "Weight": "{}".format(weightOfPoke)}

    headers = {'content-type': 'application/json',
               'Authorization': '{key}'.format(key=api_auth_key)}

    # POST REQUEST W/headers and body
    try:
        result = requests.post(
            'http://httpbin.org/post', headers=headers,
            data=json.dumps(body)  # json.dumps = serializing - turns python dictionary into json string
        )
    except requests.exceptions.HTTPError:
        print(
            "POST Request returned an error, Bad Status Code: {}. If you entered the URL manually check your spelling and try again".format(
                result.status_code))
    else:
        print("POST Request is successful, Status code:", result.status_code)
        print(result.text)
        return result.text

def sendPokeInfo(nameOfPoke,weightOfPoke):
    body = {"Name": " {}".format(nameOfPoke),
            "Weight": "{}".format(weightOfPoke)}

    headers = {'content-type': 'application/json',
               'Authorization': '{key}'.format(key=api_auth_key)}

    # POST REQUEST W/headers and body
    try:
        result = requests.post(
            'http://httpbin.org/post', headers=headers,
            data=json.dumps(body)  # json.dumps = serializing - turns python dictionary into json string
        )
    except requests.exceptions.HTTPError:
        print(
            "POST Request returned an error, Bad Status Code: {}. If you entered the URL manually check your spelling and try again".format(result.status_code))
    else:
        print(result.text)  # to check the 'post' request
        return "POST Request is successful, Status code: {}".format(result.status_code)



def viewPokeInfo(nameOfPoke,weightOfPoke):
    body1 = {"Name": " {}".format(nameOfPoke),
             "Weight": "{}".format(weightOfPoke)}

    headers1 = {'content-type': 'application/json',
                'Authorization': '{key}'.format(key=api_auth_key)}
    try:
        result1 = requests.get(
            'http://httpbin.org/get', params=body1, headers=headers1,
        )

    except requests.exceptions.HTTPError:
        print(
            "GET Request returned an error, Bad Status Code: {}. If you entered the URL manually check your spelling and try again".format(
                result1.status_code))
    else:
        print(result1.text)  # to check that the 'get' request
        return "GET Request is successful, Status code: {}".format(result1.status_code)




#This runs the flow of the code-like piecing the puzzle pieces together in correct order#
def main():
    pokemon_number = input("Enter a pokemon ID:")
    ourPokemon = choosePokemon(pokemon_number)
    name = getPokeName(ourPokemon)
    weight = getPokeWeight(ourPokemon)
    print(sendPokeInfo(nameOfPoke=name, weightOfPoke=weight))
    print(viewPokeInfo(nameOfPoke=name, weightOfPoke=weight))


if __name__ == '__main__':
    main()