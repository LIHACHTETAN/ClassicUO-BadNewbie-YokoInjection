# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Try traite les erreurs d’exécution de son corps et des fonctions appelées. Catch reçoit l’erreur, Finally effectue la finalisation, Throw crée une erreur ou la relance. Un résultat API égal à 0 ou false reste un résultat ordinaire à vérifier explicitement : il ne déclenche pas Catch.

## Syntaxe exacte

```text
Try
    statements
Catch
    handlerStatements
Finally
    cleanupStatements
End Try
Catch name
Catch name As Exception
Catch name As String
Throw stringExpression
Throw
```

## Paramètres

- `Try / statements` — Try exige un Catch, un Finally ou les deux avant End Try. Les blocs peuvent être imbriqués. Un corps réussi saute Catch. Plusieurs Catch, les filtres When et Exit Try ne sont pas implémentés dans ce sous-ensemble.
- `Catch / name / As type` — La variable de Catch est facultative. name reçoit le message sous forme de String. As String indique cette représentation ; As Exception est une écriture de compatibilité, ni objet .NET ni filtre de type. Les autres types sont rejetés. Un nouveau nom devient local à la procédure et masque une globale homonyme. Une locale existante reçoit une affectation normale respectant son type/Const. Déclarez un String avant Try si la variable doit exister sans exécuter Catch.
- `Finally / End Try` — Finally est facultatif en présence de Catch et son corps peut être vide. Fin normale, erreurs, Return, Exit Sub/Function et transferts de boucle/GoTo vers l’extérieur exécutent les Finally concernés. End Try est obligatoire. L’annulation ignore volontairement Catch et le Finally du script pour ne pas retarder l’arrêt d’urgence.
- `Throw stringExpression` — Throw stringExpression évalue une seule fois le message et crée une nouvelle erreur de script. Le message doit être String ; utilisez CStr explicitement pour d’autres valeurs. C’est une forme Basic, pas Throw New Exception(...) de VB.NET. Sans gestionnaire, l’exécution courante échoue, pas tous les autres scripts.
- `Throw` — Throw sans message est permis seulement dans Catch, y compris ses blocs imbriqués. Il relance l’erreur active en conservant message, fichier et ligne d’origine. Une fonction appelée depuis Catch a besoin de son propre Catch pour employer ce Throw.

## Retour

Try/Catch/Finally et Throw ne renvoient ni ID, ni nombre, ni Boolean. Catch fournit le message dans name ; Throw transfère le contrôle au lieu de renvoyer une valeur. Les exemples renvoient explicitement deux Strings et Integer 13 depuis Main. Les API appelées conservent leurs retours habituels.

## Comportement

- La préparation valide les blocs et interdit GoTo/On Error GoTo à l’intérieur de Try, Catch ou Finally. Le générateur conserve les adresses des gestionnaires et finalisations. Chaque appel possède ses gestionnaires actifs ; l’erreur atteint le Catch admissible le plus proche. Une erreur dans Catch traverse son Finally vers un gestionnaire externe. Sans gestionnaire structuré, les règles On Error ordinaires peuvent intervenir.
- Retour, erreur ou saut en attente sont conservés pendant Finally. Les finalisations imbriquées vont de l’intérieur vers l’extérieur. Une nouvelle erreur dans Finally remplace l’erreur en attente. Basic autorise aussi Return et les sauts sortants depuis Finally : ils remplacent la continuation en attente, contrairement à VB.NET. Une relance conserve la première position d’erreur, même dans une fonction appelée.
- Pause/arrêt restent actifs. Try ne crée ni thread, ni nouvelle tentative, ni attente. Les adresses préparées sont réutilisées ; testez directement les conditions habituelles au lieu d’utiliser des exceptions. L’arrêt d’urgence saute la finalisation du script ; les ressources appartenant à l’hôte suivent leur propre durée de vie dans le moteur.

## Exemples

### 1. Valider un paramètre et conserver le message

