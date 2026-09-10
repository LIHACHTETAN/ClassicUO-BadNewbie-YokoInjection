# Option Explicit

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Exige la déclaration des variables avant l’exécution du script. Il s’agit d’une directive de fichier du langage Basic de ce moteur, pas d’une commande UO ni d’un appel de fonction.

## Syntaxe exacte

```text
Option Explicit
Option Explicit On
Option Explicit Off
```

## Paramètres

- `On / Off` — On active la vérification stricte ; Off la désactive. Sans mot après Explicit, On est implicite. Sans directive, le mode historique non strict est conservé. Ne mettez ni parenthèses ni guillemets.

## Retour

Aucune valeur. La directive n’est pas une expression et ne renvoie ni TRUE/FALSE, ni nombre, ni ID. Les RETURN des exemples appartiennent à Main ou Enough, pas à Option Explicit.

## Comportement

- Placez une seule directive avant les variables, constantes et procédures. Des lignes vides et commentaires peuvent la précéder. Une directive répétée ou tardive produit SC013, même pour passer ensuite à Off.
- Avec On, lire ou affecter une variable non déclarée produit SC006 avec sa position dans le code. Les noms de tableaux, compteurs FOR et objets recevant un appel sont aussi vérifiés. VAR/DIM/CONST déclarent des noms, tout comme les paramètres et la variable nommée de CATCH. FOR VAR déclare son compteur.
- Déclarez les variables locales avant leur utilisation. Une variable locale d’une procédure ne déclare pas ce nom dans une autre. Les déclarations globales sont accessibles aux procédures. Ce contrôle des noms ne prouve pas l’initialisation dans toutes les branches.
- Le parseur lit tout le fichier ; l’analyseur résout les déclarations ; une erreur stricte bloque l’exécution avant la première commande. Un rechargement applique le mode du nouveau fichier indépendamment du script précédent. Avec Off, des avertissements restent possibles et lire une valeur inexistante peut encore échouer à l’exécution.
- La directive seule n’effectue aucune action de jeu et n’envoie aucun paquet. Elle ne garantit ni la compatibilité complète avec VB.NET ni l’existence d’une cible.

## Exemples

### 1. Déclarer avant d’affecter

```vb
# On active le contrôle. DIM déclare count comme Integer ; l’affectation de 5 réussit. Main renvoie 5. Remplacer count par coutn non déclaré bloque le lancement avec SC006.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    RETURN count
END SUB
```

**Explication des paramètres et du déroulement:**

On active le contrôle. DIM déclare count comme Integer ; l’affectation de 5 réussit. Main renvoie 5. Remplacer count par coutn non déclaré bloque le lancement avec SC006.

### 2. Paramètre et constante globale

```vb
# La directive seule signifie On. minimum est une constante globale valant 3. amount est un paramètre déclaré dans Enough et une variable locale distincte dans Main. Enough compare 5 >= 3 et renvoie TRUE, soit 1.
Option Explicit
CONST minimum = 3
FUNCTION Enough(amount)
    RETURN amount >= minimum
END FUNCTION
SUB Main()
    VAR amount = 5
    RETURN Enough(amount)
END SUB
```

**Explication des paramètres et du déroulement:**

La directive seule signifie On. minimum est une constante globale valant 3. amount est un paramètre déclaré dans Enough et une variable locale distincte dans Main. Enough compare 5 >= 3 et renvoie TRUE, soit 1.

### 3. Exécuter un ancien script

```vb
# Off permet à l’affectation de créer legacyCounter sans DIM. Main renvoie 7. Cet exemple de compatibilité peut encore afficher un avertissement ; déclarez la variable et utilisez On pour le contrôle strict.
Option Explicit Off
SUB Main()
    legacyCounter = 7
    RETURN legacyCounter
END SUB
```

**Explication des paramètres et du déroulement:**

Off permet à l’affectation de créer legacyCounter sans DIM. Main renvoie 7. Cet exemple de compatibilité peut encore afficher un avertissement ; déclarez la variable et utilisez On pour le contrôle strict.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: optionExplicit
Analysis/SanityAnalyzer.cs
Analysis/InvalidSymbolVisitor.cs
Runtime/InjectionRuntime.cs
-->
