# UO.LastStatusY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Devuelve la coordenada Y guardada del último objeto con estado aceptado.

## Sintaxis exacta

```text
UO.LastStatusY() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — coordenada Y guardada, no un píxel de la ventana ni un Boolean. 0 antes del primer estado o tras limpiar; cero también es una coordenada válida. Comprobar UO.LastStatus() para distinguir un registro ausente.

## Comportamiento

- Sin parámetros. La lectura no envía paquetes, no abre ventanas ni espera respuestas. UO.GetStatus(id), RequestStats y UpdateObject solicitan datos; enviar la solicitud no cambia LastStatus.
- Un paquete 0x11 aceptado guarda juntos serial y X/Y conocidos en World, compartido por los scripts. Un objeto desconocido/destruido o un paquete básico incompleto no sustituye el registro. Un estado posterior de otro objeto puede sustituirlo.
- X/Y reflejan Entity al recibir el estado, no su posición actual. Para mobile son casillas del mundo; un objeto dentro de un contenedor puede tener coordenadas de su contenido. El paquete de estado no lleva X/Y. Mover o eliminar el objeto después no cambia lo guardado; World.Clear lo reinicia. GetX/GetY leen la posición actual de un objeto presente.
- Las llamadas separadas no son atómicas: puede llegar una actualización entre ellas. Un serial igual no demuestra una respuesta nueva a tu solicitud. laststatus sin paréntesis es un valor intrínseco dinámico, salvo que una variable lo oculte; UO.LastStatus() es la función registrada.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. ReadSavedStatus es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. CharacterStatus

CharacterStatus valida el paquete básico y Entity mediante World.Get, actualiza el estado y guarda serial/X/Y. La posición procede de Entity, no del paquete.

Integer — coordenada Y guardada, no un píxel de la ventana ni un Boolean. 0 antes del primer estado o tras limpiar; cero también es una coordenada válida. Comprobar UO.LastStatus() para distinguir un registro ausente.

Código del proyecto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; función `CharacterStatus`.

#### 2. LastStatusY

ExecuteStealthCompatibility devuelve el serial del bridge como Integer. LastStatusX/LastStatusY usan IStatusSnapshotBridge; un bridge externo antiguo sin esa interfaz mantiene GetX/GetY.

Integer — coordenada Y guardada, no un píxel de la ventana ni un Boolean. 0 antes del primer estado o tras limpiar; cero también es una coordenada válida. Comprobar UO.LastStatus() para distinguir un registro ausente.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `LastStatusY`.

#### 3. Invoke

Invoke lee World en el hilo del juego respetando la cancelación. No espera una respuesta de red ni modifica el estado.

Sin parámetros. La lectura no envía paquetes, no abre ventanas ni espera respuestas. UO.GetStatus(id), RequestStats y UpdateObject solicitan datos; enviar la solicitud no cambia LastStatus.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 4. Clear

Clear pone serial y ambas coordenadas a 0, incluso al conservar los scripts activos.

X/Y reflejan Entity al recibir el estado, no su posición actual. Para mobile son casillas del mundo; un objeto dentro de un contenedor puede tener coordenadas de su contenido. El paquete de estado no lleva X/Y. Mover o eliminar el objeto después no cambia lo guardado; World.Clear lo reinicia. GetX/GetY leen la posición actual de un objeto presente.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Clear`.

Las llamadas separadas no son atómicas: puede llegar una actualización entre ellas. Un serial igual no demuestra una respuesta nueva a tu solicitud. laststatus sin paréntesis es un valor intrínseco dinámico, salvo que una variable lo oculte; UO.LastStatus() es la función registrada.


## Ejemplos

### Leer el último valor

```vb
# Leer el último valor
#
# Devuelve la coordenada Y guardada del último objeto con estado aceptado.
#
# Integer — coordenada Y guardada, no un píxel de la ventana ni un Boolean. 0 antes del primer
# estado o tras limpiar; cero también es una coordenada válida. Comprobar UO.LastStatus() para
# distinguir un registro ausente.

SUB Main()
    # Una sola lectura. HEX muestra un serial hexadecimal; CStr muestra una coordenada numérica. No
    # selecciona un objeto.

    VAR value = UO.LastStatusY()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Una sola lectura. HEX muestra un serial hexadecimal; CStr muestra una coordenada numérica. No selecciona un objeto.

### Solicitar estado y leer los datos conocidos

```vb
# Solicitar estado y leer los datos conocidos
#
# Devuelve la coordenada Y guardada del último objeto con estado aceptado.
#
# Integer — coordenada Y guardada, no un píxel de la ventana ni un Boolean. 0 antes del primer
# estado o tras limpiar; cero también es una coordenada válida. Comprobar UO.LastStatus() para
# distinguir un registro ausente.

SUB Main()
    # subject es el serial de self. 500 es una espera de ejemplo en milisegundos, no una garantía de
    # respuesta. El registro puede ser antiguo o pertenecer a otro objeto.

    VAR subject = UO.Self()
    IF subject <> 0 THEN
        UO.GetStatus(subject)
        WAIT(500)
        VAR value = UO.LastStatusY()
        UO.Print('Known value: ' + CStr(value))
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- subject es el serial de self. 500 es una espera de ejemplo en milisegundos, no una garantía de respuesta. El registro puede ser antiguo o pertenecer a otro objeto.

### Función completa ReadSavedStatus

```vb
# Función completa ReadSavedStatus
#
# Devuelve la coordenada Y guardada del último objeto con estado aceptado.
#
# Integer — coordenada Y guardada, no un píxel de la ventana ni un Boolean. 0 antes del primer
# estado o tras limpiar; cero también es una coordenada válida. Comprobar UO.LastStatus() para
# distinguir un registro ausente.

SUB Main()
    # expectedId es el serial guardado en Main. La función se define completa debajo; -1 significa
    # que el registro ya no está seleccionado, no un código propio del comando. Las comprobaciones
    # antes/después reducen la mezcla de objetos sin garantizar atomicidad para el mismo serial.

    VAR expectedId = UO.LastStatus()
    IF expectedId <> 0 THEN
        VAR value = ReadSavedStatus(expectedId)
        UO.Print('Checked value: ' + CStr(value))
    END IF
END SUB

SUB ReadSavedStatus(expectedId)
    IF expectedId = 0 OR UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    VAR value = UO.LastStatusY()
    IF UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Explicación de los parámetros y la ejecución:**

- expectedId es el serial guardado en Main. La función se define completa debajo; -1 significa que el registro ya no está seleccionado, no un código propio del comando. Las comprobaciones antes/después reducen la mezcla de objetos sin garantizar atomicidad para el mismo serial.
