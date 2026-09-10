# VAR / DIM

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

VAR e DIM scalare dichiarano un valore con nome. L’assegnazione valuta l’espressione e conserva il risultato. Una dichiarazione dentro una procedura è locale alla chiamata; fuori dalle procedure è globale allo script.

## Sintassi esatta

```text
VAR name [AS type] [= expression] [, name ...]
DIM name [AS type] [= expression] [, name ...]
name = expression
LET name = expression
SET name = expression
```

## Parametri

- `name` — Identificatore senza virgolette: lettere, cifre e trattini bassi, iniziando con una lettera o un trattino basso. Mantenere la stessa grafia ed evitare parole chiave.
- `type` — AS facoltativo. Integer/Long/Short/Byte usano la conversione intera con segno a 32 bit del motore; Double/Single/Decimal il suo numero a doppia precisione; String testo; Boolean/Bool un valore logico; Variant/Object conservano il tipo del valore. Gli alias non impongono intervalli byte/short/long distinti di VB.NET.
- `expression` — Inizializzatore facoltativo in VAR/DIM, espressione destra obbligatoria nell’assegnazione. Si valuta quando viene eseguita la riga. AS String senza inizializzazione parte da testo vuoto; i numeri tipizzati e Boolean partono da zero. Senza inizializzatore, VAR senza tipo e VAR AS Variant/Object contengono Unit (nessun valore), mentre DIM scalare fornisce 0. Una variabile senza tipo può poi contenere un valore di tipo diverso.

## Restituisce

Nessun valore. VAR, DIM e l’assegnazione non restituiscono risultati. Leggere il nome fornisce il valore conservato. RETURN negli esempi restituisce quel valore da Main, non da DIM.

## Comportamento

- Le parentesi quadre nella sintassi indicano parti facoltative; non scriverle intorno ad AS o all’inizializzatore. DIM per array ha una forma diversa.
- LET e SET sono forme compatibili dell’assegnazione ordinaria. Con Option Explicit On non dichiarano nomi. AS si applica anche alle assegnazioni successive; una conversione non valida o un tipo non supportato produce un errore di esecuzione.
- I nomi locali appartengono alla chiamata di procedura. Una dichiarazione in IF non crea un ambito separato. Un ramo mai eseguito non crea un valore durante l’esecuzione. Dichiarare prima della diramazione se il valore serve dopo.
- Compatibilità Injection: la procedura chiamata eredita i valori scalari globali correnti del chiamante e i loro tipi AS. Riassegnare uno scalare nella procedura chiamata non modifica il chiamante. Restituire il nuovo valore o passare un argomento BYREF per aggiornarlo. I valori Array/Object non vengono clonati in profondità. Una nuova esecuzione principale inizializza nuovamente le globali; una dichiarazione locale nasconde il nome nel proprio ambito senza sostituire quella globale.
- Il motore valuta l’inizializzatore, definisce lo spazio nell’ambito corrente e converte il tipo. Le assegnazioni successive valutano prima il lato destro. I calcoli sono locali; le variabili non vengono salvate automaticamente in un profilo o file JSON.

## Esempi

### 1. Aggiornare un intero

```vb
# count parte da 0, riceve 5, poi LET aggiunge 2. Main restituisce Integer 7. Il primo DIM dichiara il nome; le assegnazioni successive aggiornano il valore.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    LET count = count + 2
    RETURN count
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

count parte da 0, riceve 5, poi LET aggiunge 2. Main restituisce Integer 7. Il primo DIM dichiara il nome; le assegnazioni successive aggiornano il valore.

### 2. Testo e valore logico

```vb
# label parte come String vuota. SET memorizza "ore". enabled è Boolean TRUE; il ramo IF restituisce String "ore". TRUE senza virgolette rappresenta 1 logico.
Option Explicit On
SUB Main()
    DIM label AS String
    VAR enabled AS Boolean = TRUE
    SET label = "ore"
    IF enabled = TRUE THEN
        RETURN label
    END IF
    RETURN "disabled"
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

label parte come String vuota. SET memorizza "ore". enabled è Boolean TRUE; il ramo IF restituisce String "ore". TRUE senza virgolette rappresenta 1 logico.

### 3. Dato globale e calcolo locale

```vb
# baseAmount è globale e vale 4. extra è locale a Calculate e vale 3. Calculate restituisce 7; Main lo salva nel proprio result locale e restituisce 7. extra non è una variabile locale di Main.
Option Explicit On
VAR baseAmount AS Integer = 4
FUNCTION Calculate()
    VAR extra = 3
    RETURN baseAmount + extra
END FUNCTION
SUB Main()
    VAR result = Calculate()
    RETURN result
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

baseAmount è globale e vale 4. extra è locale a Calculate e vale 3. Calculate restituisce 7; Main lo salva nel proprio result locale e restituisce 7. extra non è una variabile locale di Main.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim
Runtime/Interpreter.cs: VisitVarDef / VisitAssignment
Runtime/SemanticScope.cs: DefineVar / SetVar / Coerce
-->
