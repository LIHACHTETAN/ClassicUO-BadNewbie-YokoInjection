# Cos

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Calcola il coseno.

## Sintassi esatta

```text
Cos(radians:Any) -> Decimal
```

## Parametri

- `radians` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. Radianti, non gradi o direzioni del gioco. Risultato finito in [-1,1]; NaN/infinito danno NaN.

## Restituisce

Decimal — cos(radians). Radianti, non gradi o direzioni del gioco. Risultato finito in [-1,1]; NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- Radianti, non gradi o direzioni del gioco. Risultato finito in [-1,1]; NaN/infinito danno NaN.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Decimal — cos(radians). Radianti, non gradi o direzioni del gioco. Risultato finito in [-1,1]; NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

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
# Calcola il coseno.
#
# Decimal — cos(radians). Radianti, non gradi o direzioni del gioco. Risultato finito in [-1,1];
# NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # radians = 0; risultato atteso 1 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Cos(0)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- radians = 0; risultato atteso 1 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Calcola il coseno.
#
# Decimal — cos(radians). Radianti, non gradi o direzioni del gioco. Risultato finito in [-1,1];
# NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # radians = 3.141592653589793; risultato atteso ~-1 (~ indica approssimazione). value conserva
    # il risultato; CStr formatta per Print.

    VAR inputValue = 3.141592653589793
    VAR value = Cos(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- radians = 3.141592653589793; risultato atteso ~-1 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Calcola il coseno.
#
# Decimal — cos(radians). Radianti, non gradi o direzioni del gioco. Risultato finito in [-1,1];
# NaN/infinito danno NaN. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

# manual-check: scalar-math Cos
SUB Main()
    # degrees in gradi; pi/180 converte prima di Cos. CosineDegrees(60)≈0.5.

    VAR value = CosineDegrees(60)
    UO.Print(CStr(value))
END SUB

SUB CosineDegrees(degrees)
    RETURN Cos(degrees*3.141592653589793/180)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- degrees in gradi; pi/180 converte prima di Cos. CosineDegrees(60)≈0.5.
