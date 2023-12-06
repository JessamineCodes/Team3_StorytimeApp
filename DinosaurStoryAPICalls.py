# def random_dinosaur_api():

#  get_dino_url = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random"
#  arr = []
#  response = requests.get(get_dino_url)
#  results = (response.content)

#  arr.append(results)

#  convert = str(arr[0])

#  return convert

# Import random module to allow for random selection of astronauts from API response
import random
# Import requests module to allow for API calls
import requests

# Base URL for API calls
get_dino_url = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random"

# Function to get API response
def get_random_dino_info_response():
    response = requests.get(get_dino_url)
    return response.json()
