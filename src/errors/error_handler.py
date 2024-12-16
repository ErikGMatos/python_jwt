from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_unauthorized import HttpUnauthorizedError
from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpUnauthorizedError, HttpNotFoundError)):
        return HttpResponse(
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            },
            status_code=error.status_code,
        )

    return HttpResponse(
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        },
        status_code=500,
    )
