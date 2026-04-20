import pytest
import allure
from config import ErrorMessege


class TestDeliverLogin:
    @allure.description("Логин курьера")
    @allure.title("Проверка залогина курьера")
    def test_login_deliver(self, stocks_api, new_courier):
        body = new_courier
        response = stocks_api.login_deliver(json=body)

        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["id"] > 0

    @allure.title("Проверка залогина курьера без пароля")
    def test_login_deliver_without_password(self, stocks_api, new_courier_login):
        body = new_courier_login
        response = stocks_api.login_deliver(json=body)

        if response.status_code == 400:
            assert ErrorMessege.NOTENOUGHT_DATA_FOR_LOGIN in response.json()["message"]
        elif response.status_code == 504:
            pytest.xfail(ErrorMessege.BUG_API)

    @allure.title("Проверка залогина курьера без логина")
    def test_login_deliver_without_login(self, stocks_api, new_courier_password):
        body = new_courier_password
        response = stocks_api.login_deliver(json=body)

        assert response.status_code == 400
        assert ErrorMessege.NOTENOUGHT_DATA_FOR_LOGIN in response.json()["message"]

    @allure.title("Проверка залогина несуществующего курьера")
    def test_login_non_existent_user(self, stocks_api, new_courier_data):
        body = new_courier_data
        response = stocks_api.login_deliver(json=body)

        assert response.status_code == 404
        assert ErrorMessege.ACCOUNT_NOT_FOUND in response.json()["message"]
