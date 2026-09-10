# UO.IsWorldCellPassable

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Verifica un passaggio alla cella vicina e restituisce percorribilità e altezza.

## Sintassi esatta

```text
UO.IsWorldCellPassable(CurrX:Any, CurrY:Any, CurrZ:Any, DestX:Any, DestY:Any, DestZ:Any, WorldNum:Any) -> Array
```

## Parametri

- `CurrX` — Coordinata mondiale X obbligatoria della cella iniziale: intero 0..65535 nella mappa caricata, non una coordinata del gump.
- `CurrY` — Coordinata mondiale Y obbligatoria della cella iniziale: intero 0..65535 nella mappa caricata, non una coordinata del gump.
- `CurrZ` — Altezza iniziale obbligatoria −128..127, non numero di piano. Le altezze non valide sono rifiutate, non limitate.
- `DestX` — Coordinata mondiale X obbligatoria della cella di destinazione: intero 0..65535 nella mappa caricata, non una coordinata del gump.
- `DestY` — Coordinata mondiale Y obbligatoria della cella di destinazione: intero 0..65535 nella mappa caricata, non una coordinata del gump.
- `DestZ` — Z di riserva in ingresso obbligatoria, di solito CurrZ. Non è var: la variabile non cambia e non imposta un piano. Leggere l’altezza calcolata da result[1]. Questo bridge fornisce sempre la propria altezza; l’argomento conserva la forma Pascal.
- `WorldNum` — Numero mappa obbligatorio: UO.WorldNum(). Verifica solo la mappa attuale con dimensioni note; non carica altre mappe.

## Restituisce

Array di due Integer: [0] — percorribilità, 1 = TRUE, 0 = FALSE; [1] — Z calcolata. Solo il primo elemento è logico; non confrontare l’array con TRUE. Altezze nulle/negative sono valide; con [0]=0 non dimostrano raggiungibilità. Argomenti rifiutati restituiscono [0, CurrZ].

## Comportamento

- Nessun movimento, apertura di porte, bersaglio o pacchetto di rete. Legge geometria locale esistente; il server può rifiutare un passo successivo. Le letture sono istantanee separate.
- Cella vicina: differenze X/Y non oltre 1. Destinazioni lontane, coordinate fuori mappa, personaggio/mappa assente o IsDestroyed sono rifiutati prima delle collisioni. Per l’intero percorso: GetPathArray o NewMoveXY.
- X/Y identiche e valide danno [1, CurrZ] senza collisioni: non serve un passo. Non verifica la possibilità di lasciare la cella. Stato del personaggio e regole Pathfinder influenzano il passo vicino; geometria non caricata può causare rifiuto.

### Funzioni interne: dalla chiamata al risultato

Queste sono le vere fasi interne C#. IsCellOpen è una funzione ausiliaria completamente definita nell’esempio, non un comando integrato nascosto.

#### 1. ExecuteStealthCompatibility

Legge sette argomenti Integer. DestZ serve solo se un altro bridge non fornisce altezza. Restituisce un array senza modificare argomenti.

Array di due Integer: [0] — percorribilità, 1 = TRUE, 0 = FALSE; [1] — Z calcolata. Solo il primo elemento è logico; non confrontare l’array con TRUE. Altezze nulle/negative sono valide; con [0]=0 non dimostrano raggiungibilità. Argomenti rifiutati restituiscono [0, CurrZ].

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ExecuteStealthCompatibility`.

#### 2. CheckWorldStep

Invoke verifica personaggio, mappa, dimensioni, coordinate, altezza e adiacenza prima della sottrazione; sceglie la direzione. Richiede X/Y finali esatte dopo CanWalkForQuery.

Array di due Integer: [0] — percorribilità, 1 = TRUE, 0 = FALSE; [1] — Z calcolata. Solo il primo elemento è logico; non confrontare l’array con TRUE. Altezze nulle/negative sono valide; con [0]=0 non dimostrano raggiungibilità. Argomenti rifiutati restituiscono [0, CurrZ].

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `CheckWorldStep`.

#### 3. CanWalkForQuery

Rimuove temporaneamente il predicato di celle vietate di un altro percorso, lo ripristina in finally e chiama CanWalk senza avviare un percorso.

Nessun movimento, apertura di porte, bersaglio o pacchetto di rete. Legge geometria locale esistente; il server può rifiutare un passo successivo. Le letture sono istantanee separate.

Sorgente del progetto: `src/ClassicUO.Client/Game/Pathfinder.cs`; funzione `CanWalkForQuery`.

#### 4. CanWalk

Verifica passo principale e lati diagonali. Restituisce bool e aggiorna coordinate ref solo per un passo accettato.

Le funzioni di collisione leggono geometria caricata e stato del personaggio. Un ripiego laterale diagonale non equivale a raggiungere la cella richiesta.

Sorgente del progetto: `src/ClassicUO.Client/Game/Pathfinder.cs`; funzione `CanWalk`.

#### 5. CalculateNewZ

Riceve X/Y di destinazione, Z iniziale per ref e direzione. Sceglie superficie e spazio libero secondo lo stato del personaggio; bool indica percorribilità, z altezza.

Le funzioni di collisione leggono geometria caricata e stato del personaggio. Un ripiego laterale diagonale non equivale a raggiungere la cella richiesta.

Sorgente del progetto: `src/ClassicUO.Client/Game/Pathfinder.cs`; funzione `CalculateNewZ`.

#### 6. CalculateMinMaxZ

Riceve nuova cella, Z attuale, direzione e modalità. Usa CreateItemList per calcolare ref minZ/maxZ dalla geometria iniziale.

Le funzioni di collisione leggono geometria caricata e stato del personaggio. Un ripiego laterale diagonale non equivale a raggiungere la cella richiesta.

Sorgente del progetto: `src/ClassicUO.Client/Game/Pathfinder.cs`; funzione `CalculateMinMaxZ`.

#### 7. CreateItemList

Riceve lista, X/Y e modalità. Raccoglie oggetti caricati e regole di collisione; bool indica geometria disponibile. Map.GetTile usa load=false senza leggere nuovi blocchi.

Le funzioni di collisione leggono geometria caricata e stato del personaggio. Un ripiego laterale diagonale non equivale a raggiungere la cella richiesta.

Sorgente del progetto: `src/ClassicUO.Client/Game/Pathfinder.cs`; funzione `CreateItemList`.

Nessun movimento, apertura di porte, bersaglio o pacchetto di rete. Legge geometria locale esistente; il server può rifiutare un passo successivo. Le letture sono istantanee separate.


## Esempi

### Verificare la cella a est

```vb
# Verificare la cella a est
#
# Verifica un passaggio alla cella vicina e restituisce percorribilità e altezza.
#
# Array di due Integer: [0] — percorribilità, 1 = TRUE, 0 = FALSE; [1] — Z calcolata. Solo il
# primo elemento è logico; non confrontare l’array con TRUE. Altezze nulle/negative sono valide;
# con [0]=0 non dimostrano raggiungibilità. Argomenti rifiutati restituiscono [0, CurrZ].

