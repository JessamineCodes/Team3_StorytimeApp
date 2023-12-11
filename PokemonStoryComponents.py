from PokemonStoryApiCalls import get_pokemon_info, p_name, p_ability, p_move, poke_type
from pronouns import pronouns
import random

# Starter pokemon dictionary
starter_pokemon = my_dict = {
    'Fire type': ['Charmander', 'Torchic', 'Cyndaquil'],
    'Water type': ['Squirtle', 'Totodile', 'Piplup'],
    'Grass type': ['Bulbasaur', 'Chikorita', 'Treecko']
}

# Gets a random key from the dictionary
random_type = random.choice(list(starter_pokemon.keys()))

# Gets the list associated with the type key and gets a random pokemon
pokemon_list = starter_pokemon[random_type]
random_pokemon = random.choice(pokemon_list)

# Used throughout story so needed in global scope
random_professor = random.choice(["Professor Alpine", "Professor Elm", "Professor Oak", "Professor Ivy", "Professor Juniper"])

# Method for creating paragraph one, takes child name and age as inputs
def paragraph_one(child_name, child_age, child_pronouns):

    response = f'''In a bustling town named Pokeville a young trainer called {child_name} was eager to embark on {pronouns[child_pronouns]['possessive']} Pokémon journey. Being {child_age} meant {child_name} could finally become a Pokémon trainer and {child_name} couldn't wait to see what was in store! {pronouns[child_pronouns]['subject'].title()} set off to the training centre where {pronouns[child_pronouns]['subject']} could choose {pronouns[child_pronouns]['possessive']} very own Pokémon. {child_name} stood in front of a desk facing 3 Poké Balls, each holding a different type of Pokémon: Fire, Water and Grass. {child_name} chose the {random_type} {random_pokemon} as {pronouns[child_pronouns]['possessive']} loyal companion. They became best friends immediately! Just then, {child_name} felt a vibration coming from {pronouns[child_pronouns]['possessive']} pocket. It was an urgent message from {random_professor} giving {child_name} {pronouns[child_pronouns]['possessive']} very first mission as a trainer!'''
    return response

# Function to create paragraph two of the story using child's name, and random elements
# Returns string containing paragraph two of the story from two possible options
def paragraph_two(child_name, child_pronouns):
    random_location = random.choice(["Abandoned Ship", "Granite Cave", "Desert Underpass", "Viridian Forest"])
    random_pokemon_aid = random.choice(["HP potion", "berry juice", "revive", "poison antidote"])
    random_gyms = random.choice(["Pewter City Gym", "Saffron City Gym", "Cortondo Gym", "Vermillion City Gym", "Goldenrod Gym", "Snowpoint City Gym"])

    option_one = f'''{child_name} had been given the huge responsibility of rescuing an injured pokémon from {random_location}. Feeling brave, {child_name} ran as fast as {pronouns[child_pronouns]['subject']} could, grateful that {pronouns[child_pronouns]['subject']} had {pronouns[child_pronouns]['possessive']} trusty map in {pronouns[child_pronouns]['possessive']} pack already. As soon as {pronouns[child_pronouns]['subject']} got there, {child_name} found the injured pokémon lying on the ground. Using {pronouns[child_pronouns]['possessive']} Pokédex, {child_name} realised it was a wild {p_name}, a {poke_type} type Pokémon. After inspecting their injuries closer, {child_name} gave the {p_name} a {random_pokemon_aid}! {child_name} waited and waited to see if {p_name} would wake up. Suddenly, {child_name} heard a gentle growl. {p_name} was awake! With the help of {random_pokemon}, {child_name} managed to get {p_name} safely to the Pokémon Centre to be treated by Nurse Joy.'''

    option_two = f'''{child_name} has been given the unique opportunity as a young trainer, to face {pronouns[child_pronouns]['possessive']} very first battle at {random_gyms}. Once {pronouns[child_pronouns]['subject']} arrived, the energy was electric! Everyone had come to witness who would be crowned the Pokémon master of the {random_gyms}. The trainer {child_name} was facing was called Misty. Misty released {p_name} onto the battlefield whilst {child_name} released {random_pokemon}. {p_name} used {p_move}, but it missed! {random_pokemon} used scratch, it was super effective! {p_name} was defeated and {child_name} had a triumphant victory!'''

    return random.choice([option_one, option_two])

# Function to create paragraph three of the story using child's name as input
def paragraph_three(child_name, child_pronouns):
    response = f'''Just then, a bright glow surrounded {random_pokemon}. {child_name} watched as {random_pokemon} levelled up and learnt {p_ability}. Filled with newfound confidence {child_name} made {pronouns[child_pronouns]['possessive']} way back to the city, eager to tell {random_professor} the amazing news! The news of {child_name}'s bravery travelled fast and {child_name} couldn't wait for {pronouns[child_pronouns]['possessive']} next adventure.'''
    return response

# Function for creating the full story using all three paragraphs, takes child name and age as inputs
def pokemon_story_text(child_name, child_age, child_pronouns):
    para_one = paragraph_one(child_name, child_age, child_pronouns)
    para_two = paragraph_two(child_name, child_pronouns)
    para_three = paragraph_three(child_name, child_pronouns)
    return f'''{para_one}

{para_two}

{para_three}'''
