# Import random module to allow for random selection of various story elements
import random

# import pronouns dictionary
from pronouns import pronouns

# Import function to get dinosaur's info from dinosaur_story_api_calls.py
from dinosaur_story_api_calls import dino_desc, dino_species


# Function to create paragraph one of the story using child's name, age and pronouns, dinosaur species and random elements
# Returns string containing paragraph one of the story
def paragraph_one(child_name, child_age, child_pronouns, dino_species):
    rand_portal_desc = random.choice(["glowing green", "spinning purple", "flickering blue", "flashing red", "huge and sparking"])
    rand_dr_desc = random.choice(["an elderly man in a  silver labcoat", "a woman in a green labcoat and huge glasses", "a youn man in an orange hazard suit"])
    rand_dr_name = random.choice(["Dr. Corinthius Potterdew", "Professor Alex Hammerhill", "Dr. Dru Dino", "Professor T Rex", "Dr. Lesley Lizard"])

    response = f"{child_name} wanted to be a famous paleontologist when {pronouns[child_pronouns]['subject']} grew up. Early every Saturday morning, {pronouns[child_pronouns]['subject']} went to the Natural History Museum to see the fossils. One morning when no-one else was around, {pronouns[child_pronouns]['subject']} heard an explosion followed by a roar. {child_name} was only {child_age} years old but was also very brave, so {pronouns[child_pronouns]['subject']} rushed towards the noise. {pronouns[child_pronouns]['subject'].title()} stumbled into a side room and saw a {rand_portal_desc} portal and {rand_dr_desc} trapped under a table. The scientist called out to {child_name} and said, 'Help me, child! I am {rand_dr_name}, a time-travelling vet. I was on my way to the past to treat a {dino_species} when there was a fluctuation in the time-space portal capacitor and now I'm stuck under here! The {dino_species} needs urgent help, please take this medikit and go help it!' {child_name} agreed, grabbed the kit and jumped into the portal."
    return response

# Function to create paragraph two of the story using child's name and pronouns, dinosaur species and random elements
# Returns string containing paragraph two of the story from two possible options
def paragraph_two(child_name, child_pronouns, dino_species):
    rand_weather = random.choice(["super sunny", "heavily rainy", "wickedly windy", "scarily stormy"])

    option_one = f"{child_name} found {pronouns[child_pronouns]['reflexive']} in a prehistoric jungle where it was {rand_weather}. {pronouns[child_pronouns]['subject']} could hear the {dino_species} roaring in the distance. {pronouns[child_pronouns]['subject'].title()} ran towards the sound and saw the {dino_species} lying on the ground. It had a huge gash on its side! {child_name} opened the medikit and took out a bandage. {pronouns[child_pronouns]['subject'].title()} wrapped the bandage around the {dino_species}'s wound and gave it a painkiller. The {dino_species} slowly got to its feet and roared in gratitude."

    option_two = f"{child_name} found {pronouns[child_pronouns]['reflexive']} on a prehistoric beach where it was {rand_weather}. Just along the beach was a cluster of huge eggs. All of them were broken except one. From inside the egg {child_name} could hear something crying. The baby {dino_species} wasn't able to get out of the egg! {child_name} opened the medikit and took out a pair of gloves. {pronouns[child_pronouns]['subject'].title()} put the gloves on and helped break apart the egg shell. The baby {dino_species} gave a tiny roar in gratitude and nuzzled {child_name}."

    return random.choice([option_one, option_two])

# Function to create paragraph three of the story using child's name and pronouns, dinosaur species, dinosaur description and random elements.
# Returns string containing paragraph three of the story with two possible endings.
def paragraph_three(child_name, child_pronouns, dino_species, dino_desc):
    rand_ending = random.choice([f"'Wow! Yes, please!' and {pronouns[child_pronouns]['subject']} travelled history together saving endangered animals.", f"'No, thanks! I want to go back and live with the dinosaurs!' So {child_name} jumped back into the portal and lived happily ever after with the {dino_species}."])

    response = f"Suddenly, there was a flash of light and {child_name} found {pronouns[child_pronouns]['reflexive']} back in the museum. The time-travelling vet was standing in front of {pronouns[child_pronouns]['object']}. 'Thank you for saving the {dino_species}. Did you know: {dino_desc} You are a true hero, {child_name}, I could use someone like you - do you want to become my assistant?' {child_name} said, {rand_ending}"
    return response

# Function to create the full story text using child's name, pronouns and age and dinosaurs details from API call
def dinosaur_story_text(child_name, child_age, child_pronouns):
    para_one = paragraph_one(child_name, child_age, child_pronouns, dino_species)
    para_two = paragraph_two(child_name, child_pronouns, dino_species)
    para_three = paragraph_three(child_name, child_pronouns, dino_species, dino_desc)
    response = f'''{para_one}

{para_two}

{para_three}'''
    return response
