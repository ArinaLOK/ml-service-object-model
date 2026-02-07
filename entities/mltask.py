from uuid import uuid4, UUID
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

# Статус задачи
class TaskStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    DONE = "DONE"
    FAILED = "FAILED"


# Результат предсказания
class PredictionResult:
    def __init__(self, output_data: bytes):
        self._output_data: bytes = output_data
        self._created_at: datetime = datetime.utcnow()

    @property
    def output_data(self) -> bytes:
        return self._output_data

    @property
    def created_at(self) -> datetime:
        return self._created_at

# ML Task 
class MLTask:
    def __init__(
        self, 
        user_id: UUID, 
        model_id: UUID, 
        input_data: bytes, 
        cost: Decimal
    ):
        self._id: UUID = uuid4()
        self._user_id: UUID = user_id
        self._model_id: UUID = model_id
        self._input_data: bytes = input_data
        self._status: TaskStatus = TaskStatus.PENDING
        self._result: Optional[PredictionResult] = None
        self._created_at: datetime = datetime.utcnow()
        self._completed_at: Optional[datetime] = None
        self._cost: Decimal = cost

    # Свойства
    @property
    def id(self) -> UUID:
        return self._id

    @property
    def user_id(self) -> UUID:
        return self._user_id

    @property
    def model_id(self) -> UUID:
        return self._model_id

    @property
    def input_data(self) -> bytes:
        return self._input_data

    @property
    def status(self) -> TaskStatus:
        return self._status

    @property
    def result(self) -> Optional[PredictionResult]:
        return self._result

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def completed_at(self) -> Optional[datetime]:
        return self._completed_at

    @property
    def cost(self) -> Decimal:
        return self._cost


    # Методы управления задачей
    def start(self):
        self._status = TaskStatus.RUNNING

    def complete(self, result: PredictionResult):
        self._status = TaskStatus.DONE
        self._result = result
        self._completed_at = datetime.utcnow()

    def fail(self):
        self._status = TaskStatus.FAILED
        self._completed_at = datetime.utcnow()