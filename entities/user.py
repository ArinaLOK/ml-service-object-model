from uuid import uuid4
from .account import Account

class User:
    def __init__(self, email: str, role: str):
        self._id: str = str(uuid4())
        self._email: str = email
        self._role: str = role
        self._account: Account = Account()

    @property
    def id(self) -> str:
        return self._id

    @property
    def email(self) -> str:
        return self._email

    @property
    def role(self) -> str:
        return self._role

    @property
    def account(self) -> Account:
        return self._account
