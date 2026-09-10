# UO.Random

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Elige un entero pseudoaleatorio. Random(min,max) incluye ambos límites; la forma anterior Random(max) excluye el límite superior.

## Sintaxis exacta

```text
UO.Random(max:Integer) -> Integer
UO.Random(min:Integer, max:Integer) -> Integer
```

## Parámetros

- `min` — Límite inferior, solo con dos argumentos. Entero con signo de 32 bits entre -2147483648 y 2147483647; debe ser <= max.
- `max` — Dos argumentos: límite superior incluido, cualquier Integer con signo. Un argumento: límite superior excluido, 0..2147483647. Random(0) devuelve 0.

## Devuelve

Integer — un número elegido, no un booleano ni un serial. Dos argumentos: min <= resultado <= max. Un argumento positivo: 0 <= resultado < max. Se permiten repeticiones.

## Comportamiento

- No existe la forma sin argumentos. Límites iguales devuelven ese valor. Límites invertidos o un único argumento negativo causan un error del script; no se intercambian.
- Se admite todo el intervalo con signo de 32 bits sin desbordar max+1. Para fracciones discretas, divida enteros: Random(0,100)/100.0.
- El generador pertenece al runtime del script; las llamadas simultáneas se sincronizan. No hay parámetro seed y es diferente de BASIC Rnd. Guarde el resultado para reutilizarlo.
- La llamada es local: no espera, no mueve ni envía paquetes. Compruebe las coordenadas aleatorias; Random(0)=0 no crea un índice válido en un array vacío.

## Ejemplos

### Lanzar un dado

```vb
# Lanzar un dado
#
# Elige un entero pseudoaleatorio. Random(min,max) incluye ambos límites; la forma anterior
# Random(max) excluye el límite superior.
#
# Integer — un número elegido, no un booleano ni un serial. Dos argumentos: min <= resultado <=
# max. Un argumento positivo: 0 <= resultado < max. Se permiten repeticiones.

SUB Main()
    # min=1 y max=6 incluyen los seis valores. roll guarda una elección; STR la convierte en texto.
    # Otra llamada puede producir el mismo valor.

    VAR roll = UO.Random(1, 6)
    UO.Print(STR(roll))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- min=1 y max=6 incluyen los seis valores. roll guarda una elección; STR la convierte en texto. Otra llamada puede producir el mismo valor.

### Esperar un intervalo aleatorio

```vb
# Esperar un intervalo aleatorio
#
# Elige un entero pseudoaleatorio. Random(min,max) incluye ambos límites; la forma anterior
# Random(max) excluye el límite superior.
#
# Integer — un número elegido, no un booleano ni un serial. Dos argumentos: min <= resultado <=
# max. Un argumento positivo: 0 <= resultado < max. Se permiten repeticiones.

SUB Main()
    # min=350 y max=700 son límites incluidos en milisegundos. Random calcula delay; UO.Wait(delay)
    # realiza la espera. Respete el retraso mínimo necesario para el servidor.

    VAR delay = UO.Random(350, 700)
    UO.Print(STR(delay))
    UO.Wait(delay)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- min=350 y max=700 son límites incluidos en milisegundos. Random calcula delay; UO.Wait(delay) realiza la espera. Respete el retraso mínimo necesario para el servidor.

### Índices anteriores y límites iguales

```vb
# Índices anteriores y límites iguales
#
# Elige un entero pseudoaleatorio. Random(min,max) incluye ambos límites; la forma anterior
# Random(max) excluye el límite superior.
#
# Integer — un número elegido, no un booleano ni un serial. Dos argumentos: min <= resultado <=
# max. Un argumento positivo: 0 <= resultado < max. Se permiten repeticiones.

SUB Main()
    # Random(10) da 0..9, nunca 10. Random(7,7) siempre da 7. Random(-2,2) puede dar -2,-1,0,1,2.
    # Cada expresión realiza una elección independiente.

    VAR index = UO.Random(10)
    VAR fixedValue = UO.Random(7, 7)
    VAR offset = UO.Random(-2, 2)
    UO.Print(STR(index) + ', ' + STR(fixedValue) + ', ' + STR(offset))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Random(10) da 0..9, nunca 10. Random(7,7) siempre da 7. Random(-2,2) puede dar -2,-1,0,1,2. Cada expresión realiza una elección independiente.
