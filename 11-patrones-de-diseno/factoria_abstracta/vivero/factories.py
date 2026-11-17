from abc import ABC, abstractmethod
from .plant import Plant
from .plants import Daisy, Rose, Bonsai, Oak


### ¡¡¡FACTORIAS TRABAJAN CON ABSTRACTOS NO CONCRETOS!!!
### 3- FACTORIA ABSTRACTA
class PlantFactory(ABC):
    @abstractmethod
    def create_small(self) -> Plant:
        pass

    @abstractmethod
    def create_big(self) -> Plant:
        pass

### 4- FACTORIA
class FlowerFactory(PlantFactory):
    def create_small(self) -> Plant:
        return (Daisy())

    def create_big(self) -> Plant:
        return (Rose())


class TreeFactory(PlantFactory):
    def create_small(self) -> Plant:
        return (Bonsai())

    def create_big(self) -> Plant:
        return (Oak())
