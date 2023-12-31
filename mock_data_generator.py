from faker import Faker
from story_classes import DinosaurStory, SpaceStory, PokemonStory

import random
f = Faker()

#  test data requirements, please populate:

parents = 8  # number of users/parents needed
children = 10  # number of children needed
max_age = 10  # max age of child
max_stories = 4  # max number of stories

# empty lists and dictionaries to store parent test data, do not change:

list_user_dicts = []
list_story_dicts = []
list_userIDs = []
userID = 0
story_count = 0

for parent in range(parents):
    test_user_dict = {key: [] for key in ['username', 'email', 'password', 'userID']}
    userID += 1
    first_name = f.first_name()
    last_name = f.last_name()
    username = f"{first_name} {last_name}"
    email = f"{first_name}.{last_name}@{f.domain_name()}"
    password = f.password()
    test_user_dict['username'] = username
    test_user_dict['email'] = email
    test_user_dict['password'] = password
    test_user_dict['userID'] = userID
    list_user_dicts.append(test_user_dict)
    list_userIDs.append(userID)


for child in range(children):

    gender = random.choice(["male", "female"])
    if gender == "male":
        child_name = f.first_name_male()
        pronouns = "he"
    else:
        child_name = f.first_name_female()
        pronouns = "she"
    child_age = random.randint(1, max_age)
    parentID = random.choice(list_userIDs)

    for story in range(max_stories):
        test_story_dict = {key: [] for key in ['title', 'content', 'child_name', 'userID']}
        story_count += 1
        theme = random.choice(["Dinosaurs", "Space", "Pokemon"])
        title = f"{child_name}'s {theme} Story"
        test_story_dict['title'] = title
        if theme == "Dinosaurs":
            test_story_dict['story_instance'] = DinosaurStory(child_name, pronouns, child_age)
            test_story_dict['content'] = test_story_dict['story_instance'].generate_story()
        elif theme == "Space":
            test_story_dict['story_instance'] = SpaceStory(child_name, pronouns, child_age)
            test_story_dict['content'] = test_story_dict['story_instance'].generate_story()
        elif theme == "Pokemon":
            test_story_dict['story_instance'] = PokemonStory(child_name, pronouns, child_age)
            test_story_dict['content'] = test_story_dict['story_instance'].generate_story()
        else:
            print("Error: theme not found")
        test_story_dict['story_instance'].user_id = parentID
        test_story_dict['child_name'] = child_name
        list_story_dicts.append(test_story_dict)

# secondary loop to guarantee some stories generated for user 1 for demo purposes
for child in range(1):

    gender = random.choice(["male", "female"])
    if gender == "male":
        child_name = f.first_name_male()
        pronouns = "he"
    else:
        child_name = f.first_name_female()
        pronouns = "she"
    child_age = random.randint(1, max_age)
    parentID = 1

    for story in range(2):
        test_story_dict = {key: [] for key in ['title', 'content', 'child_name', 'userID']}
        story_count += 1
        theme = random.choice(["Dinosaurs", "Space", "Pokemon"])
        title = f"{child_name}'s {theme} Story"
        test_story_dict['title'] = title
        if theme == "Dinosaurs":
            test_story_dict['story_instance'] = DinosaurStory(child_name, pronouns, child_age)
            test_story_dict['content'] = test_story_dict['story_instance'].generate_story()
        elif theme == "Space":
            test_story_dict['story_instance'] = SpaceStory(child_name, pronouns, child_age)
            test_story_dict['content'] = test_story_dict['story_instance'].generate_story()
        elif theme == "Pokemon":
            test_story_dict['story_instance'] = PokemonStory(child_name, pronouns, child_age)
            test_story_dict['content'] = test_story_dict['story_instance'].generate_story()
        else:
            print("Error: theme not found")
        test_story_dict['story_instance'].user_id = parentID
        test_story_dict['child_name'] = child_name
        list_story_dicts.append(test_story_dict)
