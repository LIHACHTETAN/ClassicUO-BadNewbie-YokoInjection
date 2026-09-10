# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Public expose un membre du module au code extérieur. Private limite l’accès aux fonctions, procédures et initialiseurs de son propre module. Le modificateur précède la déclaration, pas l’appel.

## Syntaxe exacte

```text
Public declaration
Private declaration
```

## Paramètres

- `visibility` — visibility : Public ou Private. Sans modificateur, SUB/FUNCTION du module sont publics ; VAR/DIM/CONST sont privés.
- `declaration` — declaration : SUB/FUNCTION, VAR/DIM scalaire ou CONST. Public accepte aussi Module et les déclarations au niveau du fichier. Private est interdit au niveau du fichier et dans le corps d’une procédure. Déclarez un nom de membre sans point.

## Retour

Public et Private ne renvoient rien et ne changent ni type de champ ni résultat de fonction. Normalize(12) renvoie Integer 10 par RETURN ; NextCount() renvoie le nouveau compteur, pas TRUE/FALSE.

## Comportement

- Dans Module, noms courts et qualifiés des propres membres sont admis. L’extérieur accède uniquement aux membres Public par ModuleName.Member. Public ne crée pas de nom global court.
- Contrôle avant exécution, même avec Option Explicit Off : accès à un Private étranger = SC019 ; déclaration incorrecte de module/modificateur = SC018 ou erreur de syntaxe. Aucun initialiseur ne s’exécute après ces erreurs.
- Une fonction publique peut appeler un assistant privé : l’accès dépend du module où l’appelante est déclarée. Un assistant privé ne se lance pas séparément par l’IDE, un raccourci ou l’API de procédures de l’hôte.
- Public Const reste immuable et Public Var modifiable. Une variable locale explicite masque un champ homonyme uniquement dans sa procédure. Private ne chiffre pas le code et ne le cache pas à son propriétaire.
- Dans le débogueur, les noms courts et accès Private dépendent du cadre sélectionné. Le champ est accessible dans le module ; le cadre appelant extérieur refuse ModuleName.privateField.

## Exemples

### 1. Interface publique, assistant privé

```vb
# value=12 passe à Limits.Normalize puis Clamp. maximum=10 plafonne le résultat ; les deux fonctions renvoient Integer 10. Main appelle seulement Normalize. Un appel extérieur Limits.Clamp(12) est interdit.
Option Explicit On
Module Limits
    Private Const maximum = 10
    Private Function Clamp(ByVal value)
        If value > maximum Then
            Return maximum
        End If
        Return value
    End Function
    Public Function Normalize(ByVal value)
        Return Clamp(value)
    End Function
End Module
Sub Main()
    Return Limits.Normalize(12)
End Sub
```

**Explication des paramètres et du déroulement:**

value=12 passe à Limits.Normalize puis Clamp. maximum=10 plafonne le résultat ; les deux fonctions renvoient Integer 10. Main appelle seulement Normalize. Un appel extérieur Limits.Clamp(12) est interdit.

### 2. Champ privé et variable locale

```vb
# VAR value=7 sans modificateur est privée dans Store. Read renvoie le champ 7 ; LocalValue crée sa propre value=9 sans modifier le champ. Main renvoie 7*10+9, Integer 79.
Option Explicit On
Module Store
    Var value = 7
    Public Function Read()
        Return value
    End Function
    Public Function LocalValue()
        Var value = 9
        Return value
    End Function
End Module
Sub Main()
    Return Store.Read() * 10 + Store.LocalValue()
End Sub
```

**Explication des paramètres et du déroulement:**

VAR value=7 sans modificateur est privée dans Store. Read renvoie le champ 7 ; LocalValue crée sa propre value=9 sans modifier le champ. Main renvoie 7*10+9, Integer 79.

### 3. Constante publique, compteur privé

```vb
# Public Const increment=2 se lit par Counter.increment. Private count commence à 1. NextCount ajoute increment, stocke puis renvoie 3. Main renvoie 3*10+2, Integer 32. L’accès extérieur à Counter.count et la modification d’increment sont interdits.
Option Explicit On
Module Counter
    Public Const increment = 2
    Private Var count = 1
    Public Function NextCount()
        count += increment
        Return count
    End Function
End Module
Sub Main()
    Var result = Counter.NextCount()
    Return result * 10 + Counter.increment
End Sub
```

**Explication des paramètres et du déroulement:**

Public Const increment=2 se lit par Counter.increment. Private count commence à 1. NextCount ajoute increment, stocke puis renvoie 3. Main renvoie 3*10+2, Integer 32. L’accès extérieur à Counter.count et la modification d’increment sont interdits.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