SUB Main()
    # x/y/z sono l’origine, x+1/y la vicina; sesto argomento Z di riserva, ultimo mappa attuale.
    # Verificare result[0] prima di result[1].

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR result = UO.IsWorldCellPassable(x,y,z,x+1,y,z,UO.WorldNum())
    IF result[0] = TRUE THEN
        UO.Print('Passable, Z=' + CStr(result[1]))
    ELSE
        UO.Print('Blocked')
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- x/y/z sono l’origine, x+1/y la vicina; sesto argomento Z di riserva, ultimo mappa attuale. Verificare result[0] prima di result[1].

### Leggere Z senza modificare l’argomento

```vb
# Leggere Z senza modificare l’argomento
#
# Verifica un passaggio alla cella vicina e restituisce percorribilità e altezza.
#
# Array di due Integer: [0] — percorribilità, 1 = TRUE, 0 = FALSE; [1] — Z calcolata. Solo il
# primo elemento è logico; non confrontare l’array con TRUE. Altezze nulle/negative sono valide;
# con [0]=0 non dimostrano raggiungibilità. Argomenti rifiutati restituiscono [0, CurrZ].

SUB Main()
    # proposedZ resta 0. targetZ viene da result[1], non dall’argomento. In caso di rifiuto non si
    # deduce l’altezza.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR proposedZ = 0
    VAR result = UO.IsWorldCellPassable(x,y,z,x,y+1,proposedZ,UO.WorldNum())
    IF result[0] = 1 THEN
        VAR targetZ = result[1]
        UO.Print('Input=' + CStr(proposedZ) + '; result=' + CStr(targetZ))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- proposedZ resta 0. targetZ viene da result[1], non dall’argomento. In caso di rifiuto non si deduce l’altezza.

### Funzione IsCellOpen completa

```vb
# Funzione IsCellOpen completa
#
# Verifica un passaggio alla cella vicina e restituisce percorribilità e altezza.
#
# Array di due Integer: [0] — percorribilità, 1 = TRUE, 0 = FALSE; [1] — Z calcolata. Solo il
# primo elemento è logico; non confrontare l’array con TRUE. Altezze nulle/negative sono valide;
# con [0]=0 non dimostrano raggiungibilità. Argomenti rifiutati restituiscono [0, CurrZ].

SUB Main()
    # La funzione completa dopo Main riceve X/Y/Z iniziali, X/Y finali e mappa. Aggiunge il sesto
    # argomento e restituisce solo Integer 1/0, non un array. IsCellOpen è confrontabile con TRUE.
    # Nessun movimento.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR openCell = IsCellOpen(x,y,UO.GetZ(),x+1,y+1,UO.WorldNum())
    IF openCell = TRUE THEN
        UO.Print('Diagonal cell is locally passable')
    END IF
END SUB

SUB IsCellOpen(x,y,z,toX,toY,map)
    VAR cellResult = UO.IsWorldCellPassable(x,y,z,toX,toY,z,map)
    IF GetArrayLength(cellResult) <> 2 THEN
        RETURN 0
    END IF
    RETURN cellResult[0]
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- La funzione completa dopo Main riceve X/Y/Z iniziali, X/Y finali e mappa. Aggiunge il sesto argomento e restituisce solo Integer 1/0, non un array. IsCellOpen è confrontabile con TRUE. Nessun movimento.
