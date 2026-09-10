# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

While teste avant chaque passage et répète tant que la condition est vraie. Ce moteur ferme le bloc avec Wend ; End While de VB.NET n’est pas accepté.

## Syntaxe exacte

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## Paramètres

- `condition` — Expression réévaluée à chaque contrôle, y compris le premier et le dernier. Utilisez une comparaison ou un booléen numérique : 0/False arrête, 1/True continue, comme les autres nombres non nuls. Le texte n’est pas converti en Boolean.
- `statements` — Instructions effectuant le travail et faisant évoluer la condition. Une condition fausse dès le départ ignore tout le corps.
- `Wend / exit` — Wend revient au contrôle. Continue While le relance ; Exit While quitte le While le plus proche, même à travers une boucle interne d’un autre type. Break quitte la boucle la plus proche de tout type.

## Retour

While, Wend, Exit While et Break n’ont pas de résultat. RETURN dans le corps termine toute la procédure/fonction. Les exemples renvoient Integer 6,1,406. Le résultat de recherche 1 est un indice, pas un indicateur booléen.

## Comportement

- Exécution : contrôler, exécuter le corps, revenir au contrôle. Aucune borne n’est mémorisée et aucun compteur n’est incrémenté automatiquement.
- Assurez explicitement la progression. Pour interroger régulièrement le jeu, ajoutez un Wait adapté et une échéance : While ne dort pas et n’expire pas seul. Pause et arrêt restent disponibles.
- Les transferts Continue et sortie exécutent les Finally des Try quittés. Placez en-tête, instructions et Wend sur des lignes distinctes dans une procédure ou fonction.

## Exemples

### 1. Somme des chiffres

```vb
# DigitSum reçoit number=123 ByVal. MOD 10 lit le dernier chiffre et Fix(number/10) le retire : 123→12→1→0. total=3+2+1=6. Le dernier contrôle faux termine la boucle ; Main reçoit 6. Avec 0, aucun passage et résultat 0.
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**Explication des paramètres et du déroulement:**

DigitSum reçoit number=123 ByVal. MOD 10 lit le dernier chiffre et Fix(number/10) le retire : 123→12→1→0. total=3+2+1=6. Le dernier contrôle faux termine la boucle ; Main reçoit 6. Avec 0, aucun passage et résultat 0.

### 2. Premier élément correspondant

```vb
# FirstAbove reçoit values=[4,7,9], threshold=6. Le contrôle de longueur protège values[index]. À index=1, 7>6 affecte found=1 puis Exit While arrête. Sans correspondance, found reste -1. Main renvoie l’indice zéro-based 1.
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**Explication des paramètres et du déroulement:**

FirstAbove reçoit values=[4,7,9], threshold=6. Le contrôle de longueur protège values[index]. À index=1, 7>6 affecte found=1 puis Exit While arrête. Sans correspondance, found reste -1. Main renvoie l’indice zéro-based 1.

### 3. Nombre de contrôles

```vb
# CanContinue reçoit checks ByRef, index et limit=3 ByVal, incrémente checks et renvoie index<limit en 1/0. Contrôles aux indices 0,1,2,3 : quatre appels pour trois passages. total=6 ; Main renvoie 400+6=406.
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**Explication des paramètres et du déroulement:**

CanContinue reçoit checks ByRef, index et limit=3 ByVal, incrémente checks et renvoie index<limit en 1/0. Contrôles aux indices 0,1,2,3 : quatre appels pour trois passages. total=6 ; Main renvoie 400+6=406.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
