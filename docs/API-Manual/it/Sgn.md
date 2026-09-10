# Sgn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Restituisce il segno.

## Sintassi esatta

```text
Sgn(value:Any) -> Integer
```

## Parametri

- `value` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. -1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli infiniti danno il proprio segno.

## Restituisce

Integer — sign(value). -1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli infiniti danno il proprio segno. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- -1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli infiniti danno il proprio segno.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Integer — sign(value). -1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli infiniti danno il proprio segno. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; funzione `Register`.

#### 2. BasicDouble

BasicDouble conserva Integer/Decimal, legge il testo con NumberStyles.Float invariante e altrimenti dà 0. Abs gestisce direttamente Integer ordinari prima del ripiego Double.

Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; funzione `BasicDouble`.

#### 3. BasicSgn

-1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli infiniti danno il proprio segno.

Integer — sign(value). -1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli infiniti danno il proprio segno. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; funzione `BasicSgn`.

Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.


## Esempi

### Calcolo diretto

```vb
# Calcolo diretto
#
# Restituisce il segno.
#
# Integer — sign(value). -1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli
# infiniti danno il proprio segno. Numero, non ID o esito. 1/0 non significano
# riuscita/fallimento.

SUB Main()
    # value = -8; risultato atteso -1 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Sgn(-8)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value = -8; risultato atteso -1 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Restituisce il segno.
#
# Integer — sign(value). -1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli
# infiniti danno il proprio segno. Numero, non ID o esito. 1/0 non significano
# riuscita/fallimento.

SUB Main()
    # value = 10-10; risultato atteso 0 (~ indica approssimazione). value conserva il risultato;
    # CStr formatta per Print.

    VAR inputValue = 10-10
    VAR value = Sgn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value = 10-10; risultato atteso 0 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Restituisce il segno.
#
# Integer — sign(value). -1 negativo, 0 zero, +1 positivo. NaN causa errore matematico; gli
# infiniti danno il proprio segno. Numero, non ID o esito. 1/0 non significano
# riuscita/fallimento.

# manual-check: scalar-math Sgn
SUB Main()
    # current/destination su un asse. StepToward dà -1/0/1, non otto direzioni né movimento.

    VAR value = StepToward(12,10)
    UO.Print(CStr(value))
END SUB

SUB StepToward(current,destination)
    RETURN Sgn(CDbl(destination)-CDbl(current))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- current/destination su un asse. StepToward dà -1/0/1, non otto direzioni né movimento.
