# Patrones de diseño

## Índice

1. [Patrón de diseño](#1-patrón-de-diseño)
2. [Factoría abstracta](#2-factoría-abstracta)
3. [Estrategia](#3-estrategia)

---

## 1. Patrón de diseño

- Un **patrón de diseño** es una **SOLUCIÓN REUTILIZABLE A UN PROBLEMA TÍPICO DE DISEÑO** en POO: no es código que se copia, es **UNA FORMA DE ORGANIZAR CLASES**.
- El catálogo clásico es el libro *Design Patterns* (1994) de la **Gang of Four (GoF)**: 23 patrones en 3 grupos.

| Grupo | Qué resuelve | Ejemplo |
|---|---|---|
| **Creacionales** | **QUIÉN Y CÓMO CREA** los objetos | Factoría abstracta |
| **Estructurales** | Cómo se **COMBINAN** clases y objetos | Adapter, Decorator |
| **De comportamiento** | Cómo se **REPARTEN LAS TAREAS** entre objetos | Estrategia |

## 2. Factoría abstracta

- La **factoría abstracta** (*Abstract Factory*) es un patrón **creacional**: una clase que **CREA OBJETOS DE UNA FAMILIA** sin que quien la usa sepa **QUÉ CLASE CONCRETA** recibe.
- Problema que resuelve: sin factoría, el código que usa los objetos tiene que escribir `Rose()`, `Oak()`… -> **DEPENDE DE LAS CLASES CONCRETAS** y hay que tocarlo con cada familia nueva.

Piezas (ejemplo completo en [`factoria_abstracta/`](factoria_abstracta/)):

| Nº | Pieza | Qué es | Ejemplo |
|---|---|---|---|
| 1 | **Producto ABC** | Clase Base | `Plant` |
| 2 | **Producto** | Clases Hijas | `Daisy`, `Rose`, `Bonsai`, `Oak` |
| 3 | **Factoría ABC** | **Factoria Base** con un **método** `create_...` **abstracto por producto** (LO CLAVE)| `PlantFactory` |
| 4 | **Factoría** | **Una por familia**: implementa `create_` y decide qué clase crear | `FlowerFactory`, `TreeFactory` |
| 5 | **Cliente** | El código que usa la factoría | `show()` en `main.py` |

> EL CLIENTE (5) **SOLO CONOCE LAS ABC (1 y 3)**


- **Familia nueva** (p. ej. cactus) -> nueva factoría concreta + sus productos. **EL CLIENTE NO SE TOCA.**
- **No confundir:** El tipo de retorno de `create_...` es **SIEMPRE EL ABSTRACTO** (`-> Plant`), también en las factorías concretas.
- **No confundir:** el paquete **SOLO EXPONE LAS FACTORÍAS** en su `__init__.py` (tema 09); los productos concretos quedan dentro.

## 3. Estrategia

- La **estrategia** (*Strategy*) es un patrón **de comportamiento**: **ENCAPSULA CADA FORMA DE HACER ALGO EN SU PROPIA CLASE**, todas con la **MISMA INTERFAZ**, para que sean **INTERCAMBIABLES** sin tocar el código que las usa.
- Problema que resuelve: sin estrategia, el código que usa los objetos tiene que preguntar `if es_rosa: ... elif es_roble: ...` --> **CADA COMPORTAMIENTO NUEVO OBLIGA A TOCARLO**.

Piezas (ejemplo completo en [`estrategia/`](estrategia/)):

| Nº | Pieza | Qué es | Ejemplo |
|---|---|---|---|
| 1 | **Estrategia ABC** | Clase Base con el **método abstracto** que hace la tarea (LO CLAVE) | `CareStrategy` con `care(plant)` |
| 2 | **Estrategia** | Clases Hijas: **una por forma de hacerlo** | `WaterStrategy`, `PruneStrategy` |
| 3 | **Contexto** | El código que **RECIBE** una estrategia y llama a su método | `garden_day()` |

> EL CONTEXTO (3) **SOLO CONOCE LA ABC (1)**: llama a `care()` sin saber cuál le ha tocado (polimorfismo, tema 08 §6).

- **Comportamiento nuevo** (p. ej. abonar) -> nueva estrategia concreta. **EL CONTEXTO NO SE TOCA** (principio **ABIERTO/CERRADO**: abierto a extensión, cerrado a modificación).
- **No confundir:** la estrategia **NO HEREDA DEL OBJETO**: lo **RECIBE COMO PARÁMETRO** (`care(plant: Plant)`). Una estrategia **USA** una planta, no **ES** una planta.
- **No confundir con la factoría:** la factoría decide **QUÉ OBJETO SE CREA**; la estrategia decide **QUÉ HACE** ese objeto.
