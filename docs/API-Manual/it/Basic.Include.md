# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Include carica un altro file sorgente prima di analisi ed esecuzione. Rende disponibili funzioni e variabili senza avviare automaticamente procedure o thread.

## Sintassi esatta

```text
Include "fileName"
```

## Parametri

- `fileName` — fileName: nome non vuoto tra apici singoli o doppi. Percorso relativo o assoluto letterale, non variabile né espressione. Estensione libera; il contenuto deve essere codice supportato dal motore.

## Restituisce

Nessun valore: direttiva di preparazione. Non assegnare Include(...) né attendere ID, TRUE/FALSE o 1/0. Le funzioni incluse restituiscono i propri valori con RETURN.

## Comportamento

- Include su una riga separata fuori da SUB/FUNCTION. Cerca accanto al file includente, poi nella sua sottocartella Include. Percorsi annidati relativi alla libreria corrente. Salvare il file principale prima di usare percorsi relativi.
- Ogni percorso completo viene incluso una volta. Un ciclo A → B → A produce SC016. Errori di percorso, accesso o sintassi bloccano l’avvio prima delle inizializzazioni globali. Diagnostica e debugger mantengono file e riga originali.
- Chiudere stringhe e SUB/FUNCTION nel file che li apre. Ridichiarare variabili globali o costanti produce SC017 prima dell’esecuzione.
- Il prossimo avvio legge le librerie modificate; uno script preparato o attivo mantiene il proprio codice. Nessuna copia di profili o avvio di altri script.
- Ogni file può indicare Option Explicit prima delle proprie dichiarazioni; altrimenti eredita il principale. Le dichiarazioni condividono uno spazio dei nomi senza creare automaticamente moduli.
- UTF-8 con riconoscimento BOM. Limiti: 128 file incluso il principale, 32 livelli, 16.777.216 caratteri sorgente. Include in commenti o stringhe non carica file.
- Ogni esempio usa una cartella distinta. Salvare Main.bas e tutti i file mostrati con nomi e sottocartelle esatti. Gruppi pronti: API Manual/Examples/Basic.Include/1, /2, /3. Avviare Main.bas, non unire i file.

## Esempi

### 1. Funzione condivisa

```vb
# Main.bas include Common.bas e chiama Add(4, 7). left e right sono per valore; Add restituisce la somma e Main Integer 11. Common.bas non parte da solo.
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Main.bas include Common.bas e chiama Add(4, 7). left e right sono per valore; Add restituisce la somma e Main Integer 11. Common.bas non parte da solo.

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. Libreria annidata

```vb
# Main.bas include lib/Route.bas, che include Math.bas dalla propria cartella lib. Distance(-3, 5) passa dx=-3 e dy=5 a Manhattan; Abs elimina i segni, somma Integer 8. Non muove il personaggio.
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Main.bas include lib/Route.bas, che include Math.bas dalla propria cartella lib. Distance(-3, 5) passa dx=-3 e dy=5 a Manhattan; Abs elimina i segni, somma Integer 8. Non muove il personaggio.

**lib/Route.bas**

```vbnet
Option Explicit On
Include "Math.bas"
FUNCTION Distance(ByVal dx, ByVal dy)
    RETURN Manhattan(dx, dy)
END FUNCTION
```

**lib/Math.bas**

```vbnet
Option Explicit On
FUNCTION Manhattan(ByVal dx, ByVal dy)
    RETURN Abs(dx) + Abs(dy)
END FUNCTION
```

### 3. Inclusione ripetuta

```vb
# Common.bas e ./Common.bas sono lo stesso file: CONST e funzione dichiarate una volta. SharedValue=7; GetShared() restituisce 7, Main moltiplica per 2 e restituisce Integer 14. Entrambi usano Option Explicit On.
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Common.bas e ./Common.bas sono lo stesso file: CONST e funzione dichiarate una volta. SharedValue=7; GetShared() restituisce 7, Main moltiplica per 2 e restituisce Integer 14. Entrambi usano Option Explicit On.

**Common.bas**

```vbnet
Option Explicit On
CONST SharedValue = 7
FUNCTION GetShared()
    RETURN SharedValue
END FUNCTION
```

<!-- implementation references (not callable script procedures):
Parsing/ScriptSourceGraph.cs: Load / Builder.AddInclude / ResolveLine
Runtime/InjectionRuntime.cs: Prepare / Load
Runtime/Interpreter.cs: Location / EvaluateInitializer / CallObserved
Analysis/SanityAnalyzer.cs: Analyze
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: PrepareScriptForExecution
InjectionScript.Lsp/Workspace.cs: UpdateDiagnostic
-->
