import unittest
# from unittest.mock import patch
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
    story_manager.execute_query(SQL_queries.insert_user, ('TestUser1', 'Test1@user.com', 'PassW0rd!'))
    story_manager.execute_query(SQL_queries.insert_user, ('TestUser2', 'Test2@user.com', 'pAssWord2'))
    story_manager.execute_query(SQL_queries.insert_user, ('TestUser3', 'Test3@user.com', 'pa5Sw0ord3'))
    story_manager.execute_query(SQL_queries.insert_story, ('TestTitle1', 'TestContent', 'TestChildname1','TestUser1'))
    story_manager.execute_query(SQL_queries.insert_story, ('TestTitle2', 'TestContent', 'TestChildname2','TestUser1'))
    story_manager.execute_query(SQL_queries.insert_story, ('TestTitle3', 'TestContent', 'TestChildname2','TestUser2'))
    story_manager.execute_query(SQL_queries.insert_story, ('TestTitle4', 'TestContent', 'TestChildname3','TestUser3'))
    story_manager.execute_query(SQL_queries.insert_story, ('TestTitle5', 'TestContent', 'TestChildname4','TestUser3'))


class TestDBManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize mock_db configuration
        cls.mock_db_config = {'database': 'mock_db', 'user': os.getenv('DB_USER'), 'password': os.getenv('DB_PASS'),
                               'host': 'localhost'}

        cls.handler = SetUpAndTearDownHandler(db_config=cls.mock_db_config)
        cls.handler.setup()
        add_test_data()
    @classmethod
    def tearDownClass(cls):
        cls.handler.teardown()

    def test_fetch_query_success(self):
        expected = [(3,)]
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query("""SELECT count(UserID) FROM Users""")
        self.assertEqual(expected, result)

    def test_fetch_query_fail(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.fetch_query("""SELECT * FROM nontable""")


    def test_execute_query_success(self):
        expected = True
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query("""INSERT INTO users (Username, Email, PasswordHash) VALUES ('test_execute_name', 'test_execute_email', 'test_execute_password')""")
        self.assertEqual(expected, result)

    def test_execute_query_fail(self):
        with self.assertRaises(Exception):
            story_manager = StoryManager(db_config=self.mock_db_config)
            story_manager.fetch_query("""SELECT * FROM nontable""")

    def test_insert_user_success(self):
        expected = True
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query("""INSERT INTO users (Username, Email, PasswordHash) VALUES ('test_insert_name', 'test_insert_email', 'test_insert_password')""")
        self.assertEqual(expected, result)

    def test_insert_user_fail(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query("""INSERT INTO nontable (Username, Email, PasswordHash) VALUES ('test_insert_name', 'test_insert_email', 'test_insert_password')""")
        self.assertEqual(expected, result)

    def test_insert_user_fail_duplicate_email(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query("""INSERT INTO nontable (Username, Email, PasswordHash) VALUES ('TestUser', 'Test1@user.com', 'PassWrd!')""")
        self.assertEqual(expected, result)

    def test_insert_user_fail_nonuser(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query("""INSERT INTO nontable (Username, Email, PasswordHash) VALUES ('', 'Test4@user.com', 'PassW0rd!')""")
        self.assertEqual(expected, result)

    def test_insert_user_fail_nonpassword(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query("""INSERT INTO nontable (Username, Email, PasswordHash) VALUES ('TestUser4', 'Test4@user.com', ''""")
        self.assertEqual(expected, result)

    def test_insert_story_success(self):
        expected = True
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query(story_manager.insert_story('Test Title 4', 'Test Content 4'))
        self.assertEqual(expected, result)

    def test_insert_story_fail(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query(story_manager.insert_story('', 'TestContent'))
        self.assertEqual(expected, result)

    def test_insert_mock_story_success(self):
        expected = True
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query(story_manager.insert_mock_story('TestTitle', 'TestContent', 'TestChildname', 'TestUser'))
        self.assertEqual(expected, result)


    def test_insert_mock_story_fail_notitle(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query(story_manager.insert_mock_story('', 'TestContent','TestChildname', 'TestUser'))
        self.assertEqual(expected, result)

    def test_insert_mock_story_fail_nocontent(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query(story_manager.insert_mock_story('TestTitle', '','TestChildname', 'TestUser'))
        self.assertEqual(expected, result)

    def test_insert_mock_story_fail_nochildname(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query(story_manager.insert_mock_story('TestTitle', 'TestContent','', 'TestUser'))
        self.assertEqual(expected, result)

    def test_insert_mock_story_fail_nouserid(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.execute_query(story_manager.insert_mock_story('TestTitle', 'TestContent','TestChildname', ''))
        self.assertEqual(expected, result)

    def test_fetch_all_child_stories_success(self):
        expected = True
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query(story_manager.fetch_all_child_stories('TestChildname2'))
        self.assertEqual(expected, result)

    def test_fetch_all_child_stories_fail_unknownchild(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query(SQL_queries.fetch_all_child_stories('TestChildname5'))
        self.assertEqual(expected, result)

    def test_fetch_all_user_stories_success(self):
        expected = [('TestTitle1', 'TestTitle2')]
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query(story_manager.fetch_all_user_stories(1))
        self.assertEqual(expected, result)

    def test_fetch_all_user_stories_fail_unknownuser(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query(SQL_queries.fetch_all_user_stories(4))
        self.assertEqual(expected, result)

    def test_fetch_user_id_success(self):
        expected = [(3,)]
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query(SQL_queries.fetch_user)
        self.assertEqual(expected, result)


    def test_fetch_story_by_id_success(self):
        expected = [('TestTitle3',)]
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query(SQL_queries.fetch_story_by_id(3))
        self.assertEqual(expected, result)

    def test_insert_story_by_id_fail(self):
        expected = Exception
        story_manager = StoryManager(db_config=self.mock_db_config)
        result = story_manager.fetch_query(SQL_queries.fetch_story_by_id(''))
        self.assertEqual(expected, result)


# if this script is executed directly, run the unit tests.
if __name__ == '__main__':
    unittest.main()