```vb
# CheckedAmount reçoit amount=-2 comme Integer par ByVal. La valeur négative déclenche Throw "amount must be non-negative". Catch reçoit ce String dans problem et le copie dans message ; As Exception ne crée pas d’objet. Finally met finished à 1. Main renvoie "amount must be non-negative:1". Un montant non négatif reviendrait normalement sans exécuter Catch.
Option Explicit On
Function CheckedAmount(ByVal amount As Integer) As Integer
    If amount < 0 Then
        Throw "amount must be non-negative"
    End If
    Return amount
End Function

Sub Main()
    Dim message=""
    Dim finished=0
    Try
        CheckedAmount(-2)
    Catch problem As Exception
        message=problem
    Finally
        finished=1
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Explication des paramètres et du déroulement:**

CheckedAmount reçoit amount=-2 comme Integer par ByVal. La valeur négative déclenche Throw "amount must be non-negative". Catch reçoit ce String dans problem et le copie dans message ; As Exception ne crée pas d’objet. Finally met finished à 1. Main renvoie "amount must be non-negative:1". Un montant non négatif reviendrait normalement sans exécuter Catch.

### 2. Relancer vers le gestionnaire externe

```vb
# Le Throw interne crée "missing item". Catch interne met trace à 1 ; Throw sans message conserve la même erreur. Finally interne ajoute 2, Catch externe copie outerProblem dans message et ajoute 3, Finally externe ajoute 4. Main renvoie "1234:missing item". trace représente l’ordre d’exécution, pas un code d’erreur.
Option Explicit On
Sub Main()
    Dim trace=0
    Dim message=""
    Try
        Try
            Throw "missing item"
        Catch problem
            trace=1
            Throw
        Finally
            trace=trace*10+2
        End Try
    Catch outerProblem
        message=outerProblem
        trace=trace*10+3
    Finally
        trace=trace*10+4
    End Try
    Return CStr(trace) & ":" & message
End Sub
```

**Explication des paramètres et du déroulement:**

Le Throw interne crée "missing item". Catch interne met trace à 1 ; Throw sans message conserve la même erreur. Finally interne ajoute 2, Catch externe copie outerProblem dans message et ajoute 3, Finally externe ajoute 4. Main renvoie "1234:missing item". trace représente l’ordre d’exécution, pas un code d’erreur.

### 3. Finaliser chaque itération commencée

```vb
# number prend 1, 2 et 3. Seul 1 est ajouté à total : Continue For saute 2, Exit For termine à 3. Les trois Try commencés exécutent Finally, donc finished atteint 3. Main renvoie 1*10+3=13. Finally n’exige pas d’erreur ; le transfert de boucle attend la finalisation de l’itération.
Option Explicit On
Sub Main()
    Dim total=0
    Dim finished=0
    For Var number=1 To 3
        Try
            If number=2 Then
                Continue For
            End If
            If number=3 Then
                Exit For
            End If
            total+=number
        Finally
            finished+=1
        End Try
    Next
    Return total*10+finished
End Sub
```

**Explication des paramètres et du déroulement:**

number prend 1, 2 et 3. Seul 1 est ajouté à total : Continue For saute 2, Exit For termine à 3. Les trois Try commencés exécutent Finally, donc finished atteint 3. Main renvoie 1*10+3=13. Finally n’exige pas d’erreur ; le transfert de boucle attend la finalisation de l’itération.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: tryStatement / catchClause / finallyClause / throwStatement
Analysis/TryStructureValidator.cs: VisitTryStatement / VisitSubrutine / VisitCatchClause / VisitThrowStatement
Runtime/Instructions/Generator.cs: Generate(TryStatementContext)
Runtime/Instructions/TryInstruction.cs: TryInstruction / CatchInstruction / FinallyInstruction / EndTryInstruction
Runtime/Interpreter.cs: CallSubrutine / TryHandleStructuredError / Transfer / DeferReturn / Failure
Runtime/SemanticScope.cs: IsLocal / DefineVar / SetVar
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/try-catch-finally-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/throw-statement
-->
