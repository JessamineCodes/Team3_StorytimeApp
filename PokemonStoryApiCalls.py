# Import random module to allow for random selection of pokemon from API response
import random
# Import requests module to allow for API calls
import requests


# Base URL for API calls
base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info():
    try:
        # getting a random number for the endpoint 
        random_pokemon_id = random.randint(1, 200)
        endpoint = random_pokemon_id
        url = f"{base_url}{endpoint}"


        response = requests.get(url)
        response.raise_for_status() # If the HTTP request returns unsucessful status code this will raise a HTTPError


        data = response.json()
        pokemon_name = data['name'].title()
        pokemon_ability = data['abilities'][0]['ability']['name'].title()
        pokemon_move = data['moves'][0]['move']['name'].title()
        pokemon_type = data['types'][0]['type']['name'].title()
    
        return pokemon_name, pokemon_ability, pokemon_move, pokemon_type
    
    except requests.exceptions.RequestException as e:
        # This will handle any network issue or server errors 
        print(f"Request Exception: {e}")
        return None, None 
    
    except KeyError as e:
        # This will handle errors if expected keys are not found in API response
        print(f"Key Error: {e}")
        return None, None
    
    except Exception as e:
        # This should handle any other unexpected exceptions
        print(f"An error occured: {e}")
        return None, None


p_name, p_ability, p_move, poke_type = get_pokemon_info()

