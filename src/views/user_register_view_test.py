import pytest

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.user_register_view import UserRegisterView


class MockController:
    def registry(self, _username, _password):
        return {"alguma": "coisa"}


def test_handle_user_register():
    body = {
        "username": "MyUsername",
        "password": "MyPassword",
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_reguister_view = UserRegisterView(mock_controller)

    response = user_reguister_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == {"data": {"alguma": "coisa"}}


def test_handle_user_register_with_validation_error():
    body = {
        "password": "MyPassword",
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_reguister_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_reguister_view.handle(request)
