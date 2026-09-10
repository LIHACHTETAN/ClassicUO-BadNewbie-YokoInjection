# +, -, *, /, MOD

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Un’espressione aritmetica calcola un valore: + somma, - sottrae o cambia segno, * moltiplica, / divide, MOD restituisce il resto intero. Assegnare il risultato a una variabile oppure restituirlo con RETURN.

## Sintassi esatta

```text
left + right
left - right
-right
left * right
left / right
left MOD right
(expression)
```

## Parametri

- `left` — Operando numerico sinistro: letterale, variabile dichiarata, espressione tra parentesi o risultato di funzione. Il meno unario non ha operando sinistro.
- `right` — Operando numerico destro. Per / è il divisore; per MOD deve rimanere diverso da zero dopo la conversione in Integer. Ad esempio 0.5 viene troncato a 0 e causa un errore.
- `operator / precedence` — Precedenza: meno unario, poi * / MOD allo stesso livello da sinistra a destra, poi + - binari da sinistra a destra. Le parentesi modificano l’ordine. Più unario, potenza ^ e divisione intera con barra inversa non sono supportati.

## Restituisce

Integer per +, -, * e meno unario su interi; Decimal se un operando numerico coinvolto è Decimal. / restituisce sempre Decimal: 5/2=2.5. MOD restituisce Integer. È un numero calcolato; il significato di successo o quantità dipende dallo script.

## Comportamento

- MOD converte entrambi gli operandi in interi con segno a 32 bit, troncando verso zero le frazioni rappresentabili. Il resto conserva il segno del dividendo: -17 MOD 5=-2; -2147483648 MOD -1=0. Anche la grafia mOd funziona.
- MOD per zero genera un errore gestibile con TRY/CATCH. / usa la divisione in virgola mobile: un numeratore non nullo diviso per zero produce Infinity con segno, 0/0 produce NaN. Controllare il divisore se serve un risultato finito.
- Le operazioni intere +, -, * e negazione mantengono i 32 bit bassi in caso di overflow, senza promozione automatica. Convertire prima un operando in Decimal per grandi calcoli se l’approssimazione è accettabile. I calcoli decimali hanno arrotondamenti binari.
- Gli operatori numerici ordinari non interpretano automaticamente il testo. String+String concatena, String+Integer fallisce. Usare una conversione esplicita, ad esempio CDbl. MOD infisso interpreta il testo intero più rigorosamente della funzione separata BasicMod.
- L’interprete valuta gli operandi nell’ordine dell’espressione, seleziona il token operatore e crea una InjectionValue. Le espressioni tra parentesi terminano prima. Movimento, attesa o rete avvengono solo se un operando richiama una relativa API.

## Esempi

### 1. Precedenza e parentesi

```vb
# plain=2+3*4 esegue prima la moltiplicazione e vale 14. grouped=(2+3)*4 vale 20. Main restituisce plain*100+grouped=1420 per verificare entrambi i calcoli.
Option Explicit On
SUB Main()
    VAR plain = 2 + 3 * 4
    VAR grouped = (2 + 3) * 4
    RETURN plain * 100 + grouped
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

plain=2+3*4 esegue prima la moltiplicazione e vale 14. grouped=(2+3)*4 vale 20. Main restituisce plain*100+grouped=1420 per verificare entrambi i calcoli.

### 2. Gruppi completi e oggetti rimasti

```vb
# DescribeBatches riceve total=27 e size=5. La guardia rifiuta dimensioni nulle o negative. Fix(total/size) trasforma 5.4 in 5 gruppi completi; total mOd size dà 2 oggetti rimasti. CStr converte i numeri nel testo restituito "5:2". La funzione ausiliaria è definita per intero.
Option Explicit On
FUNCTION DescribeBatches(total, size)
    IF size <= 0 THEN
        RETURN "invalid"
    END IF
    VAR whole = Fix(total / size)
    VAR remaining = total mOd size
    RETURN CStr(whole) + ":" + CStr(remaining)
END FUNCTION
SUB Main()
    RETURN DescribeBatches(27, 5)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

DescribeBatches riceve total=27 e size=5. La guardia rifiuta dimensioni nulle o negative. Fix(total/size) trasforma 5.4 in 5 gruppi completi; total mOd size dà 2 oggetti rimasti. CStr converte i numeri nel testo restituito "5:2". La funzione ausiliaria è definita per intero.

### 3. Gestire un divisore non valido

```vb
# 10 MOD 0 genera un errore prima dell’assegnazione a unusedResult. CATCH lo salva in problem e imposta caught=TRUE. Main restituisce 1 come indicatore della gestione dell’errore nell’esempio, non come risultato del MOD fallito.
Option Explicit On
SUB Main()
    VAR caught = FALSE
    TRY
        VAR unusedResult = 10 MOD 0
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

10 MOD 0 genera un errore prima dell’assegnazione a unusedResult. CATCH lo salva in problem e imposta caught=TRUE. Main restituisce 1 come indicatore della gestione dell’errore nell’esempio, non come risultato del MOD fallito.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: signedOperand / additiveOperand / comparativeOperand
Runtime/Interpreter.cs: VisitSignedOperand / VisitAdditiveOperand / VisitComparativeOperand
Runtime/InjectionValue.cs: arithmetic operators
Runtime/NumberConversions.cs: ToInt
-->
