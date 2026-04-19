import requests
from allure import step

BASE_URL = "https://qa-scooter.praktikum-services.ru"


class StockApi:
    @step("Создание курьера")
    def create_new_deliver(self, **kwargs):
        return requests.post(f"{BASE_URL}/api/v1/courier", **kwargs)

    @step("Логин курьера в системе")
    def login_deliver(self, **kwargs):
        return requests.post(f"{BASE_URL}/api/v1/courier/login", **kwargs)

    @step("Создание заказа")
    def create_order(self, **kwargs):
        return requests.post(f"{BASE_URL}/api/v1/orders", **kwargs)

    @step("Получение списка заказов")
    def get_order(self, **kwargs):
        return requests.get(f"{BASE_URL}/api/v1/orders", **kwargs)
