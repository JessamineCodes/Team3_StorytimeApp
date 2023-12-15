import mysql.connector
from mysql.connector import errorcode
from unittest import TestCase
from mock import patch
import db_management
import os


# mock db setup:
DB_HOST = "localhost"
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = "3306"
DB_NAME = "mockdb"


class MockDB(TestCase):

    @classmethod
    def setUpClass(cls):
        cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cursor = cnx.cursor(dictionary=True)

        # drop database if it already exists
        try:
            cursor.execute("DROP DATABASE {}".format(DB_NAME))
            cursor.close()
            print("DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(DB_NAME, err))
        cursor = cnx.cursor(dictionary=True)

        # create database
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cnx.database = DB_NAME

        # create table

        query = """CREATE TABLE IF NOT EXISTS users (
                    UserID INT PRIMARY KEY AUTO_INCREMENT,
                    Username VARCHAR(50) NOT NULL,
                    Email VARCHAR(100) NOT NULL UNIQUE,
                    PasswordHash VARCHAR(255) NOT NULL,
                    DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP
                    )"""
        try:
            cursor.execute(query)
            cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("table 'users' already exists")
            else:
                print(err.msg)
        else:
            print("table created: users")

        query = """CREATE TABLE IF NOT EXISTS stories (
                        StoryID INT PRIMARY KEY AUTO_INCREMENT,
                        Title VARCHAR(100) NOT NULL,
                        Content TEXT NOT NULL,
                        DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
                        UserID INT NOT NULL,
                        ChildName VARCHAR(100) NOT NULL,
                        FOREIGN KEY (UserID) REFERENCES users(UserID)
                        )"""
        try:
            cursor.execute(query)
            cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("table 'stories' already exists")
            else:
                print(err.msg)
        else:
            print("table created: stories")

        # insert data

        insert_data_query = """INSERT INTO users (Username, Email, PasswordHash) VALUES ('Test user 1', 'Pam@pam.com', '1234!%CFG')
                                    INSERT INTO users (Username, Email, PasswordHash) VALUES ('Test user 2', 'Pam@pam.com', '1&2FH34!') 
                                    INSERT INTO users (Username, Email, PasswordHash) VALUES ('Test user 3', 'Pam@pam.com', '19SR8!')      
                                    INSERT INTO stories (Title, Content, ChildName, UserId) VALUES ('Test Title', Test Content', 'Test child name', '1')
                                    INSERT INTO stories (Title, Content, ChildName, UserId) VALUES ('Test Title', Test Content', 'Test child name', '2')
                                    INSERT INTO stories (Title, Content, ChildName, UserId) VALUES ('Test Title', Test Content', 'Test child name', '3')
                                        """
        try:
            cursor.execute(insert_data_query)
            cnx.commit()
        except mysql.connector.Error as err:
            print("Data insertion to test_table failed \n" + err)
        cursor.close()
        cnx.close()





        testconfig = {
            'host': DB_HOST,
            'user': DB_USER,
            'password': DB_PASS,
            'database': DB_NAME
        }
        cls.mock_db_config = patch.dict(db_management.config, testconfig)

    @classmethod
    def tearDownClass(cls):
        cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP DATABASE {}".format(DB_NAME))
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exist. Dropping db failed".format(DB_NAME))
        cnx.close()

