# UO.Frozen

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit l’indicateur de paralysie d’un mobile connu du client.

## Syntaxe exacte

```text
UO.Frozen() -> Integer
UO.Frozen(value:Any) -> Integer
```

## Paramètres

- `value` — Serial/ID facultatif du mobile : entier, chaîne hexadécimale, self, lasttarget, autre alias standard ou nom AddObject. Ce n’est pas un graphic/type. Sans argument, self est choisi. Un alias inconnu donne 0 ; aucun curseur de ciblage ne s’ouvre.

## Retour

Integer Boolean : 1 = TRUE si un mobile chargé porte IsParalyzed ; 0 = FALSE si ce drapeau est absent, si le mobile est inconnu ou supprimé, ou si l’objet est un item. Ce n’est pas la durée restante et 0 ne garantit pas la possibilité de se déplacer.

## Comportement

- Utilisez Paralyzed pour vérifier le drapeau de paralysie. Les variantes Is/Get, GetParalisa, Frozen et GetLocked lisent le même drapeau.
- La lecture est locale. Elle n’applique ni ne guérit la paralysie, n’attend pas sa fin et ne demande pas d’actualisation au serveur.
- Pour ce prédicat, value = TRUE, value = 1 et IF value sont équivalents. TRUE/FALSE s’écrivent sans guillemets. Le résultat est un indicateur, pas une quantité ou un ID.

## Exemples

### Tester self avec TRUE

```vb
# Tester self avec TRUE
#
# Lit l’indicateur de paralysie d’un mobile connu du client.
#
# Integer Boolean : 1 = TRUE si un mobile chargé porte IsParalyzed ; 0 = FALSE si ce drapeau est
# absent, si le mobile est inconnu ou supprimé, ou si l’objet est un item. Ce n’est pas la durée
# restante et 0 ne garantit pas la possibilité de se déplacer.

SUB Main()
    # Les parenthèses vides choisissent self. state conserve un instantané ; TRUE est la constante
    # numérique 1.
    # FALSE n’exclut pas un mur, une endurance épuisée ou une autre cause d’immobilité.

    VAR state = UO.Frozen()
    IF state = TRUE THEN
        UO.Print('Paralysis flag is set')
    ELSE
        UO.Print('Paralysis flag is absent or unavailable')
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- Les parenthèses vides choisissent self. state conserve un instantané ; TRUE est la constante numérique 1.
- FALSE n’exclut pas un mur, une endurance épuisée ou une autre cause d’immobilité.

### Tester le mobile sélectionné

```vb
# Tester le mobile sélectionné
#
# Lit l’indicateur de paralysie d’un mobile connu du client.
#
# Integer Boolean : 1 = TRUE si un mobile chargé porte IsParalyzed ; 0 = FALSE si ce drapeau est
# absent, si le mobile est inconnu ou supprimé, ou si l’objet est un item. Ce n’est pas la durée
# restante et 0 ne garantit pas la possibilité de se déplacer.

SUB Main()
    # target conserve le serial de la dernière cible en hexadécimal. IsNpc vérifie un mobile chargé,
    # joueurs compris.
    # L’argument désigne ce target enregistré. Il n’ouvre pas de curseur et ne change pas
    # lasttarget.

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR state = UO.Frozen(target)
        UO.Print('Selected mobile paralysis 1/0: ' + STR(state))
    ELSE
        UO.Print('No loaded mobile selected')
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- target conserve le serial de la dernière cible en hexadécimal. IsNpc vérifie un mobile chargé, joueurs compris.
- L’argument désigne ce target enregistré. Il n’ouvre pas de curseur et ne change pas lasttarget.

### Attendre la fin avec une limite

```vb
# Attendre la fin avec une limite
#
# Lit l’indicateur de paralysie d’un mobile connu du client.
#
# Integer Boolean : 1 = TRUE si un mobile chargé porte IsParalyzed ; 0 = FALSE si ce drapeau est
# absent, si le mobile est inconnu ou supprimé, ou si l’objet est un item. Ce n’est pas la durée
# restante et 0 ne garantit pas la possibilité de se déplacer.

SUB Main()
    # Au plus dix attentes de 100 ms. Chaque appel sans argument relit self.
    # Après la boucle, la présence de self est vérifiée séparément. L’observation dure environ une
    # seconde plus l’exécution ; elle ne garantit pas la guérison.

    VAR attempts = 0
    WHILE UO.Frozen() = TRUE AND attempts < 10
        WAIT(100)
        attempts = attempts + 1
    WEND
    IF UO.IsNpc('self') THEN
        IF UO.Frozen() = FALSE THEN
            UO.Print('Paralysis flag is clear')
        ELSE
            UO.Print('Still paralyzed')
        END IF
    ELSE
        UO.Print('Self is unavailable')
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- Au plus dix attentes de 100 ms. Chaque appel sans argument relit self.
- Après la boucle, la présence de self est vérifiée séparément. L’observation dure environ une seconde plus l’exécution ; elle ne garantit pas la guérison.
