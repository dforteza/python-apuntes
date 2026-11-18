# Biblioteca estándar

## Índice

1. [Módulo random](#1-módulo-random)
2. [Módulo sys](#2-módulo-sys)
3. [Módulo os](#3-módulo-os)
4. [Módulo enum](#4-módulo-enum)

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

## 2. Módulo sys

Un **módulo de la biblioteca estándar** que da acceso a **datos del intérprete de Python que se está ejecutando**. Hay que importarlo: `import sys`.

**Atributos del módulo `sys`** (son **variables, no funciones**: van sin paréntesis):

| Atributo | Tipo | Qué contiene | Ejemplo dentro del venv `lab_env` |
|---|---|---|---|
| `sys.executable` | `str` | ruta del intérprete que ejecuta el programa | `"/home/user/lab_env/bin/python3"` |
| `sys.prefix` | `str` | carpeta del entorno activo | `"/home/user/lab_env"` |
| `sys.base_prefix` | `str` | carpeta del Python instalado en el sistema | `"/usr"` |
| `sys.path` | `list[str]` | carpetas donde `import` busca los módulos, en orden | `sys.path.append(".")` añade una |

Ya vistos: detectar un venv → [tema 09 §1](../09-modulos-y-paquetes/09-modulos-y-paquetes.md#1-entornos-virtuales) · `sys.argv` → [tema 03 §3](../03-colecciones/03-colecciones.md#3-listas) · `sys.stdin` / `stdout` / `stderr` → [tema 07 §7](../07-ficheros-y-flujos/07-ficheros-y-flujos.md#7-stdin-stdout-stderr-y-flush)

Teoría: [ut6_modulos_librerias.pdf §4](https://github.com/dforteza/PythonBasics/blob/main/docs/teoria/ut6_modulos_librerias.pdf) (`sys.path`) · [ut5_entrada_salida.pdf](https://github.com/dforteza/PythonBasics/blob/main/docs/teoria/ut5_entrada_salida.pdf) (`argv` y flujos)

Doc: [sys](https://docs.python.org/3/library/sys.html)

> `sys.executable` ES EL **FICHERO** DEL INTÉRPRETE; `sys.prefix` ES LA **CARPETA** DEL ENTORNO.

## 3. Módulo os

Un **módulo de la biblioteca estándar** para trabajar con el **sistema operativo**: variables de entorno, rutas, ficheros... Hay que importarlo: `import os`.

**Funciones del módulo `os`:**

| Firma | Devuelve | Ejemplo |
|---|---|---|
| `os.getenv(key: str, default: str \| None = None) -> str \| None` | el valor de la variable de entorno `key`, o `default` si no existe | `os.getenv("HOME")` → `"/home/user"` |
| `os.path.basename(path: str) -> str` | la última parte de la ruta | `os.path.basename("/home/user/lab_env")` → `"lab_env"` |
| `os.path.dirname(path: str) -> str` | la ruta sin la última parte | `os.path.dirname("/home/user/lab_env")` → `"/home/user"` |
| `os.path.join(*paths: str) -> str` | une las partes con `/` | `os.path.join("logs", "2026")` → `"logs/2026"` |

Ya visto: `.env` y variables de entorno → [tema 09 §4](../09-modulos-y-paquetes/09-modulos-y-paquetes.md#4-variables-de-entorno-y-env)

Teoría: [ut5_rutas_directorios.pdf §2.1](https://github.com/dforteza/PythonBasics/blob/main/docs/teoria/ut5_rutas_directorios.pdf) (`os.path`)

Doc: [os.getenv](https://docs.python.org/3/library/os.html#os.getenv) · [os.path](https://docs.python.org/3/library/os.path.html)

> `os.path` SOLO TRABAJA CON EL **TEXTO** DE LA RUTA: NO COMPRUEBA QUE EXISTA.

## 4. Módulo enum

Un **módulo de la biblioteca estándar** para crear **ENUMERACIONES**. Hay que importarlo: `from enum import Enum`.

- Una **ENUMERACIÓN** (`Enum`) es una **CLASE CON UN CONJUNTO CERRADO DE VALORES POSIBLES**, cada uno con nombre. Se usa cuando un dato **SOLO PUEDE SER UNA DE UNAS POCAS OPCIONES** (p. ej. un color, un rango, un tipo).
- Cada opción es un **MIEMBRO**: tiene un **nombre** (`RED`) y un **valor** (`"red"`).

```python
from enum import Enum


class Color(Enum):
    RED = "red"
    BLUE = "blue"
```

| Expresión | Devuelve | Ejemplo |
|---|---|---|
| `Color.RED` | el **miembro** | `Color.RED` |
| `Color.RED.value` | su **valor** | `"red"` |
| `Color.RED.name` | su **nombre** | `"RED"` |
| `Color("red")` | el miembro **a partir de su valor** | `Color.RED` |
| `Color("green")` | valor que no existe | `ValueError` |

> **PARA MOSTRARLO, USA `.value`:** `print(Color.RED)` → `Color.RED`; `print(Color.RED.value)` → `red`.

- **Comparar:** `color == Color.RED` (con el miembro, no con `"red"`).

Doc: [enum](https://docs.python.org/3/library/enum.html)
