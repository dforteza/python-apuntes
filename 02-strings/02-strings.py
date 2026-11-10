# 1. DEFINICIÓN STRING
print("== 1. Definición string ==")

# Crear
print("comillas:", "hola" == 'hola')       # True
print("str():", repr(str(42)))             # '42'
print("varias líneas:", repr("""dos
líneas"""))                                # 'dos\nlíneas'

# Leer: igual que listas y tuplas
x = "python"
print("posición:", x[0], x[-1])            # p n
print("trozo:", x[:2])                     # py
print("len():", len(x))                    # 6

# in: también busca trozos de texto
print("in:", "th" in x)                    # True

# Actualizar: no se puede
try:
    x[0] = "C"
except TypeError as e:
    print("x[0] = 'C':", e)                # 'str' object does not support...

# Hay que crear otro
print("otro:", "C" + x[1:])                # Cython

# Los métodos no cambian el string: hay que guardar el resultado
x = "hola"
x.upper()
print("sin guardar:", x)                   # hola
x = x.upper()
print("guardando:", x)                     # HOLA

print()

# 2. MAYÚSCULAS Y MINÚSCULAS
print("== 2. Mayúsculas y minúsculas ==")

x = "hola MUNDO"
print("upper():", x.upper())               # HOLA MUNDO
print("lower():", x.lower())               # hola mundo
print("capitalize():", x.capitalize())     # Hola mundo
print("title():", x.title())               # Hola Mundo

# Comparar sin distinguir mayúsculas
print("sin pasar:", "Fire" == "FIRE")                  # False
print("pasando:", "Fire".lower() == "FIRE".lower())    # True

print()
# 3. BUSCAR Y COMPROBAR
print("== 3. Buscar y comprobar ==")

x = "python"
print("startswith():", x.startswith("py"))  # True
print("endswith():", x.endswith("on"))     # True
print("find():", x.find("th"))             # 2
print("find() si no está:", x.find("z"))   # -1
print("count():", x.count("o"))            # 1

print("isdigit():", "42".isdigit())        # True
print("isalpha():", "abc".isalpha())       # True
print("isupper():", "ABC".isupper())       # True
print("islower():", "abc".islower())       # True

# isdigit() con negativo: mejor int() con try
print("isdigit() con -5:", "-5".isdigit())  # False
try:
    print("int() con -5:", int("-5"))      # -5
except ValueError as e:
    print(e)

print()

# 4. LIMPIAR, REEMPLAZAR, DIVIDIR Y UNIR
print("== 4. Limpiar, reemplazar, dividir y unir ==")

# Limpiar: repr para ver los espacios y el \n
print("strip():", repr("  hola  ".strip()))     # 'hola'
print("lstrip():", repr("  hola  ".lstrip()))   # 'hola  '
print("rstrip():", repr("  hola  ".rstrip()))   # '  hola'
print('rstrip("\\n"):', repr("hola\n".rstrip("\n")))  # 'hola'

# Reemplazar
print("replace():", "hola".replace("o", "a"))   # hala

# Dividir
print("split():", "a b  c".split())             # ['a', 'b', 'c']
print('split(":"):', "a:b".split(":"))          # ['a', 'b']
print("splitlines():", "a\nb\n".splitlines())   # ['a', 'b']

# Unir
print("join():", ", ".join(["a", "b"]))         # a, b
try:
    ", ".join([1, 2])
except TypeError as e:
    print("join() con int:", e)                 # sequence item 0: expected str...

print()
# 5. FORMATEAR
print("== 5. Formatear ==")

n = "Ana"
p = 3.14159

print("+:", "Hola " + n)                   # Hola Ana
print("*:", "ab" * 2)                      # abab
print("f-string:", f"Hola {n}")            # Hola Ana
print("expresión:", f"{2 + 3}")            # 5
print("2 decimales:", f"{p:.2f}")          # 3.14
print("format():", "Hola {}".format(n))    # Hola Ana

# + solo une strings
try:
    "Edad: " + 42
except TypeError as e:
    print("+ con int:", e)                 # can only concatenate str...
print("con f-string:", f"Edad: {42}")      # Edad: 42
