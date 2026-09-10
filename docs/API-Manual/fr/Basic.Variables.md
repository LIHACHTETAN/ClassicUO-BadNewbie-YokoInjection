# VAR / DIM

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

VAR et DIM scalaire déclarent une valeur nommée. Une affectation évalue l’expression et stocke son résultat. Une déclaration dans une procédure est locale à cet appel ; en dehors des procédures, elle est globale au script.

## Syntaxe exacte

```text
VAR name [AS type] [= expression] [, name ...]
DIM name [AS type] [= expression] [, name ...]
name = expression
LET name = expression
SET name = expression
```

## Paramètres

- `name` — Identifiant sans guillemets : lettres, chiffres et traits de soulignement, commençant par une lettre ou un trait de soulignement. Gardez la même orthographe et évitez les mots-clés.
- `type` — Annotation AS facultative. Integer/Long/Short/Byte utilisent l’entier signé 32 bits du moteur ; Double/Single/Decimal son nombre en double précision ; String du texte ; Boolean/Bool un booléen ; Variant/Object conservent la nature de la valeur. Ces alias n’imposent pas les plages byte/short/long distinctes de VB.NET.
- `expression` — Initialisation facultative dans VAR/DIM, expression droite obligatoire pour affecter. Elle est évaluée à l’exécution de la ligne. AS String sans initialisation donne un texte vide ; les nombres typés et Boolean valent zéro par défaut. Sans initialisation, VAR non typé et VAR AS Variant/Object contiennent Unit (absence de valeur), tandis que DIM scalaire fournit 0. Une variable non typée peut ensuite contenir une autre nature de valeur.

## Retour

Aucune valeur. VAR, DIM et l’affectation ne renvoient pas de résultat. Lire le nom donne la valeur stockée. RETURN dans chaque exemple renvoie cette valeur depuis Main, pas depuis DIM.

## Comportement

- Les crochets de la syntaxe indiquent une partie facultative ; ne les écrivez pas autour de AS ou de l’initialisation. DIM tableau utilise une autre forme.
- LET et SET sont des formes compatibles de l’affectation ordinaire. Avec Option Explicit On, ils ne déclarent aucun nom. Le type AS s’applique aussi aux affectations suivantes ; une conversion impossible ou un type non pris en charge provoque une erreur d’exécution.
- Les noms locaux appartiennent à l’appel de procédure. Une déclaration dans IF ne crée pas de portée de bloc séparée. Une branche jamais exécutée ne crée pas de valeur à l’exécution. Déclarez avant le branchement si la valeur est nécessaire après.
- Compatibilité Injection : la procédure appelée hérite des valeurs scalaires globales actuelles de l’appelant et de leurs types AS. Réaffecter un scalaire dans la procédure appelée ne modifie pas l’appelant. Renvoyez la nouvelle valeur ou passez un argument BYREF pour effectuer cette mise à jour. Les valeurs Array/Object ne sont pas clonées en profondeur. Une nouvelle exécution principale réinitialise les globales ; une déclaration locale masque le nom de son cadre sans remplacer la déclaration globale.
- Le moteur évalue l’initialisation, définit le stockage dans la portée actuelle puis applique la conversion. Une affectation suivante évalue d’abord son expression droite. Ces calculs sont locaux ; les variables ne sont pas automatiquement enregistrées dans un profil ou fichier JSON.

## Exemples

### 1. Modifier un entier

```vb
# count commence à 0, reçoit 5, puis LET ajoute 2. Main renvoie l’Integer 7. Le premier DIM déclare le nom ; les affectations suivantes modifient sa valeur.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    LET count = count + 2
    RETURN count
END SUB
```

**Explication des paramètres et du déroulement:**

count commence à 0, reçoit 5, puis LET ajoute 2. Main renvoie l’Integer 7. Le premier DIM déclare le nom ; les affectations suivantes modifient sa valeur.

### 2. Texte et indicateur logique

```vb
# label commence comme String vide. SET stocke "ore". enabled est le Boolean TRUE ; la branche IF renvoie la String "ore". TRUE sans guillemets représente le 1 logique.
Option Explicit On
SUB Main()
    DIM label AS String
    VAR enabled AS Boolean = TRUE
    SET label = "ore"
    IF enabled = TRUE THEN
        RETURN label
    END IF
    RETURN "disabled"
END SUB
```

**Explication des paramètres et du déroulement:**

label commence comme String vide. SET stocke "ore". enabled est le Boolean TRUE ; la branche IF renvoie la String "ore". TRUE sans guillemets représente le 1 logique.

### 3. Entrée globale et calcul local

```vb
# baseAmount est global et vaut 4. extra est local à Calculate et vaut 3. Calculate renvoie 7 ; Main le stocke dans son propre result local et renvoie 7. extra n’est pas une variable locale de Main.
Option Explicit On
VAR baseAmount AS Integer = 4
FUNCTION Calculate()
    VAR extra = 3
    RETURN baseAmount + extra
END FUNCTION
SUB Main()
    VAR result = Calculate()
    RETURN result
END SUB
```

**Explication des paramètres et du déroulement:**

baseAmount est global et vaut 4. extra est local à Calculate et vaut 3. Calculate renvoie 7 ; Main le stocke dans son propre result local et renvoie 7. extra n’est pas une variable locale de Main.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim
Runtime/Interpreter.cs: VisitVarDef / VisitAssignment
Runtime/SemanticScope.cs: DefineVar / SetVar / Coerce
-->
