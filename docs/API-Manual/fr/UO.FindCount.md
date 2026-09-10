# UO.FindCount

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Compte les objets trouvés ou les unités d’une pile désignée par son ID.

## Syntaxe exacte

```text
UO.FindCount() -> Integer
UO.FindCount(id:Any) -> Integer
```

## Paramètres

- `id` — Facultatif, uniquement pour FindCount. Serial d’un objet : Integer, chaîne décimale/hexadécimale, lasttarget, lastobject, backpack ou nom AddObject. Fournir un ID, pas un graphic/type. Nom inconnu : 0. self désigne le personnage, donc renvoie ici 0. Sans argument, compter les objets de la recherche.

## Retour

Integer — FindCount() compte les objets trouvés : une pile vaut un item. FindCount(id) lit son Amount actuel ; ID inconnu/supprimé ou personnage : 0. Un objet non empilable a normalement Amount=1. Ce n’est ni un ID, ni un type, ni un Boolean.

## Comportement

- FindType avec 1–5 arguments, FindTypeEx et Count/CountEx/CountGround remplacent les résultats de ce script. Une recherche sans correspondance vide cet instantané. Conserver les valeurs utiles avant une nouvelle recherche.
- Ces lectures ne recherchent rien, n’ouvrent aucun conteneur, ne déplacent rien et n’envoient aucun paquet. Elles utilisent les données du client. FindCount(id) ne nécessite aucune recherche préalable et ne la modifie pas.
- FindItem/FindCount()/FindFullQuantity sont des instantanés. FindQuantity et FindCount(id) lisent la quantité actuelle ; l’objet peut changer ou disparaître après la recherche.

## Exemples

### Lire une recherche d’or

```vb
# Lire une recherche d’or
#
# Compte les objets trouvés ou les unités d’une pile désignée par son ID.
#
# Integer — FindCount() compte les objets trouvés : une pile vaut un item. FindCount(id) lit son
# Amount actuel ; ID inconnu/supprimé ou personnage : 0. Un objet non empilable a normalement
# Amount=1. Ce n’est ni un ID, ni un type, ni un Boolean.

SUB Main()
    # type=0x0EED désigne l’or ; color=-1 accepte toute teinte ; backpack sélectionne le contenu
    # direct avec cette forme de FindType. value conserve le résultat ; STR l’affiche.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindCount()
    UO.Print(STR(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- type=0x0EED désigne l’or ; color=-1 accepte toute teinte ; backpack sélectionne le contenu direct avec cette forme de FindType. value conserve le résultat ; STR l’affiche.

### Comparer objets, pile et total

```vb
# Comparer objets, pile et total
#
# Compte les objets trouvés ou les unités d’une pile désignée par son ID.
#
# Integer — FindCount() compte les objets trouvés : une pile vaut un item. FindCount(id) lit son
# Amount actuel ; ID inconnu/supprimé ou personnage : 0. Un objet non empilable a normalement
# Amount=1. Ce n’est ni un ID, ni un type, ni un Boolean.

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
# Compte les objets trouvés ou les unités d’une pile désignée par son ID.
#
# Integer — FindCount() compte les objets trouvés : une pile vaut un item. FindCount(id) lit son
# Amount actuel ; ID inconnu/supprimé ou personnage : 0. Un objet non empilable a normalement
# Amount=1. Ce n’est ni un ID, ni un type, ni un Boolean.

SUB Main()
    # Le premier type est l’or ; 0x0F7A désigne un autre réactif. Le second FindType remplace
    # l’instantané. saved garde la valeur précédente ; la dernière lecture utilise le nouveau
    # résultat.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindCount()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindCount()))
END SUB
```

**Explication des paramètres et du déroulement:**

- Le premier type est l’or ; 0x0F7A désigne un autre réactif. Le second FindType remplace l’instantané. saved garde la valeur précédente ; la dernière lecture utilise le nouveau résultat.

### Lire directement un ID

```vb
# Lire directement un ID
#
# Compte les objets trouvés ou les unités d’une pile désignée par son ID.
#
# Integer — FindCount() compte les objets trouvés : une pile vaut un item. FindCount(id) lit son
# Amount actuel ; ID inconnu/supprimé ou personnage : 0. Un objet non empilable a normalement
# Amount=1. Ce n’est ni un ID, ni un type, ni un Boolean.

SUB Main()
    # lasttarget doit désigner un objet déjà sélectionné en jeu. Aucun nouveau curseur de ciblage.
    # FindCount(id) lit sa pile actuelle, renvoie 0 si l’objet est absent et laisse l’instantané
    # intact.

    VAR id = lasttarget
    VAR amount = UO.FindCount(id)
    UO.Print(STR(amount))
END SUB
```

**Explication des paramètres et du déroulement:**

- lasttarget doit désigner un objet déjà sélectionné en jeu. Aucun nouveau curseur de ciblage. FindCount(id) lit sa pile actuelle, renvoie 0 si l’objet est absent et laisse l’instantané intact.
