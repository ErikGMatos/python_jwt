from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.composer.balance_editor_composer import balance_editor_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.user_register_composer import user_register_composer
from src.main.middlewares.auth_jwt import auth_jwt_verify
from src.views.http_types.http_request import HttpRequest

bank_routes_bp = Blueprint('bank_routes', __name__)


@bank_routes_bp.route('/bank/registry', methods=['POST'])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route('/bank/login', methods=['POST'])
def create_login():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route('/bank/balance/<user_id>', methods=['PATCH'])
def edit_balance(user_id):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json,
            params={
                'user_id': user_id
            },
            token_infos=token_information,
            headers=request.headers
        )
        http_response = balance_editor_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
