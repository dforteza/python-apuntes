from b import saluda_b


def saluda_a() -> str:
    return "A"


def presenta() -> str:
    return "A presenta a " + saluda_b()
