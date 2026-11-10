# Iteradores y generadores

Ejemplos: [05-iteradores-y-generadores.py](05-iteradores-y-generadores.py) (mismos números de sección)

## Índice

1. [Definición iterable e iterador](#1-definición-iterable-e-iterador)
2. [iter() y next()](#2-iter-y-next)
3. [Generadores y yield](#3-generadores-y-yield)
4. [Expresiones generadoras](#4-expresiones-generadoras)
5. [Type hint Generator](#5-type-hint-generator)

---

## 1. Definición iterable e iterador

- **Iterable**: OBJETO que SE PUEDE RECORRER CON `for`. Por ejemplo, una lista.
- **Iterador**: OBJETO que DA LOS VALORES DE 1 EN 1 y recuerda por dónde va. Por ejemplo, un fichero abierto.

Todo iterador se puede recorrer con `for`, así que también es iterable. La tabla compara los iterables que no son iteradores, como una lista, con los iteradores.

| | Iterable | Iterador |
|---|---|---|
| Ejemplos | lista, tupla, set, dict, `str` | fichero abierto, generador |
| Recuerda por dónde va | no | sí |
| Recorrerlo otra vez | vuelve a empezar | ya no da nada |

Doc: [iterable](https://docs.python.org/3/glossary.html#term-iterable) · [iterador](https://docs.python.org/3/glossary.html#term-iterator)

> UN ITERADOR SE GASTA: CUANDO HA DADO TODOS SUS VALORES, QUEDA VACÍO. Es lo mismo que pasa con el segundo `read()` de un fichero.

## 2. iter() y next()

| Forma | Qué hace |
|---|---|
| `iter(x)` | crea un iterador a partir del iterable `x` |
| `next(it)` | da el siguiente valor (`StopIteration` si no quedan) |
| `next(it, valor)` | igual, pero da `valor` si no quedan |

Con `x = [10, 20]` e `it = iter(x)`:

| Llamada | Resultado |
|---|---|
| `next(it)` | `10` |
| `next(it)` | `20` |
| `next(it)` | `StopIteration` |

**`for` por dentro:** llama a `iter(x)`, luego a `next()` en cada vuelta, y termina al recibir `StopIteration`.

Doc: [iter](https://docs.python.org/3/library/functions.html#iter) · [next](https://docs.python.org/3/library/functions.html#next)

> `next()` SOLO FUNCIONA CON ITERADORES: `next(x)` SOBRE UNA LISTA DA `TypeError`. Primero hay que crear el iterador con `iter(x)`.

## 3. Generadores y yield

Un **generador** es un iterador creado con una función que lleva `yield`.

```python
def letras():
    yield "A"
    yield "B"
```

Con `g = letras()`:

| Llamada | Resultado | Qué hace la función |
|---|---|---|
| `letras()` | el generador | todavía no se ejecuta |
| `next(g)` | `"A"` | se ejecuta hasta el primer `yield` y se pausa |
| `next(g)` | `"B"` | sigue por donde iba hasta el siguiente `yield` y se pausa |
| `next(g)` | `StopIteration` | sigue y llega al final |

| | `return` | `yield` |
|---|---|---|
| Qué hace | da un valor y **termina** | da un valor y **se pausa** |
| Llamar a la función da | el valor | el generador |

**Para qué sirve:** calcula cada valor cuando se lo piden, en vez de guardarlos todos en memoria. Por eso puede dar valores sin fin.

Doc: [generadores](https://docs.python.org/3/tutorial/classes.html#generators) · [yield](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)

> LLAMAR A LA FUNCIÓN NO EJECUTA SU CÓDIGO, SOLO CREA EL GENERADOR. El código se ejecuta con `next()` o con `for`.

## 4. Expresiones generadoras

Crean un generador en una línea, sin `def` ni `yield`. Se escriben como una [comprehension](../03-colecciones/03-colecciones.md#7-comprehensions), pero con paréntesis.

Con `x = [1, 2, 3]`:

| Forma | Crea | Calcula los valores | Recorrerla otra vez |
|---|---|---|---|
| `[v * 2 for v in x]` | lista | todos, al crearla | vuelve a empezar |
| `(v * 2 for v in x)` | generador | de uno en uno, al pedirlos | ya no da nada |

Dentro de una función basta con sus paréntesis: `sum(v * 2 for v in x)` → `12`.

Doc: [expresiones generadoras](https://docs.python.org/3/tutorial/classes.html#generator-expressions)

> ÚSALA SI SOLO VAS A RECORRER LOS VALORES UNA VEZ; SI NECESITAS GUARDARLOS O USARLOS VARIAS VECES, USA UNA LISTA.

## 5. Type hint Generator

Sintaxis: `Generator[str, None, None]`, con `from typing import Generator`.

| Posición | Qué indica | Valor habitual |
|---|---|---|
| 1ª | tipo de lo que da `yield` | el que corresponda |
| 2ª | tipo de lo que recibe con `send()` | `None` |
| 3ª | tipo de lo que devuelve `return` | `None` |

Doc: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator)

> LO NORMAL ES CAMBIAR SOLO EL PRIMERO: LOS DOS `None` DICEN QUE NO USA NI `send()` NI `return` CON VALOR.
