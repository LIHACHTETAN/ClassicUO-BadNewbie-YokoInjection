# UO.GetFoundedText

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge il testo memorizzato della voce del diario selezionata da questo script.

## Sintassi esatta

```text
UO.GetFoundedText() -> String
```

## Parametri

Nessun parametro.

## Restituisce

String — testo selezionato, oppure stringa vuota se non è selezionata alcuna voce. Anche una voce esistente può avere testo vuoto. Non è un serial, un indice o un valore booleano di successo.

## Comportamento

- InJournal, InJournalBetweenTimes, Journal/GetJournal e LastJournalMessage sostituiscono la selezione. Una ricerca senza risultati, un indice Journal non valido o la cancellazione da questo script la azzera. Nessun argomento; nessuna nuova ricerca.
- I nuovi messaggi non sostituiscono il testo memorizzato. Se la voce viene rimossa, il testo resta disponibile, mentre GetFoundedTextIndex/LineIndex diventa -1. Un altro script può svuotare il diario condiviso; le variabili salvate non cambiano.

## Esempi

### Leggere un messaggio trovato

```vb
# Leggere un messaggio trovato
#
# Legge il testo memorizzato della voce del diario selezionata da questo script.
#
# String — testo selezionato, oppure stringa vuota se non è selezionata alcuna voce. Anche una
# voce esistente può avere testo vuoto. Non è un serial, un indice o un valore booleano di
# successo.

SUB Main()
    # needle è una sottostringa con distinzione tra maiuscole e minuscole. Controllare InJournal >
    # 0: il risultato è la posizione più 1, non il numero di corrispondenze.

    IF UO.InJournal('needle') > 0 THEN
        VAR text = UO.GetFoundedText()
        UO.Print(text)
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- needle è una sottostringa con distinzione tra maiuscole e minuscole. Controllare InJournal > 0: il risultato è la posizione più 1, non il numero di corrispondenze.

### Leggere una riga selezionata

```vb
# Leggere una riga selezionata
#
# Legge il testo memorizzato della voce del diario selezionata da questo script.
#
# String — testo selezionato, oppure stringa vuota se non è selezionata alcuna voce. Anche una
# voce esistente può avere testo vuoto. Non è un serial, un indice o un valore booleano di
# successo.

SUB Main()
    # Journal(0) seleziona la voce più recente. Salvare testo e indice prima di Print, che può
    # aggiungere un messaggio. Il testo vuoto non dimostra l’assenza della voce.

    VAR latest = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR text = UO.GetFoundedText()
    IF index >= 0 THEN
        UO.Print(text)
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Journal(0) seleziona la voce più recente. Salvare testo e indice prima di Print, che può aggiungere un messaggio. Il testo vuoto non dimostra l’assenza della voce.

### Conservare il testo prima di un’altra ricerca

```vb
# Conservare il testo prima di un’altra ricerca
#
# Legge il testo memorizzato della voce del diario selezionata da questo script.
#
# String — testo selezionato, oppure stringa vuota se non è selezionata alcuna voce. Anche una
# voce esistente può avere testo vuoto. Non è un serial, un indice o un valore booleano di
# successo.

SUB Main()
    # saved copia il primo risultato prima che la seconda ricerca sostituisca la selezione. Messaggi
    # e ricerche successivi non modificano questa variabile.

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.GetFoundedText()
        VAR another = UO.InJournal('failed')
        UO.Print(saved)
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- saved copia il primo risultato prima che la seconda ricerca sostituisca la selezione. Messaggi e ricerche successivi non modificano questa variabile.
