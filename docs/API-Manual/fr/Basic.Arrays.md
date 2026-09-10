# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

DIM crée un tableau dynamique ; REDIM remplace son stockage. PRESERVE copie les valeurs aux indices communs. Une dimension indique la borne supérieure incluse, pas le nombre d’éléments. Initialiser les cases avant lecture.

## Syntaxe exacte

```text
DIM name[upper]
DIM name(upper) AS type
DIM grid[xUpper][yUpper]
DIM grid(xUpper, yUpper)
REDIM name[upper]
REDIM PRESERVE name[upper]
name[index] = value
GetArrayLength(name)
```

## Paramètres

- `name` — name : variable du tableau. DIM la déclare ; REDIM remplace un tableau dans une variable existante. Lire et écrire avec items[i] ou grid[x][y].
- `upper` — upper : expression convertie en Integer, évaluée une fois de gauche à droite. DIM items[2] crée trois cases 0..2. -1 crée une dimension vide ; une borne inférieure ou une longueur débordante échoue. La mémoire limite la taille réelle.
- `PRESERVE` — PRESERVE : facultatif après REDIM. Copie récursivement les indices communs ; réduire supprime les valeurs hors des nouvelles bornes. Sans lui, les cases ne sont pas initialisées.
- `AS type` — AS type : annotation acceptée dans DIM ; elle ne type, initialise ou convertit pas les éléments. Plusieurs types de valeurs peuvent coexister.

## Retour

DIM et REDIM ne renvoient aucune valeur (Unit). items[i] renvoie la valeur et son type réel : Integer, Decimal, String, Array ou Object. Lire une case non initialisée provoque une erreur, pas zéro ou FALSE. GetArrayLength(array) renvoie la longueur extérieure en Integer, ou 0 pour une valeur non tableau.

## Comportement

- DIM grid(1, 2) équivaut à grid[1][2] : deux lignes de trois cases. Les appels dans les bornes sont conservés. Accéder avec grid[1][2] ; les parenthèses dans une expression désignent un appel de fonction.
- Affectation et passage ByVal copient la référence, pas les éléments : les alias voient les mutations communes. REDIM crée un nouveau tableau ; les alias conservent l’ancien. PRESERVE copie les coordonnées communes des tableaux imbriqués, sans cloner intégralement les objets.
- Indices à partir de zéro uniquement. DIM items[2]=5 et les initialiseurs REDIM sont refusés avec SC014 ; affecter les cases séparément. Mauvais indice ou lecture non initialisée provoquent des erreurs interceptables.
- Ce dialecte diffère des tableaux typés VB.NET par les types dynamiques et PRESERVE multidimensionnel. Un booléen stocké utilise 1/0 ; un nombre quelconque ou une longueur n’est pas un indicateur de succès.
- RETURN array renvoie la référence du tableau ; son stockage survit à la fonction créatrice. Affecter le résultat ne copie pas les éléments. Une fonction partagée peut créer un tableau pour un champ Module. Chaque nouveau lancement crée ses propres tableaux lorsque DIM est exécuté.

## Exemples

### 1. Additionner les éléments

```vb
# Abs(-2) donne la borne 2 : Main crée 3 cases et écrit 2, 4, 6. Sum reçoit la référence ByVal, parcourt 0..GetArrayLength(items)-1 et renvoie 12. La fonction complète ne modifie rien et accepte un tableau vide.
Option Explicit On
FUNCTION Sum(ByVal items)
    VAR total = 0
    VAR i = 0
    FOR i = 0 TO GetArrayLength(items) - 1
        total += items[i]
    NEXT
    RETURN total
END FUNCTION
SUB Main()
    DIM items(Abs(-2))
    items[0] = 2
    items[1] = 4
    items[2] = 6
    RETURN Sum(items)
END SUB
```

**Explication des paramètres et du déroulement:**

Abs(-2) donne la borne 2 : Main crée 3 cases et écrit 2, 4, 6. Sum reçoit la référence ByVal, parcourt 0..GetArrayLength(items)-1 et renvoie 12. La fonction complète ne modifie rien et accepte un tableau vide.

### 2. Agrandir et conserver

```vb
# values contient 7 et 8. REDIM PRESERVE values(2) crée 3 cases et copie les indices 0 et 1. Initialiser la nouvelle case 2 avec 9. Main renvoie 7*100+8*10+9=789.
Option Explicit On
SUB Main()
    DIM values[1]
    values[0] = 7
    values[1] = 8
    REDIM PRESERVE values(2)
    values[2] = 9
    RETURN values[0] * 100 + values[1] * 10 + values[2]
END SUB
```

**Explication des paramètres et du déroulement:**

values contient 7 et 8. REDIM PRESERVE values(2) crée 3 cases et copie les indices 0 et 1. Initialiser la nouvelle case 2 avec 9. Main renvoie 7*100+8*10+9=789.

### 3. Observer les alias

```vb
# grid a deux lignes de deux cases. alias partage le tableau : alias[0][1]=9 modifie aussi grid. PRESERVE agrandit grid à trois lignes et conserve 9 ; alias garde deux lignes. "9:3:2" indique la valeur, la nouvelle longueur extérieure et celle de l’ancien alias.
Option Explicit On
SUB Main()
    DIM grid[1][1]
    grid[0][1] = 4
    VAR alias = grid
    alias[0][1] = 9
    REDIM PRESERVE grid[2][1]
    RETURN CStr(grid[0][1]) + ":" + CStr(GetArrayLength(grid)) + ":" + CStr(GetArrayLength(alias))
END SUB
```

**Explication des paramètres et du déroulement:**

grid a deux lignes de deux cases. alias partage le tableau : alias[0][1]=9 modifie aussi grid. PRESERVE agrandit grid à trois lignes et conserve 9 ; alias garde deux lignes. "9:3:2" indique la valeur, la nouvelle longueur extérieure et celle de l’ancien alias.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
