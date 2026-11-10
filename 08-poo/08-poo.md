# Programación orientada a objetos

## Índice

1. [Clase y objeto](#1-clase-y-objeto)
2. [Constructor y self](#2-constructor-y-self)
3. [Atributos de instancia y de clase](#3-atributos-de-instancia-y-de-clase)
4. [Encapsulación](#4-encapsulación)
5. [Herencia y super()](#5-herencia-y-super)
6. [Polimorfismo](#6-polimorfismo)
7. [Métodos de clase y estáticos](#7-métodos-de-clase-y-estáticos)
8. [Clase anidada](#8-clase-anidada)
9. [Métodos dunder](#9-métodos-dunder)
10. [Clases abstractas](#10-clases-abstractas)

---

## 1. Clase y objeto

- Una **clase** es un **TIPO DE DATO NUEVO**: el molde que define qué **atributos** (datos) y **métodos** (funciones) tendrán sus objetos.
- Un **objeto** (o **instancia**) es un **VALOR CONCRETO DE ESE TIPO**, con sus propios datos.

```python
class Plant:
    def show(self):
        print("I am a plant")


rose = Plant()      # crea un objeto
rose.show()         # I am a plant
print(type(rose))   # <class '__main__.Plant'>
```

> CREAR UN OBJETO ES **LLAMAR A LA CLASE** COMO SI FUERA UNA FUNCIÓN: `Plant()`.

## 2. Constructor y self

- **`__init__`** es el **MÉTODO INICIALIZADOR**: Python lo llama **AUTOMÁTICAMENTE AL CREAR EL OBJETO** para darle sus datos iniciales. Se le suele llamar constructor, pero cuando se ejecuta el objeto **ya existe**.
- **`self`** es el **PRIMER PARÁMETRO de todo método de instancia**: **EL OBJETO QUE EJECUTA EL MÉTODO**. Python lo pasa solo.

```python
class Plant:
    def __init__(self, name, height=0.0):
        self.name = name
        self.height = height

    def show(self):
        print(f"{self.name}: {self.height}cm")


rose = Plant("Rose", 25.0)   # Python llama a __init__(rose, "Rose", 25.0)
rose.show()                  # Rose: 25.0cm
cactus = Plant("Cactus")     # height toma su valor por defecto (tema 04)
```

> `rose.show()` ES LO MISMO QUE `Plant.show(rose)`: **`self` ES `rose`**.

## 3. Atributos de instancia y de clase

| | De instancia | De clase |
|---|---|---|
| **Qué es** | dato **PROPIO DE CADA OBJETO** | dato **COMPARTIDO POR TODOS** los objetos |
| **Dónde se crea** | `self.name = name`, normalmente en `__init__` | en el cuerpo de la clase: `total = 0` |
| **Acceso** | `rose.name` | `Plant.total` |

```python
class Plant:
    total = 0                   # de clase

    def __init__(self, name):
        self.name = name        # de instancia
        Plant.total += 1


rose = Plant("Rose")
oak = Plant("Oak")
print(rose.name, oak.name)      # Rose Oak
print(Plant.total)              # 2

rose.total = 10                 # crea un atributo NUEVO solo en rose
print(Plant.total, oak.total)   # 2 2
```

> LEER `obj.x` BUSCA **PRIMERO EN EL OBJETO Y LUEGO EN LA CLASE**; ASIGNAR `obj.x = ...` **SIEMPRE ESCRIBE EN EL OBJETO**.

`name: str` en el cuerpo de la clase **SOLO ANOTA EL TIPO** (para mypy) y no crea el atributo; `name: str = "x"` sí lo crea.

## 4. Encapsulación

La **encapsulación** consiste en **CONTROLAR EL ACCESO AL ESTADO INTERNO** del objeto: desde fuera, los datos solo se cambian a través de métodos que **VALIDAN**.

| Nivel | Sintaxis | Qué hace Python |
|---|---|---|
| Público | `self.height` | nada |
| Protegido | `self._height` | **NADA**: es una **CONVENCIÓN** que significa "no lo uses desde fuera" |
| Privado | `self.__height` | lo **RENOMBRA** a `_Plant__height` **(*name mangling*)** para que una clase hija no lo pise por accidente |

Los **getters y setters** son los métodos que dan ese acceso controlado; el setter valida antes de cambiar nada:

```python
class Plant:
    def __init__(self, height):
        self._height = height

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height < 0:
            print("Invalid height")   # rechaza: no cambia nada
        else:
            self._height = height


rose = Plant(25.0)
rose.set_height(-5)                   # Invalid height
print(rose.get_height())              # 25.0
rose._height = -5                     # funciona: el _ no lo impide
```

> EN PYTHON **NADA ES PRIVADO DE VERDAD**: `_` ES UN AVISO Y `__` SOLO CAMBIA EL NOMBRE.

`@property` hace lo mismo que un getter y un setter, pero se usa como un atributo (`rose.height = 5`): [property](https://docs.python.org/3/library/functions.html#property).

## 5. Herencia y super()

- La **herencia** crea una **clase hija** que **RECIBE TODOS LOS ATRIBUTOS Y MÉTODOS** de su **clase madre**: `class Flower(Plant):`.
- **`super()`** hace que la búsqueda del método **EMPIECE EN LA CLASE MADRE**; el método se sigue ejecutando **SOBRE `self`**: `super().show()` == `Plant.show(self)`.

| Llamada (dentro de `Flower`) | Python busca `show()` en... | Ejecuta |
|---|---|---|
| `self.show()` | `Flower` → `Plant` | el de `Flower` (lo encuentra primero) |
| `super().show()` | **`Plant`** (se salta `Flower`) | el de `Plant` |

Si la hija define un método con el mismo nombre que la madre:

| | Sobreescritura | Resultado |
|---|---|---|
| **TOTAL** | sin `super()` | el método de la madre **NO SE EJECUTA** |
| **PARCIAL** | con `super().metodo()` | se ejecuta **LO DE LA MADRE + LO DE LA HIJA** |

```python
class Plant:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Plant: {self.name}")


class Flower(Plant):
    def __init__(self, name, color):
        super().__init__(name)          # la madre crea name
        self.color = color              # la hija añade color

    def show(self):
        super().show()                  # amplía: lo de la madre...
        print(f" Color: {self.color}")  # ...y lo suyo


Flower("Rose", "red").show()
# Plant: Rose
#  Color: red
```

> SI LA HIJA DEFINE `__init__` Y **NO LLAMA A `super().__init__()`**, LOS ATRIBUTOS DE LA MADRE **NO SE CREAN** → `AttributeError` AL USARLOS.

## 6. Polimorfismo

[definicion](https://github.com/dforteza/java-basics/blob/master/teoria/ut7/ut7-resumen.md#3-polimorfismo)

```python
def display(plant):                # no sabe qué tipo de planta recibe
    plant.show()


garden = [Plant("Oak"), Flower("Rose", "red")]
for plant in garden:
    display(plant)                 # cada objeto usa SU show()
# Plant: Oak
# Plant: Rose
#  Color: red
```

> EL MÉTODO SE BUSCA **EN LA CLASE DEL OBJETO** CUANDO SE EJECUTA LA LLAMADA, NO AL ESCRIBIR EL CÓDIGO.

### Duck typing

El ***duck typing*** consiste en que Python **NO COMPRUEBA LA CLASE DEL OBJETO, SOLO QUE TENGA EL MÉTODO** que se llama ("si camina como un pato y hace cuac, es un pato"). Por eso el polimorfismo **NO NECESITA HERENCIA**.

```python
class Robot:                 # no hereda de Plant
    def show(self):
        print("I am a robot")


display(Robot())             # I am a robot → funciona: tiene show()
display(42)                  # AttributeError: 'int' object has no attribute 'show'
```

> SI EL OBJETO NO TIENE EL MÉTODO, EL ERROR SALTA **AL EJECUTAR LA LLAMADA**, NO ANTES.

Con type hints (`def display(plant: Plant)`), mypy rechaza el `Robot` aunque funcione. Para tipar el *duck typing* existe `Protocol` (pm-06).

## 7. Métodos de clase y estáticos

El tipo de método depende de **A QUÉ ACCEDE**: al objeto, a la clase o solo a sus parámetros.

| | De instancia | De clase | Estático |
|---|---|---|---|
| **Accede a** | los datos del objeto (`self`) | la clase (`cls`) | solo a sus parámetros |
| **Decorador** | ninguno | `@classmethod` | `@staticmethod` |
| **Primer parámetro** | `self` | `cls` | ninguno |
| **Uso típico** | trabajar con los datos del objeto | **CONSTRUCTOR ALTERNATIVO** | **FUNCIÓN DE UTILIDAD** ligada a la clase |

```python
class Plant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_older_than_year(days):
        return days > 365             # no usa self ni cls

    @classmethod
    def anonymous(cls):
        return cls("Unknown", 0)      # = Plant("Unknown", 0)


print(Plant.is_older_than_year(400))  # True
seed = Plant.anonymous()
print(seed.name)                      # Unknown
```

> `cls(...)` **CREA UN OBJETO** DE LA CLASE DESDE LA QUE LLAMAS: `Flower.anonymous()` CREARÍA UNA `Flower`.

Un **decorador** (`@...`) es una **FUNCIÓN QUE TRANSFORMA LA FUNCIÓN DE DEBAJO**:<br> 
`@staticmethod` encima de `f` == `f = staticmethod(f)` después.

## 8. Clase anidada

Una **clase anidada** es una **CLASE DEFINIDA DENTRO DE OTRA**. Como se define en el cuerpo de la clase (igual que `total = 0`), **LA CLASE `Stats` ES UN ATRIBUTO DE CLASE** de `Plant`.

Se usa para una pieza interna que **SOLO TIENE SENTIDO DENTRO DE LA EXTERIOR**.

```python
class Plant:
    class Stats:
        def __init__(self):
            self._grow_calls = 0

        def add_grow(self):
            self._grow_calls += 1

        def display(self):
            print(f"Stats: {self._grow_calls} grow")

    def __init__(self, name):
        self.name = name
        self._stats = self.Stats()    # cada planta tiene SU objeto Stats

    def grow(self):
        self._stats.add_grow()

    def show_stats(self):
        self._stats.display()


rose = Plant("Rose")
rose.grow()
rose.show_stats()                     # Stats: 1 grow
```

> `self.Stats()` BUSCA `Stats` **EN LA CLASE DEL OBJETO**: SI `Tree` DEFINE SU PROPIA `Stats`, UN `Tree` USA LA SUYA AUNQUE EL CÓDIGO ESTÉ EN `Plant`.

## 9. Métodos dunder

*(pendiente)*

## 10. Clases abstractas

*(pendiente)*
