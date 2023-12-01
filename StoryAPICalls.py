import random
import requests

open_notify_url = "http://api.open-notify.org/astros.json"


def get_response():
    response = requests.get(open_notify_url)
    return response.json()


def get_astronaut_name():
    people_on_Iss = get_response()['people']
    return random.choice(people_on_Iss)['name']


def get_no_iss_residents():
    no_people_on_Iss = get_response()['number']
    return no_people_on_Iss