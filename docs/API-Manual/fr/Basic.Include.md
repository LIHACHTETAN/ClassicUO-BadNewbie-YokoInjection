# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Include charge un autre fichier source avant analyse et exécution. Ses fonctions et variables deviennent disponibles sans lancer automatiquement une procédure ou un thread.

## Syntaxe exacte

```text
Include "fileName"
```

## Paramètres

- `fileName` — fileName : nom non vide entre apostrophes ou guillemets. Chemin relatif ou absolu littéral, pas une variable ni une expression. Toute extension est admise ; le contenu doit être du code accepté par ce moteur.

## Retour

Aucune valeur : directive de préparation des sources. Ne pas affecter Include(...) ni attendre ID, TRUE/FALSE ou 1/0. Les fonctions incluses renvoient leurs propres valeurs avec RETURN.

## Comportement

- Écrire Include seul sur une ligne hors SUB/FUNCTION. Recherche à côté du fichier appelant puis dans son sous-dossier Include. Les chemins imbriqués partent de la bibliothèque courante. Enregistrer le fichier principal avant un chemin relatif.
- Chaque chemin complet est inclus une fois. Un cycle A → B → A produit SC016. Erreurs de chemin, accès et syntaxe empêchent le démarrage avant les initialisations globales. Diagnostics et débogueur conservent fichier et ligne d’origine.
- Fermer les chaînes et SUB/FUNCTION dans leur fichier d’origine. Redéclarer une variable globale ou constante produit SC017 avant exécution.
- Le lancement suivant relit les bibliothèques modifiées ; un script préparé ou actif conserve son instantané. Aucun réglage de profil copié ni autre script lancé.
- Chaque fichier peut placer Option Explicit avant ses déclarations ; sinon il hérite du fichier principal. Les déclarations partagent un espace de noms, sans création automatique de module.
- Lecture UTF-8 avec reconnaissance du BOM. Limites : 128 fichiers avec le principal, 32 niveaux, 16 777 216 caractères source. Include dans les commentaires ou chaînes ne charge rien.
- Chaque exemple est un dossier distinct : enregistrer Main.bas et tous les fichiers affichés avec leurs noms et sous-dossiers exacts. Ensembles prêts dans API Manual/Examples/Basic.Include/1, /2, /3. Lancer Main.bas sans concaténer les fichiers.

## Exemples

### 1. Fonction partagée

```vb
# Main.bas inclut Common.bas et appelle Add(4, 7). left et right sont passés par valeur ; Add renvoie leur somme et Main renvoie Integer 11. Common.bas ne démarre pas seul.
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**Explication des paramètres et du déroulement:**

Main.bas inclut Common.bas et appelle Add(4, 7). left et right sont passés par valeur ; Add renvoie leur somme et Main renvoie Integer 11. Common.bas ne démarre pas seul.

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. Bibliothèque imbriquée

```vb
# Main.bas inclut lib/Route.bas, qui inclut Math.bas depuis son dossier lib. Distance(-3, 5) passe dx=-3 et dy=5 à Manhattan ; Abs retire les signes, somme Integer 8. Ce calcul ne déplace pas le personnage.
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**Explication des paramètres et du déroulement:**

Main.bas inclut lib/Route.bas, qui inclut Math.bas depuis son dossier lib. Distance(-3, 5) passe dx=-3 et dy=5 à Manhattan ; Abs retire les signes, somme Integer 8. Ce calcul ne déplace pas le personnage.

**lib/Route.bas**

```vbnet
Option Explicit On
Include "Math.bas"
FUNCTION Distance(ByVal dx, ByVal dy)
    RETURN Manhattan(dx, dy)
END FUNCTION
```

**lib/Math.bas**

```vbnet
Option Explicit On
FUNCTION Manhattan(ByVal dx, ByVal dy)
    RETURN Abs(dx) + Abs(dy)
END FUNCTION
```

### 3. Inclusion répétée

```vb
# Common.bas et ./Common.bas désignent le même fichier : CONST et fonction déclarées une fois. SharedValue=7 ; GetShared() renvoie 7, Main multiplie par 2 et renvoie Integer 14. Les deux fichiers utilisent Option Explicit On.
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**Explication des paramètres et du déroulement:**

Common.bas et ./Common.bas désignent le même fichier : CONST et fonction déclarées une fois. SharedValue=7 ; GetShared() renvoie 7, Main multiplie par 2 et renvoie Integer 14. Les deux fichiers utilisent Option Explicit On.

**Common.bas**

```vbnet
Option Explicit On
CONST SharedValue = 7
FUNCTION GetShared()
    RETURN SharedValue
END FUNCTION
```

<!-- implementation references (not callable script procedures):
Parsing/ScriptSourceGraph.cs: Load / Builder.AddInclude / ResolveLine
Runtime/InjectionRuntime.cs: Prepare / Load
Runtime/Interpreter.cs: Location / EvaluateInitializer / CallObserved
Analysis/SanityAnalyzer.cs: Analyze
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: PrepareScriptForExecution
InjectionScript.Lsp/Workspace.cs: UpdateDiagnostic
-->
