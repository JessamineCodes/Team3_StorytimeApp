from db_management import StoryManager
import db_management
from mock_db import MockDB
# import mock
# from mock import patch


class TestDBManagement(MockDB):
    # def test_execute_query(self):
    #     with self.mock_db_config:

    #         expected = 1
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.execute_query("""SELECT count(UserID) FROM Users""")
    #         self.assertEqual(expected, result)

    def test_fetch_query(self):
        s = StoryManager()
        with self.mock_db_config:

            expected = [(3,)]
            result = s.fetch_query("""SELECT count(UserID) FROM Users""")
            self.assertEqual(expected, result)


    # # unit tests for insert_user function
    #
    # def test_insert_new_user(self):
    #     with self.mock_db_config:
    #         expected = True
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.execute_query(story_manager.insert_user('TestUser4', 'Test4@user.com', '14!fC!59'))
    #         self.assertEqual(expected, result)
    #
    # def test_null_username(self):
    #     with self.mock_db_config:
    #         expected = Exception
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.execute_query(story_manager.insert_user('', 'Test5@user.com', '14!%CFg9'))
    #         self.assertEqual(expected, result)
    #
    # def test_null_password(self):
    #     with self.mock_db_config:
    #         expected = Exception
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.execute_query(story_manager.insert_user('TestUser5', 'Test6@user.com', ''))
    #         self.assertEqual(expected, result)
    #
    # def test_duplicate_email(self):
    #     with self.mock_db_config:
    #         expected = Exception
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.execute_query(story_manager.insert_user('TestUserD', 'Test1@user.com', '14!%CFg9'))
    #         self.assertEqual(expected, result)
    #
    #
    # # unit tests for insert_story function
    #
    # def test_insert_story(self):
    #     with self.mock_db_config:
    #         expected = True
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.execute_query(story_manager.insert_story('Test Title 4', 'Test Content 4'))
    #         self.assertEqual(expected, result)
    #
    # # unit tests for fetch_all_child_stories
    #
    # def test_fetch_all_child_stories(self):
    #     with self.mock_db_config:
    #         expected = ['Test Title 2']
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.fetch_all_child_stories(['Test childname2'])
    #         self.assertEqual(expected, result)
    #
    # # unit tests for fetch_all_user_stories
    #
    # def test_fetch_all_user_stories(self):
    #     with self.mock_db_config:
    #         expected = ['Test Title 1', 'Test Title 3']
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.fetch_all_child_stories(['1'])
    #         self.assertEqual(expected, result)
    #
    # # unit tests fetch_user_id
    #
    # def test_fetch_user_id(self):
    #     with self.mock_db_config:
    #         expected = 4
    #         story_manager = db_management.StoryManager()
    #         result = story_manager.fetch_user_id()
    #         self.assertEqual(expected, result)


