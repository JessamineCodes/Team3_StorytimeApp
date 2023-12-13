# Import method for creating space story text from SpaceStoryComponents.py
from SpaceStoryComponents import space_story_text
# Import method for creating dinosaur story text from DinosaurStoryComponents.py
from DinosaurStoryComponents import dinosaur_story_text
# Import method for creating pokemon story text from PokemonStoryComponents.py
from PokemonStoryComponents import pokemon_story_text
# Import abstract base class module
import abc


# Class for creating a story object - initialised with 3 inputs about the child and chosen theme
class Story:
    __metaclass__ = abc.ABCMeta

    def __init__(self, child_name, child_pronouns, child_age):
        self.child_name = child_name
        self.child_pronouns = child_pronouns
        self.child_age = int(child_age)

    @abc.abstractmethod
    def generate_story(self):
        pass

class SpaceStory(Story):
    def __init__(self, child_name, child_pronouns, child_age):
        super().__init__(child_name, child_pronouns, child_age)

    def generate_story(self):
        return space_story_text(self.child_name, self.child_age)

class DinosaurStory(Story):
    def __init__(self, child_name, child_pronouns, child_age):
        super().__init__(child_name, child_pronouns, child_age)

    def generate_story(self):
        return dinosaur_story_text(self.child_name, self.child_age)

class PokemonStory(Story):
    def __init__(self, child_name, child_pronouns, child_age):
        super().__init__(child_name, child_pronouns, child_age)

    def generate_story(self):
        return pokemon_story_text(self.child_name, self.child_age)

      
# Testing the class by creating a space story object and printing the story text
space_story_instance = Story("Jo", "he", "12", "space")
space_story = space_story_instance.generate_story()
print(f"Printing space story with pronouns {space_story_instance.child_pronouns}")
print(space_story)
print("------------------------------------------------------------------")


# Testing the class by creating a dino story object and printing the story text
dinosaur_story_instance = DinosaurStory("Rose", "she", "9", "dinosaur")
dinosaur_story = dinosaur_story_instance.generate_story()
print(f"Printing dinosaur story with pronouns {dinosaur_story_instance.child_pronouns}")
print(dinosaur_story)
print("------------------------------------------------------------------")


# Testing the class by creating a pokemon story object and printing the story text
pokemon_story_instance = Story("Max", "ze", "8", "pokemon")
pokemon_story = pokemon_story_instance.generate_story()
print(f"Printing pokemon story with pronouns {pokemon_story_instance.child_pronouns}")
print(pokemon_story)
print("------------------------------------------------------------------")

