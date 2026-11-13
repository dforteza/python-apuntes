from b import saluda_b
from c import saluda_a


def presenta() -> str:
    return saluda_a() + " presenta a " + saluda_b()
