# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

AndAlso e OrElse combinano condizioni saltando l’operando destro inutile. AndAlso lo salta se la sinistra è falsa; OrElse se è vera. Servono a proteggere accessi all’array ed evitare chiamate inutili.

## Sintassi esatta

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## Parametri

- `left` — left: espressione valutata per prima, una volta. Zero Integer o Decimal è falso; ogni numero diverso da zero è vero.
- `right` — right: espressione valutata una volta solo se necessaria. Letture, chiamate ed effetti saltati non avvengono. Gli operandi valutati devono essere numerici; convertire esplicitamente il testo con CBool.

## Restituisce

Integer 1 (TRUE) o 0 (FALSE), non l’operando originale. result=1 equivale a result=TRUE; result=0 a result=FALSE. Qui vero vale 1, non il -1 numerico di VB.NET. Un conteggio normale resta un conteggio; questa operazione produce un booleano.

## Comportamento

- I confronti appartengono agli operandi. AndAlso precede OrElse; operatori uguali si associano da sinistra. Le parentesi cambiano il raggruppamento. Anche le espressioni saltate sono analizzate e controllate da Option Explicit.
- Per compatibilità, sequenze AND/OR/XOR mantengono il vecchio raggruppamento immediato da sinistra dentro un operando, prima di AndAlso/OrElse. TRUE OR FALSE AndAlso FALSE dà FALSE; TRUE OrElse FALSE AND FALSE dà TRUE. Usare parentesi nei casi misti. AND, OR, && e || valutano entrambi i lati.
- Il motore valuta la sinistra, controlla la verità numerica e restituisce un booleano oppure valuta la destra necessaria. Gli errori necessari arrivano a CATCH; FINALLY e pausa/arresto restano attivi. Saltare una chiamata ne salta anche le azioni.

## Esempi

### 1. Proteggere il primo elemento

```vb
# FirstEquals riceve items ed expected. GetArrayLength(items)>0 evita items[0] negli array vuoti. Main passa [42] e un array vuoto, ottiene 1 e 0, poi restituisce 10. La funzione completa non modifica l’array.
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

FirstEquals riceve items ed expected. GetArrayLength(items)>0 evita items[0] negli array vuoti. Main passa [42] e un array vuoto, ottiene 1 e 0, poi restituisce 10. La funzione completa non modifica l’array.

### 2. Una chiamata alternativa

```vb
# Probe incrementa calls ByRef e restituisce TRUE. TRUE OrElse Probe(calls) salta la chiamata; FALSE OrElse Probe(calls) la esegue una volta. Entrambe le condizioni danno 1; Main restituisce il conteggio delle chiamate, 1.
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Probe incrementa calls ByRef e restituisce TRUE. TRUE OrElse Probe(calls) salta la chiamata; FALSE OrElse Probe(calls) la esegue una volta. Entrambe le condizioni danno 1; Main restituisce il conteggio delle chiamate, 1.

### 3. Divisione protetta e precedenza

```vb
# AverageExceeds(total, count, limit) divide solo con count>0. (25,0,10) dà 0; (25,2,10) dà 1 perché 12.5>10. TRUE OrElse FALSE AndAlso FALSE dà 1 saltando il gruppo AndAlso. Main restituisce "0:1:1".
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

AverageExceeds(total, count, limit) divide solo con count>0. (25,0,10) dà 0; (25,2,10) dà 1 perché 12.5>10. TRUE OrElse FALSE AndAlso FALSE dà 1 saltando il gruppo AndAlso. Main restituisce "0:1:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
