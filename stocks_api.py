import requests
from allure import step
from config import BASE_URL, COURIER_ENDPOINT, COURIER_LOGIN_ENDPOINT, ORDERS_ENDPOINT


class StockApi:
    @step("Создание курьера")
    def create_new_deliver(self, **kwargs):
        return requests.post(f"{BASE_URL}{COURIER_ENDPOINT}", **kwargs)

    @step("Логин курьера в системе")
    def login_deliver(self, **kwargs):
        return requests.post(f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}", **kwargs)

    @step("Создание заказа")
    def create_order(self, **kwargs):
        return requests.post(f"{BASE_URL}{ORDERS_ENDPOINT}", **kwargs)

    @step("Получение списка заказов")
    def get_order(self, **kwargs):
        return requests.get(f"{BASE_URL}{ORDERS_ENDPOINT}", **kwargs)
