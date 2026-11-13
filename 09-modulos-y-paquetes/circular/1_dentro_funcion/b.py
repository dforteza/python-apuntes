def saluda_b() -> str:
    from a import saluda_a
    return "B, amigo de " + saluda_a()
