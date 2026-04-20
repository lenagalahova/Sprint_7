import pytest
from stocks_api import StockApi
from helpers.create_random_data_deliver import (
    create_new_courier_and_return_login_password,
    register_new_courier,
)


@pytest.fixture
def new_courier_data():
    return create_new_courier_and_return_login_password()


@pytest.fixture
def new_courier_data_without_login():
    full_data = create_new_courier_and_return_login_password()
    payload = {"password": full_data["password"], "firstName": full_data["firstName"]}
    return payload


@pytest.fixture
def new_courier_data_without_pass():
    full_data = create_new_courier_and_return_login_password()
    payload = {"login": full_data["login"], "firstName": full_data["firstName"]}
    return payload


@pytest.fixture
def new_courier_data_without_firstname():
    full_data = create_new_courier_and_return_login_password()
    payload = {"login": full_data["login"], "password": full_data["password"]}
    return payload


@pytest.fixture
def new_courier():
    return register_new_courier()


@pytest.fixture
def new_courier_login():
    full_data = register_new_courier()
    payload = {"login": full_data["login"]}
    return payload


@pytest.fixture
def new_courier_password():
    full_data = register_new_courier()
    payload = {"password": full_data["password"]}
    return payload


@pytest.fixture
def stocks_api():
    return StockApi()
