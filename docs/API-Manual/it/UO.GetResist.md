# UO.GetResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge una resistenza del proprio personaggio tramite un numero o un nome.

## Sintassi esatta

```text
UO.GetResist(resistance:Any) -> Integer
```

## Parametri

- `resistance` — resistance obbligatorio: numeri 0=physical, 1=fire, 2=cold, 3=poison, 4=energy; nomi physical/phys/armor, fire, cold, poison, energy. Ignora maiuscole e spazi esterni. Nessun serial, type, hue, cursore o secondo argomento.

## Restituisce

Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0 può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0 anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un successo.

## Comportamento

- Prima distingue il tipo: "1" e "0" sono nomi ignoti e restituiscono 0. Un Decimal non testuale viene troncato verso zero: 1.9 -> fire, -0.9 -> physical. TRUE=1 sceglie fire, FALSE=0 physical; anche Array/Unit diventano 0. Usare interi espliciti o nomi validi. Nessuna risoluzione AddObject.
- GetResistance sceglie un solo getter del bridge; numero/nome ignoto dà Integer 0 senza lettura. Non acquisisce atomicamente cinque campi né modifica resistenze.
- PhysicalResistance è il campo armatura/status del server: indice d’armatura con regole classiche, resistenza fisica con regole basate sulle resistenze. Non converte le regole né calcola la percentuale di danno evitato. Armor e alias fisici leggono lo stesso campo.
- I campi elementali arrivano con CharacterStatus (0x11), type >= 4. La query non verifica l’era del server. Uno status compatto/vecchio senza questi campi conserva la cache; un nuovo Player parte da 0. Resistenza al veleno non è Poisoned; nessun campo è l’abilità Resisting Spells.
- CharacterStatus verifica il corpo fisso prima delle modifiche, poi converte le word in Int16 con segno. Un corpo troncato conserva i dati precedenti. La coda opzionale type 6 mantiene il comportamento esistente; questi getter non ne leggono i massimi di resistenza.
- Invoke legge sul thread del gioco; l’attesa rispetta l’annullamento dello script. Nessun pacchetto, richiesta status, target, modifica o ritardo incorporato.
- Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.

### Funzioni interne: dalla chiamata al risultato

Passaggi nativi della lettura locale. ResistanceAtLeast sotto è una funzione BASIC utente completa, non un’API nascosta o un comando per indossare protezioni.

#### 1. RegisterCharacterGetterAliases

Registra GetResist(resistance) e UO.GetResist(resistance) con un argomento collegato a GetResistance. Nessun intrinseco senza argomenti per questo selettore.

resistance obbligatorio: numeri 0=physical, 1=fire, 2=cold, 3=poison, 4=energy; nomi physical/phys/armor, fire, cold, poison, energy. Ignora maiuscole e spazi esterni. Nessun serial, type, hue, cursore o secondo argomento.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `RegisterCharacterGetterAliases`.

#### 2. GetResistance

Prima distingue il tipo: "1" e "0" sono nomi ignoti e restituiscono 0. Un Decimal non testuale viene troncato verso zero: 1.9 -> fire, -0.9 -> physical. TRUE=1 sceglie fire, FALSE=0 physical; anche Array/Unit diventano 0. Usare interi espliciti o nomi validi. Nessuna risoluzione AddObject.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`. GetResistance sceglie un solo getter del bridge; numero/nome ignoto dà Integer 0 senza lettura. Non acquisisce atomicamente cinque campi né modifica resistenze.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `GetResistance`.

#### 3. ToInt

ToInt riceve qui solo un selettore non testuale. Integer invariato, Decimal troncato verso zero, Array/Unit danno 0. Il risultato è un indice, non una resistenza. GetResistance gestisce i nomi testuali.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/NumberConversions.cs`; funzione `ToInt`.

#### 4. Invoke

Invoke legge il campo Player selezionato nella mappa sopra, mantenendo il segno. Player assente/distrutto dà 0. Nessuna richiesta status o attesa di nuovi dati.

