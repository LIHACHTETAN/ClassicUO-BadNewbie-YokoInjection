# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Wait Until teste une condition jusqu’au succès ou à l’expiration du délai. C’est une extension Basic, pas une instruction VB.NET. Elle reste dans le script courant sans créer de thread ni lancer une autre procédure.

## Syntaxe exacte

```text
Wait Until condition Timeout milliseconds
```

## Paramètres

- `condition` — condition est évaluée immédiatement puis entre de courtes attentes. Utilisez un Boolean ou une comparaison : le nombre 0 signifie false, les autres valeurs suivent If. Le String "false" n’est pas Boolean false. Les appels UO et fonctions personnelles sont possibles ; leurs erreurs se propagent et leurs effets se répètent à chaque test.
- `Timeout milliseconds` — Timeout est obligatoire. milliseconds est évalué une seule fois avant le premier test : Integer 0..2147483647. Nombres négatifs, fractions et Strings provoquent une erreur avant condition. Zéro permet seulement le test immédiat. Ailleurs, timeout reste un nom de variable valide.

## Retour

L’instruction ne renvoie rien. Le succès passe à la ligne suivante ; l’expiration produit une erreur avec fichier et ligne, traitable par Try/Catch ou On Error. Sinon l’exécution courante échoue. Aucun false automatique : l’exemple 2 construit explicitement une fonction renvoyant True/1 ou False/0.

## Comportement

- Le moteur mémorise la durée et démarre un Stopwatch monotone. Le premier test immédiat peut réussir même avec zéro délai. Après false, la boucle vérifie annulation et pause, calcule le temps restant et attend au plus 10 ms avant de tester à nouveau. Elle évite une boucle active permanente ; l’ordonnanceur peut prolonger l’intervalle.
- La pause suspend les tests, mais le temps réel écoulé compte dans le délai. À la reprise, un délai expiré est signalé avant un nouveau test. L’arrêt interrompt l’attente et ignore Catch/Finally du script comme les autres annulations d’urgence. Un appel bloqué dans condition ne peut pas être interrompu de force : gardez les fonctions courtes. Un test commencé termine avant le traitement de son résultat ou erreur.
- L’erreur de condition reste intacte, sans devenir un timeout. Erreurs ordinaires et expirations exécutent les Finally concernés. Les variables appartiennent à l’appel courant ; chaque nouvelle entrée crée un nouveau délai. Ni End Wait ni paramètre d’intervalle supplémentaire. Wait(milliseconds) reste une fonction de délai distincte.

## Exemples

### 1. Interroger une fonction avec une limite

```vb
# checks commence à 0 ; Ready le reçoit ByRef et l’incrémente par test. required=3 est ByVal ; budget=5000 autorise cinq secondes. Deux tests donnent false, le troisième true ; Main renvoie Integer 3. C’est une démonstration déterministe, sans simulation de serveur ; remplacez la condition par votre contrôle réel.
Option Explicit On
Function Ready(ByRef checks As Integer, ByVal required As Integer) As Boolean
    checks += 1
    Return checks >= required
End Function

Sub Main()
    Dim checks As Integer = 0
    Const budget = 5000
    Wait Until Ready(checks, 3) Timeout budget
    Return checks
End Sub
```

**Explication des paramètres et du déroulement:**

checks commence à 0 ; Ready le reçoit ByRef et l’incrémente par test. required=3 est ByVal ; budget=5000 autorise cinq secondes. Deux tests donnent false, le troisième true ; Main renvoie Integer 3. C’est une démonstration déterministe, sans simulation de serveur ; remplacez la condition par votre contrôle réel.

### 2. Créer une fonction renvoyant Boolean

```vb
# TryWait reçoit ready=False et budget=0. Le test immédiat échoue avec un timeout. Catch problem renvoie False ; Main renvoie 0, comparable à False. ready=True donnerait 1/True. Cette fonction intercepte toutes les erreurs : examinez problem pour les distinguer. ready est une valeur Boolean, pas un callback.
Option Explicit On
Function TryWait(ByVal ready As Boolean, ByVal budget As Integer) As Boolean
    Try
        Wait Until ready Timeout budget
        Return True
    Catch problem
        Return False
    End Try
End Function

Sub Main()
    Dim success = TryWait(False, 0)
    Return success
End Sub
```

**Explication des paramètres et du déroulement:**

TryWait reçoit ready=False et budget=0. Le test immédiat échoue avec un timeout. Catch problem renvoie False ; Main renvoie 0, comparable à False. ready=True donnerait 1/True. Cette fonction intercepte toutes les erreurs : examinez problem pour les distinguer. ready est une valeur Boolean, pas un callback.

### 3. Conserver une erreur et finaliser

```vb
# CheckStatus reçoit state=-1 et lance immédiatement "disconnected". Le délai de 3000 ms ne remplace pas l’erreur. Catch copie problem dans message ; Finally fixe finished=True/1. Main renvoie "disconnected:1". state=1 réussirait immédiatement, state=0 resterait false jusqu’au délai. Aucune connexion au jeu n’est nécessaire.
Option Explicit On
Function CheckStatus(ByVal state As Integer) As Boolean
    If state < 0 Then
        Throw "disconnected"
    End If
    Return state = 1
End Function

Sub Main()
    Dim message = ""
    Dim finished = False
    Try
        Wait Until CheckStatus(-1) Timeout 3000
    Catch problem
        message = problem
    Finally
        finished = True
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Explication des paramètres et du déroulement:**

CheckStatus reçoit state=-1 et lance immédiatement "disconnected". Le délai de 3000 ms ne remplace pas l’erreur. Catch copie problem dans message ; Finally fixe finished=True/1. Main renvoie "disconnected:1". state=1 réussirait immédiatement, state=0 resterait false jusqu’au délai. Aucune connexion au jeu n’est nécessaire.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
