# Tan

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Calcola la tangente.

## Sintassi esatta

```text
Tan(radians:Any) -> Decimal
```

## Parametri

- `radians` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. Radianti. Risultato illimitato, enorme e instabile vicino a pi/2+k*pi. NaN/infinito danno NaN.

## Restituisce

Decimal — tan(radians). Radianti. Risultato illimitato, enorme e instabile vicino a pi/2+k*pi. NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- Radianti. Risultato illimitato, enorme e instabile vicino a pi/2+k*pi. NaN/infinito danno NaN.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Decimal — tan(radians). Radianti. Risultato illimitato, enorme e instabile vicino a pi/2+k*pi. NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

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
# Calcola la tangente.
#
# Decimal — tan(radians). Radianti. Risultato illimitato, enorme e instabile vicino a pi/2+k*pi.
# NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # radians = 0; risultato atteso 0 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Tan(0)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- radians = 0; risultato atteso 0 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Calcola la tangente.
#
# Decimal — tan(radians). Radianti. Risultato illimitato, enorme e instabile vicino a pi/2+k*pi.
# NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # radians = 0.7853981633974483; risultato atteso ~1 (~ indica approssimazione). value conserva
    # il risultato; CStr formatta per Print.

    VAR inputValue = 0.7853981633974483
    VAR value = Tan(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- radians = 0.7853981633974483; risultato atteso ~1 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Calcola la tangente.
#
# Decimal — tan(radians). Radianti. Risultato illimitato, enorme e instabile vicino a pi/2+k*pi.
# NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

# manual-check: scalar-math Tan
SUB Main()
    # degrees in gradi; pi/180 converte prima di Tan. TangentDegrees(45)≈1; evitare singolarità.

    VAR value = TangentDegrees(45)
    UO.Print(CStr(value))
END SUB

SUB TangentDegrees(degrees)
    RETURN Tan(degrees*3.141592653589793/180)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- degrees in gradi; pi/180 converte prima di Tan. TangentDegrees(45)≈1; evitare singolarità.
