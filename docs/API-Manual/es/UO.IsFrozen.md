# UO.IsFrozen

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el indicador de parálisis de un mobile conocido por el cliente.

## Sintaxis exacta

```text
UO.IsFrozen() -> Integer
UO.IsFrozen(value:Any) -> Integer
```

## Parámetros

- `value` — Serial/ID opcional del mobile: entero, cadena hexadecimal, self, lasttarget, otro alias estándar o nombre AddObject. No es graphic/type. Sin argumento se elige self. Un alias desconocido da 0; no abre un cursor de selección.

## Devuelve

Integer Boolean: 1 = TRUE si un mobile cargado tiene IsParalyzed; 0 = FALSE si falta el indicador, el mobile es desconocido o está eliminado, o el objeto es un item. No es la duración restante; 0 no garantiza que pueda moverse.

## Comportamiento

- Usa Paralyzed para comprobar el indicador de parálisis. Las variantes Is/Get, GetParalisa, Frozen y GetLocked leen el mismo indicador.
- La consulta es local. No aplica ni cura la parálisis, no espera a que termine y no solicita una actualización al servidor.
- Para esta comprobación, value = TRUE, value = 1 e IF value son equivalentes. TRUE/FALSE se escriben sin comillas. El resultado es un indicador, no una cantidad ni un ID.

## Ejemplos

### Comprobar self con TRUE

```vb
# Comprobar self con TRUE
#
# Lee el indicador de parálisis de un mobile conocido por el cliente.
#
# Integer Boolean: 1 = TRUE si un mobile cargado tiene IsParalyzed; 0 = FALSE si falta el
# indicador, el mobile es desconocido o está eliminado, o el objeto es un item. No es la
# duración restante; 0 no garantiza que pueda moverse.

SUB Main()
    # Los paréntesis vacíos eligen self. state guarda una instantánea; TRUE es la constante numérica
    # 1.
    # FALSE no descarta una pared, falta de stamina u otra causa que impida moverse.

    VAR state = UO.IsFrozen()
    IF state = TRUE THEN
        UO.Print('Paralysis flag is set')
    ELSE
        UO.Print('Paralysis flag is absent or unavailable')
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Los paréntesis vacíos eligen self. state guarda una instantánea; TRUE es la constante numérica 1.
- FALSE no descarta una pared, falta de stamina u otra causa que impida moverse.

### Comprobar el mobile seleccionado

```vb
# Comprobar el mobile seleccionado
#
# Lee el indicador de parálisis de un mobile conocido por el cliente.
#
# Integer Boolean: 1 = TRUE si un mobile cargado tiene IsParalyzed; 0 = FALSE si falta el
# indicador, el mobile es desconocido o está eliminado, o el objeto es un item. No es la
# duración restante; 0 no garantiza que pueda moverse.

SUB Main()
    # target guarda el serial del último objetivo como cadena hexadecimal. IsNpc comprueba un mobile
    # cargado, incluidos los jugadores.
    # El argumento elige ese target guardado. No abre un cursor ni cambia lasttarget.

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR state = UO.IsFrozen(target)
        UO.Print('Selected mobile paralysis 1/0: ' + STR(state))
    ELSE
        UO.Print('No loaded mobile selected')
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- target guarda el serial del último objetivo como cadena hexadecimal. IsNpc comprueba un mobile cargado, incluidos los jugadores.
- El argumento elige ese target guardado. No abre un cursor ni cambia lasttarget.

### Esperar el final con un límite

```vb
# Esperar el final con un límite
#
# Lee el indicador de parálisis de un mobile conocido por el cliente.
#
# Integer Boolean: 1 = TRUE si un mobile cargado tiene IsParalyzed; 0 = FALSE si falta el
# indicador, el mobile es desconocido o está eliminado, o el objeto es un item. No es la
# duración restante; 0 no garantiza que pueda moverse.

SUB Main()
    # Como máximo diez esperas de 100 ms. Cada llamada sin argumento vuelve a leer self.
    # Después del bucle se comprueba por separado que self siga disponible. Se observa
    # aproximadamente un segundo más la ejecución; no se garantiza la recuperación.

    VAR attempts = 0
    WHILE UO.IsFrozen() = TRUE AND attempts < 10
        WAIT(100)
        attempts = attempts + 1
    WEND
    IF UO.IsNpc('self') THEN
        IF UO.IsFrozen() = FALSE THEN
            UO.Print('Paralysis flag is clear')
        ELSE
            UO.Print('Still paralyzed')
        END IF
    ELSE
        UO.Print('Self is unavailable')
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Como máximo diez esperas de 100 ms. Cada llamada sin argumento vuelve a leer self.
- Después del bucle se comprueba por separado que self siga disponible. Se observa aproximadamente un segundo más la ejecución; no se garantiza la recuperación.
