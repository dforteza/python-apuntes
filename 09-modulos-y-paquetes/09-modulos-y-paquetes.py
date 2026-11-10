import os
import site
import sys

import paquetito

# 1. ENTORNOS VIRTUALES
print("== 1. Entornos virtuales ==")

# Prueba: ejecútalo fuera y dentro de un venv y compara la salida
print("python en uso:", sys.executable)    # /usr/bin/python3 o .../lab_env/bin/python3
print("sys.prefix:", sys.prefix)           # /usr o .../lab_env
print("sys.base_prefix:", sys.base_prefix)  # /usr en los dos casos

# Distintos: estamos dentro de un venv
print("dentro de un venv:", sys.prefix != sys.base_prefix)  # False o True

# Dónde se instalan los paquetes
print("paquetes en:", site.getsitepackages()[0])  # .../site-packages

print()

# 4. VARIABLES DE ENTORNO Y .ENV
print("== 4. Variables de entorno y .env ==")

# Leer: con valor por defecto si no existe
print("HOME:", os.getenv("HOME"))                # /home/...
print("no existe:", os.getenv("NO_EXISTE"))      # None
print("con defecto:", os.getenv("NO_EXISTE", "valor"))  # valor

# El .env necesita python-dotenv: se importa aquí para que el resto
# del fichero funcione sin tenerlo instalado
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("Falta python-dotenv: pip install python-dotenv")
else:
    with open("demo.env", "w") as f:
        f.write("MATRIX_MODE=development\nAPI_KEY=clave_del_env\n")

    # Ya está en el entorno antes de cargar el .env
    os.environ["MATRIX_MODE"] = "production"

    load_dotenv("demo.env")
    print("MATRIX_MODE:", os.getenv("MATRIX_MODE"))  # production: gana el entorno
    print("API_KEY:", os.getenv("API_KEY"))          # clave_del_env: viene del .env

    os.remove("demo.env")

print()

# 7. PAQUETES Y __INIT__.PY
print("== 7. Paquetes y __init__.py ==")

# Camino largo: directo al fichero, se alcanza todo
from paquetito.matematicas import multiplica
print("multiplica:", multiplica(2, 3))  # 6

# Por el paquete: solo lo importado en __init__.py
print("paquetito.suma:", paquetito.suma(2, 3))    # 5
print("paquetito.resta:", paquetito.resta(2, 3))  # -1
print("paquetito tiene multiplica:", hasattr(paquetito, "multiplica"))  # False

# Con *: solo lo que está en __all__
from paquetito import *
print("* trae suma:", "suma" in globals())    # True
print("* trae resta:", "resta" in globals())  # False

print()
