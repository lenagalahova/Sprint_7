import random
import string
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def create_new_courier_and_return_login_password():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {"login": login, "password": password, "firstName": first_name}


def create_new_courier_without_login():

    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {"password": password, "firstName": first_name}


def create_new_courier_without_pass():

    login = generate_random_string(10)
    first_name = generate_random_string(10)

    return {"login": login, "firstName": first_name}


def create_new_courier_without_firstname():

    login = generate_random_string(10)
    password = generate_random_string(10)

    return {"login": login, "password": password}


def register_new_courier():

    login = generate_random_string(10)
    password = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
    }
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    if response.status_code == 201:
        return {"login": login, "password": password}


def register_new_courier_return_login():

    login = generate_random_string(10)
    password = generate_random_string(10)

    payload = {"login": login, "password": password}
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    if response.status_code == 201:
        return {"login": login}
    return None


def register_new_courier_return_password():

    login = generate_random_string(10)
    password = generate_random_string(10)

    payload = {"login": login, "password": password}
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    if response.status_code == 201:
        return {"password": password}
    return None
