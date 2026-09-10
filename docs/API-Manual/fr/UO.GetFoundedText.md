# UO.GetFoundedText

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le texte mémorisé de l’entrée du journal sélectionnée par ce script.

## Syntaxe exacte

```text
UO.GetFoundedText() -> String
```

## Paramètres

Aucun paramètre.

## Retour

String — texte sélectionné, ou chaîne vide si aucune entrée n’est sélectionnée. Une entrée existante peut aussi avoir un texte vide. Ce n’est ni un serial, ni un index, ni un indicateur booléen de réussite.

## Comportement

- InJournal, InJournalBetweenTimes, Journal/GetJournal et LastJournalMessage remplacent la sélection. Une recherche infructueuse, un index Journal invalide ou un effacement par ce script la réinitialise. Aucun argument ; aucune nouvelle recherche.
- Les nouveaux messages ne remplacent pas le texte mémorisé. Si l’entrée est supprimée ou évincée, le texte reste disponible, mais GetFoundedTextIndex/LineIndex vaut -1. Un autre script peut vider le journal partagé ; les variables mémorisées restent inchangées.

## Exemples

### Lire un message trouvé

```vb
# Lire un message trouvé
#
# Lit le texte mémorisé de l’entrée du journal sélectionnée par ce script.
#
# String — texte sélectionné, ou chaîne vide si aucune entrée n’est sélectionnée. Une entrée
# existante peut aussi avoir un texte vide. Ce n’est ni un serial, ni un index, ni un indicateur
# booléen de réussite.

SUB Main()
    # needle est une sous-chaîne sensible à la casse. Vérifiez InJournal > 0 : le résultat est la
    # position plus 1, pas le nombre de correspondances.

    IF UO.InJournal('needle') > 0 THEN
        VAR text = UO.GetFoundedText()
        UO.Print(text)
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- needle est une sous-chaîne sensible à la casse. Vérifiez InJournal > 0 : le résultat est la position plus 1, pas le nombre de correspondances.

### Lire une ligne sélectionnée

```vb
# Lire une ligne sélectionnée
#
# Lit le texte mémorisé de l’entrée du journal sélectionnée par ce script.
#
# String — texte sélectionné, ou chaîne vide si aucune entrée n’est sélectionnée. Une entrée
# existante peut aussi avoir un texte vide. Ce n’est ni un serial, ni un index, ni un indicateur
# booléen de réussite.

SUB Main()
    # Journal(0) sélectionne l’entrée la plus récente. Conservez texte et index avant Print, qui
    # peut ajouter un message. Un texte vide ne prouve pas l’absence de l’entrée.

    VAR latest = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR text = UO.GetFoundedText()
    IF index >= 0 THEN
        UO.Print(text)
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- Journal(0) sélectionne l’entrée la plus récente. Conservez texte et index avant Print, qui peut ajouter un message. Un texte vide ne prouve pas l’absence de l’entrée.

### Conserver le texte avant une autre recherche

```vb
# Conserver le texte avant une autre recherche
#
# Lit le texte mémorisé de l’entrée du journal sélectionnée par ce script.
#
# String — texte sélectionné, ou chaîne vide si aucune entrée n’est sélectionnée. Une entrée
# existante peut aussi avoir un texte vide. Ce n’est ni un serial, ni un index, ni un indicateur
# booléen de réussite.

SUB Main()
    # saved copie le premier résultat avant que la seconde recherche ne remplace la sélection. Les
    # recherches et messages suivants ne modifient pas cette variable.

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.GetFoundedText()
        VAR another = UO.InJournal('failed')
        UO.Print(saved)
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- saved copie le premier résultat avant que la seconde recherche ne remplace la sélection. Les recherches et messages suivants ne modifient pas cette variable.
