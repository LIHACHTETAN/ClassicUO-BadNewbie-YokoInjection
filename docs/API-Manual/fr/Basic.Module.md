# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Module regroupe fonctions, procédures, VAR/DIM et CONST sous un nom. À l’extérieur, utilisez Tools.Sum ou Counter.count ; les membres du module courant acceptent un nom court.

## Syntaxe exacte

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## Paramètres

- `moduleName` — moduleName : identifiant simple insensible à la casse, par exemple Tools. UO est réservé. Les noms de module dupliqués et les modules imbriqués sont refusés.
- `members` — members : SUB/FUNCTION, VAR/DIM scalaires, CONST, Include et une directive Option Explicit valide. Un champ peut contenir un tableau ou un objet. DIM[...] directement dans un module est indisponible ; créez le tableau par une fonction et stockez-le dans VAR.
- `member / arguments` — member / arguments : nom du membre et arguments de la fonction. Tools.Sum(2, 3) transmet left=2 et right=3. Le champ Counter.count ne prend pas de parenthèses.

## Retour

Module ne renvoie rien et ne s’appelle pas comme Module(...). Tools.Sum(...) renvoie le RETURN de la fonction ; un champ fournit sa valeur. Les comparaisons produisent Integer 1/0, équivalents à TRUE/FALSE dans les conditions et comparaisons. Un nombre, ID ou compteur quelconque n’est pas automatiquement un résultat booléen.

## Comportement

- Déclarez Module au niveau du fichier et terminez par End Module. Include peut charger un module ou ses membres ; les erreurs conservent fichier et ligne d’origine. Option Explicit appartient au fichier physique.
- La préparation collecte les noms qualifiés, résout les noms courts dans le module et vérifie les accès avant exécution. Un paramètre, VAR, CONST ou DIM local explicite masque un champ homonyme. Sinon le champ du module précède la variable globale classique.
- Les champs sont initialisés dans l’ordre des déclarations au début de chaque lancement. Les appels imbriqués de ce lancement partagent leurs modifications. Un nouveau lancement repart à zéro ; les scripts concurrents ne partagent pas cet état. Aucune persistance sur disque.
- Les fonctions/procédures sont Public par défaut ; les champs/constantes sont Private. Private exige Module. Voir Public / Private.
- L’IDE affiche les noms qualifiés. Une procédure publique sans argument obligatoire peut être lancée depuis la liste ; les assistants privés restent internes. Complétion, navigation et inspection respectent le module courant.

## Exemples

### 1. Noms identiques, modules distincts

```vb
# Tools.Sum additionne left=2 et right=3 et renvoie 5 ; Other.Sum les multiplie et renvoie 6. Les noms qualifiés distinguent les fonctions. Main renvoie Integer 11.
Option Explicit On
Module Tools
    Public Function Sum(ByVal left, ByVal right)
        Return left + right
    End Function
End Module
Module Other
    Public Function Sum(ByVal left, ByVal right)
        Return left * right
    End Function
End Module
Sub Main()
    Return Tools.Sum(2, 3) + Other.Sum(2, 3)
End Sub
```

**Explication des paramètres et du déroulement:**

Tools.Sum additionne left=2 et right=3 et renvoie 5 ; Other.Sum les multiplie et renvoie 6. Les noms qualifiés distinguent les fonctions. Main renvoie Integer 11.

### 2. Champ partagé pendant un lancement

```vb
# count commence à 0. Chaque Increment ajoute 1 au même champ ; après deux appels before=2. Read voit Counter.count=5. Main renvoie 2*10+5, Integer 25. Le prochain lancement repart de 0.
Option Explicit On
Module Counter
    Public Var count As Integer = 0
    Public Sub Increment()
        count += 1
    End Sub
    Public Function Read()
        Return count
    End Function
End Module
Sub Main()
    Counter.Increment()
    Counter.Increment()
    Var before = Counter.Read()
    Counter.count = 5
    Return before * 10 + Counter.Read()
End Sub
```

**Explication des paramètres et du déroulement:**

count commence à 0. Chaque Increment ajoute 1 au même champ ; après deux appels before=2. Read voit Counter.count=5. Main renvoie 2*10+5, Integer 25. Le prochain lancement repart de 0.

### 3. Résultat booléen

```vb
# maximum=4 est accessible dans Limits. Allowed(3) renvoie Integer 1 ; Allowed(7) renvoie Integer 0. accepted=TRUE et rejected=FALSE vérifient ces résultats. Main renvoie Integer 10 si les deux tests réussissent.
Option Explicit On
Module Limits
    Private Const maximum = 4
    Public Function Allowed(ByVal amount)
        Return amount <= maximum
    End Function
End Module
Sub Main()
    Var accepted = Limits.Allowed(3)
    Var rejected = Limits.Allowed(7)
    If accepted = TRUE AndAlso rejected = FALSE Then
        Return 10
    End If
    Return 0
End Sub
```

**Explication des paramètres et du déroulement:**

maximum=4 est accessible dans Limits. Allowed(3) renvoie Integer 1 ; Allowed(7) renvoie Integer 0. accepted=TRUE et rejected=FALSE vérifient ces résultats. Main renvoie Integer 10 si les deux tests réussissent.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
