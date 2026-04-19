import allure


class TestGetOrder:
    @allure.title("Проверяем, что orders это список")
    @allure.description("Проверка, что в тело ответа возвращается список заказов.")
    def test_get_order(self, stocks_api):
        response = stocks_api.get_order()

        assert "orders" in response.json()
        assert type(response.json()["orders"]) is list
        assert response.status_code == 200
