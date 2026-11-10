# Módulos y paquetes

Ejemplos: [09-modulos-y-paquetes.py](09-modulos-y-paquetes.py) (mismos números de sección)

## Índice

1. [Entornos virtuales](#1-entornos-virtuales)
2. [pip y requirements.txt](#2-pip-y-requirementstxt)
3. [Poetry](#3-poetry)
4. [Variables de entorno y .env](#4-variables-de-entorno-y-env)
5. [Módulos e import](#5-módulos-e-import)
6. [\_\_name\_\_](#6-__name__)
7. [Paquetes y \_\_init\_\_.py](#7-paquetes-y-__init__py)
8. [Imports absolutos y relativos](#8-imports-absolutos-y-relativos)
9. [Import circular](#9-import-circular)

---

## 1. Entornos virtuales

Un **entorno virtual** (venv) es una **CARPETA con su propio `python` y sus propios paquetes**, separada del Python del sistema. Así, cada proyecto instala lo suyo sin afectar a los demás.

| Para qué | Comando |
|---|---|
| Crear | `python3 -m venv lab_env` |
| Activar | `source lab_env/bin/activate` |
| Salir | `deactivate` |
| Comprobar cuál usas | `which python3` |
| Borrar | `deactivate` y `rm -rf lab_env` |

| Aísla | No aísla |
|---|---|
| los paquetes instalados | la versión de Python: usa con la que lo creaste |
| | los ficheros del ordenador |
| | las variables de entorno |

**Detectarlo desde Python:**

| Dónde se ejecuta | `sys.prefix` | `sys.base_prefix` |
|---|---|---|
| fuera del venv | `/usr` | `/usr` (iguales) |
| dentro del venv | `/ruta/a/lab_env` | `/usr` (distintos) |

Doc: [venv](https://docs.python.org/3/library/venv.html) · [sys.prefix](https://docs.python.org/3/library/sys.html#sys.prefix) · [sys.base_prefix](https://docs.python.org/3/library/sys.html#sys.base_prefix)

> EL VENV NO SE SUBE AL REPOSITORIO: GUARDA RUTAS DE TU ORDENADOR. SE SUBE LA LISTA DE PAQUETES Y CADA UNO CREA EL SUYO.

## 2. pip y requirements.txt

**pip** es un **GESTOR DE PAQUETES** (*package manager*): instala paquetes externos, descargados de [PyPI](https://pypi.org), en el entorno activo. No ejecuta tu código: eso lo hace `python`, el **INTÉRPRETE**. **`requirements.txt`** es la **LISTA DE PAQUETES** que necesita el proyecto.

| Para qué | Comando |
|---|---|
| Instalar un paquete | `pip install numpy` |
| Instalar desde la lista | `pip install -r requirements.txt` |
| Ver lo instalado | `pip list` |
| Ver lo instalado, en formato lista | `pip freeze` |
| Guardarlo en la lista | `pip freeze > requirements.txt` |
| Desinstalar | `pip uninstall numpy` |

**Cómo se indica la versión** en `requirements.txt`, con un paquete por línea:

| Línea | Instala |
|---|---|
| `numpy` | la última |
| `numpy>=1.25` | la última que sea 1.25 o superior |
| `numpy==1.26.4` | exactamente esa |

`requirements.txt` de ejemplo:

```text
numpy>=1.25
pandas==2.1.0
```

Importar un paquete que no está instalado da `ModuleNotFoundError`.

Doc: [pip](https://pip.pypa.io/en/stable/user_guide/) · [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

> PIP INSTALA EN EL ENTORNO ACTIVO: ACTIVA EL VENV ANTES DE INSTALAR. Fuera de un venv, en tu Ubuntu da el error `externally-managed-environment`.

## 3. Poetry

**Poetry** es un **GESTOR DE DEPENDENCIAS Y DE PROYECTOS** (*dependency manager*). No ejecuta tu código: eso lo hace `python`, el **INTÉRPRETE**. Poetry hace tres cosas:

1. Crea el entorno virtual.
2. Instala los paquetes dentro de él.
3. Fija las versiones exactas.

**pipx** es un **INSTALADOR DE APLICACIONES DE LÍNEA DE COMANDOS** escritas en Python: pone cada una en su propio entorno aislado y la deja disponible en todo el sistema. **pip**, en cambio, instala paquetes en el entorno activo, para que tu código los importe.

**Archivos:**

| Fichero | Qué es | Quién lo escribe |
|---|---|---|
| `pyproject.toml` | **FICHERO DE CONFIGURACIÓN DEL PROYECTO**: guarda sus datos y sus **dependencias**, es decir, los paquetes que necesita | tú o Poetry |
| `poetry.lock` | **FICHERO DE BLOQUEO** (*lock file*): guarda las versiones exactas instaladas | Poetry |

Los dos se suben al repositorio; así, cualquiera que instale el proyecto obtiene las mismas versiones.

`pyproject.toml` mínimo:

```toml
[project]
name = "demo"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["numpy>=1.25"]

[tool.poetry]
package-mode = false
```

`package-mode = false` es necesario porque, sin esa línea, `poetry install` da error al intentar instalar tu proyecto como paquete.

**Comandos:**

| Para qué | Comando |
|---|---|
| Instalar Poetry (una vez por ordenador) | `pipx install poetry` |
| Crear el `pyproject.toml` con un **asistente interactivo**; no crea el entorno ni instala nada | `poetry init` |
| Añadir un paquete | `poetry add numpy` |
| Instalar todas las dependencias del `pyproject.toml`; equivale a `pip install -r requirements.txt` | `poetry install` |
| Ejecutar un script dentro del entorno de Poetry, sin activar nada | `poetry run python script.py` |

**Pasos en un proyecto nuevo, sin `pyproject.toml`:**

1. `poetry init`
2. `poetry add numpy`
3. `poetry run python script.py`

**Pasos en un proyecto con `pyproject.toml` ya escrito:**

1. `poetry install`
2. `poetry run python script.py`

**pip vs Poetry:** `poetry.lock` es una **LISTA DE VERSIONES EXACTAS** que Poetry escribe solo; con `requirements.txt`, esa lista la tienes que escribir tú a mano.

## 4. Variables de entorno y .env

Una **variable de entorno** es un DATO con nombre QUE VIVE fuera de el programa, EN LA TERMINAL. Python recibe una copia al arrancar.

**Leerlas:**

| Código | Si no existe |
|---|---|
| `os.environ["API_KEY"]` | `KeyError` |
| `os.getenv("API_KEY")` | `None` |
| `os.getenv("API_KEY", "valor")` | `"valor"` |

**Guardarlas en un fichero:**

| Fichero | Qué es | ¿Se sube? |
|---|---|---|
| `.env` | **FICHERO DE TEXTO** con tus variables y sus valores reales | no: se añade a `.gitignore` |
| `.env.example` | **PLANTILLA** con los mismos nombres, sin valores reales | sí |

```text
API_KEY=abc123
```

**Cargarlas:** Python no lee el `.env` por sí solo. Lo hace `load_dotenv()`, de la **LIBRERÍA EXTERNA python-dotenv** (`pip install python-dotenv`):

```python
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("API_KEY"))    # abc123
```

> SI UNA VARIABLE ESTÁ EN LA TERMINAL Y EN EL `.env`, GANA LA DE LA TERMINAL.

## 5. Módulos e import

Un **módulo** es un **FICHERO `.py`** cuyo código puedes usar desde otro fichero. `import` lo carga y lo **ejecuta**, solo la primera vez que se importa.

**Formas de importar:**

| Código | Cómo lo usas |
|---|---|
| `import math` | `math.sqrt(9)` |
| `from math import sqrt` | `sqrt(9)` |
| `import numpy as np` | `np.array([1, 2])` |

**Dónde lo busca Python**, en orden, según la lista `sys.path`:

1. La carpeta del script que ejecutas.
2. La librería estándar.
3. Los paquetes instalados del entorno activo.

Si no lo encuentra, da `ModuleNotFoundError`.

> NO LLAMES A TU FICHERO COMO UN MÓDULO QUE USAS: SI CREAS `random.py` EN LA CARPETA DE TU SCRIPT, `import random` IMPORTA EL TUYO.

## 6. \_\_name\_\_

**`__name__`** es una **VARIABLE GLOBAL DEL MÓDULO que Python crea automáticamente**: cada archivo tiene la suya. Su valor depende de **cómo se use el fichero**:

| Cómo se usa `saludo.py` | Valor de `__name__` |
|---|---|
| Lo **ejecutas**: `python3 saludo.py` | `"__main__"` |
| Lo **importas**: `import saludo` | `"saludo"` |

Sirve para que una parte del código se ejecute **solo al lanzar el fichero, no al importarlo**:

```python
def saludar():
    print("hola")


if __name__ == "__main__":
    saludar()
```

> SIN ESTE `if`, EL CÓDIGO SUELTO DEL MÓDULO TAMBIÉN SE EJECUTA AL IMPORTARLO.

### Shebang

El **shebang** es la **PRIMERA LÍNEA del fichero, que empieza por `#!`** e indica al **SISTEMA OPERATIVO** qué intérprete debe ejecutarlo. Para Python es un comentario.

```python
#!/usr/bin/env python3
print("hola")
```

| Cómo lo ejecutas | Requisito |
|---|---|
| `python3 saludo.py` | ninguno: el shebang se ignora |
| `./saludo.py` | shebang + permiso de ejecución: `chmod +x saludo.py` |

> `/usr/bin/env python3` BUSCA `python3` EN EL `PATH`: FUNCIONA EN CUALQUIER MÁQUINA Y USA EL DEL VENV SI ESTÁ ACTIVADO.

## 7. Paquetes y \_\_init\_\_.py

- Un **módulo** es un **FICHERO `.py`**. 
- Un **paquete** es una **CARPETA QUE AGRUPA MÓDULOS**.

```text
paquetito/             ← paquete
├── __init__.py
└── matematicas.py     ← módulo: define suma(), resta() y multiplica()
```

**Camino largo:** se indica `carpeta.fichero`, con puntos en lugar de `/`.

```python
from paquetito.matematicas import multiplica

multiplica(2, 3)
```

**`__init__.py`** es el **FICHERO QUE PYTHON EJECUTA AL IMPORTAR EL PAQUETE**. `import paquetito` ejecuta solo ese fichero: **no abre los demás**. Lo que importas en él **pasa a estar disponible en el paquete**.

**`__all__`** es la **LISTA DE NOMBRES QUE TRAE `from paquete import *`**. Solo afecta al `*`: **no impide usar nada**.

```python
# paquetito/__init__.py
from paquetito.matematicas import resta, suma

__all__ = ["suma"]
```

**Qué se puede usar con este `__init__.py`:**

| Forma de importar | `suma` | `resta` | `multiplica` |
|---|---|---|---|
| `from paquetito import *` | sí | no: no está en `__all__` | no |
| `import paquetito` y `paquetito.nombre()` | sí | sí: está importada en `__init__.py` | `AttributeError` |
| `from paquetito.matematicas import nombre` | sí | sí | sí |

Además, `__all__` deja claro que el import de `__init__.py` es intencionado: sin él, flake8 y mypy pueden avisar de que no se usa.

> `__init__.py` Y `__all__` NO OCULTAN NADA: `multiplica` SIGUE ACCESIBLE POR EL CAMINO LARGO.

## 8. Imports absolutos y relativos

Hay dos formas de indicar dónde está un módulo:

| Tipo | Qué es | Ejemplo |
|---|---|---|
| **Absoluto** | **CAMINO COMPLETO**, empezando por el paquete | `from paquetito.matematicas import suma` |
| **Relativo** | **CAMINO DESDE EL PAQUETE DEL FICHERO**, empezando por un punto | `from .matematicas import suma` |

**Qué significan los puntos:**

```text
paquetito/
├── matematicas.py
├── geometria.py        ← . llega a matematicas
└── avanzado/
    └── calculos.py     ← .. sube a paquetito y llega a matematicas
```

```python
# paquetito/geometria.py
from .matematicas import multiplica

# paquetito/avanzado/calculos.py
from ..matematicas import suma
```

**Cuál usar:**

| Desde dónde | Usa | Por qué |
|---|---|---|
| Un script que ejecutas | absoluto | no tiene paquete (`__package__` es `None`): el punto da `ImportError` |
| Un fichero del paquete, hacia otro del mismo paquete | relativo | si renombras el paquete, no hay que cambiarlos |
| Un fichero del paquete, hacia un módulo de fuera | absoluto | el punto no puede salir del paquete |

> EL PUNTO SIGNIFICA "MI PAQUETE", NO "MI CARPETA".
