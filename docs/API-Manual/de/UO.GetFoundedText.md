# UO.GetFoundedText

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest den gespeicherten Text des von diesem Skript ausgewählten Journaleintrags.

## Genaue Syntax

```text
UO.GetFoundedText() -> String
```

## Parameter

Keine Parameter.

## Rückgabewert

String — ausgewählter Text oder eine leere Zeichenfolge ohne Auswahl. Auch ein vorhandener Eintrag kann leeren Text enthalten. Kein Serial, Zeilenindex oder boolescher Erfolgswert.

## Verhalten

- InJournal, InJournalBetweenTimes, Journal/GetJournal und LastJournalMessage ersetzen die Auswahl. Eine erfolglose Suche, ein ungültiger Journal-Index oder das Leeren durch dieses Skript setzt sie zurück. Keine Argumente; keine neue Suche.
- Neue Meldungen ersetzen den gespeicherten Text nicht. Wird der Eintrag gelöscht oder verdrängt, bleibt der Text erhalten; GetFoundedTextIndex/LineIndex wird -1. Andere Skripte können das gemeinsame Journal leeren; gespeicherte Variablen bleiben unverändert.

## Beispiele

### Gefundene Meldung lesen

```vb
# Gefundene Meldung lesen
#
# Liest den gespeicherten Text des von diesem Skript ausgewählten Journaleintrags.
#
# String — ausgewählter Text oder eine leere Zeichenfolge ohne Auswahl. Auch ein vorhandener
# Eintrag kann leeren Text enthalten. Kein Serial, Zeilenindex oder boolescher Erfolgswert.

SUB Main()
    # needle ist eine Teilzeichenfolge mit Beachtung der Groß-/Kleinschreibung. InJournal > 0
    # prüfen: Das Ergebnis ist Position plus 1, nicht die Trefferzahl.

    IF UO.InJournal('needle') > 0 THEN
        VAR text = UO.GetFoundedText()
        UO.Print(text)
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- needle ist eine Teilzeichenfolge mit Beachtung der Groß-/Kleinschreibung. InJournal > 0 prüfen: Das Ergebnis ist Position plus 1, nicht die Trefferzahl.

### Ausgewählte Zeile lesen

```vb
# Ausgewählte Zeile lesen
#
# Liest den gespeicherten Text des von diesem Skript ausgewählten Journaleintrags.
#
# String — ausgewählter Text oder eine leere Zeichenfolge ohne Auswahl. Auch ein vorhandener
# Eintrag kann leeren Text enthalten. Kein Serial, Zeilenindex oder boolescher Erfolgswert.

SUB Main()
    # Journal(0) wählt den neuesten Eintrag. Text und Index vor Print speichern, da Print eine
    # Meldung hinzufügen kann. Leerer Text bedeutet nicht automatisch einen fehlenden Eintrag.

    VAR latest = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR text = UO.GetFoundedText()
    IF index >= 0 THEN
        UO.Print(text)
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Journal(0) wählt den neuesten Eintrag. Text und Index vor Print speichern, da Print eine Meldung hinzufügen kann. Leerer Text bedeutet nicht automatisch einen fehlenden Eintrag.

### Text vor weiterer Suche speichern

```vb
# Text vor weiterer Suche speichern
#
# Liest den gespeicherten Text des von diesem Skript ausgewählten Journaleintrags.
#
# String — ausgewählter Text oder eine leere Zeichenfolge ohne Auswahl. Auch ein vorhandener
# Eintrag kann leeren Text enthalten. Kein Serial, Zeilenindex oder boolescher Erfolgswert.

SUB Main()
    # saved kopiert den ersten Treffer, bevor die zweite Suche die Auswahl ersetzt. Spätere
    # Meldungen oder Suchen ändern diese Variable nicht.

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.GetFoundedText()
        VAR another = UO.InJournal('failed')
        UO.Print(saved)
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- saved kopiert den ersten Treffer, bevor die zweite Suche die Auswahl ersetzt. Spätere Meldungen oder Suchen ändern diese Variable nicht.
