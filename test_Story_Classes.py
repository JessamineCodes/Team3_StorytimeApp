import unittest
#import 'patch' to mock the 'find_story_by_id' method of the Story class.
from unittest.mock import patch
#import classes with methods to be tested
from StoryClasses import SpaceStory, DinosaurStory, PokemonStory
from StoryClasses import Story


class TestStory(unittest.TestCase):
    #test the initialization of the Story class
    def test_init(self):
        story = Story("Alice", "she", 8)
        self.assertEqual(story.child_name, "Alice")
        self.assertEqual(story.child_pronouns, "she")
        self.assertEqual(story.child_age, 8)
#use the patch decorater from the unitest module to mock the 'find_story_by_id' method and verify that
    #the method is behaving as expected, irrespecitve of external dependencies.
    @patch('StoryClasses.Story.find_story_by_id')
    # Test the 'find_story_by_id' method
    def test_find_story_by_id(self, mock_get_story_by_id):
        #configure the mock to return a list as it would in real usage
        mock_get_story_by_id.return_value = ["Mocked Story"]
        story = Story.find_story_by_id(1, mock_get_story_by_id)

        #check that the method used the mock and returned the expected result
        mock_get_story_by_id.assert_called_once_with(1, mock_get_story_by_id)
        self.assertEqual(story, ["Mocked Story"])




class TestSpaceStory(unittest.TestCase):
    #test the 'generate_story' method of SpaceStory
    def test_generate_story(self):
        space_story = SpaceStory("Bob", "he", 6)
        result = space_story.generate_story()
        self.assertIn("Bob", result)
        self.assertIn("he", result)
        self.assertIn("6", result)


class TestDinosaurStory(unittest.TestCase):
    #test the 'generate_story' method of DinosaurStory
    def test_generate_story(self):
        dinosaur_story = DinosaurStory("Charlie", "they", 7)
        result = dinosaur_story.generate_story()
        self.assertIn("Charlie", result)
        self.assertIn("they", result)
        self.assertIn("7", result)


class TestPokemonStory(unittest.TestCase):
    # Test the 'generate_story' method of PokemonStory
    def test_generate_story(self):
        pokemon_story = PokemonStory("David", "he", 9)
        result = pokemon_story.generate_story()
        self.assertIn("David", result)
        self.assertIn("he", result)
        self.assertIn("9", result)

#if this script is executed directly, run the unit tests.
if __name__ == '__main__':
    unittest.main()
