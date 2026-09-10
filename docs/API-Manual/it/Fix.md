# Fix

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Tronca la parte frazionaria verso zero.

## Sintassi esatta

```text
Fix(value:Any) -> Integer
```

## Parametri

- `value` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. Ingresso finito, risultato troncato in -2147483648..2147483647. -2.9 diventa -2, non floor=-3. Fuori intervallo/NaN/Infinity non sono validi.

## Restituisce

Integer — truncate(value). Ingresso finito, risultato troncato in -2147483648..2147483647. -2.9 diventa -2, non floor=-3. Fuori intervallo/NaN/Infinity non sono validi. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- Ingresso finito, risultato troncato in -2147483648..2147483647. -2.9 diventa -2, non floor=-3. Fuori intervallo/NaN/Infinity non sono validi.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Integer — truncate(value). Ingresso finito, risultato troncato in -2147483648..2147483647. -2.9 diventa -2, non floor=-3. Fuori intervallo/NaN/Infinity non sono validi. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; funzione `Register`.

#### 2. BasicDouble

BasicDouble conserva Integer/Decimal, legge il testo con NumberStyles.Float invariante e altrimenti dà 0. Abs gestisce direttamente Integer ordinari prima del ripiego Double.

Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; funzione `BasicDouble`.

Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.


## Esempi

### Calcolo diretto

```vb
# Calcolo diretto
#
# Tronca la parte frazionaria verso zero.
#
# Integer — truncate(value). Ingresso finito, risultato troncato in -2147483648..2147483647.
# -2.9 diventa -2, non floor=-3. Fuori intervallo/NaN/Infinity non sono validi. Numero, non ID o
# esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # value = 2.9; risultato atteso 2 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Fix(2.9)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value = 2.9; risultato atteso 2 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Tronca la parte frazionaria verso zero.
#
# Integer — truncate(value). Ingresso finito, risultato troncato in -2147483648..2147483647.
# -2.9 diventa -2, non floor=-3. Fuori intervallo/NaN/Infinity non sono validi. Numero, non ID o
# esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # value = -2.9; risultato atteso -2 (~ indica approssimazione). value conserva il risultato;
    # CStr formatta per Print.

    VAR inputValue = -2.9
    VAR value = Fix(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value = -2.9; risultato atteso -2 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Tronca la parte frazionaria verso zero.
#
# Integer — truncate(value). Ingresso finito, risultato troncato in -2147483648..2147483647.
# -2.9 diventa -2, non floor=-3. Fuori intervallo/NaN/Infinity non sono validi. Numero, non ID o
# esito. 1/0 non significano riuscita/fallimento.

# manual-check: scalar-math Fix
SUB Main()
    # total>=0 e size>0: lotti completi; 27/5 dà 5. Ingresso invalido: ripiego 0, valido anche senza
    # lotti. Quoziente entro Integer.

    VAR value = WholeBatches(27,5)
    UO.Print(CStr(value))
END SUB

SUB WholeBatches(total,size)
    IF total < 0 OR size <= 0 THEN
        RETURN 0
    END IF
    RETURN Fix(CDbl(total)/CDbl(size))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- total>=0 e size>0: lotti completi; 27/5 dà 5. Ingresso invalido: ripiego 0, valido anche senza lotti. Quoziente entro Integer.
