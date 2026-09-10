# List

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

List() crée une collection ordonnée de taille variable. Conservez l’objet dans une variable : items.Add est une méthode d’objet, pas une commande globale List.Add.

## Syntaxe exacte

```text
List() -> Object:List
List(source:Array/List) -> Object:List
items.Add(value:Any) -> Unit
items.Insert(index:Number, value:Any) -> Unit
items.Item(index:Number) -> Any
items[index] = value
items.Set(index:Number, value:Any) -> Unit
items.Count() -> Integer
items.Contains(value:Any) -> Integer:1/0
items.IndexOf(value:Any) -> Integer:index/-1
items.Remove(value:Any) -> Integer:1/0
items.RemoveAt(index:Number) -> Unit
items.Clear() -> Unit
items.ToArray() -> Array
```

## Paramètres

- `source` — source : absent, la collection est vide. List accepte un tableau ou List ; Dictionary accepte Dictionary. Le conteneur est copié, mais les références imbriquées restent partagées.
- `index / key` — index / key : positions List numériques entières à partir de 0 ; Insert accepte aussi Count(). Les clés Dictionary sont du texte ou des nombres finis. Les nombres 1 et 1.0 partagent une clé, pas le texte "1".
- `value` — value : valeur Basic initialisée, y compris tableau ou collection. Unit ne peut être stocké. Égalité numérique, texte sensible à la casse, identité de référence pour tableaux/objets.
- `fallback` — fallback : Get renvoie ce secours si la clé est absente, sans insertion. Tous les arguments, y compris l’expression fallback, sont évalués avant l’appel.

## Retour

La création renvoie Object:List. Item/index lit une valeur ; Count compte les éléments ; IndexOf renvoie une position depuis 0 ou -1. Contains/Remove renvoient 1=TRUE ou 0=FALSE. Add/Insert/Set/RemoveAt/Clear renvoient Unit ; ToArray, un nouvel Array.

## Comportement

- Add ajoute à la fin ; Insert insère avant la position ; Set/index remplace un élément existant ; Item/index le lit. Remove supprime la première valeur égale, RemoveAt une position, Clear tout le contenu.
- Contains vérifie la présence, IndexOf trouve la première occurrence. Un index négatif, fractionnaire, textuel ou hors limites produit une erreur interceptable sans mutation.
- For Each conserve l’ordre. ToArray crée un instantané superficiel : parcourez-le si vous modifiez la liste originale.
- Une mutation pendant le For Each direct, y compris Set, déclenche une erreur interceptable au pas suivant. Try/Finally se déroule normalement. Une mutation refusée conserve les données.
- Alias et arguments ByVal partagent la collection. Copies et instantanés ne dupliquent que le conteneur extérieur. ByRef indexé et affectation composée évaluent conteneur/clé une seule fois ; remplacer la variable ne redirige pas la réécriture.
- Ces données sont locales au script : les méthodes ne déplacent aucun objet de jeu et n’utilisent pas le réseau. Une pile enregistrée comme élément occupe une position.

## Exemples

### 1. Construire et additionner

```vb
# Add produit [3,7], Insert(1,5) produit [3,5,7], Set(0,2) produit [2,5,7]. For Each additionne les trois valeurs. Main renvoie Integer 14.
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(3)
    items.Add(7)
    items.Insert(1, 5)
    items.Set(0, 2)
    Var total = 0
    For Each item In items
        total += item
    Next
    Return total
End Sub
```

**Explication des paramètres et du déroulement:**

Add produit [3,7], Insert(1,5) produit [3,5,7], Set(0,2) produit [2,5,7]. For Each additionne les trois valeurs. Main renvoie Integer 14.

### 2. Copies et instantané

```vb
# seed=[4,6]. copied et snapshot gardent ces valeurs. L’original devient [9,6] ; Remove(6) renvoie TRUE=1, RemoveAt(0) le vide, Clear le laisse vide. Main renvoie 4*100+6*10+1+0, Integer 461.
Option Explicit On
Sub Main()
    Dim seed[1]
    seed[0] = 4
    seed[1] = 6
    Var items = List(seed)
    Var copied = List(items)
    Var snapshot = items.ToArray()
    items[0] = 9
    Var removed = items.Remove(6)
    items.RemoveAt(0)
    items.Clear()
    Return snapshot[0]*100 + copied[1]*10 + removed + items.Count()
End Sub
```

**Explication des paramètres et du déroulement:**

seed=[4,6]. copied et snapshot gardent ces valeurs. L’original devient [9,6] ; Remove(6) renvoie TRUE=1, RemoveAt(0) le vide, Clear le laisse vide. Main renvoie 4*100+6*10+1+0, Integer 461.

### 3. Recherche et ByRef

```vb
# NextIndex s’exécute une fois : calls=1, index 0. Bump passe 5 à 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) renvoie 6. Main renvoie Integer 601.
Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    Var items = List()
    items.Add(5)
    Var calls = 0
    Bump(items[NextIndex(calls)])
    If items.Contains(6) AndAlso items.IndexOf(6) = 0 Then
        Return items.Item(0)*100 + calls
    End If
    Return -1
End Sub
```

**Explication des paramètres et du déroulement:**

NextIndex s’exécute une fois : calls=1, index 0. Bump passe 5 à 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) renvoie 6. Main renvoie Integer 601.

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/ListObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-8.0
-->
