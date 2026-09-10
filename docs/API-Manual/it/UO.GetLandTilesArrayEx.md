# UO.GetLandTilesArrayEx

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Cerca le tessere del terreno per graphic/type in un rettangolo.

## Sintassi esatta

```text
UO.GetLandTilesArrayEx(Xmin:Any, Ymin:Any, Xmax:Any, Ymax:Any, WorldNum:Any, TileTypes:Any) -> Any
```

## Parametri

- `Xmin` — Coordinate mondiali di due angoli inclusi, 0..65535. Gli angoli invertiti vengono normalizzati. Massimo 1.000.000 di celle; limiti non validi causano un errore di script prima della lettura.
- `Ymin` — Coordinate mondiali di due angoli inclusi, 0..65535. Gli angoli invertiti vengono normalizzati. Massimo 1.000.000 di celle; limiti non validi causano un errore di script prima della lettura.
- `Xmax` — Coordinate mondiali di due angoli inclusi, 0..65535. Gli angoli invertiti vengono normalizzati. Massimo 1.000.000 di celle; limiti non validi causano un errore di script prima della lettura.
- `Ymax` — Coordinate mondiali di due angoli inclusi, 0..65535. Gli angoli invertiti vengono normalizzati. Massimo 1.000.000 di celle; limiti non validi causano un errore di script prima della lettura.
- `WorldNum` — Numero mappa/faccetta 0..255; usare UO.WorldNum(). Un’altra mappa restituisce un Array vuoto. Il cambio mappa tra porzioni scarta il risultato parziale.
- `TileTypes` — Array di graphic/type numerici. Tipi ripetuti non duplicano i record. È accettato anche uno scalare come tipo singolo. Un Array vuoto cerca tutti i tipi; un array con solo 0 cerca soltanto 0.

## Restituisce

Array di record [graphic, X, Y, Z], tutti Integer. graphic è il tipo del terreno, Z la quota della base. Nessuna corrispondenza: Array vuoto. Il numero di record è GetArrayLength(result). Gli indici iniziano da 0. Non è Boolean, serial o Pascal record; non esiste un settimo parametro di uscita.

## Comportamento

- Legge dati locali senza cambiare FindItem/FindCount, muovere, attivare target o inviare comandi al server.
- X crescente, poi Y crescente per ogni X. I record di una cella mantengono l’ordine del bridge, non di distanza o quota.
- Fino a 32 celle per porzione con un limite temporale indicativo di circa 1 ms. Verifica l’annullamento tra porzioni. Celle complesse o letture a freddo possono richiedere di più. Dividere le grandi aree; il mondo può cambiare durante la scansione.

### Funzioni interne: dalla chiamata al risultato

Passaggi C# reali, non comandi UO aggiuntivi. Gli esempi riportano tutta la procedura ausiliaria.

#### 1. ExecuteStealthCompatibility

Riceve sei argomenti; la forma normale passa un tipo, Ex converte Array o scalare in tipi.

Chiama FindPortableTiles in modalità land/static e restituisce direttamente l’Array di record.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ExecuteStealthCompatibility`.

#### 2. FindPortableTiles

Verifica coordinate, mappa e area con aritmetica a 64 bit; normalizza gli angoli e crea un HashSet di tipi.

Conserva il cursore X/Y e pianifica ScanSlice tramite ExecutePathQuerySlice. Wait(0) verifica l’annullamento tra porzioni; il cambio mappa restituisce un Array vuoto.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `FindPortableTiles`.

#### 3. ScanSlice

Elabora fino a 32 celle sul thread di gioco, salvando il cursore dopo ogni cella.

GetLandscapeTile fornisce graphic/Z/flags; GetStaticTiles fornisce triple graphic/Z/hue. Aggiunge i record corrispondenti e restituisce il controllo tra porzioni.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ScanSlice`.

#### 4. GetChunk2

Riceve coordinate del blocco e indicatore di caricamento; controlla entrambi gli assi prima dell’indice lineare.

Restituisce Chunk o null; Y fuori mappa non viene sostituita dalla colonna vicina. Riutilizza i blocchi caricati e legge gli altri quando servono.

