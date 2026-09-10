# UO.Strength

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee la Fuerza actual (Strength, STR).

## Sintaxis exacta

```text
UO.Strength() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — puntos actuales, 0..65535 en el modelo; no porcentaje, ID, habilidad, bloqueo ni Boolean. 0 también puede significar jugador ausente/destruido o sujeto no disponible. Comparar con un requisito numérico, no = TRUE. No es el límite ni necesariamente el valor base sin modificadores.

## Comportamiento

- No admite argumentos. Usar las firmas mostradas.
- Lee Player.Strength si Player existe y no está destruido; en caso contrario, 0. Un personaje muerto presente no es un objeto destruido. No se deduce de HP, maná o resistencia.
- GetStr/GetInt/GetDex aceptan ObjID, pero estos atributos solo están en PlayerMobile: cualquier serial ajeno devuelve 0, incluso para un mobile cargado. Limitación respecto a la descripción general de Stealth; no se inventan atributos remotos.
- Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.
- Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.
- Nombres equivalentes con y sin UO., sin distinguir mayúsculas: `Str Strength GetStr GetStrength`.
- Int(value) sin UO. redondea un número BASIC hacia abajo; Str(value) lo formatea como texto. Son operaciones distintas de UO.Int()/UO.Str(), que leen atributos. GetInt(ObjID) no redondea.

### Funciones internas: de la llamada al resultado

Etapas nativas de lectura. AttributeAtLeast es la función BASIC de usuario definida por completo abajo, no una API oculta ni una modificación del atributo.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases añade funciones sin argumentos e intrínsecos ausentes. Las ramas de compatibilidad existentes eligen su getter; ambas devuelven Integer. El intrínseco se relee salvo que una variable lo oculte.

Nombres equivalentes con y sin UO., sin distinguir mayúsculas: `Str Strength GetStr GetStrength`.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lee Player.Strength si Player existe y no está destruido; en caso contrario, 0. Un personaje muerto presente no es un objeto destruido. No se deduce de HP, maná o resistencia. Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.

Integer — puntos actuales, 0..65535 en el modelo; no porcentaje, ID, habilidad, bloqueo ni Boolean. 0 también puede significar jugador ausente/destruido o sujeto no disponible. Comparar con un requisito numérico, no = TRUE. No es el límite ni necesariamente el valor base sin modificadores. Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. CharacterStatus

CharacterStatus asigna el campo STR/DEX/INT recibido a Player.Strength al procesar un paquete status propio aplicable. La consulta lee la caché sin esperar otro paquete.

Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.

Código del proyecto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; función `CharacterStatus`.

#### 4. Clear

World.Clear elimina Player. Las consultas dan 0 hasta que vuelvan el jugador y sus datos. Un valor guardado no prueba el requisito tras reconectar.

Integer — puntos actuales, 0..65535 en el modelo; no porcentaje, ID, habilidad, bloqueo ni Boolean. 0 también puede significar jugador ausente/destruido o sujeto no disponible. Comparar con un requisito numérico, no = TRUE. No es el límite ni necesariamente el valor base sin modificadores.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Clear`.

World.Clear elimina Player. Las consultas dan 0 hasta que vuelvan el jugador y sus datos. Un valor guardado no prueba el requisito tras reconectar.


## Ejemplos

### Mostrar los puntos

```vb
# Mostrar los puntos
#
# Lee la Fuerza actual (Strength, STR).
#
# Integer — puntos actuales, 0..65535 en el modelo; no porcentaje, ID, habilidad, bloqueo ni
# Boolean. 0 también puede significar jugador ausente/destruido o sujeto no disponible. Comparar
# con un requisito numérico, no = TRUE. No es el límite ni necesariamente el valor base sin
# modificadores.

SUB Main()
    # value guarda el número; CStr solo lo formatea para el diario. Sin argumentos ni acción del
    # personaje.

    VAR value = UO.Strength()
    UO.Print('Strength: ' + CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value guarda el número; CStr solo lo formatea para el diario. Sin argumentos ni acción del personaje.

### Comparar dos observaciones

```vb
# Comparar dos observaciones
#
# Lee la Fuerza actual (Strength, STR).
#
# Integer — puntos actuales, 0..65535 en el modelo; no porcentaje, ID, habilidad, bloqueo ni
# Boolean. 0 también puede significar jugador ausente/destruido o sujeto no disponible. Comparar
# con un requisito numérico, no = TRUE. No es el límite ni necesariamente el valor base sin
# modificadores.

SUB Main()
    # before/after están separados por 1000 ms; WAIT pertenece al ejemplo. change=after-before puede
    # ser positivo, cero o negativo; no distingue por sí solo cada actualización intermedia o una
    # desconexión.

    VAR before = UO.Strength()
    WAIT(1000)
    VAR after = UO.Strength()
    VAR change = after - before
    UO.Print('Change: ' + CStr(change))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- before/after están separados por 1000 ms; WAIT pertenece al ejemplo. change=after-before puede ser positivo, cero o negativo; no distingue por sí solo cada actualización intermedia o una desconexión.

### Función completa para comprobar requisitos

```vb
# Función completa para comprobar requisitos
#
# Lee la Fuerza actual (Strength, STR).
#
# Integer — puntos actuales, 0..65535 en el modelo; no porcentaje, ID, habilidad, bloqueo ni
# Boolean. 0 también puede significar jugador ausente/destruido o sujeto no disponible. Comparar
# con un requisito numérico, no = TRUE. No es el límite ni necesariamente el valor base sin
# modificadores.

SUB Main()
    # minimum=80 es un requisito de ejemplo. AttributeAtLeast(minimum) rechaza jugador ausente, lee
    # una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE para >= minimum. El resultado lógico es de
    # la comparación, no del atributo.

    IF AttributeAtLeast(80) = TRUE THEN
        UO.Print('Requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB AttributeAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.Strength()
    RETURN value >= minimum
END SUB
```

**Explicación de los parámetros y la ejecución:**

- minimum=80 es un requisito de ejemplo. AttributeAtLeast(minimum) rechaza jugador ausente, lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE para >= minimum. El resultado lógico es de la comparación, no del atributo.
