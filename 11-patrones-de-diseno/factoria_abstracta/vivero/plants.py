### 2- PRODUCTOS CONCRETOS


# Import de PRODUCTO ABSTRACTO
from .plant import Plant


class Daisy(Plant):
    def __init__(self) -> None:
        super().__init__("Daisy")

    def grow(self) -> str:
        return (f"{self.name} opens its petals")


class Rose(Plant):
    def __init__(self) -> None:
        super().__init__("Rose")

    def grow(self) -> str:
        return (f"{self.name} grows thorns")


class Bonsai(Plant):
    def __init__(self) -> None:
        super().__init__("Bonsai")

    def grow(self) -> str:
        return (f"{self.name} grows slowly")


class Oak(Plant):
    def __init__(self) -> None:
        super().__init__("Oak")

    def grow(self) -> str:
        return (f"{self.name} reaches the sky")
