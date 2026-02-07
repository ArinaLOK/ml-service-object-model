from uuid import UUID, uuid4
from datetime import datetime
from decimal import Decimal
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    PREDICTION_PAYMENT = "PREDICTION_PAYMENT"


class Transaction:
    def __init__(self,transiction_type: TransactionType, amount: Decimal):
        self._id: UUID = uuid4()
        self._type: TransactionType = transiction_type
        self._amount: Decimal = amount
        self._created_at: datetime = datetime.utcnow()

    @property
    def id(self) -> UUID:
        return self._id
    
    @property
    def amount(self) -> Decimal:
        return self._amount
    
    @property
    def type(self) -> TransactionType:
        return self._type
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    class InsufficientFundsError(Exception):
        pass
        
    def getAmount(self) -> Decimal:
        return self._amount
