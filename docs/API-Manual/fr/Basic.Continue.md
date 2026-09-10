# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Continue ignore le reste du corps de la boucle englobante la plus proche du type demandé. Continue For vise For et For Each ; Continue Do vise Do/Loop et Repeat/Until ; Continue While vise While/Wend.

## Syntaxe exacte

```text
Continue For
Continue Do
Continue While
```

## Paramètres

- `kind` — kind : For, Do ou While obligatoire après Continue, sans parenthèses. La boucle doit entourer l’instruction dans la même procédure. Une boucle imbriquée d’un autre type n’intercepte pas le transfert.

## Retour

Continue ne renvoie rien et ne s’utilise pas dans une expression. Ce n’est ni TRUE/FALSE ni un redémarrage de procédure. La fonction peut ensuite produire RETURN ; les exemples renvoient Integer 10, 3 et 34.

## Comportement

- For exécute NEXT, applique STEP et teste la valeur suivante contre la limite ; For Each prend l’élément suivant. À épuisement, la boucle se termine. L’initialisation du compteur et l’expression de collection ne sont pas répétées.
- Do reteste sa condition au début ou, si elle est sur Loop, à la fin. Repeat/Until utilise UNTIL. Do/Loop sans condition continue jusqu’à sortie ou arrêt. While reteste WHILE ; Continue Do ne sélectionne jamais While/Wend.
- La préparation résout l’adresse de la boucle demandée. En son absence, SC020 survient avant les initialiseurs, même sans Option Explicit. Noms NEXT et terminaisons sont vérifiés. L’ancienne forme FOR/NEXT traversant IF reste compatible.
- Un transfert quittant TRY/CATCH exécute chaque FINALLY traversé, de l’intérieur vers l’extérieur, une fois. Une boucle entièrement dans TRY n’exécute pas ce FINALLY à chaque tour. RETURN ou une erreur dans FINALLY remplace le transfert en attente.
- Continue n’attend pas. Faites évoluer la condition ou utilisez une attente adaptée lors d’un sondage, sinon la boucle peut être infinie. Pause et arrêt restent vérifiés. Les énumérateurs natifs quittés sont libérés et les exécutions sont indépendantes. Exit For/Do/While quitte la boucle.

## Exemples

### 1. Ignorer des éléments

```vb
# values contient -2, 4, 0, 6. item<=0 provoque Continue For pour -2 et 0, sans exécuter total+=item. Cette forme fonctionne dans For Each. SumPositive et Main renvoient Integer 10, soit 4+6.
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**Explication des paramètres et du déroulement:**

values contient -2, 4, 0, 6. item<=0 provoque Continue For pour -2 et 0, sans exécuter total+=item. Cette forme fonctionne dans For Each. SumPositive et Main renvoient Integer 10, soit 4+6.

### 2. Choisir la boucle extérieure par type

```vb
# AdvanceTo reçoit limit=3 ; count commence à 0. Dans While True, count augmente puis Continue Do vise le Do extérieur. Sa condition est retestée à chaque transfert ; count=3 termine la boucle et renvoie Integer 3.
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**Explication des paramètres et du déroulement:**

AdvanceTo reçoit limit=3 ; count commence à 0. Dans While True, count augmente puis Continue Do vise le Do extérieur. Sa condition est retestée à chaque transfert ; count=3 termine la boucle et renvoie Integer 3.

### 3. Nettoyage d’un tour ignoré

```vb
# Process reçoit limit=3 et skip=2. i prend 1, 2, 3. Le second tour ignore total+=i, mais Finally augmente cleanup trois fois. total=4 et cleanup=3 ; RETURN cleanup*10+total renvoie Integer 34.
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**Explication des paramètres et du déroulement:**

Process reçoit limit=3 et skip=2. i prend 1, 2, 3. Le second tour ignore total+=i, mais Finally augmente cleanup trois fois. total=4 et cleanup=3 ; RETURN cleanup*10+total renvoie Integer 34.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
