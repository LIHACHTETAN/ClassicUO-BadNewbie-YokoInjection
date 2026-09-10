# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

For répète un bloc sur une plage numérique inclusive. Utilisez-le pour les indices ou un nombre connu d’opérations ; For Each parcourt les valeurs.

## Syntaxe exacte

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## Paramètres

- `counter / VAR` — Compteur scalaire modifiable. VAR déclare une variable de procédure ; sinon utilisez une variable existante. Avec Option Explicit On, déclarez-la avant ou utilisez For Var. Pour un type explicite, écrivez DIM counter AS Integer avant la boucle ; AS dans cet en-tête For n’est pas pris en charge.
- `start` — Expression numérique initiale, évaluée une fois puis affectée avant limit et increment.
- `limit` — Borne inclusive évaluée une fois à l’entrée. Pas positif : counter <= limit ; pas négatif : counter >= limit.
- `increment` — Pas numérique facultatif, 1 par défaut. Négatif ou fractionnaire possible ; zéro produit une erreur interceptable. Choisissez un type et un pas permettant au compteur de progresser.
- `statements / Next / exit` — Corps et Next sur des lignes distinctes. Le nom facultatif après Next doit correspondre. Continue For passe au pas suivant ; Exit For quitte le For/For Each le plus proche ; Break quitte la boucle la plus proche, quel que soit son type.

## Retour

For, Next et Exit For ne renvoient rien. Le compteur est un nombre, pas automatiquement un ID. À la fin normale, ce moteur conserve la dernière valeur exécutée, pas une valeur hors plage. Une boucle ignorée conserve start ; une sortie anticipée conserve la valeur actuelle. Les exemples renvoient Integer 12, 28, 395.

## Comportement

- À l’entrée : affecter start, mémoriser limit et le pas, refuser zéro, puis tester le premier compteur. Une direction incompatible ignore le corps ; start=limit l’exécute une fois.
- Next teste counter+step et ne l’affecte que si une autre itération tient dans la plage. 1 To 5 Step 3 visite 1 et 4. Modifier les variables ayant fourni la borne ou le pas ne modifie pas leurs valeurs mémorisées ; modifier le compteur agit sur le pas suivant.
- Structure et nom Next sont vérifiés avant exécution ; une incohérence produit SC020. Utilisez des compteurs distincts pour les boucles imbriquées. Une sortie de Try exécute Finally. Pause/arrêt restent actifs ; aucune attente ni échéance automatique.

## Exemples

### 1. Sommer les cellules

```vb
# values[2] crée les indices 0,1,2 contenant 2,4,6. Sum reçoit le tableau ByVal, initialise index=0 et mémorise length-1=2. Le pas implicite 1 visite les trois cellules ; total=12 est renvoyé à Main.
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**Explication des paramètres et du déroulement:**

values[2] crée les indices 0,1,2 contenant 2,4,6. Sum reçoit le tableau ByVal, initialise index=0 et mémorise length-1=2. Le pas implicite 1 visite les trois cellules ; total=12 est renvoyé à Main.

### 2. Supprimer depuis la fin

```vb
# items contient -1,3,-2,5. Le départ est Count()-1=3, la borne 0, le pas -1. Une suppression négative décale uniquement les indices déjà visités, sans sauter de cellule restante. Il reste 3 et 5 ; Count()*10+3+5 renvoie 28.
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**Explication des paramètres et du déroulement:**

items contient -1,3,-2,5. Le départ est Count()-1=3, la borne 0, le pas -1. Une suppression négative décale uniquement les indices déjà visités, sans sauter de cellule restante. Il reste 3 et 5 ; Count()*10+3+5 renvoie 28.

### 3. Bornes mémorisées et compteur final

```vb
# ReadLimit incrémente calls ByRef et renvoie value. Départ=1, borne=5, pas=2 sont évalués une fois chacun : calls=3. upper=99 et stride=1 dans le corps ne les changent pas. Visites 1,3,5 ; total=9, index reste 5. Main renvoie 395.
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**Explication des paramètres et du déroulement:**

ReadLimit incrémente calls ByRef et renvoie value. Départ=1, borne=5, pas=2 sont évalués une fois chacun : calls=3. upper=99 et stride=1 dans le corps ne les changent pas. Visites 1,3,5 ; total=9, index reste 5. Main renvoie 395.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
