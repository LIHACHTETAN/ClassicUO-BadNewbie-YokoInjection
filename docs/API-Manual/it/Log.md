# Log

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Calcola il logaritmo naturale.

## Sintassi esatta

```text
Log(number:Any) -> Decimal
```

## Parametri

- `number` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. Base e, non 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity: Infinity.

## Restituisce

Decimal — ln(number). Base e, non 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity: Infinity. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- Base e, non 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity: Infinity.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Decimal — ln(number). Base e, non 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity: Infinity. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

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
# Calcola il logaritmo naturale.
#
# Decimal — ln(number). Base e, non 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity:
# Infinity. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # number = 1; risultato atteso 0 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Log(1)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- number = 1; risultato atteso 0 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Calcola il logaritmo naturale.
#
# Decimal — ln(number). Base e, non 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity:
# Infinity. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # number = 2.718281828459045; risultato atteso ~1 (~ indica approssimazione). value conserva il
    # risultato; CStr formatta per Print.

    VAR inputValue = 2.718281828459045
    VAR value = Log(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- number = 2.718281828459045; risultato atteso ~1 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Calcola il logaritmo naturale.
#
# Decimal — ln(number). Base e, non 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity:
# Infinity. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

# manual-check: scalar-math Log
SUB Main()
    # value>0, baseValue>0 e <>1. Log(value)/Log(baseValue); LogBase(100,10)≈2. Ingresso invalido:
    # ripiego 0, anche possibile logaritmo valido.

    VAR value = LogBase(100,10)
    UO.Print(CStr(value))
END SUB

SUB LogBase(value,baseValue)
    IF value <= 0 OR baseValue <= 0 OR baseValue = 1 THEN
        RETURN 0
    END IF
    RETURN Log(value)/Log(baseValue)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value>0, baseValue>0 e <>1. Log(value)/Log(baseValue); LogBase(100,10)≈2. Ingresso invalido: ripiego 0, anche possibile logaritmo valido.
