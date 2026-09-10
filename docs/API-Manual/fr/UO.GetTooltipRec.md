# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit les propriétés structurées d’un objet : identifiant cliloc et paramètres de substitution de chaque entrée.

## Syntaxe exacte

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## Paramètres

- `ObjID` — Serial obligatoire de l’objet, pas son graphic/type ni un identifiant cliloc. Entier, chaîne décimale/hex, self, backpack, lasttarget, finditem ou nom AddObject. 0 ne sélectionne aucun objet.

## Retour

Array<Array> : chaque ligne contient [clilocID:Integer, parameters:Array<String>]. rows[i][0] est l’identifiant du message ; rows[i][1] contient ses paramètres. GetArrayLength(rows) compte les propriétés. Tableau vide si aucune entrée reçue ou ObjID=0. Ce ne sont pas des serials d’objets.

## Comportement

- Le cache est lu immédiatement. Sans OPL, une requête attend au plus 120 ms ; l’annulation de la procédure interrompt l’attente. Une OPL déjà connue et vide est renvoyée immédiatement.
- Le tableau BASIC représente TClilocRec : Count correspond à GetArrayLength(rows), Items aux lignes. Les tabulations initiales de transport sont ignorées ; les paramètres internes vides gardent leur position. #nombre reste une chaîne à localiser. Les paramètres absents donnent un tableau vide. Modifier cet instantané ne modifie pas le cache.
- https://stealth.od.ua/api/GetTooltipRec/

## Exemples

### Lister les identifiants des propriétés

```vb
# Lister les identifiants des propriétés
#
# Lit les propriétés structurées d’un objet : identifiant cliloc et paramètres de substitution
# de chaque entrée.
#
# Array<Array> : chaque ligne contient [clilocID:Integer, parameters:Array<String>]. rows[i][0]
# est l’identifiant du message ; rows[i][1] contient ses paramètres. GetArrayLength(rows) compte
# les propriétés. Tableau vide si aucune entrée reçue ou ObjID=0. Ce ne sont pas des serials
# d’objets.

SUB Main()
    # ObjID=lasttarget sélectionne l’objet. i commence à 0 ; row[0] est un ID cliloc. Un tableau
    # vide ne lance pas la boucle.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**Explication des paramètres et du déroulement:**

- ObjID=lasttarget sélectionne l’objet. i commence à 0 ; row[0] est un ID cliloc. Un tableau vide ne lance pas la boucle.

### Traduire chaque propriété

```vb
# Traduire chaque propriété
#
# Lit les propriétés structurées d’un objet : identifiant cliloc et paramètres de substitution
# de chaque entrée.
#
# Array<Array> : chaque ligne contient [clilocID:Integer, parameters:Array<String>]. rows[i][0]
# est l’identifiant du message ; rows[i][1] contient ses paramètres. GetArrayLength(rows) compte
# les propriétés. Tableau vide si aucune entrée reçue ou ObjID=0. Ce ne sont pas des serials
# d’objets.

SUB Main()
    # GetClilocByID reçoit ClilocID=row[0] et Params=row[1], dans leur ordre. Ne passez pas la ligne
    # entière comme Params.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR text = UO.GetClilocByID(row[0], row[1])
        UO.Print(text)
        i = i + 1
    WEND
END SUB
```

**Explication des paramètres et du déroulement:**

- GetClilocByID reçoit ClilocID=row[0] et Params=row[1], dans leur ordre. Ne passez pas la ligne entière comme Params.

### Lire un paramètre numérique

```vb
# Lire un paramètre numérique
#
# Lit les propriétés structurées d’un objet : identifiant cliloc et paramètres de substitution
# de chaque entrée.
#
# Array<Array> : chaque ligne contient [clilocID:Integer, parameters:Array<String>]. rows[i][0]
# est l’identifiant du message ; rows[i][1] contient ses paramètres. GetArrayLength(rows) compte
# les propriétés. Tableau vide si aucune entrée reçue ou ObjID=0. Ce ne sont pas des serials
# d’objets.

SUB Main()
    # wanted=1060401 est un exemple d’ID de propriété à remplacer. args[0] est une String. Vérifiez
    # la taille et IsNumeric avant Val : le paramètre peut être du texte ou #cliloc.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR wanted = 1060401
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR args = row[1]
        IF row[0] = wanted AND GetArrayLength(args) > 0 THEN
            IF IsNumeric(args[0]) THEN
                UO.Print('Value: ' + STR(Val(args[0])))
            END IF
        END IF
        i = i + 1
    WEND
END SUB
```

**Explication des paramètres et du déroulement:**

- wanted=1060401 est un exemple d’ID de propriété à remplacer. args[0] est une String. Vérifiez la taille et IsNumeric avant Val : le paramètre peut être du texte ou #cliloc.
