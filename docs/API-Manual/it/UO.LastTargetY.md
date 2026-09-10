# UO.LastTargetY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge Y salvata nell’ultima selezione del bersaglio.

## Sintassi esatta

```text
UO.LastTargetY() -> Integer
```

## Parametri

Nessun parametro.

## Restituisce

Integer — coordinata Y salvata, non pixel o Boolean. 0 prima della selezione/dopo Clear o per oggetti ignoti; zero è anche una coordinata valida. Funziona sul terreno/statici con LastTarget()=0.

## Comportamento

- Nessun parametro, cursore, selezione, attacco o pacchetto. LastTarget differisce da LastAttack e LastStatus. La normale selezione di self non sostituisce il bersaglio; ClientMarkChar può cambiarlo esplicitamente.
- SetEntity salva Entity.X/Y noti, eventualmente coordinate interne al contenitore. SetLand/SetStatic salvano celle del mondo. Movimento/rimozione successivi non li cambiano. GetX/GetY(serial) danno la posizione attuale.
- Clear e World.Clear azzerano anche mantenendo gli script. Un serial ignoto assegnato esplicitamente riceve X/Y=0, non le vecchie coordinate. L’esistenza sul server non è garantita.
- Letture separate non sono atomiche. Per bersagli oggetto LastTile mantiene X/Y di protocollo 65535; per terreno/statici LastTile(1)/(2) leggono X/Y. lasttarget senza parentesi è dinamico salvo mascheramento con una variabile.
- World.Clear chiama ClearWorldState: cancella cursore/callback attivo, target e pacchetto di ripetizione. Reset normale conserva la cronologia. TargetLast nativo invia il pacchetto salvato solo con un cursore server attivo; senza cronologia o con callback locale mantiene il cursore senza inviare nulla. Il callback client attivo riceve null una volta per annullamento: ClientTargetResponsePresent diventa 1 con risposta vuota. Una selezione completata non riceve un secondo risultato.

### Funzioni interne: dalla chiamata al risultato

Queste sono le vere fasi interne C#. ReadTargetValue è una funzione ausiliaria completamente definita nell’esempio, non un comando integrato nascosto.

#### 1. SetEntity

SetEntity salva serial e X/Y tramite World.Get. Entity assente/distrutta produce X/Y=0; conserva le sentinelle del protocollo.

SetEntity salva Entity.X/Y noti, eventualmente coordinate interne al contenitore. SetLand/SetStatic salvano celle del mondo. Movimento/rimozione successivi non li cambiano. GetX/GetY(serial) danno la posizione attuale.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; funzione `SetEntity`.

#### 2. SetLand

SetLand/SetStatic salvano X/Y/Z con serial 0. SavedX/SavedY sono separati dai campi trasmessi.

Integer — coordinata Y salvata, non pixel o Boolean. 0 prima della selezione/dopo Clear o per oggetti ignoti; zero è anche una coordinata valida. Funziona sul terreno/statici con LastTarget()=0.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; funzione `SetLand`.

#### 3. SetStatic

SetLand/SetStatic salvano X/Y/Z con serial 0. SavedX/SavedY sono separati dai campi trasmessi.

Integer — coordinata Y salvata, non pixel o Boolean. 0 prima della selezione/dopo Clear o per oggetti ignoti; zero è anche una coordinata valida. Funziona sul terreno/statici con LastTarget()=0.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; funzione `SetStatic`.

#### 4. LastTargetY

LastTargetX/LastTargetY leggono ITargetSnapshotBridge; un vecchio bridge esterno mantiene GetX/GetY. Invoke legge sul thread di gioco con annullamento.

Integer — coordinata Y salvata, non pixel o Boolean. 0 prima della selezione/dopo Clear o per oggetti ignoti; zero è anche una coordinata valida. Funziona sul terreno/statici con LastTarget()=0.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `LastTargetY`.

#### 5. Invoke

LastTargetX/LastTargetY leggono ITargetSnapshotBridge; un vecchio bridge esterno mantiene GetX/GetY. Invoke legge sul thread di gioco con annullamento.

Nessun parametro, cursore, selezione, attacco o pacchetto. LastTarget differisce da LastAttack e LastStatus. La normale selezione di self non sostituisce il bersaglio; ClientMarkChar può cambiarlo esplicitamente.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 6. Clear

Clear cancella serial e coordinate salvate; World.Clear lo chiama durante la pulizia.

Clear e World.Clear azzerano anche mantenendo gli script. Un serial ignoto assegnato esplicitamente riceve X/Y=0, non le vecchie coordinate. L’esistenza sul server non è garantita.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; funzione `Clear`.

#### 7. ClearWorldState

