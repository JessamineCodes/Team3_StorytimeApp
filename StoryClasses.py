# Import method for creating space story text from SpaceStoryComponents.py
from SpaceStoryComponents import space_story_text
# Import method for creating dinosaur story text from DinosaurStoryComponents.py
from DinosaurStoryComponents import dinosaur_story_text
# Import method for creating pokemon story text from PokemonStoryComponents.py
from PokemonStoryComponents import pokemon_story_text



# Class for creating a story object - initialised with 3 inputs about the child and chosen theme
class Story:
    def __init__(self, child_name, child_pronouns, child_age, theme):
        self.child_name = child_name
        self.child_pronouns = child_pronouns
        self.child_age = int(child_age)
        self.theme = theme.lower()

    # Method for generating story text based on inputs
    # Uses if statement to check which theme has been chosen and calls the relevant story text method
    def generate_story(self):
        if self.theme == "space":
            return space_story_text(self.child_name, self.child_age, self.child_pronouns)
        elif self.theme == "dinosaur":
            return dinosaur_story_text(self.child_name, self.child_age, self.child_pronouns)
        elif self.theme == "pokemon":
            return pokemon_story_text(self.child_name, self.child_age, self.child_pronouns)
        else:
            return "Theme not recognised"

# Testing the class by creating a space story object and printing the story text
space_story_instance = Story("Jo", "he", "12", "space")
space_story = space_story_instance.generate_story()
print(f"Printing space story with pronouns {space_story_instance.child_pronouns}")
print(space_story)
print("------------------------------------------------------------------")

# Testing the class by creating a dino story object and printing the story text
dinosaur_story_instance = Story("Rose", "she", "9", "dinosaur")
dinosaur_story = dinosaur_story_instance.generate_story()
print(f"Printing dinosaur story with pronouns {dinosaur_story_instance.child_pronouns}")
print(dinosaur_story)
print("------------------------------------------------------------------")

# Testing the class by creating a pokemon story object and printing the story text
pokemon_story_instance = Story("Max", "ze", "8", "pokemon")
pokemon_story = pokemon_story_instance.generate_story()
print(f"Printing pokemon story with pronouns {pokemon_story_instance.child_pronouns}")
print(pokemon_story)
