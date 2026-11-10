# Biblioteca estándar

## Índice

1. [Módulo random](#1-módulo-random)

---

## 1. Módulo random

Un **módulo de la biblioteca estándar** que genera valores **pseudoaleatorios**. Hay que importarlo: `import random`.

**Funciones del módulo `random`:**

| Firma | Devuelve | Ejemplo (cambia en cada ejecución) |
|---|---|---|
| `random.choice(seq: list \| tuple \| str)` | un elemento al azar de `seq` | `random.choice(["a", "b", "c"])` → `"b"` |
| `random.sample(population: list \| tuple \| str, k: int) -> list` | lista con `k` elementos de `population`, sin repetir posición | `random.sample(["a", "b", "c"], 2)` → `["c", "a"]` |
| `random.randint(a: int, b: int) -> int` | un `int` entre `a` y `b` | `random.randint(1, 6)` → `4` |

Doc: [random](https://docs.python.org/3/library/random.html)

> `randint(a, b)` INCLUYE LOS DOS EXTREMOS; `range(a, b)` NO INCLUYE `b`.

> UN SET O UN DICT NO VALEN EN `choice` NI EN `sample`: NO TIENEN POSICIÓN → `TypeError`.
