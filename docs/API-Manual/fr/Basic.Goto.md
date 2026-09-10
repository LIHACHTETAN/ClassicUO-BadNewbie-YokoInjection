# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

GoTo transfère l’exécution vers une étiquette de la procédure ou fonction courante. Une étiquette indique un emplacement, pas une procédure appelable. Pour le contrôle ordinaire, privilégiez If, les boucles et Return.

## Syntaxe exacte

```text
GoTo label
label:
```

## Paramètres

- `label` — Identificateur déclaré par label: sur sa propre ligne dans la même procédure. Écrivez GoTo label sans guillemets, parenthèses ni deux-points après la cible. La cible peut précéder ou suivre le saut; la casse est ignorée. Une autre procédure peut réutiliser le nom. Les points sont permis mais ne créent pas un membre de module. Nombres, expressions calculées et étiquettes d’une autre procédure ne sont pas des cibles prises en charge.

## Retour

GoTo et label: ne renvoient rien, ni 1/0 ni TRUE/FALSE. Les exemples renvoient explicitement les Integer -1, 6 et 123 depuis Main, calculés par le script.

## Comportement

- La préparation mémorise les adresses et résout les sauts après lecture de toute la procédure. L’exécution utilise cette adresse sans rechercher le texte. Les variables sont conservées et les actions antérieures ne sont pas annulées.
- Cible inconnue: SC009 et exécution bloquée par le client. Étiquette répétée dans une procédure, même avec une casse différente: SC021 avant initialisation. Include conserve le fichier et la ligne d’origine. Des caractères superflus peuvent provoquer un avertissement; respectez la syntaxe.
- Quitter des Try actifs exécute leurs Finally de l’intérieur vers l’extérieur avant la cible. Un saut dans le même Try actif le conserve. Une erreur dans Finally peut empêcher d’atteindre la cible.
- Entrez dans les boucles et Try/Catch/Finally par leur début normal. Sauter au milieu ne recrée ni initialisation omise ni contexte actif: ce n’est pas une reprise prise en charge. Utilisez Continue ou Exit pour les boucles.
- Un saut arrière n’ajoute ni limite d’essais, ni délai maximal, ni attente. Faites évoluer la condition de sortie. Le flux normal traverse aussi les étiquettes: sautez les sections inutiles ou utilisez Return. GoTo n’installe pas de gestionnaire d’erreur; voir On Error.

## Exemples

### 1. Saut vers l’avant

```vb
# amount=0 choisit NoItems et result=-1, puis Finished renvoie -1. Avec amount=4, le chemin normal affecte 40 et GoTo Finished saute NoItems. Les deux étiquettes appartiennent à Main; ce ne sont pas des appels.
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**Explication des paramètres et du déroulement:**

amount=0 choisit NoItems et result=-1, puis Finished renvoie -1. Avec amount=4, le chemin normal affecte 40 et GoTo Finished saute NoItems. Les deux étiquettes appartiennent à Main; ce ne sont pas des appels.

### 2. Répétition bornée

```vb
# attempt part de 0 et augmente avant le test. Again et again désignent la même étiquette. Trois passages ajoutent 1, 2 et 3; attempt<3 devient faux et Return donne 6. total est initialisé avant l’étiquette et n’est pas remis à zéro par le saut.
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**Explication des paramètres et du déroulement:**

attempt part de 0 et augmente avant le test. Again et again désignent la même étiquette. Trois passages ajoutent 1, 2 et 3; attempt<3 devient faux et Return donne 6. total est initialisé avant l’étiquette et n’est pas remis à zéro par le saut.

### 3. Sortir de Try imbriqués

```vb
# trace devient 1, puis GoTo Finished saute trace=99. Le Finally interne ajoute le chiffre 2, l’externe ajoute 3. Finished est atteint ensuite et renvoie 123. Chaque Finally s’exécute une fois pour ce saut.
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**Explication des paramètres et du déroulement:**

trace devient 1, puis GoTo Finished saute trace=99. Le Finally interne ajoute le chiffre 2, l’externe ajoute 3. Finished est atteint ensuite et renvoie 123. Chaque Finally s’exécute une fois pour ce saut.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
