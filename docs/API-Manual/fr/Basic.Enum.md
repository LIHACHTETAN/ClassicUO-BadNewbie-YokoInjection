# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Enum regroupe des constantes Integer nommées pour les états du script. Déclarez-le au niveau du fichier ou de Module, hors Sub/Function. Il s’agit d’un sous-ensemble de VB.NET, sans objet .NET Enum.

## Syntaxe exacte

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## Paramètres

- `Public / Private` — Public est la valeur par défaut, même dans Module. Private est limité à Module et cache le type et ses membres aux autres modules et au fichier.
- `name` — Un nom simple sans point, comme Mode, insensible à la casse. UO et les types intégrés sont réservés. Le nom complet ne peut pas répéter un Enum, Module ou une variable globale.
- `As Integer` — Facultatif : seul Integer signé sur 32 bits, -2147483648..2147483647, est accepté. As Mode dans une variable, un paramètre ou un résultat Function utilise le stockage et la conversion Integer ; la valeur n’est pas limitée aux membres déclarés. Sans initialisation, elle vaut 0.
- `member` — Un nom simple par ligne, au moins un membre. Doublons, True et False sont interdits. Sans expression, le premier vaut 0, puis chaque valeur augmente la précédente de 1. Des noms différents peuvent partager une valeur.
- `constantExpression` — Expression constante facultative : entiers décimaux/0x, parenthèses, moins unaire, + - * / Mod, membres précédents et Const numériques déjà déclarées. Le résultat final doit être entier dans la plage ; les divisions intermédiaires peuvent être fractionnaires. Une Const référencée doit également produire Integer, sans type ou As Integer/Long/Short/Byte. Aucun appel, variable, String, comparaison ni accès tableau. Références futures, cycles et dépendances de plus de 128 niveaux sont refusés.
- `name.member` — Lire Mode.Ready, ou Tools.Mode.Ready depuis l’extérieur du module. Dans Tools, Mode.Ready suffit ; With Mode permet .Ready. Affectation, += et écriture de retour ByRef ne peuvent pas modifier ces constantes. Enum n’est pas une fonction appelable.

## Retour

La déclaration ne renvoie rien et ne prend pas de parenthèses d’appel. Un membre renvoie Integer, par exemple Mode.Working = 3 : c’est un état, pas automatiquement un succès. La comparaison state = Mode.Finished renvoie 1/True ou 0/False ; ces deux formes sont utilisables. L’état 0 peut signifier Idle plutôt qu’un échec.

## Comportement

- Pendant la préparation, EnumCatalog calcule les constantes antérieures sans exécuter de script/API, attribue les valeurs automatiques et vérifie noms, accès et limites. SC026 bloque le démarrage même sans Option Explicit. Les erreurs de syntaxe bloquent aussi ; une saisie incomplète produit des diagnostics.
- DefinitionCollector installe les membres constants avant les initialisations globales et les valeurs Optional, qui peuvent donc référencer un Enum situé plus bas. Dans Enum, seules les constantes antérieures restent disponibles. Le script préparé conserve le catalogue, remplacé au chargement d’un autre script.
- ScriptBindings résout une fois les noms de module et Private. L’exécution lit des constantes, sans recalcul en boucle ni réflexion. As Mode devient Integer, parfois affiché ainsi par le débogueur. Include peut fournir la déclaration. Aucun attribut Flags, méthode System.Enum, import implicite ou liste automatique des membres.

## Exemples

### 1. Nommer les états

```vb
# Idle=0 et Queued=1 sont automatiques. Working=10 relance la séquence, Finished=11. state As TaskState reçoit 10. Main renvoie String "0:1:10:11" ; CStr convertit les nombres en texte. Adaptez les noms à votre script ; aucune procédure ne démarre.
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**Explication des paramètres et du déroulement:**

Idle=0 et Queued=1 sont automatiques. Working=10 relance la séquence, Finished=11. state As TaskState reçoit 10. Main renvoie String "0:1:10:11" ; CStr convertit les nombres en texte. Adaptez les noms à votre script ; aucune procédure ne démarre.

### 2. Cacher un état de module

```vb
# Controller.Mode est interne. NextMode reçoit distance ByVal As Integer sans modifier l’argument de l’appelant. distance<=1 choisit Arrived=5, sinon Walking=4 ; state commence à 0. Main passe 3 et 1, reçoit 4 et 5 et renvoie Integer 45. Il n’y a aucun déplacement : distance est une entrée d’exemple. À l’extérieur, Controller.NextMode est accessible, Controller.Mode.Arrived ne l’est pas.
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**Explication des paramètres et du déroulement:**

Controller.Mode est interne. NextMode reçoit distance ByVal As Integer sans modifier l’argument de l’appelant. distance<=1 choisit Arrived=5, sinon Walking=4 ; state commence à 0. Main passe 3 et 1, reçoit 4 et 5 et renvoie Integer 45. Il n’y a aucun déplacement : distance est une entrée d’exemple. À l’extérieur, Controller.NextMode est accessible, Controller.Mode.Arrived ne l’est pas.

### 3. Changer d’état et renvoyer Boolean

```vb
# La Const Integer antérieure FirstState=2 donne Idle=2, Working=3, Finished=4. Advance reçoit state ByRef et modifie la variable de Main ; With Mode abrège les noms et Select Case choisit la transition. Deux appels donnent 2→3→4. IsFinal reçoit une copie ByVal et compare Finished : Main renvoie 1/True, contre 0/False après une seule transition. Un autre Advance lancerait "No next state". Les constantes ne changent jamais.
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**Explication des paramètres et du déroulement:**

La Const Integer antérieure FirstState=2 donne Idle=2, Working=3, Finished=4. Advance reçoit state ByRef et modifie la variable de Main ; With Mode abrège les noms et Select Case choisit la transition. Deux appels donnent 2→3→4. IsFinal reçoit une copie ByVal et compare Finished : Main renvoie 1/True, contre 0/False après une seule transition. Un autre Advance lancerait "No next state". Les constantes ne changent jamais.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
