# UO.FindQuantity

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit la quantité actuelle du premier résultat.

## Syntaxe exacte

```text
UO.FindQuantity() -> Any
```

## Paramètres

Aucun paramètre.

## Retour

Integer — Amount actuel de l’objet identifié par FindItem(); 1 pour un personnage présent, 0 pour un objet absent/supprimé. Les autres piles ne sont pas ajoutées. Lecture au moment de l’appel.

## Comportement

- FindType avec 1–5 arguments, FindTypeEx et Count/CountEx/CountGround remplacent les résultats de ce script. Une recherche sans correspondance vide cet instantané. Conserver les valeurs utiles avant une nouvelle recherche.
- Ces lectures ne recherchent rien, n’ouvrent aucun conteneur, ne déplacent rien et n’envoient aucun paquet. Elles utilisent les données du client. FindCount(id) ne nécessite aucune recherche préalable et ne la modifie pas.
- FindItem/FindCount()/FindFullQuantity sont des instantanés. FindQuantity et FindCount(id) lisent la quantité actuelle ; l’objet peut changer ou disparaître après la recherche.

## Exemples

### Lire une recherche d’or

```vb
# Lire une recherche d’or
#
# Lit la quantité actuelle du premier résultat.
#
# Integer — Amount actuel de l’objet identifié par FindItem(); 1 pour un personnage présent, 0
# pour un objet absent/supprimé. Les autres piles ne sont pas ajoutées. Lecture au moment de
# l’appel.

SUB Main()
    # type=0x0EED désigne l’or ; color=-1 accepte toute teinte ; backpack sélectionne le contenu
    # direct avec cette forme de FindType. value conserve le résultat ; STR l’affiche.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindQuantity()
    UO.Print(STR(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- type=0x0EED désigne l’or ; color=-1 accepte toute teinte ; backpack sélectionne le contenu direct avec cette forme de FindType. value conserve le résultat ; STR l’affiche.

### Comparer objets, pile et total

```vb
# Comparer objets, pile et total
#
# Lit la quantité actuelle du premier résultat.
#
# Integer — Amount actuel de l’objet identifié par FindItem(); 1 pour un personnage présent, 0
# pour un objet absent/supprimé. Les autres piles ne sont pas ajoutées. Lecture au moment de
# l’appel.

SUB Main()
    # Les quatre lectures suivent la même recherche. Deux piles de 50 : objets=2, première pile=50,
    # total=100. FindItem est l’ID unique de la première pile, pas son type.

    UO.FindType(0x0EED, -1, 'backpack')
    UO.Print(STR(UO.FindCount()))
    UO.Print(STR(UO.FindQuantity()))
    UO.Print(STR(UO.FindFullQuantity()))
    UO.Print('0x' + Hex(UO.FindItem()))
END SUB
```

**Explication des paramètres et du déroulement:**

- Les quatre lectures suivent la même recherche. Deux piles de 50 : objets=2, première pile=50, total=100. FindItem est l’ID unique de la première pile, pas son type.

### Conserver une valeur avant de rechercher

```vb
# Conserver une valeur avant de rechercher
#
# Lit la quantité actuelle du premier résultat.
#
# Integer — Amount actuel de l’objet identifié par FindItem(); 1 pour un personnage présent, 0
# pour un objet absent/supprimé. Les autres piles ne sont pas ajoutées. Lecture au moment de
# l’appel.

SUB Main()
    # Le premier type est l’or ; 0x0F7A désigne un autre réactif. Le second FindType remplace
    # l’instantané. saved garde la valeur précédente ; la dernière lecture utilise le nouveau
    # résultat.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindQuantity()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindQuantity()))
END SUB
```

**Explication des paramètres et du déroulement:**

- Le premier type est l’or ; 0x0F7A désigne un autre réactif. Le second FindType remplace l’instantané. saved garde la valeur précédente ; la dernière lecture utilise le nouveau résultat.
