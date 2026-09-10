# CONST

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

CONST déclare un nom dont la liaison refuse les réaffectations ordinaires. L’initialisation peut être un littéral ou le résultat d’une expression, évalué lorsque la déclaration s’exécute.

## Syntaxe exacte

```text
CONST name [AS type] = expression [, name ...]
```

## Paramètres

- `name` — Identifiant sans guillemets, distinct dans sa portée. La déclaration est globale hors des procédures et locale à l’appel lorsqu’elle est dans une procédure.
- `type` — Type AS facultatif pris en charge, avec les conversions de VAR. AS Integer convertit par exemple en entier signé 32 bits du moteur. Les crochets indiquent une partie facultative ; ne les saisissez pas autour de AS.
- `expression` — Expression initiale obligatoire : nombre, texte entre guillemets, TRUE/FALSE, calcul ou résultat d’une fonction prise en charge. Elle est évaluée une fois pour cette exécution de la déclaration, pas une fois pour toujours.

## Retour

Aucune valeur. CONST est une déclaration, pas une fonction ni une requête logique. Lire son nom donne le résultat stocké. Les RETURN des exemples appartiennent à Main ou ApplyLimit.

## Comportement

- Une affectation ordinaire, LET ou SET ne peut remplacer cette liaison : une erreur de modification de constante est produite. TRY/CATCH peut la traiter. Option Explicit exige des déclarations mais ne détecte pas toute affectation incorrecte avant l’exécution.
- Une constante globale est initialisée lors d’une nouvelle exécution principale et transmise aux procédures appelées avec son indicateur constant et son type AS. Une constante locale est initialisée à sa déclaration. Une fonction d’initialisation peut donc refaire du travail au lancement suivant.
- La protection porte sur la liaison, sans figer en profondeur les contenus Array/Object. Une déclaration locale distincte peut masquer un nom global ; une autre déclaration crée une nouvelle liaison. Évitez de réutiliser les noms des constantes.
- Le moteur évalue l’initialisation, applique AS et marque la constante dans la portée. Une affectation suivante vérifie cet indicateur avant modification. Les exemples de littéraux scalaires n’effectuent pas d’action de jeu.

## Exemples

### 1. Délai fixe dans un calcul

```vb
# delay est une constante Integer locale valant 350. Multiplier par 2 crée la variable distincte doubled=700. Main renvoie 700 ; cet exemple n’attend pas.
Option Explicit On
SUB Main()
    CONST delay AS Integer = 350
    VAR doubled = delay * 2
    RETURN doubled
END SUB
```

**Explication des paramètres et du déroulement:**

delay est une constante Integer locale valant 350. Multiplier par 2 crée la variable distincte doubled=700. Main renvoie 700 ; cet exemple n’attend pas.

### 2. Passer une limite globale

```vb
# limit est une constante Integer globale valant 50. ApplyLimit reçoit amount=72 et maximum=50, puis renvoie la plus petite quantité, 50. Cette fonction est entièrement définie et ne fait que lire ses paramètres.
Option Explicit On
CONST limit AS Integer = 50
FUNCTION ApplyLimit(amount, maximum)
    IF amount > maximum THEN
        RETURN maximum
    END IF
    RETURN amount
END FUNCTION
SUB Main()
    RETURN ApplyLimit(72, limit)
END SUB
```

**Explication des paramètres et du déroulement:**

limit est une constante Integer globale valant 50. ApplyLimit reçoit amount=72 et maximum=50, puis renvoie la plus petite quantité, 50. Cette fonction est entièrement définie et ne fait que lire ses paramètres.

### 3. Traiter une réaffectation interdite

```vb
# limit commence à 3. Affecter 4 produit une erreur sans changer la constante. CATCH place l’erreur dans problem et fixe caught=TRUE. Main renvoie le 1 logique ; TRUE et 1 sont ici équivalents.
Option Explicit On
SUB Main()
    CONST limit = 3
    VAR caught = FALSE
    TRY
        limit = 4
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Explication des paramètres et du déroulement:**

limit commence à 3. Affecter 4 produit une erreur sans changer la constante. CATCH place l’erreur dans problem et fixe caught=TRUE. Main renvoie le 1 logique ; TRUE et 1 sont ici équivalents.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: constDeclaration / globalConst
Runtime/DefinitionCollector.cs: VisitGlobalConst
Runtime/Interpreter.cs: VisitConstDef
Runtime/SemanticScope.cs: DefineVar / SetVar
-->
