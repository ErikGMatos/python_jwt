from src.drivers.password_handler import PasswwordHandler
from src.models.interfaces.user_repository import UserRepositoryInterface


class UserRegisterController:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__password_handler = PasswwordHandler()

    def registry(self, username: str, password: str) -> dict:
        hashed_password = self.__create_hash_password(password)
        self.__registry_new_user(username, hashed_password)
        return self.format_response(username)

    def __create_hash_password(self, password: str) -> str:
        hashed_password = self.__password_handler.encrypt_password(password)
        return hashed_password

    def __registry_new_user(self, username: str, hashed_password: str) -> None:
        self.__user_repository.registry_user(username, hashed_password)

    def format_response(self, username) -> dict:
        return {
            "type": "User",
            "count": 1,
            "username": username
        }
