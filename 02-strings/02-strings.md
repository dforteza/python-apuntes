# Strings

Ejemplos: [02-strings.py](02-strings.py) (mismos números de sección)

## Índice

1. [Definición string](#1-definición-string)
2. [Mayúsculas y minúsculas](#2-mayúsculas-y-minúsculas)
3. [Buscar y comprobar](#3-buscar-y-comprobar)
4. [Limpiar, reemplazar, dividir y unir](#4-limpiar-reemplazar-dividir-y-unir)
5. [Formatear](#5-formatear)

---

## 1. Definición string

Secuencia de caracteres entre comillas. Ordenado e inmutable, como una tupla.

**Crear:**

| Forma | Resultado |
|---|---|
| `"hola"` o `'hola'` | string (son iguales) |
| `""` | string vacío |
| `"""texto"""` | string que puede ocupar varias líneas |
| `str(42)` | `"42"` |

**Leer:** ver [operaciones comunes](../03-colecciones/03-colecciones.md#2-operaciones-comunes). Además, `in` busca trozos de texto: `"th" in "python"` → `True`.

**Actualizar:** no se puede; `x[0] = "C"` da `TypeError`. Hay que crear otro: `x = "C" + x[1:]`.

Doc: [strings](https://docs.python.org/3/tutorial/introduction.html#text) · [métodos](https://docs.python.org/3/library/stdtypes.html#string-methods)

> NINGÚN MÉTODO CAMBIA EL STRING, TODOS DEVUELVEN UNO NUEVO: `x.upper()` SOLO NO HACE NADA, HAY QUE GUARDARLO: `x = x.upper()`.

## 2. Mayúsculas y minúsculas

Con `x = "hola MUNDO"`:

| Forma | Resultado | Qué hace |
|---|---|---|
| `x.upper()` | `"HOLA MUNDO"` | todo en mayúsculas |
| `x.lower()` | `"hola mundo"` | todo en minúsculas |
| `x.capitalize()` | `"Hola mundo"` | la primera en mayúscula y el resto en minúsculas |
| `x.title()` | `"Hola Mundo"` | la primera de cada palabra en mayúscula |

Doc: [upper](https://docs.python.org/3/library/stdtypes.html#str.upper) · [lower](https://docs.python.org/3/library/stdtypes.html#str.lower) · [capitalize](https://docs.python.org/3/library/stdtypes.html#str.capitalize) · [title](https://docs.python.org/3/library/stdtypes.html#str.title)

> PARA COMPARAR SIN DISTINGUIR MAYÚSCULAS, PASA LOS DOS A MINÚSCULAS: `a.lower() == b.lower()`.

## 3. Buscar y comprobar

Con `x = "python"`:

| Forma | Resultado | Qué hace |
|---|---|---|
| `x.startswith("py")` | `True` | comprueba cómo empieza |
| `x.endswith("on")` | `True` | comprueba cómo termina |
| `x.find("th")` | `2` | posición del trozo (`-1` si no está) |
| `x.count("o")` | `1` | veces que aparece |

| Forma | `True` si todo son... | Ejemplo |
|---|---|---|
| `x.isdigit()` | dígitos | `"42".isdigit()` → `True` |
| `x.isalpha()` | letras | `"abc".isalpha()` → `True` |
| `x.isupper()` | mayúsculas | `"ABC".isupper()` → `True` |
| `x.islower()` | minúsculas | `"abc".islower()` → `True` |

Doc: [find](https://docs.python.org/3/library/stdtypes.html#str.find) · [isdigit](https://docs.python.org/3/library/stdtypes.html#str.isdigit)

> `"-5".isdigit()` DA `False` PORQUE EL `-` NO ES UN DÍGITO: PARA VALIDAR NÚMEROS, USA `int()` CON `try`.

## 4. Limpiar, reemplazar, dividir y unir

| Forma | Resultado | Qué hace |
|---|---|---|
| `"  hola  ".strip()` | `"hola"` | quita los espacios de los dos extremos |
| `"  hola  ".lstrip()` | `"hola  "` | solo los de la izquierda |
| `"  hola  ".rstrip()` | `"  hola"` | solo los de la derecha |
| `"hola\n".rstrip("\n")` | `"hola"` | quita los caracteres que indiques |
| `"hola".replace("o", "a")` | `"hala"` | cambia un trozo por otro |
| `"a b  c".split()` | `["a", "b", "c"]` | divide por espacios |
| `"a:b".split(":")` | `["a", "b"]` | divide por lo que indiques |
| `"a\nb\n".split("\n")` | `["a", "b", ""]` | divide por `\n` y deja un `""` al final |
| `"a\nb\n".splitlines()` | `["a", "b"]` | divide por líneas, sin el `""` del final |
| `", ".join(["a", "b"])` | `"a, b"` | une una lista con ese separador |

Doc: [strip](https://docs.python.org/3/library/stdtypes.html#str.strip) · [replace](https://docs.python.org/3/library/stdtypes.html#str.replace) · [split](https://docs.python.org/3/library/stdtypes.html#str.split) · [splitlines](https://docs.python.org/3/library/stdtypes.html#str.splitlines) · [join](https://docs.python.org/3/library/stdtypes.html#str.join)

> `join` SE LLAMA SOBRE EL SEPARADOR Y SOLO ADMITE `str`: `", ".join([1, 2])` DA `TypeError`.

## 5. Formatear

Con `n = "Ana"` y `p = 3.14159`:

| Forma | Resultado | Qué hace |
|---|---|---|
| `"Hola " + n` | `"Hola Ana"` | une strings |
| `"ab" * 2` | `"abab"` | repite |
| `f"Hola {n}"` | `"Hola Ana"` | mete el valor entre llaves (f-string) |
| `f"{2 + 3}"` | `"5"` | también admite expresiones |
| `f"{p:.2f}"` | `"3.14"` | con 2 decimales |

Doc: [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) · [format](https://docs.python.org/3/library/stdtypes.html#str.format)

> `+` SOLO UNE STRINGS: `"Edad: " + 42` DA `TypeError`. USA UNA F-STRING: `f"Edad: {42}"`.
