# from StoryClasses import space_story_instance, space_story, dinosaur_story_instance, dinosaur_story
from faker import Faker
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
        test_story_dict['content'] = "Placeholder Story"
        test_story_dict['userID'] = parentID
        test_story_dict['child_name'] = child_name
        list_story_dicts.append(test_story_dict)

