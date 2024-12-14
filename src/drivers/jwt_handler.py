from datetime import datetime, timedelta, timezone

import jwt


class JwtHandler:
    def create_jwt_token(self, body: dict = None) -> str:
        if body is None:
            body = {}
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
                **body
            },
            key="minhaChave",
            algorithm="HS256"
        )
        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            token,
            key="minhaChave",
            algorithms=["HS256"])

        return token_information
