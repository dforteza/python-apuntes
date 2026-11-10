# Ficheros y flujos

Ejemplos: [07-ficheros-y-flujos.py](07-ficheros-y-flujos.py)

## Índice

1. [Definición fichero](#1-definición-fichero)
2. [open() y modos](#2-open-y-modos)
3. [Lectura](#3-lectura)
4. [Escritura](#4-escritura)
5. [close() y with](#5-close-y-with)
6. [Excepciones](#6-excepciones)
7. [stdin, stdout, stderr y flush](#7-stdin-stdout-stderr-y-flush)

---

## 1. Definición fichero

- **FICHERO:** secuencia de bytes guardada con un nombre (su ruta).
- **PYTHON HACE DE INTERMEDIARIO:** no toca el fichero directamente; `open()` devuelve un **objeto fichero** con métodos (`read()`, `write()`…).

Doc: [file object](https://docs.python.org/3/glossary.html#term-file-object)

### Tipos de objeto fichero

| Tipo | Dato (lo que da `read()` y pide `write()`) | Clase | Modo de `open()` |
|---|---|---|---|
| [Texto](https://docs.python.org/3/library/io.html#text-i-o) | `str` | `TextIOWrapper` | `"r"`, `"w"`… (por defecto) |
| [Binario](https://docs.python.org/3/library/io.html#binary-i-o) | `bytes` | `BufferedReader` / `BufferedWriter` | con `b`: `"rb"`, `"wb"`… |
| [Raw](https://docs.python.org/3/library/io.html#raw-i-o) | — | — | no se usa |

### Relación con C

El fd de C sigue existiendo, pero **dentro** del objeto. Otras utilidades del objeto:

| Uso | Devuelve | Ejemplo |
|---|---|---|
| `f.fileno()` | `int`: el fd | `3` |
| `f.name` | `str`: nombre con el que se abrió | `'x.txt'` |
| `f.mode` | `str`: modo de apertura | `'r'` |
| `f.closed` | `bool`: ¿cerrado? | `False` |
| `f.encoding` | `str`: codificación (solo texto) | `'UTF-8'` |
| `f.readable()` / `f.writable()` | `bool`: ¿se puede leer / escribir? | `True` / `False` |

Doc: [io.IOBase](https://docs.python.org/3/library/io.html#io.IOBase)

## 2. open() y modos

- **FIRMA:** `open(file, mode='r', encoding=None, ...)`
- **DEVUELVE:** objeto fichero (el tipo depende del modo, ver §1).
- **LANZA:** `OSError` si no puede abrir (ver §6).

| Parámetro | Qué es |
|---|---|
| `file` | ruta: relativa o absoluta |
| `mode` | PD: `"r"` |
| `encoding` | cómo traducir bytes a texto; recomendado `"utf-8"` |

Doc: [open()](https://docs.python.org/3/library/functions.html#open)

### Modos

| Modo | Para | Si NO existe | Si existe |
|---|---|---|---|
| `"r"` | leer (por defecto) | error | lee desde el principio |
| `"w"` | escribir | lo crea | **lo vacía al abrir** |
| `"a"` | añadir al final | lo crea | escribe detrás |
| `"x"` | crear nuevo | lo crea | error |
| `+` | leer y escribir (`"r+"`, `"w+"`) | según la letra | según la letra |
| `b` / `t` | binario / texto (por defecto) | — | — |

> `"w"` VACÍA EL FICHERO AL ABRIR, aunque no escribas nada.

## 3. Lectura

Requiere un modo de lectura (`"r"` o con `+`); si no: `UnsupportedOperation: not readable`.

| Forma | Qué lee | Devuelve | Al final del fichero |
|---|---|---|---|
| `f.read()` | todo lo que queda | `str` | `''` |
| `f.readline()` | una línea | `str` | `''` |
| `f.readlines()` | todas las líneas | `list[str]` | `[]` |
| `for line in f:` | una línea por vuelta | `str` en `line` | termina el bucle |

Doc: [read](https://docs.python.org/3/library/io.html#io.TextIOBase.read) · [readline](https://docs.python.org/3/library/io.html#io.TextIOBase.readline) · [readlines](https://docs.python.org/3/library/io.html#io.IOBase.readlines)

> EL OBJETO RECUERDA POR DÓNDE VA (cursor): cada lectura sigue donde acabó la anterior. Por eso un segundo `read()` da `''`: ya no queda nada.

## 4. Escritura

Requiere un modo de escritura (`"w"`, `"a"`, `"x"` o con `+`); si no: `UnsupportedOperation: not writable`.

| Forma | Qué escribe | Devuelve |
|---|---|---|
| `f.write(s)` | un `str` | `int`: caracteres escritos |
| `f.writelines(lista)` | cada `str` de la lista, uno tras otro | `None` |

Doc: [write](https://docs.python.org/3/library/io.html#io.TextIOBase.write) · [writelines](https://docs.python.org/3/library/io.html#io.IOBase.writelines)

> NINGUNA AÑADE `\n`: los saltos de línea los pones tú.

## 5. close() y with

| Forma | Qué hace |
|---|---|
| `f.close()` | vacía el buffer y cierra|
| `with open(ruta, modo) as f:` | cierra solo al salir del bloque, **también si salta un error dentro** |

Doc: [close](https://docs.python.org/3/library/io.html#io.IOBase.close) · [with](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

> SIN `with`, SI ALGO FALLA ENTRE `open()` Y `close()`, EL `close()` NO SE EJECUTA y el fichero queda abierto.

## 6. Excepciones

| Excepción | Cuándo | errno |
|---|---|---|
| `FileNotFoundError` | `open` en `"r"` de un fichero que no existe | 2 |
| `PermissionError` | sin permisos | 13 |
| `IsADirectoryError` | la ruta es una carpeta | 21 |
| `FileExistsError` | `open` en `"x"` de uno que ya existe | 17 |
| `UnsupportedOperation` | leer/escribir en un modo que no lo permite | — |
| `ValueError` | usar el fichero después de `close()` | — |

Doc: [jerarquía de OSError](https://docs.python.org/3/library/exceptions.html#os-exceptions)

> TODAS MENOS `ValueError` SON HIJAS DE `OSError`: un solo `except OSError as e` las captura, y `str(e)` da `[Errno 2] No such file or directory: 'foo'`.

## 7. stdin, stdout, stderr y flush

- Son **objetos fichero**, del mismo tipo que los de `open()` (`TextIOWrapper`) y con los mismos métodos. 
- **Cambia a dónde apuntan**: al teclado y a la terminal, no al disco. Python los deja **ya abiertos** al arrancar (sin `open` ni `close`), en el módulo `sys`.

| Flujo | fd | Lo usa | Para |
|---|---|---|---|
| `sys.stdin` | 0 | `input()` | entrada |
| `sys.stdout` | 1 | `print()` | salida normal |
| `sys.stderr` | 2 | `print(..., file=sys.stderr)` | errores |

Doc: [sys.stdin](https://docs.python.org/3/library/sys.html#sys.stdin) · [flush](https://docs.python.org/3/library/io.html#io.IOBase.flush)

**Buffer:** `sys.stdout.write()` (y `print()`) **ESCRIBEN EN EL BUFFER DE `stdout`, NO EN LA TERMINAL.** Si `stdout` es una terminal, el buffer se vacía al llegar un `\n`. `flush()` lo vacía en ese momento.

**`input()` hace 3 cosas**, que a mano son:

1. escribir el prompt → `sys.stdout.write("Name: ")`
2. sacarlo ya → `sys.stdout.flush()`
3. leer lo que escribe el usuario **hasta que pulsa Enter** (incluye el `\n`) y quitarle el `\n` → `sys.stdin.readline().rstrip("\n")`