Invoke legge sul thread del gioco; l’attesa rispetta l’annullamento dello script. Nessun pacchetto, richiesta status, target, modifica o ritardo incorporato.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 5. CharacterStatus

CharacterStatus verifica il corpo fisso prima delle modifiche, poi converte le word in Int16 con segno. Un corpo troncato conserva i dati precedenti. La coda opzionale type 6 mantiene il comportamento esistente; questi getter non ne leggono i massimi di resistenza.

PhysicalResistance è il campo armatura/status del server: indice d’armatura con regole classiche, resistenza fisica con regole basate sulle resistenze. Non converte le regole né calcola la percentuale di danno evitato. Armor e alias fisici leggono lo stesso campo. I campi elementali arrivano con CharacterStatus (0x11), type >= 4. La query non verifica l’era del server. Uno status compatto/vecchio senza questi campi conserva la cache; un nuovo Player parte da 0. Resistenza al veleno non è Poisoned; nessun campo è l’abilità Resisting Spells.

Sorgente del progetto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; funzione `CharacterStatus`.

#### 6. Clear

World.Clear rimuove Player. Le letture danno 0 finché giocatore e dati non tornano disponibili. Un valore salvato non prova il requisito dopo una riconnessione.

Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0 può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0 anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un successo.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Clear`.

Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.


## Esempi

### Scegliere un nome con maiuscole miste

```vb
# Scegliere un nome con maiuscole miste
#
# Legge una resistenza del proprio personaggio tramite un numero o un nome.
#
# Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0
# può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0
# anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un
# successo.

SUB Main()
    # resistance=" FiRe " sceglie il fuoco ignorando maiuscole e spazi esterni. value mantiene il
    # segno; nessun cursore.

    VAR value = UO.GetResist(' FiRe ')
    UO.Print('Fire resistance: ' + CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- resistance=" FiRe " sceglie il fuoco ignorando maiuscole e spazi esterni. value mantiene il segno; nessun cursore.

### Confrontare selettori numerici e testuali

```vb
# Confrontare selettori numerici e testuali
#
# Legge una resistenza del proprio personaggio tramite un numero o un nome.
#
# Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0
# può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0
# anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un
# successo.

SUB Main()
    # 2 sceglie il freddo, "poison" il veleno. Non sono serial. Il confronto tra due istantanee
    # produce Boolean; la resistenza al veleno non indica avvelenamento.

    VAR cold = UO.GetResist(2)
    VAR poison = UO.GetResist('poison')
    IF cold < poison THEN
        UO.Print('Cold resistance is lower')
    ELSE
        UO.Print('Cold resistance is equal or higher')
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- 2 sceglie il freddo, "poison" il veleno. Non sono serial. Il confronto tra due istantanee produce Boolean; la resistenza al veleno non indica avvelenamento.

### Funzione completa per la resistenza minima

```vb
# Funzione completa per la resistenza minima
#
# Legge una resistenza del proprio personaggio tramite un numero o un nome.
#
# Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0
# può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0
# anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un
# successo.

SUB Main()
    # minimum=50 è un requisito d’esempio, non un limite. ResistanceAtLeast rifiuta Player assente,
    # legge una volta e restituisce Integer Boolean 1=TRUE o 0=FALSE per value >= minimum. La
    # resistenza non è Boolean. Definizione completa sotto.
    # selector viene passato invariato a GetResist; qui si usa "fire". La funzione verifica Player,
    # ma non selettori arbitrari né la freschezza del dato. Usare la lista sopra.

    IF ResistanceAtLeast('fire', 50) = TRUE THEN
        UO.Print('Local fire resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(selector, minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetResist(selector)
    RETURN value >= minimum
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- minimum=50 è un requisito d’esempio, non un limite. ResistanceAtLeast rifiuta Player assente, legge una volta e restituisce Integer Boolean 1=TRUE o 0=FALSE per value >= minimum. La resistenza non è Boolean. Definizione completa sotto.
- selector viene passato invariato a GetResist; qui si usa "fire". La funzione verifica Player, ma non selettori arbitrari né la freschezza del dato. Usare la lista sopra.
