import unittest
from unittest.mock import patch, MagicMock
# import the functions to be tested
from dinosaur_story_api_calls import get_random_dino_info
from pokemon_story_api_calls import get_pokemon_info
from space_story_api_calls import get_astronaut_name, get_no_iss_residents


# test class for space story API calls
class TestSpaceStoryAPICalls(unittest.TestCase):
    # test case for function to retrieve astronaut names
    # patch decorator from unittest module used to mock the 'requests.get' function during test execution
    @patch('space_story_api_calls.requests.get')
    def test_get_astronaut_name(self, mock_requests_get):
        # mock response object created with sample astronaut names
        mock_response = MagicMock()
        mock_response.json.return_value = {'people': [{'name': 'Astronaut 1'}, {'name': 'Astronaut 2'}], 'number': 2}
        mock_requests_get.return_value = mock_response

        # test the function
        result = get_astronaut_name()

        # check that the function returns one of the expected names
        expected_names = ['Astronaut 1', 'Astronaut 2']
        self.assertIn(result, expected_names)

    # test case for function to retrieve the number of iss residents
    # patch decorator from unittest module used to mock the 'get_response' function during test execution
    @patch('space_story_api_calls.get_response')
    def test_get_no_iss_residents(self, mock_get_response):
        # mock response object created with sample iss resident data
        mock_response = {'people': [{'name': 'Astronaut 1'}, {'name': 'Astronaut 2'}], 'number': 2}
        mock_get_response.return_value = mock_response

        # test the function
        result = get_no_iss_residents()

        # check that the function returns the expected result
        self.assertEqual(result, 2)


# test class for pokemon story API calls
class TestGetPokemonInfo(unittest.TestCase):

    # test case for function to retrieve pokemon information
    # patch decorator from unittest module used to mock the 'random.randit' and 'requests.get' functions
    # during test execution. Return value of the mocked random.rand.int set to always return the same value during test execution.
    @patch('pokemon_story_api_calls.random.randint', return_value=42)
    @patch('pokemon_story_api_calls.requests.get')
    def test_get_pokemon_info(self, mock_requests_get, mock_random_randint):
        # mock the 'response.json()' method to return a sample data
        sample_data = {
            'name': 'bulbasaur',
            'abilities': [{'ability': {'name': 'chlorophyll'}}],
            'moves': [{'move': {'name': 'tackle'}}],
            'types': [{'type': {'name': 'grass'}}]
        }
        mock_requests_get.return_value.json.return_value = sample_data

        # call the function
        p_name, p_ability, p_move, poke_type = get_pokemon_info()

        # assert the expected values
        self.assertEqual(p_name, 'Bulbasaur')
        self.assertEqual(p_ability, 'Chlorophyll')
        self.assertEqual(p_move, 'Tackle')
        self.assertEqual(poke_type, 'Grass')

        # check that the 'requests.get' method was called with the correct URL
        mock_requests_get.assert_called_once_with("https://pokeapi.co/api/v2/pokemon/42")

        # check that 'random.randint' was called with the correct arguments
        mock_random_randint.assert_called_once_with(1, 200)


# test class for dinosaur story API calls
class TestGetRandomDinoInfo(unittest.TestCase):

    # test case for the function to retrieve random dinosaur information
    # patch decorator from unittest module used to mock the 'requests.get' function during test execution
    @patch('dinosaur_story_api_calls.requests.get')
    def test_get_random_dino_info(self, mock_requests_get):
        # mock the response.json() method to return sample data
        sample_data = {
            'Name': 'Tyrannosaurus Rex',
            'Description': 'A large, carnivorous dinosaur with powerful jaws.'
        }
        mock_requests_get.return_value.json.return_value = sample_data

        # call the function
        dino_species, dino_desc = get_random_dino_info()

        # assert the expected values
        self.assertEqual(dino_species, 'Tyrannosaurus Rex')
        self.assertEqual(dino_desc, 'A large, carnivorous dinosaur with powerful jaws.')

        # check that the 'requests.get' method was called with the correct URL
        mock_requests_get.assert_called_once_with("https://dinosaur-facts-api.shultzlab.com/dinosaurs/random")


# run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
