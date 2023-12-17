import unittest
# import functions to be tested
from pokemon_story_components import (
    paragraph_one,
    paragraph_two,
    paragraph_three,
    pokemon_story_text,
)
#test class for functions to create pokemon story components
class TestPokemonStoryFunctions(unittest.TestCase):
    # test case for function to create paragraph one
    def test_paragraph_one(self):
        # call the function with example inputs
        result = paragraph_one("Ash", 10, "he")
        # check that the output contains an expected substring of the story
        self.assertTrue("In a bustling town named Pokeville" in result)
    # test case for function to create paragraph two
    def test_paragraph_two(self):
        # call the function with example inputs
        result = paragraph_two("Misty", "she")
        # check that the output contains an expected substring of the story
        self.assertTrue("been given the" in result)
    # test case for function to create paragraph three
    def test_paragraph_three(self):
        # call the function with example inputs
        result = paragraph_three("Brock", "he")
        # check that the output contains an expected substring of the story
        self.assertTrue("Just then, a bright glow surrounded" in result)
    # test case for the function to create the full pokemon story text
    def test_pokemon_story_text(self):
        # call the function with example inputs
        result = pokemon_story_text("May", 12, "she")
        # check that the output contains two expected substrings of the story
        self.assertTrue("In a bustling town named Pokeville" in result)
        self.assertTrue("Just then, a bright glow surrounded" in result)

if __name__ == '__main__':
    unittest.main()
