# import the random module to allow for random selection of story options
import random

# import API call functions from SpaceStoryAPICalls.py
from SpaceStoryAPICalls import get_astronaut_name, get_no_iss_residents

# Method for creating paragraph one, takes child name and age as inputs
# Uses the get_astronaut_name function from SpaceStoryAPICalls.py to get a random astronaut name
# Returns a string containing paragraph one of the story from two possible options
def paragraph_one(child_name, child_age):
    astronaut_name = get_astronaut_name()
    return f'''{child_name} was the youngest ever astronaut in training, at just {child_age} years old.
    One day, {child_name} was  busy learning all the names of the different planets, when an alarm started to sound.
    It was a message from famous astronaut {astronaut_name} who was living on the International Space Station. The astronauts on the ISS needed {child_name}’s help!'''

# Method for creating paragraph two, takes child name as input
# There are two possible story options, randomly selected using the random module
# Also uses the random module to randomly select alien's appearance and sound from a list of options,
# and to randomly select a spaceship part from a list of options for story option 1
# Returns a string containing paragraph two of the story
def paragraph_two(child_name):
    rand_spaceship_part = random.choice(["doors", "door frames", "vents", "door locks"])
    rand_noise = random.choice(["a warbling wail", "a musical chime-like song", "a noise like a bubbling brook", "a trilling whistle"])
    rand_colour = random.choice(["hot pink", "deep purple", "lime green", "neon orange", "sunflower yellow"])
    rand_pattern = random.choice(["holographic stripes", "bumpy scales", "super fluffy fur", "a leathery hide", "silky downy hair","black polka dots", "white polka dots"])
    alien_desc = f"{rand_colour} with {rand_pattern}"

    option_one = f'''An unidentified lifeform has got stuck in the air lock of the ship - they need someone to come get it from the outside.
    {child_name} bravely pulled on their space suit and jumped in a rocket.
    In space, {child_name} parked their ship next to the ISS and went on a spacewalk to investigate the airlock.
    The outer door was jammed open, and when {child_name} peeked inside they saw a cute little {alien_desc}. One of the tentacles of the alien was trapped in one of the {rand_spaceship_part} and it was crying.
    Luckily {child_name} knew just what to do, and brought out a pack of space butter. After rubbing the tentacle in butter it slipped straight out! The alien cuddled up to {child_name} and then ate all the butter.'''

    option_two = f'''The ISS's engine is failing! And they need someone to bring them a special space screwdriver to fix it, as theirs got lost on the last spacewalk.
    {child_name} bravely pulled on their space suit and jumped in a rocket. As {child_name} approached the ISS they realised they had left the screwdriver back on Earth! Oh no! But just then they heard a {rand_noise}. {child_name} looked around and saw an alien in a shiny flying saucer. The alien was huge and {alien_desc}. To {child_name}'s surprise and relief, the alien was waving a space screwdriver!
    {child_name} borrowed the screwdriver, and with the alien's help managed to fix the engine just before it exploded!'''

    return random.choice([option_one, option_two])

# Method for creating paragraph three, takes child name as input
# Uses the get_no_iss_residents function from SpaceStoryAPICalls.py to get the number of ISS residents
# Uses the random module to randomly select alien name from a list of options for the story
# Returns a string containing paragraph three of the story
def paragraph_three(child_name):
    no_iss_residents = get_no_iss_residents()
    rand_alien_name = random.choice(["Blork", "Snuggles", "Nova", "Alexis", "Wiffle", "Werkle", "Blooblubblub", "Zing", "Meepmeep"])
    return f"From that day on they were best friends! {child_name} called the alien {rand_alien_name} and they lived together on the ISS with the other {no_iss_residents} astronauts."

# Method for creating the full story using all three paragraphs, takes child name and age as inputs
def space_story_text(child_name, child_age):
    para_one = paragraph_one(child_name, child_age)
    para_two = paragraph_two(child_name)
    para_three = paragraph_three(child_name)
    response = f'''{para_one}
    {para_two}
    {para_three}'''
    return response
