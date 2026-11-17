### 1- PRODUCTO ABSTRACTO

# Import ABC - abstractmethod
from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def grow(self) -> str:
        pass
