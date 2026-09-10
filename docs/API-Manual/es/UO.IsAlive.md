# UO.IsAlive

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Comprueba la presencia de un objeto sin estado de muerte.

## Sintaxis exacta

```text
UO.IsAlive() -> Integer
UO.IsAlive(value:Any) -> Integer
```

## Parámetros

- `value` — Objeto opcional en las formas mostradas: serial numérico/cadena hexadecimal, self, lasttarget o nombre AddObject registrado. No es un type. Si se omite, lee self. Un texto desconocido causa un error de conversión en algunas formas; compruebe primero el nombre.

## Devuelve

Integer Boolean: 1 = TRUE, 0 = FALSE. Puede compararse con números o constantes lógicas sin comillas. 1 indica que un serial positivo existe y no está marcado como muerto. Un objeto presente también devuelve 1: no es un filtro de mobile. Objetos muertos o ausentes devuelven 0.

Resultado lógico: 1 = TRUE, 0 = FALSE. Tras VAR result = comando(...), use IF result = TRUE THEN o IF result = 1 THEN; para el resultado negativo, IF result = FALSE THEN o IF result = 0 THEN. TRUE/FALSE sin comillas. Llame una vez y guarde el resultado: otra llamada puede repetir la acción o leer un estado cambiado.

## Comportamiento

- Lee el modelo local: no abre target, no solicita status, no cambia indicadores ni envía paquetes. Un objeto destruido está ausente incluso antes de eliminar su entrada del diccionario.
- Cada resultado es una lectura independiente. El mundo puede cambiar entre Exists y la siguiente llamada; varias consultas no forman una instantánea atómica.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. ReadState es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. RegisterCharacterGetterAliases

Al crear el runtime, RegisterCharacterGetterAliases registra nombres y formas. Sin argumento utiliza bridge.Self; con un argumento utiliza su serial. Se conservan los registros existentes.

1 indica que un serial positivo existe y no está marcado como muerto. Un objeto presente también devuelve 1: no es un filtro de mobile. Objetos muertos o ausentes devuelven 0.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject resuelve números, cadenas hexadecimales y nombres guardados. El nombre AddObject se resuelve en cada llamada; no busca graphic/type ni abre una selección interactiva.

Objeto opcional en las formas mostradas: serial numérico/cadena hexadecimal, self, lasttarget o nombre AddObject registrado. No es un type. Si se omite, lee self. Un texto desconocido causa un error de conversión en algunas formas; compruebe primero el nombre.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `TryGetObject`.

#### 3. Invoke

Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.

Cada resultado es una lectura independiente. El mundo puede cambiar entre Exists y la siguiente llamada; varias consultas no forman una instantánea atómica.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 4. Get

World.Get resuelve el serial y devuelve null para IsDestroyed; después lee el indicador Mobile. Alive comprueba Exists y la ausencia de IsDead; admite objetos. Dead para self lee Player.IsDead.

1 indica que un serial positivo existe y no está marcado como muerto. Un objeto presente también devuelve 1: no es un filtro de mobile. Objetos muertos o ausentes devuelven 0.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Get`.

Lee el modelo local: no abre target, no solicita status, no cambia indicadores ni envía paquetes. Un objeto destruido está ausente incluso antes de eliminar su entrada del diccionario.


## Ejemplos

### Comprobar el estado propio

```vb
# Comprobar el estado propio
#
# Comprueba la presencia de un objeto sin estado de muerte.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Puede compararse con números o constantes lógicas sin
# comillas. 1 indica que un serial positivo existe y no está marcado como muerto. Un objeto
# presente también devuelve 1: no es un filtro de mobile. Objetos muertos o ausentes devuelven
# 0.
#
# Resultado lógico: 1 = TRUE, 0 = FALSE. Tras VAR result = comando(...), use IF result = TRUE
# THEN o IF result = 1 THEN; para el resultado negativo, IF result = FALSE THEN o IF result = 0
# THEN. TRUE/FALSE sin comillas. Llame una vez y guarde el resultado: otra llamada puede repetir
# la acción o leer un estado cambiado.

SUB Main()
    # Los paréntesis vacíos leen self. active guarda un resultado; TRUE y FALSE eligen las dos
    # ramas. Print solo muestra un mensaje de ejemplo.

    VAR active = UO.IsAlive()
    IF active = TRUE THEN
        UO.Print('State is active')
    ELSE
        UO.Print('State is inactive or unavailable')
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Los paréntesis vacíos leen self. active guarda un resultado; TRUE y FALSE eligen las dos ramas. Print solo muestra un mensaje de ejemplo.

### Objeto seleccionado y función ReadState completa

```vb
# Objeto seleccionado y función ReadState completa
#
# Comprueba la presencia de un objeto sin estado de muerte.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Puede compararse con números o constantes lógicas sin
# comillas. 1 indica que un serial positivo existe y no está marcado como muerto. Un objeto
# presente también devuelve 1: no es un filtro de mobile. Objetos muertos o ausentes devuelven
# 0.
#
# Resultado lógico: 1 = TRUE, 0 = FALSE. Tras VAR result = comando(...), use IF result = TRUE
# THEN o IF result = 1 THEN; para el resultado negativo, IF result = FALSE THEN o IF result = 0
# THEN. TRUE/FALSE sin comillas. Llame una vez y guarde el resultado: otra llamada puede repetir
# la acción o leer un estado cambiado.

SUB Main()
    # lasttarget es el objeto seleccionado anteriormente. Exists comprueba su presencia. obj es el
    # único parámetro de ReadState; la función devuelve el resultado sin cambios. Su definición
    # completa se incluye en el código copiado.

    IF UO.Exists('lasttarget') THEN
        VAR observed = ReadState('lasttarget')
        UO.Print('State 1/0: ' + CStr(observed))
    END IF
END SUB

SUB ReadState(obj)
    RETURN UO.IsAlive(obj)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- lasttarget es el objeto seleccionado anteriormente. Exists comprueba su presencia. obj es el único parámetro de ReadState; la función devuelve el resultado sin cambios. Su definición completa se incluye en el código copiado.

### Detectar un cambio en medio segundo

```vb
# Detectar un cambio en medio segundo
#
# Comprueba la presencia de un objeto sin estado de muerte.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Puede compararse con números o constantes lógicas sin
# comillas. 1 indica que un serial positivo existe y no está marcado como muerto. Un objeto
# presente también devuelve 1: no es un filtro de mobile. Objetos muertos o ausentes devuelven
# 0.
#
# Resultado lógico: 1 = TRUE, 0 = FALSE. Tras VAR result = comando(...), use IF result = TRUE
# THEN o IF result = 1 THEN; para el resultado negativo, IF result = FALSE THEN o IF result = 0
# THEN. TRUE/FALSE sin comillas. Llame una vez y guarde el resultado: otra llamada puede repetir
# la acción o leer un estado cambiado.

SUB Main()
    # Ambas llamadas sin argumentos leen self; WAIT(500) significa 500 milisegundos. Se comparan dos
    # instantáneas y pueden perderse cambios intermedios. No hay espera infinita.

    VAR before = UO.IsAlive()
    WAIT(500)
    VAR after = UO.IsAlive()
    IF before <> after THEN
        UO.Print('State changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Ambas llamadas sin argumentos leen self; WAIT(500) significa 500 milisegundos. Se comparan dos instantáneas y pueden perderse cambios intermedios. No hay espera infinita.
