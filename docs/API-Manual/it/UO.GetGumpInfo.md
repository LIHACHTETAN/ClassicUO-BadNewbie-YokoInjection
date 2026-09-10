# UO.GetGumpInfo

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge un’istantanea coerente di un gump del server e dei suoi controlli.

## Sintassi esatta

```text
UO.GetGumpInfo(GumpIndex:Any) -> Array
```

## Parametri

- `GumpIndex` — Integer obbligatorio: indice da 0 a GetGumpsCount()-1, non serial né GumpID. Un indice negativo o fuori elenco non è valido. Apertura, chiusura o riordino delle finestre possono cambiarlo.

## Restituisce

Array con cinque campi: [0] Integer serial; [1] Integer GumpID; [2] Array<String> di testi non vuoti; [3] Array<String> di descrizioni dei pulsanti normali; [4] Array<String> di tutti i controlli attivi, inclusi quelli annidati. Un gump non valido, chiuso o ignorato restituisce []. Gli ID con bit più alto sono Integer negativi; Hex ne mostra i bit.

## Comportamento

- Tutti i dati vengono copiati in una richiesta al thread di gioco. Modifiche o chiusure successive non cambiano gli array salvati. Sono inclusi solo gump attivi del server, non finestre locali di zaino, mappa o impostazioni.
- Questo array BASIC non è il record Pascal TGumpInfo né il pacchetto originale del layout. Le descrizioni includono tipo, page, ID, X/Y e dimensioni; i pulsanti aggiungono ButtonID, action, toPage e grafica; i selettori checked e inactive/active. Il testo può contenere spazi e =. I pulsanti di opzione sono in [4], non [3].
- AddGumpIgnoreByID/BySerial nascondono questo risultato nello script corrente; ClearGumpsIgnore rimuove il filtro. GetGumpsCount non cambia. Anche un gump esistente può avere array di testo vuoti. Usare GetArrayLength, non Len, per la lunghezza degli array.

## Esempi

### Leggere entrambi gli ID

```vb
# Leggere entrambi gli ID
#
# Legge un’istantanea coerente di un gump del server e dei suoi controlli.
#
# Array con cinque campi: [0] Integer serial; [1] Integer GumpID; [2] Array<String> di testi non
# vuoti; [3] Array<String> di descrizioni dei pulsanti normali; [4] Array<String> di tutti i
# controlli attivi, inclusi quelli annidati. Un gump non valido, chiuso o ignorato restituisce
# []. Gli ID con bit più alto sono Integer negativi; Hex ne mostra i bit.

SUB Main()
    # 0 seleziona il primo gump del server. Verificare GetArrayLength(info)=5 prima di accedere ai
    # campi. info[0] è serial, info[1] è GumpID della stessa istantanea.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        UO.Print('Serial=' + Hex(info[0]))
        UO.Print('GumpID=' + Hex(info[1]))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- 0 seleziona il primo gump del server. Verificare GetArrayLength(info)=5 prima di accedere ai campi. info[0] è serial, info[1] è GumpID della stessa istantanea.

### Elencare i veri ButtonID

```vb
# Elencare i veri ButtonID
#
# Legge un’istantanea coerente di un gump del server e dei suoi controlli.
#
# Array con cinque campi: [0] Integer serial; [1] Integer GumpID; [2] Array<String> di testi non
# vuoti; [3] Array<String> di descrizioni dei pulsanti normali; [4] Array<String> di tutti i
# controlli attivi, inclusi quelli annidati. Un gump non valido, chiuso o ignorato restituisce
# []. Gli ID con bit più alto sono Integer negativi; Hex ne mostra i bit.

SUB Main()
    # info[3] contiene descrizioni di pulsanti. i è l’indice della riga; il campo ButtonID della
    # descrizione è l’ID da usare nella risposta. I pulsanti di opzione appartengono all’elenco
    # completo.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR buttons = info[3]
        VAR i = 0
        WHILE i < GetArrayLength(buttons)
            UO.Print(buttons[i])
            i = i + 1
        WEND
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- info[3] contiene descrizioni di pulsanti. i è l’indice della riga; il campo ButtonID della descrizione è l’ID da usare nella risposta. I pulsanti di opzione appartengono all’elenco completo.

### Conservare il testo prima della chiusura

```vb
# Conservare il testo prima della chiusura
#
# Legge un’istantanea coerente di un gump del server e dei suoi controlli.
#
# Array con cinque campi: [0] Integer serial; [1] Integer GumpID; [2] Array<String> di testi non
# vuoti; [3] Array<String> di descrizioni dei pulsanti normali; [4] Array<String> di tutti i
# controlli attivi, inclusi quelli annidati. Un gump non valido, chiuso o ignorato restituisce
# []. Gli ID con bit più alto sono Integer negativi; Hex ne mostra i bit.

SUB Main()
    # info[2] è una copia del testo. CloseSimpleGump(0) chiude localmente solo senza NoClose e non
    # restituisce un valore. Il testo salvato resta disponibile; verificare la lunghezza prima di
    # texts[0].

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR texts = info[2]
        UO.CloseSimpleGump(0)
        IF GetArrayLength(texts) > 0 THEN
            UO.Print(texts[0])
        END IF
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- info[2] è una copia del testo. CloseSimpleGump(0) chiude localmente solo senza NoClose e non restituisce un valore. Il testo salvato resta disponibile; verificare la lunghezza prima di texts[0].
