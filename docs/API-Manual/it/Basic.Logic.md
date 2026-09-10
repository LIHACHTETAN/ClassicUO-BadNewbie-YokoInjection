# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

NOT inverte una condizione. AND richiede entrambe, OR almeno una, XOR esattamente una. && equivale a AND e || a OR. Le parole chiave non distinguono le maiuscole.

## Sintassi esatta

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## Parametri

- `left` — Condizione binaria sinistra. AND/OR richiedono Integer o Decimal: zero è falso, ogni numero non nullo è vero.
- `right` — Condizione destra, numerica anche per AND/OR. Entrambi gli operandi vengono valutati: un AND sinistro falso o un OR sinistro vero non salta questa espressione.
- `NOT / grouping` — Per NOT racchiudere l’intera condizione da invertire tra parentesi. Nelle combinazioni di AND, OR e XOR indicare esplicitamente il raggruppamento.

## Restituisce

Integer 1 (TRUE) oppure Integer 0 (FALSE). Sono operazioni logiche, non bit a bit: 2 AND 4 dà 1, non una maschera. Verificare il flag restituito con =TRUE o =1, =FALSE o =0.

## Comportamento

- In questo motore AND, OR e XOR hanno la stessa precedenza da sinistra a destra: TRUE OR FALSE AND FALSE dà 0; TRUE OR (FALSE AND FALSE) dà 1. Considerare questa regola storica adattando codice VB.
- NOT(condition) valuta la condizione e la inverte. All’inizio di un confronto NOT 1=2 significa NOT(1=2). Scrivere (NOT value) se il valore invertito è esso stesso operando di un confronto.
- AND/OR rifiutano String, Array, Object e Unit. I NOT e XOR storici verificano invece l’uguaglianza allo zero numerico: "0", testo vuoto, array, oggetti e Unit risultano non nulli. Definire condizioni numeriche esplicite per tali valori; CBool ha proprie regole di conversione.
- Ogni espressione destra viene eseguita, incluse funzioni, attese ed errori. Le parentesi cambiano il raggruppamento, non questa valutazione obbligatoria. Usare IF annidati se un’espressione deve essere eseguita solo dopo una condizione riuscita.

## Esempi

### 1. Combinare flag nominati

```vb
# ready=TRUE, blocked=FALSE. NOT(blocked) dà 1, quindi canRun vale 1. ready XOR blocked è vero perché un solo flag è vero. Main restituisce canRun*10+exclusive=11.
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

ready=TRUE, blocked=FALSE. NOT(blocked) dà 1, quindi canRun vale 1. ready XOR blocked è vero perché un solo flag è vero. Main restituisce canRun*10+exclusive=11.

### 2. Osservare entrambe le chiamate

```vb
# Mark incrementa counter passato ByRef e restituisce TRUE. Main parte da counter=0. FALSE AND Mark(counter) chiama comunque Mark; TRUE OR Mark(counter) lo chiama ancora. Le condizioni valgono 0 e 1, ma Main restituisce counter=2. Mark è definita per intero.
Option Explicit On
FUNCTION Mark(ByRef counter)
    counter = counter + 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR counter = 0
    VAR first = FALSE AND Mark(counter)
    VAR second = TRUE OR Mark(counter)
    RETURN counter
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Mark incrementa counter passato ByRef e restituisce TRUE. Main parte da counter=0. FALSE AND Mark(counter) chiama comunque Mark; TRUE OR Mark(counter) lo chiama ancora. Le condizioni valgono 0 e 1, ma Main restituisce counter=2. Mark è definita per intero.

### 3. Rendere esplicito il gruppo

```vb
# legacy calcola TRUE OR FALSE, poi AND FALSE e dà 0. grouped calcola prima FALSE AND FALSE tra parentesi, poi OR con TRUE e dà 1. Main restituisce legacy*10+grouped=1.
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

legacy calcola TRUE OR FALSE, poi AND FALSE e dà 0. grouped calcola prima FALSE AND FALSE tra parentesi, poi OR con TRUE e dà 1. Main restituisce legacy*10+grouped=1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
