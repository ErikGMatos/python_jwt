# Bank Account Management System

This project is a Flask-based web application for managing bank accounts, including user registration, login, and balance editing.

The Bank Account Management System provides a secure and efficient way to handle basic banking operations through a RESTful API. It utilizes JSON Web Tokens (JWT) for authentication and authorization, ensuring that only authorized users can access and modify account information.

The system is built with a modular architecture, separating concerns into controllers, models, and views. This design promotes maintainability and scalability, allowing for easy extension of functionality as needed. The application uses SQLite as its database, providing a lightweight and portable solution for data storage.

Key features of the Bank Account Management System include:

- User registration with secure password hashing
- User login with JWT token generation
- Balance editing for authenticated users
- Error handling and standardized HTTP responses
- Middleware for JWT verification
- Modular and extensible architecture

This system is ideal for developers looking to implement basic banking functionality in their applications or as a starting point for more complex financial systems.

## Repository Structure

```
.
├── example_jwt.py
├── init
│   └── schema.sql
├── run.py
└── src
    ├── configs
    │   └── jwt_configs.py
    ├── controllers
    │   ├── balance_editor.py
    │   ├── interfaces
    │   │   ├── balance_editor.py
    │   │   ├── login_creator.py
    │   │   └── user_register.py
    │   ├── login_creator.py
    │   └── user_register.py
    ├── drivers
    │   ├── jwt_handler.py
    │   └── password_handler.py
    ├── errors
    │   ├── error_handler.py
    │   └── types
    │       ├── http_bad_request.py
    │       ├── http_not_found.py
    │       └── http_unauthorized.py
    ├── main
    │   ├── composer
    │   │   ├── balance_editor_composer.py
    │   │   ├── login_creator_composer.py
    │   │   └── user_register_composer.py
    │   ├── middlewares
    │   │   └── auth_jwt.py
    │   ├── routes
    │   │   └── bank_account_routes.py
    │   └── server
    │       └── server.py
    ├── models
    │   ├── interfaces
    │   │   └── user_repository.py
    │   ├── repositories
    │   │   └── user_repository.py
    │   └── settings
    │       └── db_connection_handler.py
    └── views
        ├── balance_editor_view.py
        ├── http_types
        │   ├── http_request.py
        │   └── http_response.py
        ├── interfaces
        │   └── view_interface.py
        ├── login_creator_view.py
        └── user_register_view.py
```

## Usage Instructions

### Installation

1. Ensure you have Python 3.7+ installed on your system.
2. Clone the repository:
   ```
   git clone <repository_url>
   cd bank-account-management-system
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. Set up environment variables:
   - `KEY`: Secret key for JWT encoding/decoding
   - `ALGORITHM`: Algorithm for JWT encoding/decoding (e.g., "HS256")
   - `JWT_HOURS`: JWT token expiration time in hours

2. Initialize the SQLite database:
   ```
   sqlite3 storage.db < init/schema.sql
   ```

### Running the Application

To start the server, run:

```
python run.py
```

The server will start on `http://0.0.0.0:3000` by default.

### API Endpoints

1. User Registration:
   - URL: `/bank/registry`
   - Method: POST
   - Body: `{ "username": "string", "password": "string" }`
   - Response: `{ "type": "User", "count": 1, "username": "string" }`

2. User Login:
   - URL: `/bank/login`
   - Method: POST
   - Body: `{ "username": "string", "password": "string" }`
   - Response: `{ "access": true, "token": "string", "username": "string" }`

3. Edit Balance:
   - URL: `/bank/balance/<user_id>`
   - Method: POST
   - Headers: 
     - `Authorization: Bearer <token>`
     - `uid: <user_id>`
   - Body: `{ "new_balance": float }`
   - Response: `{ "user_id": int, "username": "string", "balance": float }`

### Error Handling

The application uses custom error classes to handle different types of errors:

- `HttpBadRequestError`: 400 Bad Request
- `HttpUnauthorizedError`: 401 Unauthorized
- `HttpNotFoundError`: 404 Not Found

These errors are caught and formatted by the `error_handler.py` module to provide consistent error responses.

## Data Flow

The request data flow through the application follows these steps:

1. The client sends an HTTP request to one of the API endpoints.
2. The request is received by the Flask server (`server.py`).
3. The appropriate route handler in `bank_account_routes.py` processes the request.
4. For protected routes, the `auth_jwt_verify()` middleware checks the JWT token.
5. The route handler creates an `HttpRequest` object and passes it to the corresponding view.
6. The view validates the input and calls the appropriate controller method.
7. The controller interacts with the `UserRepository` to perform database operations.
8. The result is passed back through the layers: controller -> view -> route handler.
9. The route handler returns an `HttpResponse` object, which is converted to a JSON response by Flask.

```
Client <-> Flask Server <-> Routes <-> Views <-> Controllers <-> UserRepository <-> SQLite Database
                              ^
                              |
                        JWT Middleware
```

## Testing

To run the tests, execute:

```
python -m unittest discover -v
```

This will run all the test files in the project, including controller tests, repository tests, and view tests.

## Troubleshooting

1. Database Connection Issues:
   - Ensure the `storage.db` file exists in the root directory.
   - Check file permissions for the database file.
   - Verify the `db_connection_handler.py` is using the correct connection string.

2. JWT Authentication Failures:
   - Confirm that the environment variables (`KEY`, `ALGORITHM`, `JWT_HOURS`) are set correctly.
   - Check that the token is being sent in the `Authorization` header with the "Bearer" prefix.
   - Verify that the `uid` in the header matches the user ID in the token payload.

3. Password Hashing Issues:
   - Ensure the `bcrypt` library is installed correctly.
   - Check that the `PasswwordHandler` class is being used consistently for both hashing and verification.

For more detailed debugging:

1. Enable debug mode in Flask by setting `debug=True` in `run.py`.
2. Check the console output for detailed error messages and stack traces.
3. Use logging statements in critical parts of the code to track the flow of execution.

If issues persist, review the relevant test files (e.g., `user_repository_test.py`, `login_creator_test.py`) for expected behavior and input/output examples.