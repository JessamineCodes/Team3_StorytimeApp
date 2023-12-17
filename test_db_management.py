import unittest

from StoryClasses import SpaceStory

# import classes with methods to be tested
from db_management import StoryManager, SetUpAndTearDownHandler
import SQL_queries
# dotenv module allows for .env file access
from dotenv import load_dotenv
# operating system dependent functionality
import os

load_dotenv()

# mock db setup:
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "mock_db"

mock_db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': DB_NAME,
    'host': DB_HOST
}


def add_test_data():
    story_manager = StoryManager(db_config=mock_db_config)
    story_manager.execute_query(SQL_queries.insert_user, ('test_user_1', 'test@user_1.com', 'password_1'))
    story_manager.execute_query(SQL_queries.insert_user, ('test_user_2', 'test@user_2.com', 'password_2'))
    story_manager.execute_query(SQL_queries.insert_user, ('test_user_3', 'test@user_3.com', 'password_3'))
    story_manager.execute_query(SQL_queries.insert_story, ('test_title_1', 'test_content_1', 'test_childname_1',1))
    story_manager.execute_query(SQL_queries.insert_story, ('test_title_2', 'test_content_2', 'test_childname_2',2))
    story_manager.execute_query(SQL_queries.insert_story, ('test_title_3', 'test_content_3', 'test_childname_2',2))
    story_manager.execute_query(SQL_queries.insert_story, ('test_title_4', 'test_content_4', 'test_childname_4',3))
    story_manager.execute_query(SQL_queries.insert_story, ('test_title_5', 'test_content_5', 'test_childname_5',3))


class TestDBManagement(unittest.TestCase):

    def setUp(self):
        # Initialize mock_db configuration
        self.mock_db_config = {'database': 'mock_db', 'user': os.getenv('DB_USER'), 'password': os.getenv('DB_PASS'),
                               'host': 'localhost'}

        self.handler = SetUpAndTearDownHandler(self.mock_db_config)
        self.handler.setup()
        add_test_data()

    def tearDown(self):
        self.mock_db_config = {'database': 'mock_db', 'user': os.getenv('DB_USER'), 'password': os.getenv('DB_PASS'),
                               'host': 'localhost'}
        self.handler = SetUpAndTearDownHandler(self.mock_db_config)
        self.handler.teardown()

    def test_fetch_query_success(self): ## PASS
        expected = [(3,)]
        story_manager = StoryManager(self.mock_db_config)
        result = story_manager.fetch_query("""SELECT count(UserID) FROM Users""")
        self.assertEqual(expected, result)

    def test_fetch_query_fail(self): ## PASS
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.fetch_query("""SELECT * FROM nontable""")

    def test_execute_query_success(self): ## PASS
        expected = True
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query("""INSERT INTO users (Username, Email, PasswordHash) VALUES ('test_execute_name', 'test_execute_email', 'test_execute_password')""")
        self.assertEqual(expected, result)

    def test_insert_user_success(self): #PASS
        expected = True
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query("""INSERT INTO users (Username, Email, PasswordHash) VALUES ('test_insert_name', 'test_insert_email', 'test_insert_password')""")
        self.assertEqual(expected, result)

    def test_insert_user_fail(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query("""INSERT INTO nontable (Username, Email, PasswordHash) VALUES ('test_insert_name', 'test_insert_email', 'test_insert_password')""")

    def test_insert_user_fail_duplicate_email(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query("""INSERT INTO nontable (Username, Email, PasswordHash) VALUES ('TestUser', 'Test1@user.com', 'PassWrd!')""")

    def test_insert_user_fail_nonuser(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query("""INSERT INTO nontable (Username, Email, PasswordHash) VALUES ('', 'Test4@user.com', 'PassW0rd!')""")

    def test_insert_user_fail_nonpassword(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query("""INSERT INTO nontable (Username, Email, PasswordHash) VALUES ('test_user_4', 'test@user_4.com', ''""")

    def test_insert_story_success(self):
        expected = True
        story_manager = StoryManager(db_config=self.mock_db_config)
        eg_story = SpaceStory("test_childname_5", "she", 8)
        eg_story.user_id = 3
        result = story_manager.execute_query(story_manager.insert_story(eg_story, eg_story.generate_story()))
        self.assertEqual(expected, result)

    def test_insert_story_fail(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query(story_manager.insert_story('', 'TestContent'))

    # def test_insert_mock_story_success(self):
    #     expected = True
    #     story_manager = StoryManager(db_config=self.mock_db_config)
    #     result = story_manager.execute_query(story_manager.insert_mock_story('TestTitle', 'TestContent', 'TestChildname', 4))
    #     self.assertEqual(expected, result)

    def test_insert_mock_story_fail_notitle(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query(story_manager.insert_mock_story('', 'TestContent','TestChildname', 'TestUser'))

    def test_insert_mock_story_fail_nocontent(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query(story_manager.insert_mock_story('TestTitle', '','TestChildname', 'TestUser'))

    def test_insert_mock_story_fail_no_child_name(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query(story_manager.insert_mock_story('TestTitle', '','TestChildname', 'TestUser'))

    def test_insert_mock_story_fail_no_user_id(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.execute_query(story_manager.insert_mock_story('TestTitle', 'TestContent','TestChildname', ''))

    def test_fetch_all_child_stories_fail_unknownchild(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.fetch_query(SQL_queries.fetch_all_child_stories('unknown_child'))

    def test_fetch_all_user_stories_success(self):
        expected = [(2, 'test_title_2', 'test_content_2', 'test_childname_2'), (3, 'test_title_3', 'test_content_3', 'test_childname_2')]
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query("SELECT StoryID, Title, Content, ChildName FROM stories WHERE UserId = %s", (2,))
        self.assertEqual(expected, result)

    def test_fetch_user_id_success(self):
        expected = [(3,)]
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query(SQL_queries.fetch_user)
        self.assertEqual(expected, result)

    def test_fetch_story_by_id_success(self):
        expected = [('test_title_3', 'test_content_3')]
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query("SELECT Title, Content FROM stories WHERE StoryID = %s", (3,))
        self.assertEqual(expected, result)

    def test_insert_story_by_id_fail(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.fetch_query(SQL_queries.fetch_story_by_id(''))

# if this script is executed directly, run the unit tests.
if __name__ == '__main__':
    unittest.main()