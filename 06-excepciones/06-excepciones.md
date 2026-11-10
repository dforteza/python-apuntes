# Excepciones

Ejemplos: [06-excepciones.py](06-excepciones.py) (mismos números de sección)

## Índice

1. [Definición excepción](#1-definición-excepción)
2. [raise](#2-raise)
3. [try y except](#3-try-y-except)
4. [Varios except](#4-varios-except)
5. [Excepciones propias](#5-excepciones-propias)
6. [finally](#6-finally)

---

## 1. Definición excepción

Una excepción es un **objeto** que representa un error ocurrido durante la ejecución.

- **Lanzar** (`raise`): hacer saltar el error.
- **Capturar** (`except`): recoger el error y decidir qué hacer con él.
- **Subir**: si la función donde salta el error no lo captura, pasa a la función que la llamó.

| Excepción | Cuándo | Ejemplo |
|---|---|---|
| `ValueError` | tipo correcto, valor incorrecto | `int("abc")` |
| `ZeroDivisionError` | dividir entre cero | `10 / 0` |
| `FileNotFoundError` | el fichero no existe | `open("no_existe.txt")` |
| `TypeError` | tipo incorrecto | `"abc" + 1` |

Doc: [excepciones](https://docs.python.org/3/tutorial/errors.html#exceptions) · [lista completa](https://docs.python.org/3/library/exceptions.html)

> SI NADIE CAPTURA EL ERROR, EL PROGRAMA TERMINA Y MUESTRA EL TRACEBACK.

## 2. raise

Sintaxis: `raise ValueError("mensaje")`

| Parte | Qué hace |
|---|---|
| `ValueError("mensaje")` | **crea** el objeto con el mensaje |
| `raise` | **lanza** ese objeto |

Doc: [raise](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)

> CREAR NO ES LANZAR: SIN `raise`, EL OBJETO SE CREA Y NO PASA NADA. Lo que hay después del `raise` no se ejecuta.

## 3. try y except

Sintaxis:

```python
try:
    ...
except ValueError as e:
    ...
```

| Qué pasa dentro del `try` | Resultado |
|---|---|
| no hay error | se salta el `except` |
| error de ese tipo | el resto del `try` no se ejecuta; entra en el `except` y el programa sigue |
| error de otro tipo | no se captura: sigue subiendo |

`e` es el **mismo objeto** que se lanzó: `print(e)` muestra su mensaje.

Doc: [try y except](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

## 4. Varios except

| Forma | Cuándo |
|---|---|
| un `except` por tipo | cada error se trata de forma distinta |
| `except (ValueError, TypeError) as e:` | varios errores se tratan igual (con paréntesis) |

Doc: [varios except](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

> SE COMPRUEBAN DE ARRIBA ABAJO Y SOLO SE EJECUTA EL PRIMERO QUE ENCAJA.

## 5. Excepciones propias

Son clases tuyas que heredan de `Exception`, para los errores de tu programa que no encajan en uno de Python.

```python
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass
```

| Captura | Qué recoge |
|---|---|
| `except PlantError` | solo `PlantError` |
| `except GardenError` | `GardenError` y `PlantError` |

Doc: [excepciones propias](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions)

> EL `except` DEL PADRE TAMBIÉN RECOGE A LOS HIJOS: PON PRIMERO EL HIJO, O EL SUYO NO SE EJECUTARÁ NUNCA.

## 6. finally

Bloque que se ejecuta siempre al salir del `try`. Sirve para cerrar lo que abriste.

```python
try:
    ...
except ValueError as e:
    ...
finally:
    ...
```

| Cómo sale del `try` | Orden |
|---|---|
| sin error | `try` → `finally` |
| error capturado | `except` → `finally` |
| error capturado con `return` | `except` hasta el `return` → `finally` → vuelve a quien llamó |
| error sin capturar | `finally` → el error sube |

Doc: [finally](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)

> `finally` SE EJECUTA SIEMPRE, TAMBIÉN SI HAY UN `return` O UN ERROR SIN CAPTURAR.
