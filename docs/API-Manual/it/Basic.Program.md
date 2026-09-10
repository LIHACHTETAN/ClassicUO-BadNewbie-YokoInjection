# SUB Main()

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Un file Basic contiene definizioni di procedure/funzioni e dichiarazioni globali facoltative. Le azioni eseguibili vanno in una procedura. Questi esempi sono file completi con Main() come punto di ingresso.

## Sintassi esatta

```text
Option Explicit On
SUB Main()
    statement
END SUB
# comment
; comment
REM comment
// comment
' comment
```

## Parametri

- `Main / entry` — Procedura scelta per l’avvio. Main è un nome convenzionale, non un’istruzione automatica. SUB Main() dichiara una procedura senza argomenti. Una funzione ausiliaria lavora solo quando viene chiamata.
- `statement` — Un’istruzione eseguibile per riga dentro SUB…END SUB o FUNCTION…END FUNCTION. VAR/CONST globali e Option Explicit stanno fuori; Option Explicit precede le dichiarazioni.
- `comment` — # e ; aprono commenti fuori dalle stringhe, anche dopo il codice. REM, // e l’apostrofo aprono intere righe di commento dopo eventuali rientri. Dentro una stringa questi caratteri possono rimanere testo.

## Restituisce

Caricare il file o dichiarare SUB non restituisce valori. RETURN expression restituisce il valore e termina immediatamente la chiamata. La fine del corpo o RETURN senza espressione produce Unit, cioè nessun valore.

## Comportamento

- Salvare in UTF-8 per conservare commenti e stringhe localizzati. CRLF e LF sono ammessi. Rientri e righe vuote migliorano la lettura ma non sostituiscono END SUB o END FUNCTION.
- Parole chiave, nomi di procedure e variabili ignorano maiuscole/minuscole: itemCount, ITEMCOUNT e ItemCount indicano la stessa associazione. Le stringhe mantengono la grafia; le chiavi di UO.SetGlobal("Key", …) sono dati, non identificatori.
- Un nome semplice inizia con lettera ASCII o sottolineatura, poi ammette lettere, cifre e sottolineature. Evitare parole riservate e nomi API. UO.Print è una chiamata qualificata. I due punti dopo un nome definiscono un’etichetta, non un separatore generale di istruzioni.
- Il motore normalizza il Basic supportato, analizza l’intero file, raccoglie dichiarazioni e verifica nomi. Le funzioni ausiliarie possono quindi stare dopo Main. Il caricamento non avvia tutte le definizioni: l’avvio inizializza la procedura scelta e segue le sue chiamate.
- Gli esempi calcolano solo valori. Verificato il modello, inserire nel suo corpo le chiamate UO necessarie. Sono regole di questo motore, senza garantire tutte le funzionalità di altri Basic.

## Esempi

### 1. Commenti e testo letterale

```vb
# Main dichiara note con "ore #1; keep". # e ; dentro la stringa restano invariati. Gli altri commenti #, REM, // e apostrofo non fanno nulla. RETURN restituisce il testo originale.
Option Explicit On
# Complete file
SUB Main()
    REM Full-line comment
    VAR note = "ore #1; keep" # Trailing comment
    // Another full-line comment
    ' Another full-line comment
    RETURN note
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Main dichiara note con "ore #1; keep". # e ; dentro la stringa restano invariati. Gli altri commenti #, REM, // e apostrofo non fanno nulla. RETURN restituisce il testo originale.

### 2. Funzione ausiliaria completa

```vb
# Main chiama DoubleCount con amount=7. Definita sotto Main, la funzione moltiplica il parametro Integer per 2 e restituisce 14. Main inoltra il risultato. Non servono file Include mancanti o funzioni non dichiarate.
Option Explicit On
SUB Main()
    RETURN DoubleCount(7)
END SUB
FUNCTION DoubleCount(ByVal amount AS Integer)
    VAR result = amount * 2
    RETURN result
END FUNCTION
```

**Spiegazione dei parametri e dell’esecuzione:**

Main chiama DoubleCount con amount=7. Definita sotto Main, la funzione moltiplica il parametro Integer per 2 e restituisce 14. Main inoltra il risultato. Non servono file Include mancanti o funzioni non dichiarate.

### 3. Maiuscole nei nomi

```vb
# itemCount parte da 3; ITEMCOUNT e itemcount aggiungono 2 alla stessa variabile. Sono accettate parole chiave a grafia mista. Main restituisce 5 senza creare altre variabili.
Option Explicit On
sUb Main()
    Var itemCount = 3
    ITEMCOUNT = itemcount + 2
    ReTuRn ItemCount
EnD sUb
```

**Spiegazione dei parametri e dell’esecuzione:**

itemCount parte da 3; ITEMCOUNT e itemcount aggiungono 2 alla stessa variabile. Sono accettate parole chiave a grafia mista. Main restituisce 5 senza creare altre variabili.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: file / subrutine / LineComment / SYMBOL
Runtime/BasicSyntaxPreprocessor.cs: Process
Runtime/InjectionRuntime.cs: Prepare / Load / CallSubrutineValues
Runtime/SemanticScope.cs: Scope
https://learn.microsoft.com/en-us/dotnet/visual-basic/reference/language-specification/introduction (comparison of identifier casing only)
-->
