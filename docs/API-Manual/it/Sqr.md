# Sqr

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Calcola la radice quadrata.

## Sintassi esatta

```text
Sqr(number:Any) -> Decimal
```

## Parametri

- `number` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. Ingresso >=0: radice non negativa. Negativo: NaN; +Infinity: Infinity; NaN invariato.

## Restituisce

Decimal — sqrt(number). Ingresso >=0: radice non negativa. Negativo: NaN; +Infinity: Infinity; NaN invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- Ingresso >=0: radice non negativa. Negativo: NaN; +Infinity: Infinity; NaN invariato.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Decimal — sqrt(number). Ingresso >=0: radice non negativa. Negativo: NaN; +Infinity: Infinity; NaN invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

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
# Calcola la radice quadrata.
#
# Decimal — sqrt(number). Ingresso >=0: radice non negativa. Negativo: NaN; +Infinity: Infinity;
# NaN invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # number = 25; risultato atteso 5 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Sqr(25)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- number = 25; risultato atteso 5 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Calcola la radice quadrata.
#
# Decimal — sqrt(number). Ingresso >=0: radice non negativa. Negativo: NaN; +Infinity: Infinity;
# NaN invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # number = 2; risultato atteso ~1.4142135623730951 (~ indica approssimazione). value conserva il
    # risultato; CStr formatta per Print.

    VAR inputValue = 2
    VAR value = Sqr(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- number = 2; risultato atteso ~1.4142135623730951 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Calcola la radice quadrata.
#
# Decimal — sqrt(number). Ingresso >=0: radice non negativa. Negativo: NaN; +Infinity: Infinity;
# NaN invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

# manual-check: scalar-math Sqr
SUB Main()
    # dx/dy sono differenze. CDbl evita overflow intero prima di sqrt(dx²+dy²).
    # SegmentLength(3,4)=5; distanza euclidea, non percorso/collisione.

    VAR value = SegmentLength(3,4)
    UO.Print(CStr(value))
END SUB

SUB SegmentLength(dx,dy)
    VAR x = CDbl(dx)
    VAR y = CDbl(dy)
    RETURN Sqr(x*x+y*y)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- dx/dy sono differenze. CDbl evita overflow intero prima di sqrt(dx²+dy²). SegmentLength(3,4)=5; distanza euclidea, non percorso/collisione.
