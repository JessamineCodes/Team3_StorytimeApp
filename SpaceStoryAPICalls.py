# Import random module to allow for random selection of astronauts from API response
import random
# Import requests module to allow for API calls
import requests

# Base URL for API calls
open_notify_url = "http://api.open-notify.org/astros.json"

# Function to get API response
def get_response():
    response = requests.get(open_notify_url)
    return response.json()

# Function to get a random astronaut name from API response
def get_astronaut_name():
    people_on_Iss = get_response()['people']
    return random.choice(people_on_Iss)['name']

# Function to get the number of people on the ISS from API response
def get_no_iss_residents():
    no_people_on_Iss = get_response()['number']
    return no_people_on_Iss
