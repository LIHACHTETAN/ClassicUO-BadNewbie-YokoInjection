# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

On Error choisit le traitement des erreurs d’exécution suivantes dans la procédure ou fonction actuelle. C’est une instruction du langage, pas un appel API. Pour une gestion structurée avec nettoyage, utilisez Try/Catch/Finally.

## Syntaxe exacte

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## Paramètres

- `label` — Étiquette existante de la même procédure, écrite label: sur une ligne séparée. Avant ou après On Error, sans distinction de casse. Ni fonction, ni chaîne, ni numéro de ligne. Une étiquette inconnue produit SC009 ; le client bloque ce script.
- `Resume Next / On Error` — On Error Resume Next poursuit automatiquement après l’instruction défaillante sans étiquette. Les instructions réussies ne changent pas. Portée : l’appel de procédure courant, pas tous les scripts.
- `0` — On Error GoTo 0 désactive le mode. Zéro est une valeur de contrôle spéciale, pas une étiquette ni un résultat Boolean. Autres étiquettes numériques et GoTo -1 ne sont pas pris en charge.
- `Resume / Resume Next` — Dans le gestionnaire, Resume recommence l’instruction défaillante ; Resume Next poursuit après elle. Une erreur enregistrée est nécessaire ; son adresse est effacée après le transfert. Aucun argument étiquette ou délai n’est accepté.

## Retour

On Error et Resume ne renvoient rien. Une erreur traitée ne devient pas TRUE/FALSE et ne répare pas automatiquement l’affectation. Les exemples renvoient explicitement Integer 5,18,10. Aucun retour arrière automatique des effets antérieurs.

## Comportement

- La préparation résout les étiquettes après lecture de toute la procédure, dans les deux directions. À l’exécution le mode est mémorisé ; Try est examiné avant On Error lors d’une exception.
- Le moteur conserve l’adresse défaillante. Le mode étiquette saute au gestionnaire ; Resume Next automatique passe l’instruction. Resume réévalue expressions et appels : corrigez la cause et considérez les effets répétés.
- GoTo 0 conserve l’adresse de l’erreur en attente. Le gestionnaire peut se désactiver, réparer puis Resume. Désactivez-le avant ses opérations susceptibles d’échouer afin d’éviter une nouvelle entrée.
- Les erreurs de syntaxe et l’annulation ne sont pas récupérées. Un retour 0, FALSE ou un statut d’échec sans exception ne déclenche pas On Error : vérifiez le résultat de la commande.
- Évitez l’entrée normale dans le gestionnaire avec Return ou GoTo. Chaque procédure appelée a son mode ; une erreur non traitée peut remonter à l’appelant. Resume y répète l’instruction d’appel entière, pas une ligne interne. Ni limite de tentatives ni attente automatique.
- Si une erreur quitte Try après nettoyage et atteint un gestionnaire externe On Error GoTo, Resume reprend tout le Try à son en-tête. Resume Next et On Error Resume Next poursuivent à la première instruction après End Try. Les actions accomplies peuvent se répéter ; la reprise ne rentre pas au milieu du corps déjà terminé.

## Exemples

### 1. Ignorer une affectation échouée

```vb
# values[0] alloue une cellule ; l’indice 5 est invalide. result=1. On Error Resume Next ignore la lecture échouée avant affectation, donc result reste 1. GoTo 0 désactive, result+=4 donne 5. Main renvoie 5 sans déclarer la lecture réussie.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**Explication des paramètres et du déroulement:**

values[0] alloue une cellule ; l’indice 5 est invalide. result=1. On Error Resume Next ignore la lecture échouée avant affectation, donc result reste 1. GoTo 0 désactive, result+=4 donne 5. Main renvoie 5 sans déclarer la lecture réussie.

### 2. Réparer puis réessayer

```vb
# ReadCell stocke 8 en cellule 0, mais index=2. L’erreur saute à FixIndex. GoTo 0 désactive la gestion ; handled=1, index=0. Resume répète result=values[index], qui stocke 8. Return empêche de tomber dans le gestionnaire. Main reçoit 18.
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**Explication des paramètres et du déroulement:**

ReadCell stocke 8 en cellule 0, mais index=2. L’erreur saute à FixIndex. GoTo 0 désactive la gestion ; handled=1, index=0. Resume répète result=values[index], qui stocke 8. Return empêche de tomber dans le gestionnaire. Main reçoit 18.

### 3. Gestionnaire avant sa déclaration de mode

```vb
# GoTo Work ignore Failed à l’entrée normale. On Error GoTo Failed installe cette étiquette antérieure. L’indice 2 échoue avant de changer result. Le gestionnaire se désactive, incrémente handled et Resume Next rejoint Return. Résultat 10 ; une étiquette n’est pas une procédure.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**Explication des paramètres et du déroulement:**

GoTo Work ignore Failed à l’entrée normale. On Error GoTo Failed installe cette étiquette antérieure. L’indice 2 échoue avant de changer result. Le gestionnaire se désactive, incrémente handled et Resume Next rejoint Return. Résultat 10 ; une étiquette n’est pas une procédure.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
