# Atn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Calcola l’arcotangente.

## Sintassi esatta

```text
Atn(number:Any) -> Decimal
```

## Parametri

- `number` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. Ingresso pendenza, uscita radianti in [-pi/2,pi/2]. Gli infiniti danno gli estremi, NaN resta NaN. Non è atan2.

## Restituisce

Decimal — atan(number). Ingresso pendenza, uscita radianti in [-pi/2,pi/2]. Gli infiniti danno gli estremi, NaN resta NaN. Non è atan2. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- Ingresso pendenza, uscita radianti in [-pi/2,pi/2]. Gli infiniti danno gli estremi, NaN resta NaN. Non è atan2.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Decimal — atan(number). Ingresso pendenza, uscita radianti in [-pi/2,pi/2]. Gli infiniti danno gli estremi, NaN resta NaN. Non è atan2. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

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
# Calcola l’arcotangente.
#
# Decimal — atan(number). Ingresso pendenza, uscita radianti in [-pi/2,pi/2]. Gli infiniti danno
# gli estremi, NaN resta NaN. Non è atan2. Numero, non ID o esito. 1/0 non significano
# riuscita/fallimento.

SUB Main()
    # number = 0; risultato atteso 0 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Atn(0)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- number = 0; risultato atteso 0 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Calcola l’arcotangente.
#
# Decimal — atan(number). Ingresso pendenza, uscita radianti in [-pi/2,pi/2]. Gli infiniti danno
# gli estremi, NaN resta NaN. Non è atan2. Numero, non ID o esito. 1/0 non significano
# riuscita/fallimento.

SUB Main()
    # number = 1; risultato atteso ~0.7853981633974483 (~ indica approssimazione). value conserva il
    # risultato; CStr formatta per Print.

    VAR inputValue = 1
    VAR value = Atn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- number = 1; risultato atteso ~0.7853981633974483 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Calcola l’arcotangente.
#
# Decimal — atan(number). Ingresso pendenza, uscita radianti in [-pi/2,pi/2]. Gli infiniti danno
# gli estremi, NaN resta NaN. Non è atan2. Numero, non ID o esito. 1/0 non significano
# riuscita/fallimento.

# manual-check: scalar-math Atn
SUB Main()
    # rise/run è la pendenza. run=0 dà ripiego 0, non angolo verticale. SlopeDegrees(1,1)≈45; non
    # distingue tutti i quadranti.

    VAR value = SlopeDegrees(1,1)
    UO.Print(CStr(value))
END SUB

SUB SlopeDegrees(rise,run)
    IF run = 0 THEN
        RETURN 0
    END IF
    RETURN Atn(CDbl(rise)/CDbl(run))*180/3.141592653589793
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- rise/run è la pendenza. run=0 dà ripiego 0, non angolo verticale. SlopeDegrees(1,1)≈45; non distingue tutti i quadranti.
