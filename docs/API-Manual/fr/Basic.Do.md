# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Do accepte un contrôle avant ou après le corps. While poursuit si vrai ; Until poursuit jusqu’à vrai. Repeat … Until est la forme historique à contrôle final.

## Syntaxe exacte

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## Paramètres

- `condition / While / Until` — Expression booléenne numérique 0/False ou 1/True. While continue si vrai, Until sort si vrai. Réévaluation à chaque contrôle ; le texte n’est pas interprété comme Boolean.
- `position / Repeat` — Après Do, la condition peut éviter le premier passage. Après Loop ou Until de Repeat, au moins un passage a lieu. Un seul emplacement de condition est autorisé. Do … Loop sans condition exige une sortie explicite.
- `statements / exit` — Corps. Continue Do atteint le prochain contrôle ; Exit Do quitte le Do ou Repeat le plus proche. Break quitte la boucle la plus proche de tout type. RETURN termine toute la procédure/fonction.

## Retour

Do, Loop, Repeat, Until et Exit Do ne renvoient rien. Main renvoie explicitement Integer 1,33,83 dans les exemples : des compteurs combinés, pas des résultats booléens de commande.

## Comportement

- La préparation associe les blocs et vérifie les transferts. Deux conditions, au début et à la fin du même Do, produisent SC020. Le moteur évalue à la position choisie et répète selon While/Until.
- Continue Do vérifie aussi la condition finale d’une boucle à contrôle final ; sinon il revient à l’en-tête. Les Finally quittés s’exécutent exactement une fois avant le transfert.
- Repeat exécute d’abord : vérifiez les tableaux vides avant d’entrer. Aucune expiration implicite. Pour attendre le jeu, ajoutez Wait et échéance ; pause/arrêt restent actifs.

## Exemples

### 1. Avant ou après

```vb
# ready=True satisfait déjà Until. Do Until ready ne passe pas : before=0. Le second contrôle suit l’incrément, donc after=1. Main renvoie before*10+after=1.
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**Explication des paramètres et du déroulement:**

ready=True satisfait déjà Until. Do Until ready ne passe pas : before=0. Le second contrôle suit l’incrément, donc after=1. Main renvoie before*10+after=1.

### 2. Tentatives limitées et nettoyage

```vb
# attempts part de 0 et augmente à chaque passage. Les deux premiers Continue Do exécutent Finally puis contrôlent attempts<4. À la troisième tentative Exit Do exécute aussi Finally. attempts=3, cleanup=3 : résultat 33. Il s’agit d’une simulation locale, pas de tentatives réseau réelles.
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**Explication des paramètres et du déroulement:**

attempts part de 0 et augmente à chaque passage. Les deux premiers Continue Do exécutent Finally puis contrôlent attempts<4. À la troisième tentative Exit Do exécute aussi Finally. attempts=3, cleanup=3 : résultat 33. Il s’agit d’une simulation locale, pas de tentatives réseau réelles.

### 3. Boucle historique avec sentinelle

```vb
# values=[3,5,0] est non vide. Repeat lit la cellule, avance index et cumule total. Until arrête au zéro ou à la longueur ; OrElse évite le second contrôle si zéro est trouvé. total=8, index=3 donnent 83.
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**Explication des paramètres et du déroulement:**

values=[3,5,0] est non vide. Repeat lit la cellule, avance index et cumule total. Until arrête au zéro ou à la longueur ; OrElse évite le second contrôle si zéro est trouvé. total=8, index=3 donnent 83.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
