# Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Int(value) arrotonda un numero Basic verso meno infinito.

## Sintassi esatta

```text
Int(value:Any) -> Integer
```

## Parametri

- `value` — Un Integer/Decimal o testo numerico obbligatorio. Il separatore è il punto in qualsiasi lingua. Testo non valido, Array, Object e Unit diventano 0; verifica gli input con IsNumeric.

## Restituisce

Integer: floor(value), ad esempio 2.9 -> 2, -2.9 -> -3. Il risultato deve rientrare in Int32 con segno; evita valori non finiti o fuori intervallo.

## Comportamento

- Calcolo locale senza interrogare il gioco. Omettere l’argomento è un errore. Gli attributi si leggono con UO.Int()/UO.Str(), non Int()/Str(). Int usa BasicDouble e Math.Floor; Str seleziona InternalSubrutines.Str per tipo e formatta indipendentemente dalla lingua.

## Esempi

### Int — 1

```vb
# Int — 1
#
# Int(value) arrotonda un numero Basic verso meno infinito.
#
# Integer: floor(value), ad esempio 2.9 -> 2, -2.9 -> -3. Il risultato deve rientrare in Int32
# con segno; evita valori non finiti o fuori intervallo.

SUB Main()
    # value=2.9. L’arrotondamento verso il basso dà Integer 2, restituito da Main.

    RETURN Int(2.9)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value=2.9. L’arrotondamento verso il basso dà Integer 2, restituito da Main.

### Int — 2

```vb
# Int — 2
#
# Int(value) arrotonda un numero Basic verso meno infinito.
#
# Integer: floor(value), ad esempio 2.9 -> 2, -2.9 -> -3. Il risultato deve rientrare in Int32
# con segno; evita valori non finiti o fuori intervallo.

SUB Main()
    # value=-2.9. L’arrotondamento verso il basso dà -3, mentre il troncamento verso zero darebbe
    # -2. Main restituisce Integer -3.

    VAR value = -2.9
    RETURN Int(value)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value=-2.9. L’arrotondamento verso il basso dà -3, mentre il troncamento verso zero darebbe -2. Main restituisce Integer -3.

### Int — 3

```vb
# Int — 3
#
# Int(value) arrotonda un numero Basic verso meno infinito.
#
# Integer: floor(value), ad esempio 2.9 -> 2, -2.9 -> -3. Il risultato deve rientrare in Int32
# con segno; evita valori non finiti o fuori intervallo.

SUB Main()
    # WholeUnits riceve total=27, size=5. size<=0 restituisce 0; altrimenti Int(total/size)
    # arrotonda 5.4 verso il basso. Main restituisce 5 unità complete. Funzione e parametri sono
    # definiti interamente.

    RETURN WholeUnits(27,5)
END SUB

SUB WholeUnits(total,size)
    IF size <= 0 THEN
        RETURN 0
    END IF
    RETURN Int(total/size)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- WholeUnits riceve total=27, size=5. size<=0 restituisce 0; altrimenti Int(total/size) arrotonda 5.4 verso il basso. Main restituisce 5 unità complete. Funzione e parametri sono definiti interamente.
