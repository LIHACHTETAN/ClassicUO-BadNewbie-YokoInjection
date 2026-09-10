# String + / &

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Unire testo con + oppure la notazione Basic compatibile &. Convertire i numeri esplicitamente con CStr prima di aggiungere etichette, quantità o coordinate.

## Sintassi esatta

```text
leftText + rightText
leftText & rightText
"label" & CStr(number)
```

## Parametri

- `leftText` — Testo sinistro: letterale, variabile String o risultato di funzione convertito in testo.
- `rightText` — Testo destro. CStr(number) converte un numero; CStr(Unit) dà testo vuoto. Specificare spazi, due punti e altri separatori.

## Restituisce

String se entrambi gli operandi sono String, senza flag di successo. Qui & viene normalizzato in + e ne eredita le regole: due numeri si sommano, quindi 2 & 3 dà Integer 5. Mescolare String e numero genera errore. È diverso dalla conversione implicita di VB.

## Comportamento

- Entrambe le parti vengono valutate e unite nell’ordine, da sinistra a destra nelle catene. Calcolare un’espressione numerica tra parentesi e convertirne il risultato prima di unirla.
- Nessun separatore, spazio, virgolette o nuova riga viene aggiunto automaticamente. & in un letterale rimane tale. Il token logico && resta AND e non concatena testo.
- CStr formatta i numeri indipendentemente dalla lingua del client, con punto decimale. Conversione e concatenazione non stampano e non inviano nulla; passare poi la String a un’API se necessario.
- Le stringhe sono immutabili: l’unione crea un nuovo valore senza modificare le sorgenti. Accrescere continuamente una lunga stringa ne copia il contenuto; generare soltanto l’output necessario, non l’intero rapporto a ogni iterazione.

## Esempi

### 1. Quantità con etichetta

```vb
# amount=50 è Integer. CStr(amount) dà "50". "Items: " include due punti e uno spazio finale. Main restituisce "Items: 50" senza stamparlo automaticamente.
Option Explicit On
SUB Main()
    VAR amount = 50
    RETURN "Items: " & CStr(amount)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

amount=50 è Integer. CStr(amount) dà "50". "Items: " include due punti e uno spazio finale. Main restituisce "Items: 50" senza stamparlo automaticamente.

### 2. Funzione completa di formattazione

```vb
# Label riceve name="ore", amount=3. Unisce nome, due punti espliciti e CStr(amount). La funzione completa restituisce "ore:3" a Main ed è riutilizzabile con altri nomi e quantità.
Option Explicit On
FUNCTION Label(name, amount)
    RETURN name + ":" + CStr(amount)
END FUNCTION
SUB Main()
    RETURN Label("ore", 3)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Label riceve name="ore", amount=3. Unisce nome, due punti espliciti e CStr(amount). La funzione completa restituisce "ore:3" a Main ed è riutilizzabile con altri nomi e quantità.

### 3. Calcolare prima di unire

```vb
# CStr(2+3) calcola prima 5 e lo converte in "5". Il secondo letterale mantiene punto e virgola, spazi e A&B. Main restituisce "Total: 5; literal: A&B".
Option Explicit On
SUB Main()
    RETURN "Total: " & CStr(2 + 3) & "; literal: A&B"
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

CStr(2+3) calcola prima 5 e lo converte in "5". Il secondo letterale mantiene punto e virgola, spazi e A&B. Main restituisce "Total: 5; literal: A&B".

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: ProtectLiteralText / ReplaceConcatenationOutsideLiterals
Runtime/InjectionValue.cs: operator + / explicit operator string
Runtime/InjectionApi.cs: CStr
-->
