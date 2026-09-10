# UO.SetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Solicita cambiar el modo de avance del atributo.

## Sintaxis exacta

```text
UO.SetStatLockState(statNum:Any, statState:Any) -> Unit
```

## Parámetros

- `statNum` — Número de atributo obligatorio: 0 — STR, 1 — DEX, 2 — INT. No es su valor actual ni un nombre textual.
- `statState` — Modo obligatorio: 0 — aumentar, 1 — disminuir, 2 — bloquear. Son tres códigos, no Boolean; true/false no describen todos los modos.

## Devuelve

Unit — no devuelve valor. No interprete el resultado como éxito/error ni lo compare con true. Una lectura posterior muestra el modelo local, no una confirmación del servidor.

## Comportamiento

- Una solicitud válida envía un paquete mediante GameActions y cambia de inmediato el modo local. Se aplican las reglas del servidor; el aumento no está garantizado. Habilidades desconocidas, índices/modos inválidos y personaje ausente se ignoran sin paquete.
- Número de atributo obligatorio: 0 — STR, 1 — DEX, 2 — INT. No es su valor actual ni un nombre textual.
- ExecuteStealthCompatibility elige la rama. Text lee el selector de habilidad; Arg lee números y modos. Un argumento no convertible puede producir un error de conversión.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. ApplyMode es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility elige la rama. Text lee el selector de habilidad; Arg lee números y modos. Un argumento no convertible puede producir un error de conversión.

Unit — no devuelve valor. No interprete el resultado como éxito/error ni lo compare con true. Una lectura posterior muestra el modelo local, no una confirmación del servidor.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.

Una solicitud válida envía un paquete mediante GameActions y cambia de inmediato el modo local. Se aplican las reglas del servidor; el aumento no está garantizado. Habilidades desconocidas, índices/modos inválidos y personaje ausente se ignoran sin paquete.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. SetStatLockState

GetStatLockState/SetStatLockState eligen StrLock, DexLock o IntLock según 0/1/2. Un número desconocido lee −1; escribir comprueba ambos límites antes del envío.

Unit — no devuelve valor. No interprete el resultado como éxito/error ni lo compare con true. Una lectura posterior muestra el modelo local, no una confirmación del servidor.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `SetStatLockState`.

#### 4. ChangeStatLock

Una solicitud válida envía un paquete mediante GameActions y cambia de inmediato el modo local. Se aplican las reglas del servidor; el aumento no está garantizado. Habilidades desconocidas, índices/modos inválidos y personaje ausente se ignoran sin paquete.

Unit — no devuelve valor. No interprete el resultado como éxito/error ni lo compare con true. Una lectura posterior muestra el modelo local, no una confirmación del servidor.

Código del proyecto: `src/ClassicUO.Client/Game/GameActions.cs`; función `ChangeStatLock`.

Una solicitud válida envía un paquete mediante GameActions y cambia de inmediato el modo local. Se aplican las reglas del servidor; el aumento no está garantizado. Habilidades desconocidas, índices/modos inválidos y personaje ausente se ignoran sin paquete.


## Ejemplos

### Leer y mostrar

```vb
# Leer y mostrar
#
# Solicita cambiar el modo de avance del atributo.
#
# Unit — no devuelve valor. No interprete el resultado como éxito/error ni lo compare con true.
# Una lectura posterior muestra el modelo local, no una confirmación del servidor.

SUB Main()
    # El ejemplo fija selector y, para escribir, mode. La primera línea elige la habilidad por
    # nombre o el atributo por número. Print solo muestra el resultado.

    VAR selector = 0
    VAR mode = 2
    UO.SetStatLockState(selector, mode)
    UO.Print(CStr(UO.GetStatLockState(selector)))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El ejemplo fija selector y, para escribir, mode. La primera línea elige la habilidad por nombre o el atributo por número. Print solo muestra el resultado.

### Usar en una condición o comparación

```vb
# Usar en una condición o comparación
#
# Solicita cambiar el modo de avance del atributo.
#
# Unit — no devuelve valor. No interprete el resultado como éxito/error ni lo compare con true.
# Una lectura posterior muestra el modelo local, no una confirmación del servidor.

SUB Main()
    # El umbral 95.1 y los modos 0/1/2 son ajustes de ejemplo. Compruebe −1 antes de cambiar el
    # modo. Leer después de escribir muestra la copia local sin esperar al servidor.

    VAR selector = 0
    VAR before = UO.GetStatLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetStatLockState(selector, 0)
        UO.Print(CStr(UO.GetStatLockState(selector)))
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El umbral 95.1 y los modos 0/1/2 son ajustes de ejemplo. Compruebe −1 antes de cambiar el modo. Leer después de escribir muestra la copia local sin esperar al servidor.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Solicita cambiar el modo de avance del atributo.
#
# Unit — no devuelve valor. No interprete el resultado como éxito/error ni lo compare con true.
# Una lectura posterior muestra el modelo local, no una confirmación del servidor.

SUB Main()
    # La función completa sigue a Main. selector elige habilidad/atributo; mode indica el modo de
    # escritura. ReadValue/ReadMode devuelven el número original; ApplyMode comprueba argumentos,
    # actúa y no devuelve valor. WAIT(1000) separa dos lecturas.

    ApplyMode(0, 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetStatLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetStatLockState(selector, mode)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- La función completa sigue a Main. selector elige habilidad/atributo; mode indica el modo de escritura. ReadValue/ReadMode devuelven el número original; ApplyMode comprueba argumentos, actúa y no devuelve valor. WAIT(1000) separa dos lecturas.
