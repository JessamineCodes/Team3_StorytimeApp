import mysql.connector
from mysql.connector import errorcode
from unittest import TestCase
from mock import patch
import db_management
from dotenv import load_dotenv
import os

load_dotenv()

# mock db setup:
DB_HOST = "localhost"
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = "3306"
DB_NAME = "mock_db"


class MockDB(TestCase):

    @classmethod
    def setUpClass(cls):
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cursor = connection.cursor(dictionary=True)

        # drop database if it already exists
        try:
            cursor.execute("DROP DATABASE {}".format(DB_NAME))
            cursor.close()
            print("mock DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(DB_NAME, err))
        cursor = connection.cursor(dictionary=True)

        # create database
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating mock database: {}".format(err))
            exit(1)
        connection.database = DB_NAME

        # create table 'users'

        create_users_table = """CREATE TABLE users (
                    UserID INT PRIMARY KEY AUTO_INCREMENT,
                    Username VARCHAR(50) NOT NULL,
                    Email VARCHAR(100) NOT NULL UNIQUE,
                    PasswordHash VARCHAR(255) NOT NULL,
                    DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP
                    )"""
        try:
            cursor.execute(create_users_table)
            connection.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("mock table 'users' already exists")
            else:
                print(err.msg)
        else:
            print("mock table created: users")

        # insert test data into 'users'

        insert_user_data = """INSERT INTO users (Username, Email, PasswordHash) VALUES ('TestUser1', 'Test1@user.com', '14!%CFg9'),
        ('TestUser2', 'Test2@user.com', '14!%dFG5'),
        ('TestUser3', 'Test3@user.com', '17!%CfG9')"""

        try:
            cursor.execute(insert_user_data)
            connection.commit()
            print("mock data inserted: users")
        except mysql.connector.Error as err:
            print("Data insertion to mock table 'user' failed \n" + err)

        # create table 'stories'

        create_stories_table = """CREATE TABLE IF NOT EXISTS stories (
                                StoryID INT PRIMARY KEY AUTO_INCREMENT,
                                Title VARCHAR(100) NOT NULL,
                                Content TEXT NOT NULL,
                                DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
                                UserID INT NOT NULL,
                                ChildName VARCHAR(100) NOT NULL,
                                FOREIGN KEY (UserID) REFERENCES users(UserID)
                                )"""
        try:
            cursor.execute(create_stories_table)
            connection.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("mock table 'stories' already exists")
            else:
                print(err.msg)
        else:
            print("mock table created: stories")

        # insert data into 'stories'

        insert_stories_data_query = """INSERT INTO stories (Title, Content, ChildName, UserId) VALUES ('Test Title 1', 'Test Content 1', 'Test childname1', '1'),
        ('Test Title 2', 'Test Content 2', 'Test childname2', '2'),
        ('Test Title 3', 'Test Content 3', 'Test childname3', '1')"""

        try:
            cursor.execute(insert_stories_data_query)
            connection.commit()
            print("mock data inserted: users")

        except mysql.connector.Error as err:
            print("Data insertion to mock table stories failed \n" + err)
        cursor.close()
        connection.close()

        testconfig = {
            'user': DB_USER,
            'password': DB_PASS,
            'database': DB_NAME,
            'host': DB_HOST
        }
        cls.mock_db_config = patch.dict(db_management.db_config, testconfig)

    @classmethod
    def tearDownClass(cls):
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = connection.cursor(dictionary=True)

        #drop test database
        try:
            cursor.execute("DROP DATABASE {}".format(DB_NAME))
            connection.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exist. Dropping mock db failed".format(DB_NAME))
        connection.close()

