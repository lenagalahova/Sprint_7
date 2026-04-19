import pytest
from stocks_api import StockApi
from helpers.create_random_data_deliver import (
    create_new_courier_and_return_login_password,
    create_new_courier_without_login,
    create_new_courier_without_pass,
    create_new_courier_without_firstname,
    register_new_courier,
    register_new_courier_return_login,
    register_new_courier_return_password,
)


@pytest.fixture
def new_courier_data():
    return create_new_courier_and_return_login_password()


@pytest.fixture
def new_courier_data_without_login():
    return create_new_courier_without_login()


@pytest.fixture
def new_courier_data_without_pass():
    return create_new_courier_without_pass()


@pytest.fixture
def new_courier_data_without_firstname():
    return create_new_courier_without_firstname()


@pytest.fixture
def new_courier():
    return register_new_courier()


@pytest.fixture
def new_courier_login():
    return register_new_courier_return_login()


@pytest.fixture
def new_courier_password():
    return register_new_courier_return_password()


@pytest.fixture
def stocks_api():
    return StockApi()
