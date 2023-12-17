# Import method for creating space story text from space_story_components.py
from space_story_components import space_story_text
# Import method for creating dinosaur story text from dinosaur_story_components.py
from dinosaur_story_components import dinosaur_story_text
# Import method for creating pokemon story text from pokemon_story_components.py
from pokemon_story_components import pokemon_story_text

# Import abstract base class module
import abc

# Import method for getting a specific story from utils
from SQL_queries import fetch_all_user_stories, fetch_story_by_id


# Class for creating a story object - initialised with 3 inputs about the child and chosen theme
class Story:
    __metaclass__ = abc.ABCMeta

    def __init__(self, child_name, child_pronouns, child_age):
        self.child_name = child_name
        self.child_pronouns = child_pronouns
        self.child_age = int(child_age)

    # Abstract method for generating the story text
    @abc.abstractmethod
    def generate_story(self):
        pass

     
    @staticmethod
    # Class level method for getting all stories by user id from the database
    def show_stories_by_user_id(user_id, db_handler):
        return db_handler.fetch_query(fetch_all_user_stories, (user_id,))   
    
    # Class level method for getting a specific story from the database
    def find_story_by_id(story_id, db_handler):
        result = db_handler.fetch_query(fetch_story_by_id, (story_id,))
        if result and len(result[0]) >= 2:  # Check if the result exists and has at least two elements
            return result[0]
        return None


class SpaceStory(Story):
    def __init__(self, child_name, child_pronouns, child_age):
        super().__init__(child_name, child_pronouns, child_age)

    def generate_story(self):
        return space_story_text(self.child_name, self.child_age, self.child_pronouns)

    def get_title(self):
        return f"{self.child_name}'s Space Story"

class DinosaurStory(Story):
    def __init__(self, child_name, child_pronouns, child_age):
        super().__init__(child_name, child_pronouns, child_age)

    def generate_story(self):
        return dinosaur_story_text(self.child_name, self.child_age, self.child_pronouns)

    def get_title(self):
        return f"{self.child_name}'s Dinosaur Story"

class PokemonStory(Story):
    def __init__(self, child_name, child_pronouns, child_age):
        super().__init__(child_name, child_pronouns, child_age)

    def generate_story(self):
        return pokemon_story_text(self.child_name, self.child_age, self.child_pronouns)

    def get_title(self):
        return f"{self.child_name}'s Pokemon Story"


# Testing the class by creating a dino story object and printing the story text
space_story_instance = SpaceStory("Jo", "he", "7")
space_story = space_story_instance.generate_story()


# print(f"Printing space story with pronouns {space_story_instance.child_pronouns}")
# print(space_story)
# print("------------------------------------------------------------------")


# Testing the class by creating a dino story object and printing the story text
dinosaur_story_instance = DinosaurStory("Rose", "she", "9")
dinosaur_story = dinosaur_story_instance.generate_story()

# print(f"Printing dinosaur story with pronouns {dinosaur_story_instance.child_pronouns}")
# print(dinosaur_story)
# print("------------------------------------------------------------------")

# Testing the class by creating a pokemon story object and printing the story text
pokemon_story_instance = PokemonStory("Max", "ze", "8")
pokemon_story = pokemon_story_instance.generate_story()

# print(f"Printing pokemon story with pronouns {pokemon_story_instance.child_pronouns}")
# print(pokemon_story)
# print("------------------------------------------------------------------")
