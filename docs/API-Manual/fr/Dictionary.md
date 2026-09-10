# Dictionary

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Dictionary() crée une collection clé → valeur. Appelez les méthodes sur l’objet retourné. Les clés numériques et textuelles diffèrent ; "ore" et "Ore" sont distinctes.

## Syntaxe exacte

```text
Dictionary() -> Object
Dictionary(source:Any) -> Object
```

## Paramètres

- `source` — source : absent, la collection est vide. List accepte un tableau ou List ; Dictionary accepte Dictionary. Le conteneur est copié, mais les références imbriquées restent partagées.

## Retour

La création renvoie Object:Dictionary. Item/index/Get renvoient une valeur ; Count compte les clés. ContainsKey/Remove renvoient 1=TRUE ou 0=FALSE. Add/Set/Clear renvoient Unit ; Keys/Values, de nouveaux Array. For Each donne des entrées : Key() renvoie la clé, Value() sa valeur.

## Comportement

- index / key : positions List numériques entières à partir de 0 ; Insert accepte aussi Count(). Les clés Dictionary sont du texte ou des nombres finis. Les nombres 1 et 1.0 partagent une clé, pas le texte "1".
- value : valeur Basic initialisée, y compris tableau ou collection. Unit ne peut être stocké. Égalité numérique, texte sensible à la casse, identité de référence pour tableaux/objets.
- fallback : Get renvoie ce secours si la clé est absente, sans insertion. Tous les arguments, y compris l’expression fallback, sont évalués avant l’appel.
- Add refuse un doublon sans écraser la valeur. Set/index crée ou remplace. Item/index exige une clé existante ; Get accepte un secours. Remove renvoie 0 pour une clé absente ; Clear vide le dictionnaire.
- NaN, infini, tableaux, objets et Unit ne sont pas des clés valides. L’ordre des clés est indéfini. Chaque entrée conserve sa paire, même après passage à l’itération suivante.
- Keys/Values créent des instantanés superficiels. Parcourez Keys() pour supprimer/remplacer ; parcourir directement le dictionnaire fournit des objets entrée.
- Une mutation pendant le For Each direct, y compris Set, déclenche une erreur interceptable au pas suivant. Try/Finally se déroule normalement. Une mutation refusée conserve les données.
- Alias et arguments ByVal partagent la collection. Copies et instantanés ne dupliquent que le conteneur extérieur. ByRef indexé et affectation composée évaluent conteneur/clé une seule fois ; remplacer la variable ne redirige pas la réécriture.
- Ces données sont locales au script : les méthodes ne déplacent aucun objet de jeu et n’utilisent pas le réseau. Une pile enregistrée comme élément occupe une position.

## Exemples

### Types de clés et secours

```vb
# Types de clés et secours
#
# Dictionary() crée une collection clé → valeur. Appelez les méthodes sur l’objet retourné. Les
# clés numériques et textuelles diffèrent ; "ore" et "Ore" sont distinctes.
#
# La création renvoie Object:Dictionary. Item/index/Get renvoient une valeur ; Count compte les
# clés. ContainsKey/Remove renvoient 1=TRUE ou 0=FALSE. Add/Set/Clear renvoient Unit ;
# Keys/Values, de nouveaux Array. For Each donne des entrées : Key() renvoie la clé, Value() sa
# valeur.

Option Explicit On
Sub Main()
    # "ore" passe de 5 à 8. La clé numérique 1 contient 2, le texte "1" contient 3. Get("wood",7)
    # renvoie 7 sans insertion. Main renvoie 8*100+2*10+3+7, Integer 830.

    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**Explication des paramètres et du déroulement:**

- "ore" passe de 5 à 8. La clé numérique 1 contient 2, le texte "1" contient 3. Get("wood",7) renvoie 7 sans insertion. Main renvoie 8*100+2*10+3+7, Integer 830.

### Entrées, instantanés et suppression

```vb
# Entrées, instantanés et suppression
#
# Dictionary() crée une collection clé → valeur. Appelez les méthodes sur l’objet retourné. Les
# clés numériques et textuelles diffèrent ; "ore" et "Ore" sont distinctes.
#
# La création renvoie Object:Dictionary. Item/index/Get renvoient une valeur ; Count compte les
# clés. ContainsKey/Remove renvoient 1=TRUE ou 0=FALSE. Add/Set/Clear renvoient Unit ;
# Keys/Values, de nouveaux Array. For Each donne des entrées : Key() renvoie la clé, Value() sa
# valeur.

Option Explicit On
Sub Main()
    # Les deux valeurs totalisent 5. Keys() permet de supprimer durant son parcours. copied garde
    # ore=2, snapshot garde deux valeurs. Après Clear, Count()=0. Main renvoie 5*100+2*10+2+0,
    # Integer 522.

    Var values = Dictionary()
    values.Add("ore", 2)
    values.Add("wood", 3)
    Var copied = Dictionary(values)
    Var snapshot = values.Values()
    Var total = 0
    For Each entry In values
        If values.ContainsKey(entry.Key()) Then
            total += entry.Value()
        End If
    Next
    For Each key In values.Keys()
        values.Remove(key)
    Next
    values.Clear()
    Return total*100 + copied["ore"]*10 + GetArrayLength(snapshot) + values.Count()
End Sub
```

**Explication des paramètres et du déroulement:**

- Les deux valeurs totalisent 5. Keys() permet de supprimer durant son parcours. copied garde ore=2, snapshot garde deux valeurs. Après Clear, Count()=0. Main renvoie 5*100+2*10+2+0, Integer 522.

### Gérer une clé dupliquée

```vb
# Gérer une clé dupliquée
#
# Dictionary() crée une collection clé → valeur. Appelez les méthodes sur l’objet retourné. Les
# clés numériques et textuelles diffèrent ; "ore" et "Ore" sont distinctes.
#
# La création renvoie Object:Dictionary. Item/index/Get renvoient une valeur ; Count compte les
# clés. ContainsKey/Remove renvoient 1=TRUE ou 0=FALSE. Add/Set/Clear renvoient Unit ;
# Keys/Values, de nouveaux Array. For Each donne des entrées : Key() renvoie la clé, Value() sa
# valeur.

Option Explicit On
Sub Main()
    # Le premier Add stocke ore=4. Le second avec 7 lève une erreur ; Catch fixe caught=1. ore=4 est
    # préservé. Main renvoie 4*10+1, Integer 41.

    Var values = Dictionary()
    values.Add("ore", 4)
    Var caught = 0
    Try
        values.Add("ore", 7)
    Catch problem
        caught = 1
    End Try
    Return values["ore"]*10 + caught
End Sub
```

**Explication des paramètres et du déroulement:**

- Le premier Add stocke ore=4. Le second avec 7 lève une erreur ; Catch fixe caught=1. ore=4 est préservé. Main renvoie 4*10+1, Integer 41.
