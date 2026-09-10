# Exp

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Eleva e a potenza.

## Sintassi esatta

```text
Exp(power:Any) -> Decimal
```

## Parametri

- `power` — Obbligatorio: Integer/Decimal o testo decimale con punto ed esponente facoltativo, come "-1.25e2". Indipendente dalla lingua. Testo invalido/esadecimale, Unit, Array e Object diventano 0; i letterali esadecimali numerici sono già Integer. Possibili NaN/Infinity. Exp(0)=1. Molto positivo: Infinity; molto negativo: underflow a 0. NaN invariato.

## Restituisce

Decimal — e^power. Exp(0)=1. Molto positivo: Infinity; molto negativo: underflow a 0. NaN invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

## Comportamento

- Calcolo locale sul thread dello script, senza server, movimento, bersaglio, attesa o modifica delle variabili globali.
- Decimal è Double binario, non .NET decimal. Confrontare risultati finiti approssimati con tolleranza. Non usare NaN/Infinity per coordinate o quantità.
- Exp(0)=1. Molto positivo: Infinity; molto negativo: underflow a 0. NaN invariato.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di registrazione/conversione. Le funzioni complete mostrano formule di script, non sostituiscono la matematica della piattaforma.

#### 1. Register

Register collega il nome BASIC a un calcolo nativo con un argomento e a System.Math dopo conversione. Nessuno script nascosto o procedura server.

Decimal — e^power. Exp(0)=1. Molto positivo: Infinity; molto negativo: underflow a 0. NaN invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

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
# Eleva e a potenza.
#
# Decimal — e^power. Exp(0)=1. Molto positivo: Infinity; molto negativo: underflow a 0. NaN
# invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # power = 0; risultato atteso 1 (~ indica approssimazione). value conserva il risultato; CStr
    # formatta per Print.

    VAR value = Exp(0)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- power = 0; risultato atteso 1 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Altro ingresso tramite variabile

```vb
# Altro ingresso tramite variabile
#
# Eleva e a potenza.
#
# Decimal — e^power. Exp(0)=1. Molto positivo: Infinity; molto negativo: underflow a 0. NaN
# invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

SUB Main()
    # power = 1; risultato atteso ~2.718281828459045 (~ indica approssimazione). value conserva il
    # risultato; CStr formatta per Print.

    VAR inputValue = 1
    VAR value = Exp(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- power = 1; risultato atteso ~2.718281828459045 (~ indica approssimazione). value conserva il risultato; CStr formatta per Print.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Eleva e a potenza.
#
# Decimal — e^power. Exp(0)=1. Molto positivo: Infinity; molto negativo: underflow a 0. NaN
# invariato. Numero, non ID o esito. 1/0 non significano riuscita/fallimento.

# manual-check: scalar-math Exp
SUB Main()
    # value iniziale, rate tasso continuo per unità, period durata in tali unità.
    # Growth(100,0.05,2)≈110.517; esempio numerico.

    VAR value = Growth(100,0.05,2)
    UO.Print(CStr(value))
END SUB

SUB Growth(value,rate,period)
    RETURN value*Exp(rate*period)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value iniziale, rate tasso continuo per unità, period durata in tali unità. Growth(100,0.05,2)≈110.517; esempio numerico.
