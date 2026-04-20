import random
import string
import requests
from config import BASE_URL, COURIER_ENDPOINT


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def create_new_courier_and_return_login_password():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {"login": login, "password": password, "firstName": first_name}


def register_new_courier():

    login = generate_random_string(10)
    password = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
    }
    response = requests.post(f"{BASE_URL}{COURIER_ENDPOINT}", data=payload)
    if response.status_code == 201:
        return {"login": login, "password": password}
