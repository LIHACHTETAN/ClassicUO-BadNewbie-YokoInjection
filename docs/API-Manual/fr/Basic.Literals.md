# 123 / 0x0EED / "text" / TRUE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Un littéral écrit une valeur directement dans le code, sans déclaration pour les nombres et textes entre guillemets. TRUE/FALSE sont des valeurs logiques prédéfinies. Un nombre entre guillemets reste du texte jusqu’à sa conversion.

## Syntaxe exacte

```text
123
-2147483648
0x0EED
0xFFFFFFFF
2.5
"text"
'text'
TRUE
FALSE
```

## Paramètres

- `integer / hexadecimal` — Integer décimal de -2147483648 à 2147483647, ou 0x suivi de chiffres hexadécimaux 0–9/A–F. Utilisez x minuscule. L’hexadécimal représente 32 bits : 0xFFFFFFFF vaut Integer -1, pas un entier positif 64 bits.
- `floating` — Flottant avec des chiffres de chaque côté du point, comme 2.5 ou -0.25. Écrivez 0.5, pas .5. Virgule, exposant 1e3 et suffixes numériques ne sont pas admis par cette grammaire.
- `text` — Texte entre deux guillemets simples ou doubles correspondants. Pour inclure un guillemet, utilisez l’autre forme ou Chr(34)/Chr(39). Les séquences avec barre oblique inverse et les guillemets doublés ne sont pas interprétés. Gardez la chaîne d’exemple sur une ligne physique.
- `TRUE / FALSE` — TRUE est Integer 1 ; FALSE est Integer 0. Ne redéclarez pas ces noms. Ce sont des valeurs, pas des appels : TRUE et non TRUE().

## Retour

Un entier/hexadécimal donne Integer ; un nombre avec point donne Decimal, flottant binaire ; un texte cité donne String. TRUE/FALSE donnent Integer 1/0. Évaluer une valeur n’effectue aucune action de jeu et ne déclare aucune variable.

## Comportement

- Le signe de -5 est une opération unaire. Le moteur traite -2147483648 comme le minimum signé sans devoir d’abord stocker sa magnitude positive. Les entiers hors plage échouent ; utilisez un flottant adapté pour un calcul nécessitant une valeur approximative plus grande.
- Les textes conservent caractères et casse. "350" n’est pas le nombre 350, "false" n’est pas FALSE. # et ; sont du texte entre guillemets, des commentaires à l’extérieur. Les conversions sont expliquées sous AS et dans les fiches des fonctions.
- Le moteur reconnaît le jeton, analyse les nombres avec une culture invariante ou retire les guillemets du texte. Changer la langue de l’IDE ne change pas le séparateur décimal du code.
- Un serial, un type graphique et une coordonnée peuvent tous être numériques. Le littéral n’impose pas leur sens : le paramètre de l’API appelée le définit.

## Exemples

### 1. Type hexadécimal et limite entière

```vb
# itemType=0x0EED vaut 3821. lowest=-2147483648 est égal au motif signé 0x80000000. Main renvoie donc itemType=3821. Aucune recherche d’objet n’est effectuée.
Option Explicit On
SUB Main()
    VAR itemType = 0x0EED
    VAR lowest = -2147483648
    IF lowest = 0x80000000 THEN
        RETURN itemType
    END IF
    RETURN 0
END SUB
```

**Explication des paramètres et du déroulement:**

itemType=0x0EED vaut 3821. lowest=-2147483648 est égal au motif signé 0x80000000. Main renvoie donc itemType=3821. Aucune recherche d’objet n’est effectuée.

### 2. Deux formes de guillemets

```vb
# owner="O'Brien" contient une apostrophe. instruction est entouré de guillemets simples et contient des doubles. Joindre owner, " | " et instruction renvoie O'Brien | say "go", sans échappement par barre inverse dans le script.
Option Explicit On
SUB Main()
    VAR owner = "O'Brien"
    VAR instruction = 'say "go"'
    RETURN owner + " | " + instruction
END SUB
```

**Explication des paramètres et du déroulement:**

owner="O'Brien" contient une apostrophe. instruction est entouré de guillemets simples et contient des doubles. Joindre owner, " | " et instruction renvoie O'Brien | say "go", sans échappement par barre inverse dans le script.

### 3. Valeurs logiques numériques

```vb
# enabled=TRUE stocke 1 ; stopped=FALSE stocke 0. Le calcul donne 1*10+0=10. Main renvoie un résultat numérique, pas le TRUE canonique.
Option Explicit On
SUB Main()
    VAR enabled = TRUE
    VAR stopped = FALSE
    RETURN enabled * 10 + stopped
END SUB
```

**Explication des paramètres et du déroulement:**

enabled=TRUE stocke 1 ; stopped=FALSE stocke 0. Le calcul donne 1*10+0=10. Main renvoie un résultat numérique, pas le TRUE canonique.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: number / literal / HEX_NUMBER / DEC_NUMBER
Runtime/Interpreter.cs: VisitNumber / VisitLiteral / VisitSignedOperand
Runtime/InjectionApiUO.cs: TRUE / FALSE intrinsic values
-->
