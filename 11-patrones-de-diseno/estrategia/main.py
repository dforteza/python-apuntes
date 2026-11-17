from abc import ABC, abstractmethod
from factoria_abstracta.vivero.plant import Plant
from factoria_abstracta.vivero.plants import Rose, Oak

# === 1- Estrategia ABC ===
class CareStrategy(ABC):
    @abstractmethod
    def care(self, plant : Plant) -> None:
        pass

# === 2- Estrategias
class WaterStrategy(CareStrategy):
    def care(self, plant : Plant) -> None:
        print(f"Watering {plant.name}")

class PruneStrategy(CareStrategy):
    def care(self, plant : Plant) -> None:
        print(f"Pruning {plant.name}")

# === 3- Contexto
def garden_day(plant : Plant, strategy : CareStrategy):
    strategy.care(plant)


if __name__ == "__main__":
    print("=== ROSE ===")
    garden_day(Rose(), WaterStrategy())
    print("=== OAK ===")
    garden_day(Oak(), PruneStrategy())
