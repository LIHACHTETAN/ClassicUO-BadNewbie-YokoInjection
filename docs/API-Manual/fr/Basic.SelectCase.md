# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Select Case choisit une branche en comparant une valeur mémorisée aux alternatives dans l’ordre. Il convient aux catégories d’objets, aux modes de script et aux intervalles. Cette instruction Basic s’écrit sans UO.; les appels de jeu dans ses expressions gardent UO.

## Syntaxe exacte

```text
Select Case expression
    Case value1, value2
        statements
        Exit Select
    Case from To to
        statements
    Case Is >= value
        statements
    Case Else
        statements
End Select
```

## Paramètres

- `expression` — Expression obligatoire: variable, valeur littérale ou appel de fonction. Elle est évaluée exactement une fois à chaque entrée, même pour un bloc vide ou limité à Case Else.
- `value / from / to` — Case accepte une valeur ou des alternatives séparées par des virgules, chacune pouvant être une expression. from To to inclut les deux bornes. Un intervalle inversé ne correspond pas. La borne supérieure n’est évaluée que si la comparaison inférieure réussit. Les virgules des arguments d’un appel ne séparent pas les alternatives.
- `Is comparison value` — Opérateurs =, <>, <, <=, > ou >=. Is est facultatif: Case Is >= 5 équivaut à Case >= 5. Ce sont les comparaisons de valeurs du moteur, pas des tests de type.
- `Case Else` — Branche de secours facultative, uniquement si aucun Case précédent ne correspond. Elle est unique et placée en dernier. Sans elle, un échec poursuit après End Select.
- `Exit Select` — Quitte le Select Case englobant le plus proche, après son End Select. Ne termine ni la boucle extérieure ni la procédure. Hors Select Case, produit une erreur de chargement.

## Retour

Select Case, Case, End Select et Exit Select ne renvoient aucune valeur et ne se comparent pas à TRUE ou 1. Les fonctions des exemples renvoient explicitement un String ou Integer avec Return. TRUE vaut numériquement 1 et FALSE vaut 0: Case True correspond à 1, pas à tout nombre non nul.

## Comportement

- La préparation crée SelectInstruction, les gardes CaseInstruction et les sauts résolus. La valeur reste privée à l’appel courant, sans variable locale artificielle. Récursion et blocs imbriqués ont des captures indépendantes; chaque nouvelle entrée remplace la capture précédente.
- CaseMatches vérifie de gauche à droite jusqu’au premier accord. Le corps choisi s’exécute une fois et un saut ignore les suivants. Les modifications faites dans un Case ne relisent pas la sélection; les effets déjà produits ne sont pas annulés.
- Nombres et chaînes suivent les comparaisons ordinaires du moteur; les chaînes distinguent la casse. Option Compare Text et les conversions automatiques VB.NET ne sont pas implémentés. Convertissez explicitement pour comparer nombre et texte.
- End Select est obligatoire. Pas de code exécutable avant le premier Case ni de For/Next partagé entre branches. Une structure incorrecte bloque le chargement. Entrez par Select Case, pas par GoTo au milieu.
- Les erreurs rejoignent le gestionnaire courant. On Error Resume Next ignore toute sélection dont l’expression échoue; un Case défaillant passe au suivant. Resume réessaie l’instruction. Exit Select exécute les Finally actifs qu’il quitte. Pause et arrêt restent contrôlés entre instructions; aucune attente ou limite de temps n’est ajoutée.

## Exemples

### 1. Classer une quantité

```vb
# DescribeAmount reçoit amount ByVal. Case 0 renvoie empty; 1 To 4 inclut 1 et 4; Is >= 5 renvoie large. Les négatifs atteignent Case Else. Main appelle avec -1, 0, 4, 5 et assemble negative:empty:small:large. Ce sont des résultats définis par le script.
Option Explicit On
Function DescribeAmount(ByVal amount)
    Select Case amount
        Case 0
            Return "empty"
        Case 1 To 4
            Return "small"
        Case Is >= 5
            Return "large"
        Case Else
            Return "negative"
    End Select
End Function

Sub Main()
    Return DescribeAmount(-1) & ":" & DescribeAmount(0) & ":" & DescribeAmount(4) & ":" & DescribeAmount(5)
End Sub
```

**Explication des paramètres et du déroulement:**

DescribeAmount reçoit amount ByVal. Case 0 renvoie empty; 1 To 4 inclut 1 et 4; Is >= 5 renvoie large. Les négatifs atteignent Case Else. Main appelle avec -1, 0, 4, 5 et assemble negative:empty:small:large. Ce sont des résultats définis par le script.

### 2. Observer les appels

```vb
# ReadMode incrémente reads ByRef et renvoie 2 une fois. Candidate incrémente checks et renvoie value. La valeur 1 échoue, 2 correspond et le candidat 3 est ignoré. selected vaut 7; Main renvoie 1*100+2*10+7=127 sans accès au jeu.
Option Explicit On
Function ReadMode(ByRef reads)
    reads += 1
    Return 2
End Function

Function Candidate(ByRef checks, ByVal value)
    checks += 1
    Return value
End Function

Sub Main()
    Dim reads = 0
    Dim checks = 0
    Dim selected = 0
    Select Case ReadMode(reads)
        Case Candidate(checks, 1)
            selected = -1
        Case Candidate(checks, 2), Candidate(checks, 3)
            selected = 7
        Case Else
            selected = -9
    End Select
    Return reads * 100 + checks * 10 + selected
End Sub
```

**Explication des paramètres et du déroulement:**

ReadMode incrémente reads ByRef et renvoie 2 une fois. Candidate incrémente checks et renvoie value. La valeur 1 échoue, 2 correspond et le candidat 3 est ignoré. selected vaut 7; Main renvoie 1*100+2*10+7=127 sans accès au jeu.

### 3. Quitter un bloc imbriqué

```vb
# route contient harvest et choisit la première alternative; trace devient 1. Le Case 2 interne exécute Exit Select, ignore trace=99, puis Finally ajoute 2. La branche extérieure ajoute 3: résultat 123. Son Case Else est ignoré. Une autre chaîne dans route donne -1.
Option Explicit On
Sub Main()
    Dim route = "harvest"
    Dim trace = 0
    Select Case route
        Case "harvest", "loot"
            trace = 1
            Select Case 2
                Case 2
                    Try
                        Exit Select
                        trace = 99
                    Finally
                        trace = trace * 10 + 2
                    End Try
            End Select
            trace = trace * 10 + 3
        Case Else
            trace = -1
    End Select
    Return trace
End Sub
```

**Explication des paramètres et du déroulement:**

route contient harvest et choisit la première alternative; trace devient 1. Le Case 2 interne exécute Exit Select, ignore trace=99, puis Finally ajoute 2. La branche extérieure ajoute 3: résultat 123. Son Case Else est ignoré. Une autre chaîne dans route donne -1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
