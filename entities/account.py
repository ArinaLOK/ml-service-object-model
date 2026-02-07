from decimal import Decimal
from typing import List
from .transaction import Transaction, TransactionType, InsufficientFundsError

class Account:
    def __init__(self):
        self._balance: Decimal = Decimal("0.00")
        self._transactions: List[Transaction] = []

    @property
    def balance(self) -> Decimal:
        return self._balance

    @property
    def transactions(self) -> List[Transaction]:
        return self._transactions

    def deposit(self, amount: Decimal) -> Transaction:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        transaction = Transaction(TransactionType.DEPOSIT, amount)
        self._transactions.append(transaction)
        return transaction

    def withdraw(self, amount: Decimal) -> Transaction:
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds")
        self._balance -= amount
        transaction = Transaction(TransactionType.WITHDRAW, amount)
        self._transactions.append(transaction)
        return transaction

    def pay_prediction(self, amount: Decimal) -> Transaction:
        if amount <= 0:
            raise ValueError("Payment must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds")
        self._balance -= amount
        transaction = Transaction(TransactionType.PREDICTION_PAYMENT, amount)
        self._transactions.append(transaction)
        return transaction
