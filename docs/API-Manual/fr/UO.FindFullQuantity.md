# UO.FindFullQuantity

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le total d’unités mémorisé par la dernière recherche.

## Syntaxe exacte

```text
UO.FindFullQuantity() -> Any
```

## Paramètres

Aucun paramètre.

## Retour

Integer — somme de max(1, Amount) des objets trouvés, plus 1 par personnage trouvé. Aucun résultat : 0. Deux piles de 50 donnent 100 ; FindCount() donne 2. Le total est mémorisé au moment de la recherche.

## Comportement

- FindType avec 1–5 arguments, FindTypeEx et Count/CountEx/CountGround remplacent les résultats de ce script. Une recherche sans correspondance vide cet instantané. Conserver les valeurs utiles avant une nouvelle recherche.
- Ces lectures ne recherchent rien, n’ouvrent aucun conteneur, ne déplacent rien et n’envoient aucun paquet. Elles utilisent les données du client. FindCount(id) ne nécessite aucune recherche préalable et ne la modifie pas.
- FindItem/FindCount()/FindFullQuantity sont des instantanés. FindQuantity et FindCount(id) lisent la quantité actuelle ; l’objet peut changer ou disparaître après la recherche.

## Exemples

### Lire une recherche d’or

```vb
# Lire une recherche d’or
#
# Lit le total d’unités mémorisé par la dernière recherche.
#
# Integer — somme de max(1, Amount) des objets trouvés, plus 1 par personnage trouvé. Aucun
# résultat : 0. Deux piles de 50 donnent 100 ; FindCount() donne 2. Le total est mémorisé au
# moment de la recherche.

SUB Main()
    # type=0x0EED désigne l’or ; color=-1 accepte toute teinte ; backpack sélectionne le contenu
    # direct avec cette forme de FindType. value conserve le résultat ; STR l’affiche.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindFullQuantity()
    UO.Print(STR(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- type=0x0EED désigne l’or ; color=-1 accepte toute teinte ; backpack sélectionne le contenu direct avec cette forme de FindType. value conserve le résultat ; STR l’affiche.

### Comparer objets, pile et total

```vb
# Comparer objets, pile et total
#
# Lit le total d’unités mémorisé par la dernière recherche.
#
# Integer — somme de max(1, Amount) des objets trouvés, plus 1 par personnage trouvé. Aucun
# résultat : 0. Deux piles de 50 donnent 100 ; FindCount() donne 2. Le total est mémorisé au
# moment de la recherche.

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
# Lit le total d’unités mémorisé par la dernière recherche.
#
# Integer — somme de max(1, Amount) des objets trouvés, plus 1 par personnage trouvé. Aucun
# résultat : 0. Deux piles de 50 donnent 100 ; FindCount() donne 2. Le total est mémorisé au
# moment de la recherche.

SUB Main()
    # Le premier type est l’or ; 0x0F7A désigne un autre réactif. Le second FindType remplace
    # l’instantané. saved garde la valeur précédente ; la dernière lecture utilise le nouveau
    # résultat.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindFullQuantity()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindFullQuantity()))
END SUB
```

**Explication des paramètres et du déroulement:**

- Le premier type est l’or ; 0x0F7A désigne un autre réactif. Le second FindType remplace l’instantané. saved garde la valeur précédente ; la dernière lecture utilise le nouveau résultat.
