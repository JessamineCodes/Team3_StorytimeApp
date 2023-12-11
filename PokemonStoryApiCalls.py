# Import random module to allow for random selection of pokemon from API response
import random
# Import requests module to allow for API calls
import requests


# Base URL for API calls
base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info():

    # getting a random number for the endpoint 
    random_pokemon_id = random.randint(1, 200)
    endpoint = random_pokemon_id

    url = f"{base_url}{endpoint}"
    response = requests.get(url)
    data = response.json()
    pokemon_name = data['name'].title()
    pokemon_ability = data['abilities'][0]['ability']['name'].title()
    pokemon_move = data['moves'][0]['move']['name'].title()
    pokemon_type = data['types'][0]['type']['name'].title()
    
    return pokemon_name, pokemon_ability, pokemon_move, pokemon_type


p_name, p_ability, p_move, poke_type = get_pokemon_info()

