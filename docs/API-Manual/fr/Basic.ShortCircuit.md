# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

AndAlso et OrElse combinent des conditions en évitant un opérande droit inutile. AndAlso le saute si la gauche est fausse ; OrElse si elle est vraie. Cela permet de protéger un accès au tableau ou d’éviter des appels.

## Syntaxe exacte

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## Paramètres

- `left` — left : expression évaluée en premier, une fois. Zéro Integer ou Decimal est faux ; tout nombre non nul est vrai.
- `right` — right : expression évaluée une fois seulement si nécessaire. Lectures, appels et effets sautés ne se produisent pas. Un opérande évalué doit être numérique ; convertir explicitement le texte avec CBool.

## Retour

Integer 1 (TRUE) ou 0 (FALSE), pas l’opérande original. result=1 équivaut à result=TRUE ; result=0 à result=FALSE. Ici vrai vaut 1, contrairement au -1 numérique de VB.NET. Un décompte ordinaire reste un décompte ; cette opération produit un booléen.

## Comportement

- Les comparaisons sont internes aux opérandes. AndAlso est prioritaire sur OrElse ; les opérateurs identiques vont de gauche à droite. Les parenthèses modifient le regroupement. Même sauté, un opérande est analysé et vérifié par Option Explicit.
- Par compatibilité, les suites AND/OR/XOR gardent leur regroupement ancien, immédiat et de gauche à droite, avant AndAlso/OrElse. TRUE OR FALSE AndAlso FALSE donne FALSE ; TRUE OrElse FALSE AND FALSE donne TRUE. Parenthéser les mélanges. AND, OR, && et || évaluent toujours les deux côtés.
- Le moteur évalue la gauche, vérifie sa vérité numérique puis renvoie un booléen ou évalue la droite requise. Les erreurs nécessaires remontent à CATCH ; FINALLY et les contrôles pause/arrêt restent actifs. Sauter un appel supprime aussi ses actions.

## Exemples

### 1. Protéger le premier élément

```vb
# FirstEquals reçoit items et expected. GetArrayLength(items)>0 empêche de lire items[0] dans un tableau vide. Main passe [42] et un tableau vide, obtient 1 et 0, puis renvoie 10. La fonction complète ne modifie pas le tableau.
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**Explication des paramètres et du déroulement:**

FirstEquals reçoit items et expected. GetArrayLength(items)>0 empêche de lire items[0] dans un tableau vide. Main passe [42] et un tableau vide, obtient 1 et 0, puis renvoie 10. La fonction complète ne modifie pas le tableau.

### 2. Un appel de secours

```vb
# Probe incrémente calls ByRef et renvoie TRUE. TRUE OrElse Probe(calls) saute l’appel ; FALSE OrElse Probe(calls) l’exécute une fois. Les deux conditions valent 1 et Main renvoie le nombre d’appels : 1.
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**Explication des paramètres et du déroulement:**

Probe incrémente calls ByRef et renvoie TRUE. TRUE OrElse Probe(calls) saute l’appel ; FALSE OrElse Probe(calls) l’exécute une fois. Les deux conditions valent 1 et Main renvoie le nombre d’appels : 1.

### 3. Division protégée et priorité

```vb
# AverageExceeds(total, count, limit) ne divise que si count>0. (25,0,10) donne 0 ; (25,2,10) donne 1 car 12.5>10. TRUE OrElse FALSE AndAlso FALSE donne 1 en sautant le groupe AndAlso. Main renvoie "0:1:1".
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**Explication des paramètres et du déroulement:**

AverageExceeds(total, count, limit) ne divise que si count>0. (25,0,10) donne 0 ; (25,2,10) donne 1 car 12.5>10. TRUE OrElse FALSE AndAlso FALSE donne 1 en sautant le groupe AndAlso. Main renvoie "0:1:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
