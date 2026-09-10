# UO.GetFoundedText

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the saved text of the journal entry selected by this script.

## Exact syntax

```text
UO.GetFoundedText() -> String
```

## Parameters

No parameters.

## Returns

String — the selected text, or an empty string when no entry is selected. A real entry may also contain empty text. This is not a serial, line index or Boolean success flag.

## Behavior

- InJournal, InJournalBetweenTimes, Journal/GetJournal and LastJournalMessage replace the selection. A failed search, an invalid Journal index or clearing through this script resets it. The getter takes no arguments and does not perform a new search.
- New messages do not replace the saved text. If the selected entry is deleted or evicted, the text remains, while GetFoundedTextIndex/LineIndex becomes -1. Another script may clear the shared journal; saved variables remain unchanged.

## Examples

### Read a matched message

```vb
# Read a matched message
#
# Reads the saved text of the journal entry selected by this script.
#
# String — the selected text, or an empty string when no entry is selected. A real entry may
# also contain empty text. This is not a serial, line index or Boolean success flag.

SUB Main()
    # needle is a case-sensitive substring. Check InJournal > 0; its result is a position plus 1,
    # not the number of matches.

    IF UO.InJournal('needle') > 0 THEN
        VAR text = UO.GetFoundedText()
        UO.Print(text)
    END IF
END SUB
```

**Parameter and execution notes:**

- needle is a case-sensitive substring. Check InJournal > 0; its result is a position plus 1, not the number of matches.

### Read a selected line

```vb
# Read a selected line
#
# Reads the saved text of the journal entry selected by this script.
#
# String — the selected text, or an empty string when no entry is selected. A real entry may
# also contain empty text. This is not a serial, line index or Boolean success flag.

SUB Main()
    # Journal(0) selects the newest entry. Save the text and index before Print, which may append a
    # message. An empty string alone does not mean the entry is absent.

    VAR latest = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR text = UO.GetFoundedText()
    IF index >= 0 THEN
        UO.Print(text)
    END IF
END SUB
```

**Parameter and execution notes:**

- Journal(0) selects the newest entry. Save the text and index before Print, which may append a message. An empty string alone does not mean the entry is absent.

### Keep text across another search

```vb
# Keep text across another search
#
# Reads the saved text of the journal entry selected by this script.
#
# String — the selected text, or an empty string when no entry is selected. A real entry may
# also contain empty text. This is not a serial, line index or Boolean success flag.

SUB Main()
    # saved copies the first match before the second search replaces the selection. Subsequent
    # arrivals or searches cannot change that variable.

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.GetFoundedText()
        VAR another = UO.InJournal('failed')
        UO.Print(saved)
    END IF
END SUB
```

**Parameter and execution notes:**

- saved copies the first match before the second search replaces the selection. Subsequent arrivals or searches cannot change that variable.
