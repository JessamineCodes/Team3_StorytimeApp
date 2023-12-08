# Import method for creating space story text from SpaceStoryComponents.py
from SpaceStoryComponents import space_story_text
# Import method for creating dinonsaur story text from DinosaurStoryComponents.py
from DinosaurStoryComponents import dinosaur_story_text


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
            return space_story_text(self.child_name, self.child_age)
        elif self.theme == "dinosaur":
            return dinosaur_story_text(self.child_name, self.child_age)
        else:
            return "Theme not recognised"
space_story = Story("Jo", "she", "12", "space").generate_story()
print(space_story)

# Testing the class by creating a space story object and printing the story text
print(Story("Jo", "she", "12", "space").generate_story())
# Testing the class by creating a dino story object and printing the story text
print(Story("Rose", "she", "9", "dinosaur").generate_story())
