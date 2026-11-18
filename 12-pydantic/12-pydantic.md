# Pydantic

## Índice

1. [Definición](#1-definición)
2. [BaseModel y conversión](#2-basemodel-y-conversión)
3. [Field y restricciones](#3-field-y-restricciones)
4. [Opcionales y por defecto](#4-opcionales-y-por-defecto)
5. [ValidationError](#5-validationerror)
6. [model_validator](#6-model_validator)
7. [Modelos anidados](#7-modelos-anidados)

---

## 1. Definición

- **VALIDAR** es **COMPROBAR QUE UNOS DATOS CUMPLEN SU TIPO Y SUS REGLAS ANTES DE USARLOS** (p. ej. `crew_size` es un `int` entre 1 y 20). Se hace con los datos que **LLEGAN DE FUERA** (JSON, ficheros, formularios, APIs), que no controlas.
- Problema: Python **NO COMPRUEBA LOS TYPE HINTS AL EJECUTAR**. `crew_size: int` acepta `"hola"` sin quejarse.
- **PYDANTIC** es una **LIBRERÍA EXTERNA QUE VALIDA DATOS A PARTIR DE LOS TYPE HINTS DE UNA CLASE**: al crear el objeto comprueba cada atributo, **CONVIERTE** lo que puede y, si algo no cumple, **LANZA UNA EXCEPCIÓN** y el objeto no se crea.
- Se instala con `pip install pydantic` dentro del venv (tema 09 §1–2). Versión actual: **2.x**.

| | mypy | Pydantic |
|---|---|---|
| Cuándo comprueba | **ANTES** de ejecutar | **AL CREAR EL OBJETO**, ejecutando |
| Qué comprueba | **TU CÓDIGO** | **LOS DATOS** que llegan |
| Si falla | avisa, el programa corre igual | **excepción**, el objeto no existe |

> **CON PYDANTIC LOS TYPE HINTS DEJAN DE SER DECORATIVOS: SE COMPRUEBAN AL EJECUTAR.**

- **No confundir:** la versión 1 usaba `@validator`; en la **2** se usa `@model_validator` (§6). Muchos tutoriales antiguos usan la 1.

Doc: [docs.pydantic.dev](https://docs.pydantic.dev/latest/)

## 2. BaseModel y conversión

- **`BaseModel`** es la **CLASE DE PYDANTIC DE LA QUE SE HEREDA** para crear un modelo. Cada **atributo de clase con type hint** es un **CAMPO** que se valida.

```python
from datetime import datetime
from pydantic import BaseModel


class Planet(BaseModel):
    name: str
    moons: int
    discovered: datetime


p = Planet(name="Saturn", moons="146", discovered="1610-07-25T00:00:00")
print(p.moons)       # 146  -> int, no str
```

| Acción | Cómo | Ejemplo |
|---|---|---|
| Crear | **SOLO CON ARGUMENTOS CON NOMBRE** | `Planet(name="Saturn", moons=146, ...)` |
| Crear desde un `dict` | desempaquetar con `**` (tema 04) | `Planet(**datos)` |
| Leer un campo | como cualquier atributo | `p.moons` |

**Conversión automática** (si el valor **SE PUEDE CONVERTIR SIN PERDER NADA**, lo convierte):

| Campo | Recibe | ¿Convierte? | Resultado |
|---|---|---|---|
| `int` | `"146"` | **Sí** | `146` |
| `int` | `1.0` | **Sí** | `1` |
| `int` | `6.5` | **No** | error: perdería el `.5` |
| `str` | `5` | **No** | error: un número no pasa a `str` |
| `datetime` | `"1610-07-25T00:00:00"` | **Sí** | `datetime(1610, 7, 25, 0, 0)` |
| `bool` | `"yes"`, `"true"`, `1` | **Sí** | `True` |
| `Color` (`Enum`, tema 10 §4) | `"red"` | **Sí** | `Color.RED` |
| `Color` (`Enum`) | `"green"` | **No** | error: `Input should be 'red' or 'blue'` |

> **PYDANTIC CONVIERTE SI NO SE PIERDE INFORMACIÓN; SI NO, ERROR.**

- **No confundir:** se crea **SIEMPRE CON `campo=valor`**. El constructor es `__init__(self, **data)`, y **`**data` SOLO RECOGE ARGUMENTOS CON NOMBRE**.

| Llamada | Resultado |
|---|---|
| `Planet(name="Saturn", moons=146, ...)` | **Pydantic** valida los datos |
| `Planet("Saturn", 146, ...)` | **`TypeError`** de Python: no hay parámetro posicional donde ponerlos |

> **`TypeError` LO LANZA PYTHON AL LLAMAR; `ValidationError` LO LANZA PYDANTIC AL VALIDAR.**

Doc: [Models](https://docs.pydantic.dev/latest/concepts/models/) · [Conversion Table](https://docs.pydantic.dev/latest/concepts/conversion_table/)

## 3. Field y restricciones

- El type hint solo comprueba el **TIPO**. Para los **LÍMITES** (rango, longitud) se usa **`Field`**, que va como **VALOR POR DEFECTO DEL CAMPO**: `campo: tipo = Field(...)`.

```python
from pydantic import BaseModel, Field


class Planet(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    moons: int = Field(ge=0, le=200)
```

| Argumento | Significa | Se usa con | Mensaje si falla |
|---|---|---|---|
| `ge` / `le` | **≥** / **≤** (*greater/less or equal*) | números | `Input should be less than or equal to 200` |
| `gt` / `lt` | **>** / **<** (estricto) | números | `Input should be greater than 0` |
| `min_length` / `max_length` | longitud mínima / máxima | `str`, `list` | `String should have at least 2 characters` |
| `default` | valor si no se pasa el campo (§4) | cualquiera | — |

> **TYPE HINT = QUÉ TIPO; `Field` = QUÉ LÍMITES.**

Doc: [Fields](https://docs.pydantic.dev/latest/concepts/fields/)

## 4. Opcionales y por defecto

- Un campo **CON VALOR POR DEFECTO** deja de ser **OBLIGATORIO**: si no se pasa, toma ese valor.
- Un campo **OPCIONAL** es el que **PUEDE NO TENER VALOR**: su tipo es **`tipo | None`** y su valor por defecto **`None`**.

```python
class Planet(BaseModel):
    has_rings: bool = False                                  # por defecto, sin límites
    notes: str | None = Field(default=None, max_length=50)   # opcional, con límite
```

| Caso | Cómo se escribe |
|---|---|
| Por defecto **sin** límites | `campo: tipo = valor` |
| Por defecto **con** límites | `campo: tipo = Field(default=valor, ...)` |
| Opcional | `campo: tipo \| None = None` |
| Opcional con límites | `campo: tipo \| None = Field(default=None, ...)` |

> **OPCIONAL = `tipo | None = None`.**

Doc: [Fields: default values](https://docs.pydantic.dev/latest/concepts/fields/#default-values)

## 5. ValidationError

- **`ValidationError`** es la **EXCEPCIÓN QUE LANZA PYDANTIC CUANDO EL OBJETO NO CUMPLE SUS REGLAS**. El objeto **NO SE CREA**. Hereda de `ValueError` (tema 06).
- Guarda **CADA ERROR EN UN `dict`** y los junta todos en **UNA SOLA** excepción.

```python
from pydantic import ValidationError

try:
    Planet(name="X", moons=6.5, discovered="2020-01-01")
except ValidationError as e:
    print(e.errors()[0]["msg"])
```

**Estructura:**

```
e                       ValidationError
└── e.errors()          list[dict]  → UN dict POR ERROR
    └── e.errors()[0]   dict        → claves: loc, msg, input, ctx
```

| Expresión | Tipo | Qué es |
|---|---|---|
| `e.error_count()` | `int` | cuántos errores hay |
| `e.errors()` | `list[dict]` | **UN `dict` POR ERROR** |
| `str(e)` | `str` | el informe completo, varias líneas |

**Claves de cada `dict`**, según **QUIÉN** detectó el error:

| Clave | Tipo | Error de `Field` (§3) | Error de `model_validator` (§6) |
|---|---|---|---|
| `"loc"` | `tuple` | el campo: `("moons",)` | `()` → es del modelo entero |
| `"msg"` | `str` | `"Input should be less than or equal to 20"` | `"Value error, Name must start with P"` → **Pydantic añade el prefijo** |
| `"input"` | — | el valor: `30` | todos los datos: `{"name": "Mars", "moons": 1}` |
| `"ctx"` | `dict` | el límite: `{"le": 20}` | **TU EXCEPCIÓN**: `{"error": ValueError("Name must start with P")}` |

> **UN ERROR = UN `dict`.** Si fallan 2 campos → 2 `dict` en la lista.

**Qué necesito → qué escribo:**

| Necesito | Escribo |
|---|---|
| cuántos errores hay | `e.error_count()` |
| el mensaje de un error de `Field` | `e.errors()[0]["msg"]` |
| el mensaje de un `model_validator` **sin prefijo** | `str(e.errors()[0]["ctx"]["error"])` |
| qué campo falló | `e.errors()[0]["loc"]` |
| qué valor falló | `e.errors()[0]["input"]` |

- **No confundir:** `"loc"` es una tupla porque a veces hacen falta **VARIOS NOMBRES**:
  - modelo simple → **un campo** → `("moons",)`
  - campo dentro de otro (§7) → `("moons", 1, "radius")`

Doc: [Validation Errors](https://docs.pydantic.dev/latest/errors/validation_errors/)

## 6. model_validator

- **`@model_validator(mode="after")`** es un **DECORADOR QUE AÑADE UNA VALIDACIÓN PROPIA AL MODELO**. Sirve para reglas que **MEZCLAN VARIOS CAMPOS** (`Field` solo mira un campo cada vez).
- **`mode="after"`**: se ejecuta **DESPUÉS** de validar los campos → `self` ya tiene los valores **convertidos y correctos**.

```python
from pydantic import BaseModel, Field, model_validator


class Planet(BaseModel):
    name: str = Field(min_length=2)
    moons: int = Field(ge=0)
    color: Color

    @model_validator(mode="after")
    def check_rules(self) -> "Planet":
        if not self.name.startswith("P"):
            raise ValueError("Name must start with P")
        if self.color == Color.BLUE and self.moons < 2:
            raise ValueError("Blue planets need 2 moons")
        return self
```

| Pieza | Qué es |
|---|---|
| `self` | el objeto **ya validado** campo por campo |
| `raise ValueError("...")` | **regla incumplida** → Pydantic la convierte en `ValidationError` |
| `return self` | **SIEMPRE AL FINAL**: todo correcto |
| `-> "Planet"` | devuelve un objeto de la propia clase (entre comillas porque aún no existe) |

**Orden al crear el objeto:**

1. Pydantic valida **los campos** (§2–4). Si alguno falla → `ValidationError` y **EL `model_validator` NO SE EJECUTA**.
2. Si todos están bien → ejecuta el `model_validator`. **EL PRIMER `raise` LO PARA**: solo sale un error.

> **`Field` = REGLAS DE UN CAMPO; `model_validator` = REGLAS ENTRE CAMPOS.**

**Su error** tiene `"loc"` vacío y el prefijo `Value error, ` en `"msg"` → ver la tabla de claves de la [§5](#5-validationerror).

- **No confundir:** olvidar `return self` → Pydantic avisa con un `UserWarning`.

Doc: [Model validators](https://docs.pydantic.dev/latest/concepts/validators/#model-validators)

## 7. Modelos anidados

- Un **MODELO ANIDADO** es un **CAMPO CUYO TIPO ES OTRO MODELO** (o una lista de modelos). Pydantic **VALIDA TAMBIÉN EL MODELO DE DENTRO**.

```python
class Moon(BaseModel):
    name: str = Field(min_length=2)
    radius: int = Field(ge=1)


class Planet(BaseModel):
    name: str
    moons: list[Moon] = Field(min_length=1, max_length=3)   # de 1 a 3 lunas


io = Moon(name="Io", radius=1821)
p = Planet(name="Jupiter", moons=[io, Moon(name="Europa", radius=1560)])
print(p.moons[0].name)    # Io
```

- En una **lista**, `min_length` / `max_length` limitan **CUÁNTOS ELEMENTOS** tiene (§3).
- Se accede encadenando: `p.moons` → lista de `Moon`; `p.moons[0].name` → el campo de la primera.

**Reglas sobre la lista** en el `model_validator` (§6): se **RECORRE** `self.moons`.

| Regla | Función | Ejemplo |
|---|---|---|
| **AL MENOS UNO** cumple | `any(...)` → `True` si alguno cumple | `any(m.radius > 1000 for m in self.moons)` |
| **TODOS** cumplen | `all(...)` → `True` si todos cumplen | `all(m.radius > 0 for m in self.moons)` |
| **CUÁNTOS** cumplen | `sum(...)` contando 1 por cada uno | `sum(1 for m in self.moons if m.radius > 1000)` |

**Si falla el modelo de dentro:**

| Cómo se crea | Dónde falla | `"loc"` |
|---|---|---|
| `Moon(...)` **antes**, como objeto | **AL CREAR LA `Moon`**: el `Planet` ni se intenta | `("radius",)` |
| como `dict` dentro del `Planet` | al crear el `Planet` | `("moons", 1, "radius")` → el camino (§5) |

> **SI FALLA UN MODELO DE DENTRO, NO SE CREA EL DE FUERA.**

- **No confundir:** pasar `dict` funciona al ejecutar, pero **mypy da error** (espera `Moon`, recibe `dict`) → crea los **OBJETOS** `Moon(...)`.

Doc: [Nested models](https://docs.pydantic.dev/latest/concepts/models/#nested-models)
