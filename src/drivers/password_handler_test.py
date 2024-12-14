from src.drivers.password_handler import PasswwordHandler


def test_encrypt():
    minha_senha = '123RocketENois'
    password_handler = PasswwordHandler()

    hashed_password = password_handler.encrypt_password(minha_senha)

    password_checked = password_handler.check_password(
        minha_senha, hashed_password)

    assert password_checked is True
