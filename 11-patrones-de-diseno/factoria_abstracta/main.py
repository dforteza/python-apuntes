from vivero import PlantFactory, FlowerFactory, TreeFactory

### 5- CLIENTE
def show(factory: PlantFactory) -> None: # factory = FlowerFactory()
    small = factory.create_small()      # no sabe qué clase recibe
    big = factory.create_big()
    print(small.grow())
    print(big.grow())


if __name__ == "__main__":
    show(FlowerFactory())
    # Daisy opens its petals
    # Rose grows thorns
    show(TreeFactory())
    # Bonsai grows slowly
    # Oak reaches the sky
