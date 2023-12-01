from StoryComponents import story_text


class StoryGenerator:
    def __init__(self, child_name, child_pronouns, child_age):
        self.child_name = child_name
        self.child_pronouns = child_pronouns
        self.child_age = int(child_age)
        self.story_text = story_text(self.child_name, self.child_age)


print(StoryGenerator("Jo", "she", "12").story_text)