World.Clear chiama ClearWorldState: cancella cursore/callback attivo, target e pacchetto di ripetizione. Reset normale conserva la cronologia. TargetLast nativo invia il pacchetto salvato solo con un cursore server attivo; senza cronologia o con callback locale mantiene il cursore senza inviare nulla. Il callback client attivo riceve null una volta per annullamento: ClientTargetResponsePresent diventa 1 con risposta vuota. Una selezione completata non riceve un secondo risultato.

World.Clear chiama ClearWorldState: cancella cursore/callback attivo, target e pacchetto di ripetizione. Reset normale conserva la cronologia. TargetLast nativo invia il pacchetto salvato solo con un cursore server attivo; senza cronologia o con callback locale mantiene il cursore senza inviare nulla. Il callback client attivo riceve null una volta per annullamento: ClientTargetResponsePresent diventa 1 con risposta vuota. Una selezione completata non riceve un secondo risultato.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; funzione `ClearWorldState`.

#### 8. TargetLast

World.Clear chiama ClearWorldState: cancella cursore/callback attivo, target e pacchetto di ripetizione. Reset normale conserva la cronologia. TargetLast nativo invia il pacchetto salvato solo con un cursore server attivo; senza cronologia o con callback locale mantiene il cursore senza inviare nulla. Il callback client attivo riceve null una volta per annullamento: ClientTargetResponsePresent diventa 1 con risposta vuota. Una selezione completata non riceve un secondo risultato.

World.Clear chiama ClearWorldState: cancella cursore/callback attivo, target e pacchetto di ripetizione. Reset normale conserva la cronologia. TargetLast nativo invia il pacchetto salvato solo con un cursore server attivo; senza cronologia o con callback locale mantiene il cursore senza inviare nulla. Il callback client attivo riceve null una volta per annullamento: ClientTargetResponsePresent diventa 1 con risposta vuota. Una selezione completata non riceve un secondo risultato.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; funzione `TargetLast`.

Letture separate non sono atomiche. Per bersagli oggetto LastTile mantiene X/Y di protocollo 65535; per terreno/statici LastTile(1)/(2) leggono X/Y. lasttarget senza parentesi è dinamico salvo mascheramento con una variabile.


## Esempi

### Leggere il valore salvato

```vb
# Leggere il valore salvato
#
# Legge Y salvata nell’ultima selezione del bersaglio.
#
# Integer — coordinata Y salvata, non pixel o Boolean. 0 prima della selezione/dopo Clear o per
# oggetti ignoti; zero è anche una coordinata valida. Funziona sul terreno/statici con
# LastTarget()=0.

SUB Main()
    # value contiene il risultato; HEX mostra l’ID, CStr la coordinata. Nessuna selezione.

    VAR value = UO.LastTargetY()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value contiene il risultato; HEX mostra l’ID, CStr la coordinata. Nessuna selezione.

### Confrontare posizione salvata e attuale

```vb
# Confrontare posizione salvata e attuale
#
# Legge Y salvata nell’ultima selezione del bersaglio.
#
# Integer — coordinata Y salvata, non pixel o Boolean. 0 prima della selezione/dopo Clear o per
# oggetti ignoti; zero è anche una coordinata valida. Funziona sul terreno/statici con
# LastTarget()=0.

SUB Main()
    # id è il serial salvato. Exists precede GetX/GetY; le posizioni possono differire. ID nullo non
    # prova la selezione di un punto.

    VAR id = UO.LastTarget()
    VAR x = UO.LastTargetX()
    VAR y = UO.LastTargetY()
    UO.Print('Saved XY: ' + CStr(x) + ',' + CStr(y))
    IF id <> 0 AND UO.Exists(id) THEN
        UO.Print('Live XY: ' + CStr(UO.GetX(id)) + ',' + CStr(UO.GetY(id)))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- id è il serial salvato. Exists precede GetX/GetY; le posizioni possono differire. ID nullo non prova la selezione di un punto.

### Funzione completa ReadTargetValue

```vb
# Funzione completa ReadTargetValue
#
# Legge Y salvata nell’ultima selezione del bersaglio.
#
# Integer — coordinata Y salvata, non pixel o Boolean. 0 prima della selezione/dopo Clear o per
# oggetti ignoti; zero è anche una coordinata valida. Funziona sul terreno/statici con
# LastTarget()=0.

SUB Main()
    # minimum/maximum configurano il filtro della funzione ausiliaria, non l’API. -1 è il suo
    # segnale fuori intervallo. La variante ID conserva ogni serial non nullo incluso il bit più
    # alto.

    VAR value = ReadTargetValue(0,65535)
    UO.Print('Checked value: ' + CStr(value))
END SUB

SUB ReadTargetValue(minimum,maximum)
    VAR value = UO.LastTargetY()
    IF value < minimum OR value > maximum THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- minimum/maximum configurano il filtro della funzione ausiliaria, non l’API. -1 è il suo segnale fuori intervallo. La variante ID conserva ogni serial non nullo incluso il bit più alto.
