import unittest
# import functions to be tested
from space_story_components import paragraph_one, paragraph_two, paragraph_three, space_story_text


# test class for functions to create space story components
class TestSpaceStoryFunctions(unittest.TestCase):
    # test case for function to create paragraph one
    def test_paragraph_one(self):
        # call the function with example inputs
        result = paragraph_one("Timmy", 8)
        # Add your assertions here based on the expected output for given inputs
        self.assertTrue("Timmy was the youngest ever astronaut" in result)

    # test case for function to create paragraph two
    def test_paragraph_two(self):
        # call the function with example inputs
        result = paragraph_two("Sally", "she")
        # check that the output contains an expected substring of the story
        self.assertIn("they need", result)
        # test case for function to create paragraph three

    def test_paragraph_three(self):
        # call the function with example inputs
        result = paragraph_three("Billy")
        # check that the output contains an expected substring of the story
        self.assertIn("From that day on they were best friends!", result)
        # test case for function to create full space story

    def test_space_story_text(self):
        # call the function with example inputs
        result = space_story_text("Tom", 10, "he")
        # check that the output contains two expected substrings of the story
        self.assertIn("Tom was the youngest ever astronaut", result)
        self.assertIn("From that day on they were best friends!", result)


if __name__ == '__main__':
    unittest.main()
