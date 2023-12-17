# Import requests module to allow for API calls
import requests

# Base URL for API calls
# URL returns a random dinosaur's name and a description
get_dino_url = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random"

# Function to get API response
# We will get one response here and pass it to the story because each API call would get a different random dinosaur
# So we cannot split into functions like we did for the space story
def get_random_dino_info():
    try:
        response = requests.get(get_dino_url)
        response.raise_for_status() # If the HTTP request returns unsucessful status code this will raise a HTTPError
        
        dinosaur_dictionary = response.json()
        dino_species = dinosaur_dictionary['Name']
        dino_desc = dinosaur_dictionary['Description']
        return dino_species, dino_desc
    
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



dino_species, dino_desc = get_random_dino_info()
