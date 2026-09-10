# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Les commandes de jeu utilisent UO.; Basic et vos fonctions utilisent leurs noms déclarés.

## Syntaxe exacte

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## Paramètres

- `UO.command` — UO.command(arguments): préfixe obligatoire du jeu. UO.GetType(id) lit un graphique/corps, pas un type Basic ou CLR.
- `BasicFunction` — BasicFunction(arguments): Int(value), Str(value), CInt(value), sans ajouter UO.
- `arguments` — Les arguments self, backpack, ground et Rhand gardent leur sens d’objet, filtre ou couche; ce ne sont pas des appels abrégés.

## Retour

La règle de nommage ne renvoie rien. Int renvoie Integer, Str String; les trois Api*Exists renvoient Integer 1/0, utilisables comme TRUE/FALSE.

## Comportement

- La casse est ignorée. InjectionApi enregistre Basic sans préfixe, InjectionApiUO le jeu avec UO. Un ancien appel abrégé produit SC005 avec suggestion UO.; aucune exécution implicite. Les valeurs de caractéristiques exigent aussi UO. ApiNameExists, ApiSignatureExists et ApiParameterExists retirent les espaces extérieurs puis vérifient le nom exact sans ajouter de préfixe. Ils lisent les métadonnées, pas le serveur. GetType(TypeName), opérateur de réflexion VB.NET, est absent.

## Exemples

### 1. 1

```vb
# graphic lit le corps du personnage ou 0 si indisponible; whole=2. registered vérifie UO.GetType avec un argument. Main renvoie "2:1" quel que soit le graphique, sans mouvement ni transfert.
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**Explication des paramètres et du déroulement:**

graphic lit le corps du personnage ou 0 si indisponible; whole=2. registered vérifie UO.GetType avec un argument. Main renvoie "2:1" quel que soit le graphique, sans mouvement ni transfert.

### 2. 2

```vb
# La Function GetType complète reçoit value=6 de CInt(6) et renvoie 7. UO.GetType lit toujours le graphique du jeu. Les deux fonctions restent distinctes.
Option Explicit On
Function GetType(value)
    Return value + 1
End Function
Sub Main()
    Var localResult = GetType(CInt(6))
    Var graphic = UO.GetType('self')
    Return localResult
End Sub
```

**Explication des paramètres et du déroulement:**

La Function GetType complète reçoit value=6 de CInt(6) et renvoie 7. UO.GetType lit toujours le graphique du jeu. Les deux fonctions restent distinctes.

### 3. 3

```vb
# oldCall=0, gameCall=1 et basicCall=1 vérifient respectivement GetType, UO.GetType(id) et Int(value). argumentName=1 conserve backpack comme sélecteur. Main renvoie "0:1:1:1". Les procédures utilisateur ne sont pas recherchées.
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**Explication des paramètres et du déroulement:**

oldCall=0, gameCall=1 et basicCall=1 vérifient respectivement GetType, UO.GetType(id) et Int(value). argumentName=1 conserve backpack comme sélecteur. Main renvoie "0:1:1:1". Les procédures utilisateur ne sont pas recherchées.

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
