# Abs

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Restituisce il valore assoluto.

## Sintassi esatta

```text
Abs(value:Any) -> Any
```

## Parametri

- `value` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. Integer resta Integer, tranne -2147483648: Decimal 2147483648. Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity.

## Restituisce

Integer/Decimal — abs(value). Integer resta Integer, tranne -2147483648: Decimal 2147483648. Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- Integer resta Integer, tranne -2147483648: Decimal 2147483648. Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Integer/Decimal — abs(value). Integer resta Integer, tranne -2147483648: Decimal 2147483648. Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; funzione `Register`.

#### 2. BasicDouble

BasicDouble conserva Integer/Decimal, legge il testo con NumberStyles.Float invariante e altrimenti dà 0. Abs gestisce direttamente Integer ordinari prima del ripiego Double.

Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; funzione `BasicDouble`.

#### 3. BasicAbs

Integer resta Integer, tranne -2147483648: Decimal 2147483648. Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity.

Integer/Decimal — abs(value). Integer resta Integer, tranne -2147483648: Decimal 2147483648. Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; funzione `BasicAbs`.

Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.


## Esempi

### Calcolo diretto

```vb
# Calcolo diretto
#
# Restituisce il valore assoluto.
#
# Integer/Decimal — abs(value). Integer resta Integer, tranne -2147483648: Decimal 2147483648.
# Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity. Numero,
# non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # value = -12; risultato atteso 12 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Abs(-12)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value = -12; risultato atteso 12 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Restituisce il valore assoluto.
#
# Integer/Decimal — abs(value). Integer resta Integer, tranne -2147483648: Decimal 2147483648.
# Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity. Numero,
# non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # value = '-2.5'; risultato atteso 2.5 (~ indica approssimazione). value conserva il risultato;
    # CStr formatta per Print.

    VAR inputValue = '-2.5'
    VAR value = Abs(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value = '-2.5'; risultato atteso 2.5 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Restituisce il valore assoluto.
#
# Integer/Decimal — abs(value). Integer resta Integer, tranne -2147483648: Decimal 2147483648.
# Decimal/testo danno Decimal. NaN rimane NaN; entrambi gli infiniti danno +Infinity. Numero,
# non ID o esito. 1/0 non significano riuscita/fallimento.

# manual-check: scalar-math Abs
SUB Main()
    # value/target numerici; tolerance è lo scarto ammesso >=0. IsWithin dà Boolean 1/0; tolleranza
    # negativa: 0.

    VAR value = IsWithin(12,10,2)
    UO.Print(CStr(value))
END SUB

SUB IsWithin(value,target,tolerance)
    IF tolerance < 0 THEN
        RETURN 0
    END IF
    RETURN Abs(CDbl(value)-CDbl(target)) <= tolerance
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value/target numerici; tolerance è lo scarto ammesso >=0. IsWithin dà Boolean 1/0; tolleranza negativa: 0.