Sorgente del progetto: `src/ClassicUO.Client/Game/Map/Map.cs`; funzione `GetChunk2`.

Legge dati locali senza cambiare FindItem/FindCount, muovere, attivare target o inviare comandi al server.


## Esempi

### Cercare vicino al personaggio

```vb
# Cercare vicino al personaggio
#
# Cerca le tessere del terreno per graphic/type in un rettangolo.
#
# Array di record [graphic, X, Y, Z], tutti Integer. graphic è il tipo del terreno, Z la quota
# della base. Nessuna corrispondenza: Array vuoto. Il numero di record è GetArrayLength(result).
# Gli indici iniziano da 0. Non è Boolean, serial o Pascal record; non esiste un settimo
# parametro di uscita.

SUB Main()
    # x/y sono le coordinate self, map è la mappa attuale. L’area 3×3 include i bordi. Ex usa due
    # tipi di esempio, la forma normale uno. Sostituire i graphic secondo le risorse, non con ID di
    # oggetti.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArrayEx(x, y, x + 2, y + 2, map, types)
    UO.Print("Records: " + CStr(GetArrayLength(rows)))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- x/y sono le coordinate self, map è la mappa attuale. L’area 3×3 include i bordi. Ex usa due tipi di esempio, la forma normale uno. Sostituire i graphic secondo le risorse, non con ID di oggetti.

### Angoli invertiti e tutti i campi

```vb
# Angoli invertiti e tutti i campi
#
# Cerca le tessere del terreno per graphic/type in un rettangolo.
#
# Array di record [graphic, X, Y, Z], tutti Integer. graphic è il tipo del terreno, Z la quota
# della base. Nessuna corrispondenza: Array vuoto. Il numero di record è GetArrayLength(result).
# Gli indici iniziano da 0. Non è Boolean, serial o Pascal record; non esiste un settimo
# parametro di uscita.

SUB Main()
    # L’area 2×2 usa angoli decrescenti che vengono normalizzati. row è un record. PrintTile è
    # definita interamente e stampa solo numeri. Per il terreno hue=0 è un argomento segnaposto; il
    # record non ha il campo hue.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArrayEx(x + 1, y + 1, x, y, map, types)
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        PrintTile(row[0], row[1], row[2], row[3], 0)
        i = i + 1
    WEND
END SUB

SUB PrintTile(graphic, x, y, z, hue)
    UO.Print("Type=" + CStr(graphic) + " X=" + CStr(x) + " Y=" + CStr(y))
    UO.Print("Z=" + CStr(z) + " hue=" + CStr(hue))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- L’area 2×2 usa angoli decrescenti che vengono normalizzati. row è un record. PrintTile è definita interamente e stampa solo numeri. Per il terreno hue=0 è un argomento segnaposto; il record non ha il campo hue.

### Ripetere con tentativi limitati

```vb
# Ripetere con tentativi limitati
#
# Cerca le tessere del terreno per graphic/type in un rettangolo.
#
# Array di record [graphic, X, Y, Z], tutti Integer. graphic è il tipo del terreno, Z la quota
# della base. Nessuna corrispondenza: Array vuoto. Il numero di record è GetArrayLength(result).
# Gli indici iniziano da 0. Non è Boolean, serial o Pascal record; non esiste un settimo
# parametro di uscita.

SUB Main()
    # Al massimo tre ricerche di una cella, con WAIT(250) tra tentativi. Ogni chiamata produce un
    # nuovo risultato. Lunghezza zero significa nessuna corrispondenza attuale, non assenza
    # definitiva sul server.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR attempt = 0
    WHILE attempt < 3
        VAR rows = UO.GetLandTilesArrayEx(x, y, x, y, map, types)
        UO.Print("Records: " + CStr(GetArrayLength(rows)))
        attempt = attempt + 1
        WAIT(250)
    WEND
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Al massimo tre ricerche di una cella, con WAIT(250) tra tentativi. Ogni chiamata produce un nuovo risultato. Lunghezza zero significa nessuna corrispondenza attuale, non assenza definitiva sul server.
