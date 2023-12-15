# Import method for creating space story text from SpaceStoryComponents.py
from SpaceStoryComponents import space_story_text
# Import method for creating dinosaur story text from DinosaurStoryComponents.py
from DinosaurStoryComponents import dinosaur_story_text
# Import method for creating pokemon story text from PokemonStoryComponents.py
from PokemonStoryComponents import pokemon_story_text

# Import abstract base class module
import abc

# Import method for getting a specific story from utils
from utils import get_story_by_id, find_stories_by_user_id


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

     # Class level method for getting a specific story from the database
    @staticmethod
    def find_story_by_id(story_id, db_handler):
        # use method from db utils to get story by id from DB
        return get_story_by_id(story_id, db_handler)
    
    def show_stories_by_user_id(user_id, db_handler):
        return find_stories_by_user_id(user_id, db_handler)
        



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
