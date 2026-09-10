# UO.GumpAutoTextEntry

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Imposta una volta il valore del primo controllo corrispondente in un gump del server; se manca, conserva un’azione in attesa.

## Sintassi esatta

```text
UO.GumpAutoTextEntry(TextEntryID:Any, Value:Any) -> Unit
```

## Parametri

- `TextEntryID` — Integer — ID esatto del tipo di controllo richiesto. Non è un indice, un GumpID o il serial della finestra. 0 è un ID ordinario, senza selezione automatica del primo elemento.
- `Value` — String — testo del campo; una stringa vuota lo cancella. Restano validi i limiti di lunghezza e caratteri del campo.

## Restituisce

Unit — nessun valore restituito: né successo, né nuovo valore, né conferma del server.

## Comportamento

- Controlla le finestre esistenti nell’ordine corrente dell’interfaccia, poi le disposizioni ricevute o ricostruite dal server. Il primo tipo e ID corrispondente consuma l’azione. Usare NumGump* con indice per una finestra precisa.
- I campi in attesa vengono compilati prima delle risposte automatiche. Ripetere tipo e ID nello stesso script sostituisce il valore ancora in attesa. Il client ammette 1024 campi in attesa; superare il limite genera un errore dello script.
- La conclusione normale della procedura conserva le azioni. L’annullamento del proprietario o Terminate con il suo nome le rimuove; TerminateAll le rimuove tutte, anche quelle di procedure concluse. Cambiare mondo svuota la coda. Nessun salvataggio nel profilo.
- Il campo può troncare o rifiutare il testo; trovare il controllo consuma comunque l’azione. Il comando non risponde con un pulsante e non attende il server. Verificare il testo con GetGumpInfo/NumGumpTextEntry.

## Esempi

### Compilare un controllo aperto

```vb
# Compilare un controllo aperto
#
# Imposta una volta il valore del primo controllo corrispondente in un gump del server; se
# manca, conserva un’azione in attesa.
#
# Unit — nessun valore restituito: né successo, né nuovo valore, né conferma del server.

SUB Main()
    # 33 è un ID di esempio: sostituirlo con quello reale da InfoGump. Il secondo argomento è il
    # valore. Se il controllo manca, l’azione rimane in attesa.

    UO.GumpAutoTextEntry(33, '500')
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- 33 è un ID di esempio: sostituirlo con quello reale da InfoGump. Il secondo argomento è il valore. Se il controllo manca, l’azione rimane in attesa.

### Compilare prima dell’apertura

```vb
# Compilare prima dell’apertura
#
# Imposta una volta il valore del primo controllo corrispondente in un gump del server; se
# manca, conserva un’azione in attesa.
#
# Unit — nessun valore restituito: né successo, né nuovo valore, né conferma del server.

SUB Main()
    # 33 è l’ID del controllo, 100 un ButtonID di conferma di esempio, 0x40001234 il serial
    # dell’oggetto che apre il modulo. Sostituirli tutti. Il campo viene compilato prima della
    # risposta anche se la finestra arriva dopo.

    UO.GumpAutoTextEntry(33, '500')
    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- 33 è l’ID del controllo, 100 un ButtonID di conferma di esempio, 0x40001234 il serial dell’oggetto che apre il modulo. Sostituirli tutti. Il campo viene compilato prima della risposta anche se la finestra arriva dopo.

### Sostituire un valore in attesa

```vb
# Sostituire un valore in attesa
#
# Imposta una volta il valore del primo controllo corrispondente in un gump del server; se
# manca, conserva un’azione in attesa.
#
# Unit — nessun valore restituito: né successo, né nuovo valore, né conferma del server.

SUB Main()
    # Entrambe le chiamate usano ID 33. Se il controllo non è ancora arrivato, resta l’ultimo
    # valore. Se è aperto, entrambe le modifiche avvengono subito nell’ordine delle chiamate.

    UO.GumpAutoTextEntry(33, '500')
    UO.GumpAutoTextEntry(33, '')
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Entrambe le chiamate usano ID 33. Se il controllo non è ancora arrivato, resta l’ultimo valore. Se è aperto, entrambe le modifiche avvengono subito nell’ordine delle chiamate.
