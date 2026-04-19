import allure


class TestDeliver:
    @allure.title("Создание нового курьера")
    @allure.description("Создание курьера")
    def test_create_new_deliver(self, stocks_api, new_courier_data):
        body = new_courier_data
        response = stocks_api.create_new_deliver(json=body)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Создание двух одинаковых курьеров")
    def test_create_new_same_deliver(self, stocks_api, new_courier_data):
        body = new_courier_data

        response_1 = stocks_api.create_new_deliver(json=body)
        assert response_1.status_code == 201
        assert response_1.json() == {"ok": True}

        response_2 = stocks_api.create_new_deliver(json=body)

        assert response_2.status_code == 409
        assert (
            response_2.json()["message"]
            == "Этот логин уже используется. Попробуйте другой."
        )

    @allure.title("Создание курьера без логина")
    def test_create_new_deliver_without_login(
        self, stocks_api, new_courier_data_without_login
    ):
        body = new_courier_data_without_login
        response = stocks_api.create_new_deliver(json=body)

        assert response.status_code == 400
        assert (
            response.json()["message"]
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Создание курьера без пароля")
    def test_create_new_deliver_without_password(
        self, stocks_api, new_courier_data_without_pass
    ):
        body = new_courier_data_without_pass
        response = stocks_api.create_new_deliver(json=body)

        assert response.status_code == 400
        assert (
            response.json()["message"]
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Создание курьера без имени")
    def test_create_new_deliver_without_firstname(
        self, stocks_api, new_courier_data_without_firstname
    ):
        body = new_courier_data_without_firstname
        response = stocks_api.create_new_deliver(json=body)

        assert response.status_code == 201
        assert response.json() == {"ok": True}
