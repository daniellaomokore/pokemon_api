# My attempt to put the code into classes + functions

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




class useAPI:
    def __init__(self, pokemon_number):
        self.pokemon_number = pokemon_number




    # this func takes in the entered id number
    def connectToAPI(self):
        try:
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(self.pokemon_number)
            response = requests.get(url)
            response.raise_for_status()
            data = response.text
            pokemon = json.loads(
                data)  # deserializing - turns json string into python dictionary that can be now accessed

        except requests.exceptions.ConnectionError as cerr:
            print("Sorry a Connection error has been found")
            logging.warning(cerr)
            return "No Connection"
        except json.decoder.JSONDecodeError:
            return "No Connection"
        except requests.exceptions.HTTPError as err:
            print("Bad Status Code", response.status_code)
            return "No Connection"
        else:
            print("Status code:", response.status_code)
            print("Pokemon {} chosen".format(self.pokemon_number))
            return pokemon




    def getPokeName(self, pokemon):

        name_of_poke = pokemon['name']
        return name_of_poke




    def getPokeWeight(self, pokemon):
        weight_of_poke = pokemon['weight']
        return weight_of_poke




    def sendPokeInfoToAPI(self, name_of_poke, weight_of_poke):
        post_body = {"Name": " {}".format(name_of_poke),
                     "Weight": "{}".format(weight_of_poke)}

        post_header = {'content-type': 'application/json',
                       'Authorization': '{key}'.format(key=api_auth_key)}

        # POST REQUEST W/post_header and post_body
        try:
            result = requests.post(
                'http://httpbin.org/post', headers=post_header,
                data=json.dumps(post_body)  # json.dumps = serializing - turns python dictionary into json string
            )
        except requests.exceptions.HTTPError:
            print(
                "POST Request returned an error, Bad Status Code: {}. If you entered the URL manually check your spelling and try again".format(
                    result.status_code))
        else:
            print(result.text)
            #print("POST Request is successful, Status code:", result.status_code)
            return "POST Request is successful, Status code: {}".format(result.status_code)




    def viewPokeInfoFromAPI(self, name_of_poke, weight_of_poke):
        get_body = {"Name": " {}".format(name_of_poke),
                    "Weight": "{}".format(weight_of_poke)}

        get_header = {'content-type': 'application/json',
                      'Authorization': '{key}'.format(key=api_auth_key)}
        try:
            result1 = requests.get(
                'http://httpbin.org/get', params=get_body, headers=get_header,
            )

        except requests.exceptions.HTTPError:
            print(
                "GET Request returned an error, Bad Status Code: {}. If you entered the URL manually check your spelling and try again".format(
                    result1.status_code))
        else:
            print(result1.text)  # to check that the 'get' request
            #print("GET Request is successful, Status code: {}".format(result1.status_code))
            return "GET Request is successful, Status code: {}".format(result1.status_code)




# This runs the flow of the code-like piecing the puzzle pieces together in correct order#
def main():
    pokemon_number = int(input("Enter a pokemon ID:"))
    current_user = useAPI(pokemon_number)
    our_pokemon = current_user.connectToAPI()
    name = current_user.getPokeName(our_pokemon)
    weight = current_user.getPokeWeight(our_pokemon)
    print(current_user.sendPokeInfoToAPI(name, weight))
    print(current_user.viewPokeInfoFromAPI(name, weight))




if __name__ == '__main__':
    main()