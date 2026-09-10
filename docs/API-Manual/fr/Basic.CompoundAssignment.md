# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Modifier une variable ou un élément de tableau existant avec +=, -=, *=, /=. Le moteur lit sa valeur, applique l’opération et écrit le résultat sans évaluer deux fois la cible.

## Syntaxe exacte

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## Paramètres

- `target` — target : scalaire existant ou élément items[index], grid[x][y]. L’élément doit être initialisé et les indices valides, à partir de zéro. Ceci ne déclare pas de variable.
- `operator` — += et &= additionnent des nombres ou joignent deux String; -= soustrait; *= multiplie; /= divise. Le préprocesseur remplace &= par +=: 5 &= 3 stocke donc 8. String et nombre exigent un CStr explicite. Écrivez chaque opérateur en un seul jeton.
- `value` — value : expression évaluée une fois après la cible et ses indices. Son type doit convenir à l’opération. Convertir les nombres avec CStr pour les ajouter à une String.

## Retour

Aucune valeur (Unit) : c’est une instruction, pas une expression ni un succès booléen. Lire target à la ligne suivante pour récupérer la valeur stockée. La conversion AS s’applique aux scalaires : Integer 5 suivi de /=2 stocke Integer 2, une variable numérique non typée reçoit Decimal 2.5.

## Comportement

- Chaque référence de tableau est capturée avant son indice. Les indices s’évaluent une fois de gauche à droite ; les bornes sont vérifiées avant l’opérande droit. La case sélectionnée reste la cible même si une fonction ByRef remplace la variable du tableau ou une case parente.
- Les règles sont celles de +, -, *, / : débordement entier sur 32 bits, / renvoie Decimal et la division flottante par zéro peut donner Infinity/NaN. String mélangé à un nombre échoue. Les éléments de tableau n’ont pas de conversion scalaire AS.
- Cible non déclarée, élément non initialisé, mauvais indice, opération incompatible, écriture CONST ou conversion ratée déclenchent une erreur interceptable. L’écriture finale est annulée, pas les effets déjà produits par les fonctions opérandes. CONST et AS sont vérifiés lors de l’écriture scalaire, après l’éventuelle exécution à droite.
- Option Explicit vérifie les noms avant exécution. Le débogueur conserve la ligne source, et les boucles respectent pause/arrêt. Lire, calculer puis écrire n’est pas une synchronisation atomique entre procédures concurrentes.

## Exemples

### 1. Les quatre opérations

```vb
# amount commence à 10 : +=2 donne 12, -=3 donne 9, *=4 donne 36, /=2 donne Decimal 18. Main renvoie la valeur stockée ; les affectations elles-mêmes ne renvoient rien.
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**Explication des paramètres et du déroulement:**

amount commence à 10 : +=2 donne 12, -=3 donne 9, *=4 donne 36, /=2 donne Decimal 18. Main renvoie la valeur stockée ; les affectations elles-mêmes ne renvoient rien.

### 2. Un seul calcul de l’indice

```vb
# NextIndex incrémente calls reçu ByRef et renvoie 0. items[0] vaut initialement 5 ; +=2 le change en 7. Un seul appel donne calls=1. Main renvoie items[0]*10+calls=71. La fonction auxiliaire est complète.
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**Explication des paramètres et du déroulement:**

NextIndex incrémente calls reçu ByRef et renvoie 0. items[0] vaut initialement 5 ; +=2 le change en 7. Un seul appel donne calls=1. Main renvoie items[0]*10+calls=71. La fonction auxiliaire est complète.

### 3. Protection d’une constante

```vb
# limit est CONST 5. limit+=1 échoue à l’écriture ; CATCH stocke l’erreur dans problem et met caught=TRUE. limit reste 5. Main renvoie "5:1" avec CStr explicites. Le drapeau représente le traitement d’erreur, pas un résultat d’affectation. La chaîne est construite dans une variable: report=CStr(limit), puis report &= ":" et report &= CStr(caught). Chaque &= met à jour report; Return report donne "5:1".
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**Explication des paramètres et du déroulement:**

limit est CONST 5. limit+=1 échoue à l’écriture ; CATCH stocke l’erreur dans problem et met caught=TRUE. limit reste 5. Main renvoie "5:1" avec CStr explicites. Le drapeau représente le traitement d’erreur, pas un résultat d’affectation. La chaîne est construite dans une variable: report=CStr(limit), puis report &= ":" et report &= CStr(caught). Chaque &= met à jour report; Return report donne "5:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
