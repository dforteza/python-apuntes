# Colecciones

## Índice

1. [Definición colecciones](#1-definición-colecciones)
2. [Operaciones comunes](#2-operaciones-comunes)
3. [Listas](#3-listas)
4. [Tuplas](#4-tuplas)
5. [Sets](#5-sets)
6. [Diccionarios](#6-diccionarios)
7. [Comprehensions](#7-comprehensions)

---

## 1. Definición colecciones

Una colección es un **objeto** que guarda varios valores bajo un solo nombre.

- **Ordenada**: mantiene el orden en que metes los elementos.
- **Mutable**: se puede cambiar después de crearla.

| Colección | Sintaxis | Ordenada | Mutable | Duplicados | Acceso |
|---|---|---|---|---|---|
| lista | `[1, 2]` | sí | sí | sí | por posición: `x[0]` |
| tupla | `(1, 2)` | sí | no | sí | por posición: `x[0]` |
| set | `{1, 2}` | no | sí | no | no hay: solo `in` y `for` |
| dict | `{"a": 1}` | sí | sí | claves no, valores sí | por clave: `x["a"]` |

Doc: [estructuras de datos](https://docs.python.org/3/tutorial/datastructures.html)

> `{}` CREA UN DICT VACÍO, NO UN SET: EL SET VACÍO ES `set()`.

## 2. Operaciones comunes

Lo que funciona igual en varias colecciones. Cada colección remite aquí y solo añade lo suyo.

**Las 4** (en un dict, trabaja con las claves):

| Forma | Devuelve o da |
|---|---|
| `len(x)` | número de elementos |
| `v in x` | `True` o `False` |
| `sum(x)` / `max(x)` / `min(x)` | suma / mayor / menor |
| `sorted(x)` | lista nueva ordenada |
| `for v in x:` | cada valor |
| `for i, v in enumerate(x):` | cada número de vuelta y su valor |

**Listas y tuplas** (las que tienen posición), con `x = [10, 20, 30, 40]`. En una tupla es igual, y los trozos salen como tupla:

| Forma | Resultado | Qué coge |
|---|---|---|
| `x[0]` | `10` | el primero (la primera posición es 0) |
| `x[-1]` | `40` | el último |
| `x[1:3]` | `[20, 30]` | del 1 al 3, sin incluir el 3 |
| `x[:2]` | `[10, 20]` | desde el principio |
| `x[1:]` | `[20, 30, 40]` | hasta el final |
| `x[::-1]` | `[40, 30, 20, 10]` | al revés |
| `x.index(20)` | `1` | posición del primer `20` |
| `x.count(20)` | `1` | veces que aparece `20` |

**Desempaquetar:** asignar cada elemento a una variable, en orden.

```python
x, y, z = (1, 2, 3)    # x = 1, y = 2, z = 3
```

> TANTAS VARIABLES COMO ELEMENTOS: SI NO, `ValueError`.

## 3. Listas

Ordenadas y mutables. Pueden mezclar tipos: `[1, "hola", 3.14]`.

**Crear:**

| Forma | Resultado |
|---|---|
| `[1, 2]` | lista de dos elementos |
| `[]` | lista vacía |
| `list(x)` | lista a partir de otra colección |

**Leer:** ver [§2](#2-operaciones-comunes).

**Actualizar:**

| Forma | Qué hace | Devuelve |
|---|---|---|
| `x[0] = 5` | cambia un elemento | — |
| `x.append(v)` | añade `v` al final | `None` |
| `x.extend(otra)` | añade al final cada elemento de `otra` | `None` |
| `x.insert(i, v)` | mete `v` en la posición `i` | `None` |
| `x.sort()` | ordena la propia lista | `None` |

**Borrar:**

| Forma | Qué hace | Devuelve |
|---|---|---|
| `x.remove(v)` | quita el primer `v` (`ValueError` si no está) | `None` |
| `x.pop()` | saca el último | el elemento |
| `x.pop(i)` | saca el de la posición `i` | el elemento |

**`sys.argv`:** lista de `str` con los argumentos de la terminal. `sys.argv[0]` es el programa y los argumentos son `sys.argv[1:]`. Hay que convertirlos para usarlos como números: `int(sys.argv[1])`.

Doc: [listas](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) · [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)

> `x.sort()` CAMBIA LA LISTA Y DEVUELVE `None`; `sorted(x)` DEVUELVE UNA LISTA NUEVA Y NO TOCA `x`.

> `b = a` NO COPIA: LAS DOS VARIABLES SON LA MISMA LISTA. Para copiarla: `b = a.copy()`.

## 4. Tuplas

Ordenadas e inmutables: para datos que no deben cambiar, como unas coordenadas.

**Crear:**

| Forma | Resultado |
|---|---|
| `(1, 2)` | tupla de dos elementos |
| `(1,)` | tupla de un elemento |
| `()` | tupla vacía |
| `tuple(x)` | tupla a partir de otra colección |

**Leer:** ver [§2](#2-operaciones-comunes).

**Actualizar:** no se puede; `x[0] = 5` da `TypeError`. Hay que crear otra: `list(x)` → cambiar la lista → `tuple(lista)`.

**Borrar elementos:** no se puede, por el mismo motivo.

Doc: [tuplas](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

> `(1)` NO ES UNA TUPLA, ES EL NÚMERO 1: LO QUE CREA LA TUPLA ES LA COMA, `(1,)`.

## 5. Sets

**Sin orden y sin duplicados**: para quitar repetidos o comparar grupos.

**Crear:**

| Forma | Resultado |
|---|---|
| `{1, 2}` | set de dos elementos |
| `set()` | set vacío |
| `set(x)` | set a partir de otra colección, sin los repetidos |

**Leer:** ver [§2, las 4](#2-operaciones-comunes). No tiene posición: `x[0]` da `TypeError`.

**Comparar**, con `a = {1, 2}` y `b = {2, 3}`:

| Forma | Resultado | Qué coge |
|---|---|---|
| `a.union(b)` | `{1, 2, 3}` | los de `a` o `b` |
| `a.intersection(b)` | `{2}` | los que están en los dos |
| `a.difference(b)` | `{1}` | los de `a` que no están en `b` |

**Actualizar:**

| Forma | Qué hace | Devuelve |
|---|---|---|
| `x.add(v)` | añade `v` (si ya está, no hace nada) | `None` |
| `x.update(otra)` | añade cada elemento de `otra` | `None` |

**Borrar:**

| Forma | Qué hace | Devuelve |
|---|---|---|
| `x.remove(v)` | quita `v` (`KeyError` si no está) | `None` |
| `x.discard(v)` | quita `v` (si no está, no hace nada) | `None` |
| `x.pop()` | saca uno cualquiera | el elemento |

Doc: [sets](https://docs.python.org/3/tutorial/datastructures.html#sets) · [métodos](https://docs.python.org/3/library/stdtypes.html#set)

> `union`, `intersection` Y `difference` DEVUELVEN UN SET NUEVO: NO CAMBIAN NI `a` NI `b`.

## 6. Diccionarios

Pares **clave → valor**: cada valor se busca por su clave, y las claves no se repiten.

**Crear:**

| Forma | Resultado |
|---|---|
| `{"a": 1, "b": 2}` | dict de dos pares |
| `{}` | dict vacío |
| `dict(a=1, b=2)` | igual, con la función `dict()` |

**Leer:** ver [§2, las 4](#2-operaciones-comunes) (trabaja con las claves). Además, con `x = {"a": 1, "b": 2}`:

| Forma | Resultado | Si la clave no existe |
|---|---|---|
| `x["a"]` | `1` | `KeyError` |
| `x.get("a")` | `1` | `None` |
| `x.get("a", 0)` | `1` | `0` (el valor que indiques) |

| Forma | Da |
|---|---|
| `x.keys()` | las claves |
| `x.values()` | los valores |
| `x.items()` | los pares |
| `for k, v in x.items():` | cada clave y su valor |

**Actualizar:**

| Forma | Qué hace | Devuelve |
|---|---|---|
| `x["a"] = 5` | cambia el valor; si la clave no existe, la crea | — |
| `x.update(otro)` | añade los pares de `otro` y pisa los que coinciden | `None` |

**Borrar:**

| Forma | Qué hace | Devuelve |
|---|---|---|
| `del x["a"]` | quita el par (`KeyError` si no está) | — |
| `x.pop("a")` | saca el par (`KeyError` si no está) | el valor |
| `x.clear()` | vacía el dict | `None` |

Doc: [diccionarios](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) · [métodos](https://docs.python.org/3/library/stdtypes.html#dict)

> `x["z"]` FALLA SI LA CLAVE NO EXISTE, PERO `x["z"] = 1` LA CREA: LEER Y ESCRIBIR SE COMPORTAN DISTINTO.

## 7. Comprehensions

Crean **una colección nueva a partir de otra en una sola línea**. Sustituyen a un `for` con `append`.

Sintaxis: `[qué_guardo for v in x if condición]` (el `if` es opcional).

| Crea | Forma | Resultado con `x = [1, 2, 3, 4]` |
|---|---|---|
| lista | `[v * 2 for v in x]` | `[2, 4, 6, 8]` |
| lista filtrada | `[v for v in x if v > 2]` | `[3, 4]` |
| set | `{v % 2 for v in x}` | `{0, 1}` |
| dict | `{v: v * 2 for v in x}` | `{1: 2, 2: 4, 3: 6, 4: 8}` |

| Dónde va el `if` | Para qué | Ejemplo con `x = [1, 2, 3, 4]` |
|---|---|---|
| al final | filtrar: decide **si** entra | `[v for v in x if v > 2]` → `[3, 4]` |
| al principio: **`if ... else`, NUNCA SOLO `if`** | elegir: decide **qué** entra | `[0 if v > 2 else v for v in x]` → `[1, 2, 0, 0]` |

Doc: [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) · [set](https://docs.python.org/3/tutorial/datastructures.html#sets) · [dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

> CON PARÉNTESIS NO SE CREA UNA TUPLA: `(v for v in x)` ES UN GENERADOR (tema 05).
