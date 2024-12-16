
from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInteface


class BalanceEditorView(ViewInteface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        user_id = http_request.params.get("user_id")
        headers_user_id = http_request.headers.get("uid")

        self.__validate_inputs(new_balance, user_id, headers_user_id)
        response = self.__controller.edit(
            new_balance=new_balance, user_id=user_id)
        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_inputs(self, new_balance: any, user_id: any, headers_user_id: any) -> None:
        if (
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
            or int(headers_user_id) != int(user_id)
            or not isinstance(user_id, str)
        ):
            raise Exception("Invalid inputs")
