# UO.GumpAutoCheckBox

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Asigna una vez el valor al primer control coincidente de un gump del servidor; si falta, conserva una acción pendiente.

## Sintaxis exacta

```text
UO.GumpAutoCheckBox(CheckBoxID:Any, Value:Any) -> Unit
```

## Parámetros

- `CheckBoxID` — Integer — ID exacto del tipo de control correspondiente. No es índice, GumpID ni serial de ventana. 0 es un ID normal, sin selección automática del primer control.
- `Value` — Integer — 1 activa, 0 desactiva. Otros números distintos de cero también activan; use 0/1. Elegir un botón de opción desmarca los demás de su mismo grupo.

## Devuelve

Unit — no devuelve ningún valor: ni éxito, ni valor nuevo, ni confirmación del servidor.

## Comportamiento

- Revisa ventanas existentes en el orden actual de la interfaz y después diseños recibidos o reconstruidos del servidor. El primer tipo e ID coincidente consume la acción. Para una ventana concreta use NumGump* con índice.
- Los campos pendientes se rellenan antes de las respuestas automáticas. Repetir tipo e ID en el mismo script sustituye un valor aún pendiente. El cliente admite 1024 campos pendientes; superar el límite causa un error de script.
- El final normal de una rutina conserva sus acciones. Cancelar su propietario o Terminate con su nombre las elimina; TerminateAll elimina todas, incluidas las de rutinas terminadas. Cambiar de mundo vacía la cola. No se guardan en el perfil.

## Ejemplos

### Rellenar un control abierto

```vb
# Rellenar un control abierto
#
# Asigna una vez el valor al primer control coincidente de un gump del servidor; si falta,
# conserva una acción pendiente.
#
# Unit — no devuelve ningún valor: ni éxito, ni valor nuevo, ni confirmación del servidor.

SUB Main()
    # 33 es un ID de ejemplo: cámbielo por el ID real de InfoGump. El segundo argumento es el valor.
    # Si falta el control, la acción queda pendiente.

    UO.GumpAutoCheckBox(33, 1)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- 33 es un ID de ejemplo: cámbielo por el ID real de InfoGump. El segundo argumento es el valor. Si falta el control, la acción queda pendiente.

### Rellenar antes de abrir

```vb
# Rellenar antes de abrir
#
# Asigna una vez el valor al primer control coincidente de un gump del servidor; si falta,
# conserva una acción pendiente.
#
# Unit — no devuelve ningún valor: ni éxito, ni valor nuevo, ni confirmación del servidor.

SUB Main()
    # 33 es el ID del control, 100 un ButtonID de confirmación de ejemplo y 0x40001234 el serial del
    # objeto que abre el formulario. Sustituya los tres. El campo se rellena antes de responder
    # aunque la ventana llegue después.

    UO.GumpAutoCheckBox(33, 1)
    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Explicación de los parámetros y la ejecución:**

- 33 es el ID del control, 100 un ButtonID de confirmación de ejemplo y 0x40001234 el serial del objeto que abre el formulario. Sustituya los tres. El campo se rellena antes de responder aunque la ventana llegue después.

### Sustituir un valor pendiente

```vb
# Sustituir un valor pendiente
#
# Asigna una vez el valor al primer control coincidente de un gump del servidor; si falta,
# conserva una acción pendiente.
#
# Unit — no devuelve ningún valor: ni éxito, ni valor nuevo, ni confirmación del servidor.

SUB Main()
    # Ambas llamadas usan ID 33. Si aún no llegó el control, queda el último valor. Si está abierto,
    # ambos cambios se realizan de inmediato en orden de llamada.

    UO.GumpAutoCheckBox(33, 1)
    UO.GumpAutoCheckBox(33, 0)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Ambas llamadas usan ID 33. Si aún no llegó el control, queda el último valor. Si está abierto, ambos cambios se realizan de inmediato en orden de llamada.
