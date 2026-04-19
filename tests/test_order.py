import pytest
from helpers.data_oder import OrderData
import allure


class TestOrder:
    @allure.title("Проверка выбора цветов")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK, GREY"]])
    def test_create_oder(self, stocks_api, colors):
        body = OrderData.BASE_ORDER.copy()
        if colors:
            body["color"] = colors

        response = stocks_api.create_order(json=body)

        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"] > 0

    @allure.title("Проверка, что цвет не указан")
    def test_create_oder_without_color(self, stocks_api):
        body = OrderData.BASE_ORDER
        response = stocks_api.create_order(json=body)

        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"] > 0
