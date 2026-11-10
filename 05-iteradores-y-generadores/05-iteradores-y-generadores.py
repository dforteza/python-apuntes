# 1. DEFINICIÓN ITERABLE E ITERADOR
print("== 1. Definición iterable e iterador ==")

x = [10, 20]

# Iterable (lista): cada recorrido vuelve a empezar
print("lista, 1ª vez:", list(x))           # [10, 20]
print("lista, 2ª vez:", list(x))           # [10, 20]

# Iterador: se gasta
it = iter(x)
print("iterador, 1ª vez:", list(it))       # [10, 20]
print("iterador, 2ª vez:", list(it))       # []

print()

# 2. ITER() Y NEXT()
print("== 2. iter() y next() ==")

# next(): da el siguiente valor
it = iter(x)
print("next() 1º:", next(it))              # 10
print("next() 2º:", next(it))              # 20

# next() sin valores: StopIteration
try:
    next(it)
except StopIteration:
    print("next() 3º: StopIteration")

# next() con valor: lo da si no quedan
print("next() con valor:", next(it, "fin"))  # fin

# next() sobre una lista: TypeError
try:
    next(x)
except TypeError as e:
    print("next(lista):", e)               # 'list' object is not an iterator

# for normal
for v in x:
    print("for:", v)                       # 10, 20

# El mismo for, escrito a mano
it = iter(x)                               # 1. crea el iterador
while True:
    try:
        v = next(it)                       # 2. pide el siguiente valor
    except StopIteration:
        break                              # 3. no quedan: termina el bucle
    print("a mano:", v)                    # 10, 20

print()
# 3. GENERADORES Y YIELD
print("== 3. Generadores y yield ==")


# yield: da un valor y se pausa. Los print muestran cuándo se ejecuta
def letras():
    print("  empieza la función")
    yield "A"
    print("  sigue tras A")
    yield "B"
    print("  sigue tras B y termina")


# Llamar a la función no ejecuta su código
g = letras()
print("tipo:", type(g))                    # <class 'generator'>

# next(): se ejecuta hasta el siguiente yield
print("next() 1º:", next(g))               # A
print("next() 2º:", next(g))               # B
try:
    next(g)
except StopIteration:
    print("next() 3º: StopIteration")

# for: llama a next() por ti
for letra in letras():
    print("for:", letra)                   # A, B


# Valores sin fin: cada uno se calcula cuando se pide
def pares():
    n = 0
    while True:
        yield n
        n += 2


g = pares()
print("sin fin:", next(g), next(g), next(g))  # 0 2 4

print()
# 4. EXPRESIONES GENERADORAS
print("== 4. Expresiones generadoras ==")

x = [1, 2, 3]

# Corchetes: lista, con todos los valores ya calculados
lista = [v * 2 for v in x]
print("lista:", lista)                     # [2, 4, 6]

# Paréntesis: generador, sin calcular nada todavía
g = (v * 2 for v in x)
print("generador:", g)                     # <generator object <genexpr> at 0x...>
print("next():", next(g))                  # 2

# Se gasta: sigue donde iba y luego queda vacío
print("el resto:", list(g))                # [4, 6]
print("otra vez:", list(g))                # []

# Dentro de una función basta con sus paréntesis
print("sum():", sum(v * 2 for v in x))     # 12

print()
# 5. TYPE HINT GENERATOR
print("== 5. Type hint Generator ==")

from typing import Generator


# Da str; no usa send() ni return con valor
def saludos() -> Generator[str, None, None]:
    yield "hola"
    yield "adiós"


print("hint:", list(saludos()))            # ['hola', 'adiós']
