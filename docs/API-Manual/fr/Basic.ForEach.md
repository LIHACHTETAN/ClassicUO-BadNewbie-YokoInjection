# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

For Each parcourt les éléments d’un tableau ou d’une collection native énumérable, sans index numérique. Cette instruction se place dans une procédure ou fonction ; ce n’est pas un appel API.

## Syntaxe exacte

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## Paramètres

- `item` — item : variable d’itération. Réutilise une variable locale, un paramètre ou un champ accessible ; sinon crée une variable locale, même avec Option Explicit On. Une constante ne peut pas recevoir les éléments.
- `type` — type : AS type facultatif, par exemple Integer. Déclare un itérateur local et convertit chaque élément. Sans AS, une variable existante conserve son type.
- `collection` — collection : expression évaluée une seule fois. Accepte un tableau ou un objet natif énumérable, pas un scalaire. Un tableau imbriqué fournit des lignes ; un second parcours donne les cellules.
- `statements / NEXT item` — statements / NEXT item : corps et fin du parcours. Le nom après NEXT est facultatif mais doit correspondre à l’itérateur. NEXT occupe sa propre ligne.

## Retour

For Each et Next ne renvoient rien. item reçoit la valeur de l’élément, pas automatiquement son index, un ID ou une quantité de pile. RETURN dans le corps termine toute la fonction. Les exemples renvoient Integer 12, 105 et 10.

## Comportement

- La préparation associe FOR EACH et NEXT avant toute initialisation ; une incohérence produit SC020. Le moteur conserve la référence de collection et un curseur distinct. Modifier item ne déplace pas ce curseur.
- Lecture des tableaux par index croissant. Un tableau vide ignore le corps et préserve un itérateur existant sans AS. Un élément non initialisé ou une conversion AS invalide produit une erreur interceptable.
- Affecter item ne remplace pas l’élément. Les tableaux et objets imbriqués restent des références : modifier une cellule de row modifie cette ligne. Réaffecter collection ne remplace pas le parcours actif ; les modifications des éléments futurs du même tableau sont visibles.
- Continue For avance le For ou For Each le plus proche ; Exit For le quitte. Erreur, RETURN et annulation libèrent les énumérateurs natifs. Certaines collections refusent les modifications pendant l’itération ; aucune copie automatique n’est garantie.
- L’itérateur reste visible dans sa procédure après la boucle et conserve sa dernière valeur. Chaque exécution a son curseur. L’IDE fournit complétion, modèles et navigation ; pause et arrêt restent actifs.

## Exemples

### 1. Sommer sans index

```vb
# values[2] contient trois éléments 2, 4, 6. SumItems reçoit ce tableau ; item prend chaque valeur. total passe de 0 à 12 et RETURN transmet Integer 12 à Main. NEXT item ferme ce parcours.
Option Explicit On
Function SumItems(values)
    Var total = 0
    For Each item In values
        total += item
    Next item
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return SumItems(values)
End Sub
```

**Explication des paramètres et du déroulement:**

values[2] contient trois éléments 2, 4, 6. SumItems reçoit ce tableau ; item prend chaque valeur. total passe de 0 à 12 et RETURN transmet Integer 12 à Main. NEXT item ferme ce parcours.

### 2. Une évaluation et une conversion

```vb
# SelectItems reçoit calls ByRef et le porte à 1 ; il renvoie ["2", "3"]. AS Integer convertit les chaînes en 2 et 3, total=5. item=100 ne change ni source ni ordre. Main renvoie calls*100+total, Integer 105.
Option Explicit On
Function SelectItems(ByRef calls)
    calls += 1
    Dim values[1]
    values[0] = "2"
    values[1] = "3"
    Return values
End Function
Sub Main()
    Var calls = 0
    Var total = 0
    For Each item As Integer In SelectItems(calls)
        total += item
        item = 100
    Next
    Return calls * 100 + total
End Sub
```

**Explication des paramètres et du déroulement:**

SelectItems reçoit calls ByRef et le porte à 1 ; il renvoie ["2", "3"]. AS Integer convertit les chaînes en 2 et 3, total=5. item=100 ne change ni source ni ordre. Main renvoie calls*100+total, Integer 105.

### 3. Tableaux imbriqués

```vb
# rows[1][1] contient deux lignes de deux cellules. row reçoit une référence de ligne ; cell reçoit 1, 2, 3, 4. Chaque NEXT ferme sa boucle. SumGrid et Main renvoient Integer 10, sans déduire ID ou quantité.
Option Explicit On
Function SumGrid(rows)
    Var total = 0
    For Each row In rows
        For Each cell In row
            total += cell
        Next cell
    Next row
    Return total
End Function
Sub Main()
    Dim rows[1][1]
    rows[0][0] = 1
    rows[0][1] = 2
    rows[1][0] = 3
    rows[1][1] = 4
    Return SumGrid(rows)
End Sub
```

**Explication des paramètres et du déroulement:**

rows[1][1] contient deux lignes de deux cellules. row reçoit une référence de ligne ; cell reçoit 1, 2, 3, 4. Chaque NEXT ferme sa boucle. SumGrid et Main renvoient Integer 10, sans déduire ID ou quantité.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
