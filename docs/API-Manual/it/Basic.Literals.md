# 123 / 0x0EED / "text" / TRUE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Un letterale scrive direttamente un valore nel codice. Numeri e testi tra virgolette non richiedono dichiarazioni. TRUE/FALSE sono valori logici predefiniti. Un numero tra virgolette rimane testo fino alla conversione.

## Sintassi esatta

```text
123
-2147483648
0x0EED
0xFFFFFFFF
2.5
"text"
'text'
TRUE
FALSE
```

## Parametri

- `integer / hexadecimal` — Integer decimale da -2147483648 a 2147483647 oppure 0x con cifre esadecimali 0–9/A–F. Usare x minuscola. Il letterale rappresenta 32 bit: 0xFFFFFFFF è Integer -1, non un positivo a 64 bit.
- `floating` — Numero mobile con cifre prima e dopo il punto: 2.5 o -0.25. Scrivere 0.5 anziché .5. Virgola, esponente 1e3 e suffissi numerici non sono supportati da questa grammatica.
- `text` — Testo tra virgolette semplici o doppie corrispondenti. Per includerne una usare l’altro tipo o Chr(34)/Chr(39). Escape con barra inversa e virgolette raddoppiate non vengono interpretati. Tenere la stringa d’esempio su una riga fisica.
- `TRUE / FALSE` — TRUE è Integer 1; FALSE è Integer 0. Non ridichiarare questi nomi. Sono valori e non chiamate: TRUE, non TRUE().

## Restituisce

Intero/esadecimale dà Integer; numero con punto dà Decimal, mobile binario; testo tra virgolette dà String. TRUE/FALSE danno Integer 1/0. Valutare un valore non effettua azioni di gioco né dichiara variabili.

## Comportamento

- Il segno di -5 è un’operazione unaria. -2147483648 viene gestito come minimo intero senza dover prima memorizzare il modulo positivo. Interi fuori intervallo falliscono; valori approssimati maggiori richiedono numeri mobili adeguati.
- Il testo conserva caratteri e maiuscole. "350" non è il numero 350; "false" non è FALSE. # e ; nelle virgolette sono testo, fuori iniziano commenti. Le conversioni sono spiegate in AS e nelle schede delle funzioni.
- Il motore riconosce il token, interpreta i numeri con cultura invariabile o rimuove le virgolette esterne. La lingua dell’IDE non cambia il separatore decimale del sorgente.
- Serial, tipo grafico e coordinata possono tutti essere numeri. Il letterale non impone il significato: lo stabilisce il parametro del comando chiamato.

## Esempi

### 1. Tipo esadecimale e limite intero

```vb
# itemType=0x0EED equivale a 3821. lowest=-2147483648 coincide con la configurazione con segno 0x80000000. Main restituisce itemType=3821. Non viene cercato alcun oggetto.
Option Explicit On
SUB Main()
    VAR itemType = 0x0EED
    VAR lowest = -2147483648
    IF lowest = 0x80000000 THEN
        RETURN itemType
    END IF
    RETURN 0
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

itemType=0x0EED equivale a 3821. lowest=-2147483648 coincide con la configurazione con segno 0x80000000. Main restituisce itemType=3821. Non viene cercato alcun oggetto.

### 2. Entrambi i tipi di virgolette

```vb
# owner="O'Brien" contiene un apostrofo. instruction usa virgolette semplici attorno a testo con doppie. Unire owner, " | " e instruction dà O'Brien | say "go", senza escape con barra inversa nello script.
Option Explicit On
SUB Main()
    VAR owner = "O'Brien"
    VAR instruction = 'say "go"'
    RETURN owner + " | " + instruction
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

owner="O'Brien" contiene un apostrofo. instruction usa virgolette semplici attorno a testo con doppie. Unire owner, " | " e instruction dà O'Brien | say "go", senza escape con barra inversa nello script.

### 3. Valori logici numerici

```vb
# enabled=TRUE memorizza 1; stopped=FALSE memorizza 0. Il calcolo dà 1*10+0=10. Main restituisce un risultato numerico, non il TRUE canonico.
Option Explicit On
SUB Main()
    VAR enabled = TRUE
    VAR stopped = FALSE
    RETURN enabled * 10 + stopped
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

enabled=TRUE memorizza 1; stopped=FALSE memorizza 0. Il calcolo dà 1*10+0=10. Main restituisce un risultato numerico, non il TRUE canonico.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: number / literal / HEX_NUMBER / DEC_NUMBER
Runtime/Interpreter.cs: VisitNumber / VisitLiteral / VisitSignedOperand
Runtime/InjectionApiUO.cs: TRUE / FALSE intrinsic values
-->
