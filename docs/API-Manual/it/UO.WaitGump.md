# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Registra una sequenza ordinata di risposte singole ai pulsanti. Lo script prosegue subito; una finestra assente non lo blocca per 30 secondi.

## Sintassi esatta

```text
UO.WaitGump(Value:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any, trigger16:Any) -> Unit
UO.WaitGump(triggerId:Integer) -> Unit
UO.WaitGump(triggerId:String) -> Unit
```

## Parametri

- `triggerId` — Integer ButtonID o String numerica. Una stringa può contenere una sequenza separata da | o virgole. Le forme con 2..16 argomenti accettano anche array e sequenze annidate. Gli ID vengono analizzati prima della registrazione. Sequenza vuota, oltre 256 pulsanti in attesa nel client o oltre 32 livelli generano un errore senza registrazione parziale.
- `Value` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger1` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger2` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger3` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger4` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger5` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger6` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger7` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger8` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger9` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger10` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger11` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger12` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger13` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger14` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger15` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.
- `trigger16` — Elemento della sequenza: Integer ButtonID, String numerica, stringa separata da |/virgole o Array di tali elementi. Da sinistra a destra secondo limiti e regole di triggerId. Value è il nome del singolo parametro Any, che accetta anche un array.

## Restituisce

Unit — nessun valore restituito: né successo, né nuovo valore, né conferma del server.

## Comportamento

- Serve un vero pulsante Activate con il ButtonID richiesto; cambi di pagina e finestre non corrispondenti vengono ignorati. Gli ID successivi non superano il primo in attesa. Al massimo una risposta per finestra a ogni ricezione della disposizione. Una disposizione ricostruita può riutilizzare lo stesso oggetto finestra.
- Un altro WaitGump dello stesso script aggiunge alla sua sequenza in attesa. Nessun filtro GumpID: usare NumGumpButton o SendGumpSelect per la selezione precisa. ButtonID=0 richiede un pulsante Activate reale con ID 0; non è una chiusura universale.
- La conclusione normale della procedura conserva le azioni. L’annullamento del proprietario o Terminate con il suo nome le rimuove; TerminateAll le rimuove tutte, anche quelle di procedure concluse. Cambiare mondo svuota la coda. Nessun salvataggio nel profilo.

## Esempi

### Una risposta

```vb
# Una risposta
#
# Registra una sequenza ordinata di risposte singole ai pulsanti. Lo script prosegue subito; una
# finestra assente non lo blocca per 30 secondi.
#
# Unit — nessun valore restituito: né successo, né nuovo valore, né conferma del server.

SUB Main()
    # 100 è il ButtonID della risposta. WaitGump lo registra prima di UseObject; la prosecuzione
    # dello script non prova la conferma del server.

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- 100 è il ButtonID della risposta. WaitGump lo registra prima di UseObject; la prosecuzione dello script non prova la conferma del server.

### Più passaggi

```vb
# Più passaggi
#
# Registra una sequenza ordinata di risposte singole ai pulsanti. Lo script prosegue subito; una
# finestra assente non lo blocca per 30 secondi.
#
# Unit — nessun valore restituito: né successo, né nuovo valore, né conferma del server.

SUB Main()
    # 7, 22 e 1 sono ButtonID di moduli successivi, controllati in questo ordine. Il numero di
    # argomenti non è un ritardo; viene registrata l’intera sequenza.

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- 7, 22 e 1 sono ButtonID di moduli successivi, controllati in questo ordine. Il numero di argomenti non è un ritardo; viene registrata l’intera sequenza.

### Annullare le attese

```vb
# Annullare le attese
#
# Registra una sequenza ordinata di risposte singole ai pulsanti. Lo script prosegue subito; una
# finestra assente non lo blocca per 30 secondi.
#
# Unit — nessun valore restituito: né successo, né nuovo valore, né conferma del server.

SUB Main()
    # La stringa 7|22|1 descrive la stessa sequenza. TerminateAll elimina tutte le azioni gump in
    # attesa e arresta tutte le procedure; l’effetto è globale.

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- La stringa 7|22|1 descrive la stessa sequenza. TerminateAll elimina tutte le azioni gump in attesa e arresta tutte le procedure; l’effetto è globale.
