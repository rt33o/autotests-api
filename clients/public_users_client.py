from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Структура запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users для операций, не требующих авторизации.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание нового пользователя.

        :param request: Словарь с email, password, firstName, lastName и middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
