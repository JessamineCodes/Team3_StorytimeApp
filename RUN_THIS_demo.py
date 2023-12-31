from db_management import StoryManager, SetUpAndTearDownHandler, DB_CONFIG
import mock_data_generator as mock


def are_you_ready():
        ready = input("Would you like to set up the database? yes or no. ")
        if ready == "yes":
            print("\nExcellent! Lets get started.\n")
        elif ready == "no":
            print("It is advised that you set up the database before visiting our story generator app.")
            are_you_ready()
        else:
            print("\nTry again - yes or no, please! \n")
            are_you_ready()


def query_data():
        data = input("Would you like to add some mock data to the database? yes or no. ")
        if data == "yes":
            print("\nPopulating database.\n")
            add_mock_data(mock.parents, mock.story_count)
            print("\nDatabase populated. Please make your way to app.py and launch our story generator app!\n")
        elif data == "no":
            print("No Problem. Please make your way to app.py and launch our story generator app!")
        else:
            print("\nTry again - yes or no, please! \n")
            query_data()


# Populating database with mock data via mock_data_generator
def add_mock_data(users, stories):
    story_manager = StoryManager()
    for x in range(users):
        story_manager.insert_user(mock.list_user_dicts[x]['username'], mock.list_user_dicts[x]['email'], mock.list_user_dicts[x]['password'])
        x += 1
    for y in range(stories):
        story_manager.insert_story(mock.list_story_dicts[y]['story_instance'], mock.list_story_dicts[y]['content'])
        y += 1


def teardown():
    SetUpAndTearDownHandler.teardown(DB_CONFIG)


def setup():
    handler = SetUpAndTearDownHandler(DB_CONFIG)
    handler.setup()
    query_data()


def main():
    print("----------------------------------")
    print("             WELCOME              ")
    print("----------------------------------")
    are_you_ready()
    setup()
    print("Goodbye")


main()
