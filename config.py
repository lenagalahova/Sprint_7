BASE_URL = "https://qa-scooter.praktikum-services.ru"

COURIER_ENDPOINT = "/api/v1/courier"
COURIER_LOGIN_ENDPOINT = "/api/v1/courier/login"
ORDERS_ENDPOINT = "/api/v1/orders"


class ErrorMessege:
    NOTENOUGHT_DATA_FOR_LOGIN = "Недостаточно данных для входа"
    LOGIN_ALREADY_USED = "Этот логин уже используется. Попробуйте другой."
    INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    BUG_API = "БАГ API: ожидается 400, но приходит 504"
