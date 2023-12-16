import unittest
# import functions to be tested
from DinosaurStoryComponents import (
    paragraph_one,
    paragraph_two,
    paragraph_three,
    dinosaur_story_text, )


# test class for functions to create dinosaur story components

class TestDinosaurStoryComponents(unittest.TestCase):
    # test case for function to create paragraph one
    def test_paragraph_one(self):
        # call the function with example inputs
        result = paragraph_one("Alex", 7, "he", "Velociraptor")
        # check that the output contains an expected substring of the story
        self.assertIn("Alex wanted to be a famous paleontologist", result)

    # test case for function to create paragraph two
    def test_paragraph_two(self):
        # call the function with example inputs
        result = paragraph_two("Emma", "she", "Triceratops")
        # check that the output contains an expected substring of the story
        self.assertIn("Emma found herself", result)

    # test case for function to create paragraph two
    def test_paragraph_three(self):
        # call the function with example inputs
        result = paragraph_three("Sam", "he", "Stegosaurus", "with spiky plates on its back")
        # check that the output contains an expected substring of the story
        self.assertIn("Suddenly, there was a flash of light", result)

    # test case for the function to create the full dinosaur story text
    def test_dinosaur_story_text(self):
        # call the function with example inputs
        result = dinosaur_story_text("Taylor", 9, "they")
        # check that the output contains two expected substrings of the story
        self.assertIn("Taylor wanted to be a famous paleontologist", result)
        self.assertIn("Suddenly, there was a flash of light", result)


if __name__ == '__main__':
    unittest.main()
