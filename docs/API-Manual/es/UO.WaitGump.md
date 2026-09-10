# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Registra una secuencia ordenada de respuestas únicas a botones. El script continúa inmediatamente; una ventana ausente no lo bloquea durante 30 segundos.

## Sintaxis exacta

```text
UO.WaitGump(Value:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any, trigger16:Any) -> Unit
UO.WaitGump(triggerId:Integer) -> Unit
UO.WaitGump(triggerId:String) -> Unit
```

## Parámetros

- `triggerId` — Integer ButtonID o String numérica. Una cadena puede contener una secuencia separada por | o comas. Las formas con 2..16 argumentos también admiten matrices y secuencias anidadas. Todos los ID se analizan antes de registrar. Una secuencia vacía, más de 256 botones pendientes en el cliente o más de 32 niveles causan un error sin registro parcial.
- `Value` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger1` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger2` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger3` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger4` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger5` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger6` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger7` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger8` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger9` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger10` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger11` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger12` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger13` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger14` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger15` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.
- `trigger16` — Elemento de secuencia: Integer ButtonID, String numérica, cadena separada por |/comas o Array de esos elementos. De izquierda a derecha con los límites de triggerId. Value nombra el único parámetro Any, que también admite una matriz.

## Devuelve

Unit — no devuelve ningún valor: ni éxito, ni valor nuevo, ni confirmación del servidor.

## Comportamiento

- Exige un botón Activate real con el ButtonID solicitado; ignora cambios de página y ventanas ajenas. Los ID posteriores no adelantan al primero pendiente. Como máximo una respuesta por ventana y recepción de diseño. Un diseño reconstruido puede reutilizar el mismo objeto ventana.
- Otro WaitGump del mismo script amplía su secuencia pendiente. No filtra por GumpID: use NumGumpButton o SendGumpSelect para elegir con precisión. ButtonID=0 requiere un botón Activate real con ID 0; no cierra cualquier ventana.
- El final normal de una rutina conserva sus acciones. Cancelar su propietario o Terminate con su nombre las elimina; TerminateAll elimina todas, incluidas las de rutinas terminadas. Cambiar de mundo vacía la cola. No se guardan en el perfil.

## Ejemplos

### Una respuesta

```vb
# Una respuesta
#
# Registra una secuencia ordenada de respuestas únicas a botones. El script continúa
# inmediatamente; una ventana ausente no lo bloquea durante 30 segundos.
#
# Unit — no devuelve ningún valor: ni éxito, ni valor nuevo, ni confirmación del servidor.

SUB Main()
    # 100 es el ButtonID de respuesta. WaitGump lo registra antes de UseObject; continuar el script
    # no demuestra confirmación del servidor.

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Explicación de los parámetros y la ejecución:**

- 100 es el ButtonID de respuesta. WaitGump lo registra antes de UseObject; continuar el script no demuestra confirmación del servidor.

### Varios pasos

```vb
# Varios pasos
#
# Registra una secuencia ordenada de respuestas únicas a botones. El script continúa
# inmediatamente; una ventana ausente no lo bloquea durante 30 segundos.
#
# Unit — no devuelve ningún valor: ni éxito, ni valor nuevo, ni confirmación del servidor.

SUB Main()
    # 7, 22 y 1 son ButtonID de formularios sucesivos, comprobados en ese orden. El número de
    # argumentos no es un retardo; se registra toda la secuencia.

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**Explicación de los parámetros y la ejecución:**

- 7, 22 y 1 son ButtonID de formularios sucesivos, comprobados en ese orden. El número de argumentos no es un retardo; se registra toda la secuencia.

### Cancelar esperas

```vb
# Cancelar esperas
#
# Registra una secuencia ordenada de respuestas únicas a botones. El script continúa
# inmediatamente; una ventana ausente no lo bloquea durante 30 segundos.
#
# Unit — no devuelve ningún valor: ni éxito, ni valor nuevo, ni confirmación del servidor.

SUB Main()
    # La cadena 7|22|1 describe la misma secuencia. TerminateAll borra todas las acciones gump
    # pendientes y detiene todas las rutinas; su efecto es global.

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**Explicación de los parámetros y la ejecución:**

- La cadena 7|22|1 describe la misma secuencia. TerminateAll borra todas las acciones gump pendientes y detiene todas las rutinas; su efecto es global.
