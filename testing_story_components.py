import unittest
from DinosaurStoryComponents import paragraph_one, paragraph_two, paragraph_three, dinosaur_story_text


class MyTestCase(unittest.TestCase):
    def test_para_one_valid_true(self):
        child_name = "Pam"
        child_age = 5
        child_pronouns = "she"
        dino_species = "Triceratops"
        result = paragraph_one(child_name, child_age,child_pronouns,dino_species)
        self.assertIn(child_name, result)  # add assertion here
        self.assertIn(str(child_age), result)
        self.assertIn(child_pronouns, result)
        self.assertIn(dino_species, result)


if __name__ == '__main__':
    unittest.main()
