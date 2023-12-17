# Import random module to allow for random selection of astronauts from API response
import random
# Import requests module to allow for API calls
import requests

# Base URL for API calls
open_notify_url = "http://api.open-notify.org/astros.json"

# Function to get API response
def get_response():
    try:
        response = requests.get(open_notify_url)
        response.raise_for_status() # If the HTTP request returns unsucessful status code this will raise a HTTPError
        return response.json()
    
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


# Function to get a random astronaut name from API response
def get_astronaut_name():
    people_on_Iss = get_response()['people']
    return random.choice(people_on_Iss)['name']


# Function to get the number of people on the ISS from API response
def get_no_iss_residents():
    no_people_on_Iss = get_response()['number']
    return no_people_on_Iss
