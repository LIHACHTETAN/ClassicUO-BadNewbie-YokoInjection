# UO.GetGumpInfo

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest einen konsistenten Schnappschuss eines Server-Gumps und seiner Elemente.

## Genaue Syntax

```text
UO.GetGumpInfo(GumpIndex:Any) -> Array
```

## Parameter

- `GumpIndex` — Erforderlicher Integer: Index ab 0 bis GetGumpsCount()-1, keine Serial und keine GumpID. Negative Indizes und Indizes außerhalb der Liste sind ungültig. Öffnen, Schließen oder Umordnen von Fenstern kann den Index ändern.

## Rückgabewert

Array mit genau fünf Feldern: [0] Integer Serial; [1] Integer GumpID; [2] Array<String> nichtleerer Texte; [3] Array<String> Beschreibungen normaler Schaltflächen; [4] Array<String> aller aktiven Elemente einschließlich verschachtelter Elemente. Ungültige, geschlossene oder ignorierte Gumps liefern []. IDs mit höchstem Bit erscheinen als negative Integer; Hex zeigt die Bits.

## Verhalten

- Alle Daten werden in einer Anfrage im Spielthread kopiert. Spätere Änderungen und das Schließen ändern gespeicherte Arrays nicht. Nur aktive Server-Gumps zählen; lokale Rucksack-, Karten- und Einstellungsfenster sind ausgeschlossen.
- Das BASIC-Array ist kein Pascal-TGumpInfo-Datensatz und kein ursprüngliches Layoutpaket. Beschreibungen enthalten Typ, page, ID, X/Y und Abmessungen. Schaltflächen ergänzen ButtonID, action, toPage und Grafiken; Umschalter checked sowie inactive/active. Text kann Leerzeichen und = enthalten. Optionsfelder stehen in [4], nicht [3].
- AddGumpIgnoreByID/BySerial unterdrücken diesen Abruf im aktuellen Skript; ClearGumpsIgnore hebt den Filter auf. GetGumpsCount bleibt unverändert. Auch vorhandene Gumps können leere Textarrays haben. Arraylängen werden mit GetArrayLength statt Len gelesen.

## Beispiele

### Beide IDs lesen

```vb
# Beide IDs lesen
#
# Liest einen konsistenten Schnappschuss eines Server-Gumps und seiner Elemente.
#
# Array mit genau fünf Feldern: [0] Integer Serial; [1] Integer GumpID; [2] Array<String>
# nichtleerer Texte; [3] Array<String> Beschreibungen normaler Schaltflächen; [4] Array<String>
# aller aktiven Elemente einschließlich verschachtelter Elemente. Ungültige, geschlossene oder
# ignorierte Gumps liefern []. IDs mit höchstem Bit erscheinen als negative Integer; Hex zeigt
# die Bits.

SUB Main()
    # 0 wählt den ersten Server-Gump. Vor dem Feldzugriff GetArrayLength(info)=5 prüfen. info[0] ist
    # die Serial und info[1] die GumpID desselben Schnappschusses.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        UO.Print('Serial=' + Hex(info[0]))
        UO.Print('GumpID=' + Hex(info[1]))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- 0 wählt den ersten Server-Gump. Vor dem Feldzugriff GetArrayLength(info)=5 prüfen. info[0] ist die Serial und info[1] die GumpID desselben Schnappschusses.

### Tatsächliche ButtonIDs auflisten

```vb
# Tatsächliche ButtonIDs auflisten
#
# Liest einen konsistenten Schnappschuss eines Server-Gumps und seiner Elemente.
#
# Array mit genau fünf Feldern: [0] Integer Serial; [1] Integer GumpID; [2] Array<String>
# nichtleerer Texte; [3] Array<String> Beschreibungen normaler Schaltflächen; [4] Array<String>
# aller aktiven Elemente einschließlich verschachtelter Elemente. Ungültige, geschlossene oder
# ignorierte Gumps liefern []. IDs mit höchstem Bit erscheinen als negative Integer; Hex zeigt
# die Bits.

SUB Main()
    # info[3] enthält Schaltflächenbeschreibungen. i ist der Zeilenindex; ButtonID in der
    # Beschreibung ist die ID für die Antwort. Optionsfelder gehören zur vollständigen Elementliste.

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

**Erläuterung der Parameter und Ausführung:**

- info[3] enthält Schaltflächenbeschreibungen. i ist der Zeilenindex; ButtonID in der Beschreibung ist die ID für die Antwort. Optionsfelder gehören zur vollständigen Elementliste.

### Text vor dem Schließen speichern

```vb
# Text vor dem Schließen speichern
#
# Liest einen konsistenten Schnappschuss eines Server-Gumps und seiner Elemente.
#
# Array mit genau fünf Feldern: [0] Integer Serial; [1] Integer GumpID; [2] Array<String>
# nichtleerer Texte; [3] Array<String> Beschreibungen normaler Schaltflächen; [4] Array<String>
# aller aktiven Elemente einschließlich verschachtelter Elemente. Ungültige, geschlossene oder
# ignorierte Gumps liefern []. IDs mit höchstem Bit erscheinen als negative Integer; Hex zeigt
# die Bits.

SUB Main()
    # info[2] ist eine Textkopie. CloseSimpleGump(0) schließt nur lokal und nur ohne NoClose; kein
    # Rückgabewert. Gespeicherter Text bleibt erhalten. Vor texts[0] die Arraylänge prüfen.

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

**Erläuterung der Parameter und Ausführung:**

- info[2] ist eine Textkopie. CloseSimpleGump(0) schließt nur lokal und nur ohne NoClose; kein Rückgabewert. Gespeicherter Text bleibt erhalten. Vor texts[0] die Arraylänge prüfen.
