from uuid import UUID, uuid4
from datetime import datetime
from decimal import Decimal

# Базовый класс для моделей(неуверена, может сделаю только под одну конкретную модель)
class MLModel:
    def __init__(self, name: str, version: str, cost_per_prediction: Decimal, weights_path: str):
        self._id: UUID = uuid4()
        self._name: str = name
        self._version: str = version
        self._cost_per_prediction: Decimal = cost_per_prediction
        self._weights_path: str = weights_path
        self._created_at: datetime = datetime.utcnow()

    # свойства для доступа
    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def cost_per_prediction(self) -> Decimal:
        return self._cost_per_prediction

    @property
    def weights_path(self) -> str:
        return self._weights_path

    @property
    def created_at(self) -> datetime:
        return self._created_at

    # метод predict (пока без реализации)
    def predict(self, input_data: bytes):
        raise NotImplementedError("Prediction not implemented yet")



    
