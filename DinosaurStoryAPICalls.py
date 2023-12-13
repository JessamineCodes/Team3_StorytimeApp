# Import requests module to allow for API calls
import requests

# Base URL for API calls
# URL returns a random dinosaur's name and a description
get_dino_url = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random"

# Function to get API response
# We will get one response here and pass it to the story because each API call would get a different random dinosaur
# So we cannot split into functions like we did for the space story
def get_random_dino_info():
    response = requests.get(get_dino_url)
    dinosaur_dictionary = response.json()
    dino_species = dinosaur_dictionary['Name']
    dino_desc = dinosaur_dictionary['Description']
    return dino_species, dino_desc


dino_species, dino_desc = get_random_dino_info()
