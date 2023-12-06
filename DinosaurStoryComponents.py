import random
from DinosaurStoryAPICalls import get_random_dino_info_response

def paragraph_one(child_name, child_age, dino_species):
    rand_portal_desc = random.choice(["glowing green", "spinning purple", "flickering blue", "flashing red", "huge and sparking"])
    rand_dr_desc = random.choice(["an elderly man in a  silver labcoat", "a woman in a green labcoat and huge glasses", "a youn man in an orange hazard suit"])
    rand_dr_name = random.choice(["Dr. Corinthius Potterdew", "Professor Alex Hammerhill", "Dr. Dru Dino", "Professor T Rex", "Dr. Lesley Lizard"])
    response = f"{child_name} wanted to be a famous paleontologist when they grew up. Early every Saturday morning, they went to the Natural History Museum to see the fossils. One morning when no-one else was around, they heard an explosion followed by a roar. Even though {child_name} was only {child_age} years old, they were very brave, so they rushed towards the noise. They stumbled into a side room and saw a {rand_portal_desc} portal and {rand_dr_desc} trapped under a table. The scientist called out to {child_name} and said, 'Help me, child! I am {rand_dr_name}, a time-travelling vet. I was on my way to the past to treat a {dino_species} when there was a fluctuation in the time-space portal capacitor and now I'm stuck under here! The {dino_species} needs urgent help, please take this medikit and go help it!' {child_name} agreed, grabbed the kit and jumped into the portal."
    return response

def paragraph_two(child_name, dino_species):
    rand_weather = random.choice(["super sunny", "heavily rainy", "wickedly windy", "scarily stormy"])

    option_one = f"{child_name} found themselves in a prehistoric jungle where it was {rand_weather}. They could hear the {dino_species} roaring in the distance. They ran towards the sound and saw the {dino_species} lying on the ground. It was covered in blood and had a huge gash on its side. {child_name} opened the medikit and took out a bandage. They wrapped the bandage around the {dino_species}'s wound and gave it a painkiller. The {dino_species} slowly got to its feet and roared in gratitude."

    option_two = f"{child_name} found themeselves on a prehistoric beach where it was {rand_weather}. Just along the beach was a cluster of huge eggs. All of them were broken except one. From inside the egg {child_name} could hear something crying.The baby {dino_species} wasn't able to get out of the egg! {child_name} opened the medikit and took out a pair of gloves. They put the gloves on and helped break apart the egg shell. The baby {dino_species} gave a tiny roar in gratitude and nuzzled {child_name}."

    return random.choice([option_one, option_two])

def paragraph_three(child_name, dino_species, dino_desc):
    rand_ending = random.choice(["'Wow! Yes, please!' and they travelled history together saving endangered animals.", f"'No, thanks! I want to go back and live with the dinosaurs!' So {child_name} jumped back into the portal and lived happily ever after with the {dino_species}."])
    return f"Suddenly, there was a flash of light and {child_name} found themselves back in the museum. The time-travelling vet was standing in front of them. 'Thank you for saving the {dino_species} Did you know: {dino_desc}. You are a true hero, {child_name}, I could use someone like you - do you want to become my assistant?' {child_name} said, {rand_ending}"

def dinosaur_story_text(child_name, child_age):
    dinosaur_dictionary = get_random_dino_info_response()
    dino_species = dinosaur_dictionary['Name']
    dino_desc = dinosaur_dictionary['Description']
    para_one = paragraph_one(child_name, child_age, dino_species)
    para_two = paragraph_two(child_name, dino_species)
    para_three = paragraph_three(child_name, dino_species, dino_desc)
    return f'''{para_one}
{para_two}
{para_three}'''
