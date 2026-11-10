# 1. DEFINICIÓN EXCEPCIÓN
print("== 1. Definición excepción ==")

# Una excepción es un objeto
error = ValueError("mensaje")
print("tipo:", type(error))                    # <class 'ValueError'>
print("mensaje:", error)                       # mensaje
print()
try:
    int("abc")
except ValueError as e:
    print("ValueError:", e)                    # invalid literal for int()...
try:
    10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)             # division by zero
try:
    open("no_existe.txt")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)             # [Errno 2] No such file...
try:
    "abc" + 1
except TypeError as e:
    print("TypeError:", e)                     # can only concatenate str...


# Subir: salta en convertir(), nadie lo captura ahí y pasa a leer_edad()
def convertir(texto: str) -> int:
    return int(texto)


def leer_edad(texto: str) -> None:
    try:
        convertir(texto)
    except ValueError:
        print("subir: capturado en leer_edad()")


leer_edad("abc")

# Sin capturar: descomenta la línea para ver el traceback (el programa termina)
# int("abc")

print()

# 2. RAISE
print("== 2. raise ==")

# Crear no es lanzar: no pasa nada
ValueError("solo lo creo")
print("crear: el programa sigue")

# raise lo lanza: lo que hay después no se ejecuta
try:
    raise ValueError("lo lanzo")
    print("esto no se imprime")
except ValueError as e:
    print("lanzar:", e)                        # lo lanzo

print()

# 3. TRY Y EXCEPT
print("== 3. try y except ==")

# Sin error: se salta el except
try:
    print("sin error:", int("42"))             # 42
except ValueError as e:
    print("no se imprime:", e)

# Error de ese tipo: el resto del try no se ejecuta y el programa sigue
try:
    print("antes del error")
    int("abc")
    print("no se imprime")
except ValueError as e:
    print("error de ese tipo:", e)             # invalid literal for int()...
print("el programa sigue")

# Error de otro tipo: este except no lo captura y sigue subiendo
try:
    try:
        10 / 0
    except ValueError:
        print("no se imprime")
except ZeroDivisionError as e:
    print("error de otro tipo, ha subido:", e)  # division by zero

print()

# 4. VARIOS EXCEPT
print("== 4. Varios except ==")

# Un except por tipo: solo se ejecuta el primero que encaja
try:
    10 / 0
except ValueError:
    print("no se imprime")
except ZeroDivisionError:
    print("un except por tipo: ZeroDivisionError")
except Exception:
    print("también encaja, pero no se imprime")

# Varios tipos en un except, con paréntesis
for texto in ["abc", None]:
    try:
        int(texto)
    except (ValueError, TypeError) as e:
        print("varios en uno:", type(e).__name__)  # ValueError / TypeError

print()

# 5. EXCEPCIONES PROPIAS
print("== 5. Excepciones propias ==")


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


# Con mensaje propio y con el mensaje por defecto
try:
    raise PlantError("the tomato is wilting")
except PlantError as e:
    print("con mensaje:", e)                   # the tomato is wilting
try:
    raise PlantError()
except PlantError as e:
    print("por defecto:", e)                   # Unknown garden error

# El except del padre también recoge al hijo
try:
    raise PlantError("hijo")
except GardenError as e:
    print("except del padre:", e)              # hijo

# Trampa: con el padre primero, el except del hijo no se ejecuta nunca
try:
    raise PlantError("hijo")
except GardenError:
    print("trampa: entra en el padre")
except PlantError:
    print("no se imprime")

print()

# 6. FINALLY
print("== 6. finally ==")

# Sin error: try → finally
try:
    print("sin error: try")
finally:
    print("sin error: finally")

# Error capturado: except → finally
try:
    int("abc")
except ValueError:
    print("capturado: except")
finally:
    print("capturado: finally")


# Error capturado con return: except hasta el return → finally → vuelve
def con_return() -> None:
    try:
        int("abc")
    except ValueError:
        print("con return: except")
        return
    finally:
        print("con return: finally")


con_return()
print("con return: ha vuelto a quien llamó")

# Error sin capturar: finally → el error sube
try:
    try:
        10 / 0
    finally:
        print("sin capturar: finally")
except ZeroDivisionError:
    print("sin capturar: ha subido")
