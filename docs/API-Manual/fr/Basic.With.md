# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

With regroupe des opérations sur un même objet mémorisé. Le point initial désigne un membre de cet objet. Basic propose aussi With UO et With moduleName pour choisir explicitement un espace de noms : ce sont des extensions du moteur.

## Syntaxe exacte

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## Paramètres

- `objectExpression / UO / moduleName` — Récepteur obligatoire : objet natif List(), Dictionary(), variable contenant un objet ou fonction qui en renvoie un. L’expression est évaluée une seule fois à l’entrée, même si le corps est vide. Nombres, chaînes, tableaux et Unit ne sont pas des récepteurs objets ici. Une variable locale objet a priorité sur un module homonyme.
- `.Method(arguments) / .field` — Appelez les méthodes avec leurs parenthèses : .Add(value), .Item(index), .Count(). Paramètres et retours gardent leur sens ; voir Basic.List/Basic.Dictionary. Les champs et propriétés arbitraires d’objets ne sont pas pris en charge ici. Un module autorise ses .field et .Procedure(arguments) accessibles ; Private reste applicable. Avec With UO, .Command(...) signifie UO.Command(...). Les commandes de jeu restent préfixées par UO ailleurs.
- `statements / End With` — Le corps peut être vide ou contenir appels, affectations, conditions et blocs correctement imbriqués. End With est obligatoire. Un point initial hors du corps est invalide. Les autres objets restent accessibles par leur nom complet.

## Retour

With est un bloc de contrôle, sans retour propre : ni ID, ni Boolean, ni indicateur de réussite. Chaque méthode conserve son contrat de retour. Les Return des exemples renvoient explicitement un Integer depuis Main ; 127, 28 et 72 sont des calculs de démonstration.

## Comportement

- La préparation valide le bloc et lie les noms relatifs. À l’entrée, l’interpréteur mémorise la référence issue de l’expression dans l’appel courant. Réaffecter la variable initiale ne change pas cette référence. Repasser par l’en-tête réévalue l’expression ; chaque appel récursif possède sa référence.
- L’en-tête d’un With interne utilise le contexte externe. Dans son corps, le point vise l’objet interne ; End With restaure le contexte externe. Return, les transferts de boucle et GoTo vers l’extérieur libèrent les portées quittées après les Finally concernés. Sauter dans le corps d’un With est interdit.
- Un mauvais récepteur ou une méthode inconnue provoque une erreur, pas false. Catch/On Error peut la traiter. Si le récepteur échoue, On Error Resume Next saute tout le bloc. With ne boucle pas, n’attend pas et ne crée pas de thread. Pause/arrêt restent actifs. Les noms liés sont mis en cache avec le script préparé ; le récepteur n’est pas réévalué à chaque méthode.

## Exemples

### 1. Une seule évaluation

```vb
# Choose reçoit values par ByVal et calls par ByRef, augmente calls à 1 et renvoie la liste initiale. Les deux .Add ajoutent 2 et 7 à cette liste mémorisée, même si values reçoit une nouvelle liste entre les appels. Item utilise les indices 0 et 1. Main renvoie 1*100+2*10+7=127.
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**Explication des paramètres et du déroulement:**

Choose reçoit values par ByVal et calls par ByRef, augmente calls à 1 et renvoie la liste initiale. Les deux .Add ajoutent 2 et 7 à cette liste mémorisée, même si values reçoit une nouvelle liste entre les appels. Item utilise les indices 0 et 1. Main renvoie 1*100+2*10+7=127.

### 2. Objets imbriqués et finalisation

```vb
# groups associe la clé texte "child" à la liste child. .Item("child") lit cet objet dans le dictionnaire externe. Les .Add(2) et .Add(7) du Finally interne modifient la liste. Après End With, .Set("result",8) vise de nouveau le dictionnaire. Count() renvoie 2 et Item("result") renvoie 8 : Main donne 28.
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**Explication des paramètres et du déroulement:**

groups associe la clé texte "child" à la liste child. .Item("child") lit cet objet dans le dictionnaire externe. Les .Add(2) et .Add(7) du Finally interne modifient la liste. Après End With, .Set("result",8) vise de nouveau le dictionnaire. Count() renvoie 2 et Item("result") renvoie 8 : Main donne 28.

### 3. Module et espace UO

```vb
# With Tools qualifie .total, .AddAmount et .CountItems. total reçoit 4 puis AddAmount reçoit amount=3 par ByVal, soit 7. CountItems reçoit un tableau de deux éléments et appelle UO.GetArrayLength(values) via With UO, obtenant 2. Main calcule 7*10+2=72. Les règles d’accès du module restent applicables.
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**Explication des paramètres et du déroulement:**

With Tools qualifie .total, .AddAmount et .CountItems. total reçoit 4 puis AddAmount reçoit amount=3 par ByVal, soit 7. CountItems reçoit un tableau de deux éléments et appelle UO.GetArrayLength(values) via With UO, obtenant 2. Main calcule 7*10+2=72. Les règles d’accès du module restent applicables.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
