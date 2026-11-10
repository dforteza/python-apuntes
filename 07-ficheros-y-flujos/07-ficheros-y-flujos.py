# repr(x): muestra x tal cual se escribe en código ('hola\n' con el \n visible)

# 1. DEFINICIÓN FICHERO
print("== 1. Definición fichero ==")

# Abrimos este mismo .py (__file__ = ruta de este script)

# Tipos de objeto fichero: texto → str / binario → bytes
f = open(__file__)
print("texto → objeto:", type(f))          # <class '_io.TextIOWrapper'>
print("texto → read():", type(f.read()))   # <class 'str'>
f.close()

f = open(__file__, "rb")
print("binario → objeto:", type(f))        # <class '_io.BufferedReader'>
print("binario → read():", type(f.read())) # <class 'bytes'>
f.close()

# Relación con C: el fd va dentro + utilidades del objeto
f = open(__file__)
print("fileno():", f.fileno())             # 3
print("name:", f.name)                     # ruta de este .py
print("mode:", f.mode)                     # r
print("closed:", f.closed)                 # False
print("encoding:", f.encoding)             # UTF-8
print("readable():", f.readable())         # True
print("writable():", f.writable())         # False
f.close()
print("closed tras close():", f.closed)    # True

print()

# 2. OPEN() Y MODOS
print("== 2. open() y modos ==")

print()

# 3. LECTURA
print("== 3. Lectura ==")

# Preparamos un fichero de 2 líneas (escritura: punto 4)
f = open("ejemplo.txt", "w")
f.write("hola\nadios\n")
f.close()

# read(): todo lo que queda; el cursor avanza
f = open("ejemplo.txt")
print("read() 1ª vez:", f.read())          # hola / adios 
print("read() 2ª vez:", f.read())          # (vacío)
f.close()

# readline(): una línea cada vez
f = open("ejemplo.txt")
print("readline() 1ª:", repr(f.readline()))   # 'hola\n'
print("readline() 2ª:", repr(f.readline()))   # 'adios\n'
print("readline() 3ª:", repr(f.readline()))   # ''
f.close()

# readlines(): todas las líneas en una lista
f = open("ejemplo.txt")
print("readlines():", f.readlines())       # ['hola\n', 'adios\n']
f.close()

# for: una línea por vuelta
f = open("ejemplo.txt")
for line in f:
    print("for -> line:", repr(line))       # 'hola\n' / 'adios\n'
f.close()

print()

# 4. ESCRITURA
print("== 4. Escritura ==")

# write
f = open("ejemplo.txt", "w")
print("write('hola') devuelve:", f.write("hola"))     # 4
print("write('adios') devuelve:", f.write("adios"))   # 5
f.close()

f = open("ejemplo.txt")
print("contenido:", repr(f.read()))        # 'holaadios'
f.close()

# writelines()
f = open("ejemplo.txt", "w")
print("writelines() devuelve:", f.writelines(["hola\n", "adios\n"]))  # None
f.close()

f = open("ejemplo.txt")
print("contenido:", repr(f.read()))        # 'hola\nadios\n'
f.close()

print()

# 5. CLOSE() Y WITH
print("== 5. close() y with ==")

# with: cierra solo al salir del bloque
with open("ejemplo.txt") as f:
    print("dentro del with, closed:", f.closed)    # False
print("fuera del with, closed:", f.closed)         # True

# with: cierra TAMBIÉN si salta un error dentro
try:
    with open("ejemplo.txt") as f:
        int("abc")                                 # ValueError a propósito
except ValueError:
    print("error dentro del with, closed:", f.closed)  # True

print()

# 6. EXCEPCIONES
print("== 6. Excepciones ==")

# Hijas de OSError: un solo except las captura todas
for ruta, modo in [("no_existe.txt", "r"),     # FileNotFoundError
                   ("/etc/shadow", "r"),       # PermissionError
                   ("/tmp", "r"),              # IsADirectoryError
                   ("ejemplo.txt", "x")]:      # FileExistsError
    try:
        open(ruta, modo)
    except OSError as e:
        print(type(e).__name__, "→", e)

# UnsupportedOperation: leer en modo "w" (también es OSError)
with open("ejemplo.txt", "w") as f:
    try:
        f.read()
    except OSError as e:
        print(type(e).__name__, "→", e)        # not readable

# ValueError: usar el fichero tras close() (NO es OSError)
try:
    f.read()
except ValueError as e:
    print(type(e).__name__, "→", e)            # I/O operation on closed file.

print()

# 7. STDIN, STDOUT, STDERR Y FLUSH
print("== 7. stdin, stdout, stderr y flush ==")

import sys
import time

# Mismos objetos que open(), ya abiertos: cambia a dónde apuntan
for flujo in [sys.stdin, sys.stdout, sys.stderr]:
    print(flujo.name, "→", type(flujo).__name__, "fd:", flujo.fileno())
# <stdin> → TextIOWrapper fd: 0
# <stdout> → TextIOWrapper fd: 1
# <stderr> → TextIOWrapper fd: 2

# stdout y stderr: dos canales distintos
print("salida normal")                         # a stdout
print("salida de error", file=sys.stderr)      # a stderr
# Prueba: python3 07-ficheros-y-flujos.py 2>/dev/null → oculta solo stderr

# Buffer: sin \n no sale nada hasta el final de los 2 s
sys.stdout.write("sin flush... ")
time.sleep(2)
sys.stdout.write("todo de golpe\n")

# flush(): sale ya, y el resto 2 s después
sys.stdout.write("con flush... ")
sys.stdout.flush()
time.sleep(2)
sys.stdout.write("por partes\n")

# input() a mano: los 3 pasos
sys.stdout.write("Name (a mano): ")
sys.stdout.flush()
name = sys.stdin.readline().rstrip("\n")
print("readline():", repr(name))               # 'lo que escribas', sin \n

# input(): lo mismo en una línea
name = input("Name (input): ")
print("input():", repr(name))                  # 'lo que escribas', sin \n
