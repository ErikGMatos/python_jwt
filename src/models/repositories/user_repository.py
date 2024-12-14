from sqlite3 import Connection

from src.models.interfaces.user_repository import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO users 
                (username, password, balance)
            VALUES (?, ?,  ?);
            ''', (username, password, 0))
        self.__conn.commit()

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            UPDATE users 
            SET balance = ?
            WHERE id = ?
            ''', (new_balance, user_id))
        self.__conn.commit()

    def get_user_by_username(self, usernamme: str) -> tuple[int, str, str]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT id, username, password
            FROM users
            WHERE username = ?
            ''', (usernamme,))
        user = cursor.fetchone()
        return user
