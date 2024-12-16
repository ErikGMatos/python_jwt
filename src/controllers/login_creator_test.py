

import pytest

from src.controllers.login_creator import LoginCreatorController
from src.drivers.password_handler import PasswwordHandler

USERNAME = "meuUsername"
PASSWORD = "minhaSenha"
HASHED_PASSWORD = PasswwordHandler().encrypt_password(PASSWORD)


class MockUserRepository:
    def get_user_by_username(self, mock_username):
        return (10, mock_username, HASHED_PASSWORD)


def test_create():
    login_creator = LoginCreatorController(MockUserRepository())
    response = login_creator.create(USERNAME, PASSWORD)

    assert response["access"] is True
    assert response["username"] == USERNAME
    assert response["token"] is not None


def test_create_with_wrong_password():
    login_creator = LoginCreatorController(MockUserRepository())

    with pytest.raises(Exception):
        login_creator.create(USERNAME, "outraSenha")
