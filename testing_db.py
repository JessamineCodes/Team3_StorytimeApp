import db_management
from db_management import DatabaseHandler, StoryManager
from mock_db import MockDB
from mock import patch


class TestDBManagement(MockDB):

    def test_db_write(self):
        with self.mock_db_config:
            self.assertEqual(db_management.StoryManager.fetch_user_id("""SELECT max(UserID) FROM Users"""), 1)
            # self.assertEqual(db_management.db_write("""DELETE FROM `test_table` WHERE id='4' """), True)
            # self.assertEqual(db_management.story_manager.SQL_queries.insert_user('TestPam', 'TestPamEmail', 'TestPamPassword'), True)
            # self.assertEqual(db_management.db_write("""INSERT INTO `test_table` (`id`, `text`, `int`) VALUES
            #                 ('1', 'test_text_3', 3)"""), False)


