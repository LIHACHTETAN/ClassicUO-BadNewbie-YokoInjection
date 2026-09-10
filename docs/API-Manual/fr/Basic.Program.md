# SUB Main()

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Un fichier Basic contient des définitions de procédures/fonctions et des déclarations globales facultatives. Placez les actions dans une procédure. Les exemples utilisent Main() comme point d’entrée et constituent des fichiers complets.

## Syntaxe exacte

```text
Option Explicit On
SUB Main()
    statement
END SUB
# comment
; comment
REM comment
// comment
' comment
```

## Paramètres

- `Main / entry` — Procédure choisie au lancement. Main est un nom conventionnel, pas une instruction automatique. SUB Main() déclare une procédure sans argument. Une fonction auxiliaire ne travaille que si elle est appelée.
- `statement` — Une instruction exécutable par ligne dans SUB…END SUB ou FUNCTION…END FUNCTION. Les VAR/CONST globaux et Option Explicit se placent hors de ces corps. Option Explicit précède les déclarations.
- `comment` — # et ; ouvrent un commentaire hors des chaînes, même après du code. REM, // et une apostrophe ouvrent une ligne entière de commentaire après une éventuelle indentation. Dans une chaîne, ces caractères peuvent rester du texte.

## Retour

Charger un fichier ou déclarer SUB ne renvoie pas de valeur. RETURN expression renvoie cette valeur et termine immédiatement l’appel. Atteindre la fin du corps ou utiliser RETURN seul produit Unit, sans valeur.

## Comportement

- Enregistrez en UTF-8 pour conserver commentaires et chaînes localisés. CRLF et LF sont admis. Indentation et lignes vides facilitent la lecture sans remplacer END SUB ou END FUNCTION.
- Mots-clés, noms de procédures et variables ignorent la casse : itemCount, ITEMCOUNT et ItemCount désignent la même liaison. La casse des textes est conservée ; les clés de UO.SetGlobal("Key", …) sont des données, pas des identifiants.
- Commencez un nom simple par une lettre ASCII ou un soulignement, puis utilisez lettres, chiffres et soulignements. Évitez les mots réservés et noms API. UO.Print est un appel qualifié. Les deux-points après un nom définissent une étiquette, pas un séparateur général d’instructions.
- Le moteur normalise le Basic pris en charge, analyse tout le fichier, collecte les déclarations et vérifie les noms. Une fonction auxiliaire peut donc être placée après Main. Le chargement ne lance pas toutes les définitions : le lancement initialise la procédure choisie et suit ses appels.
- Ces exemples calculent uniquement des valeurs. Une fois le modèle vérifié, placez les appels UO nécessaires dans son corps. Ces règles concernent ce moteur, sans promettre toutes les possibilités d’autres Basic.

## Exemples

### 1. Commentaires et texte littéral

```vb
# Main définit note avec "ore #1; keep". Les # et ; de la chaîne sont conservés. Les autres commentaires #, REM, // et apostrophe ne font rien. RETURN renvoie le texte original.
Option Explicit On
# Complete file
SUB Main()
    REM Full-line comment
    VAR note = "ore #1; keep" # Trailing comment
    // Another full-line comment
    ' Another full-line comment
    RETURN note
END SUB
```

**Explication des paramètres et du déroulement:**

Main définit note avec "ore #1; keep". Les # et ; de la chaîne sont conservés. Les autres commentaires #, REM, // et apostrophe ne font rien. RETURN renvoie le texte original.

### 2. Fonction auxiliaire complète

```vb
# Main appelle DoubleCount avec amount=7. Définie plus bas, la fonction multiplie son paramètre Integer par 2 et renvoie 14. Main transmet ce résultat. Aucun fichier Include manquant ni fonction non déclarée n’est nécessaire.
Option Explicit On
SUB Main()
    RETURN DoubleCount(7)
END SUB
FUNCTION DoubleCount(ByVal amount AS Integer)
    VAR result = amount * 2
    RETURN result
END FUNCTION
```

**Explication des paramètres et du déroulement:**

Main appelle DoubleCount avec amount=7. Définie plus bas, la fonction multiplie son paramètre Integer par 2 et renvoie 14. Main transmet ce résultat. Aucun fichier Include manquant ni fonction non déclarée n’est nécessaire.

### 3. Casse des identifiants

```vb
# itemCount commence à 3 ; ITEMCOUNT et itemcount ajoutent 2 à la même variable. Les mots-clés à casse mixte sont acceptés. Main renvoie 5, sans créer d’autres variables.
Option Explicit On
sUb Main()
    Var itemCount = 3
    ITEMCOUNT = itemcount + 2
    ReTuRn ItemCount
EnD sUb
```

**Explication des paramètres et du déroulement:**

itemCount commence à 3 ; ITEMCOUNT et itemcount ajoutent 2 à la même variable. Les mots-clés à casse mixte sont acceptés. Main renvoie 5, sans créer d’autres variables.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: file / subrutine / LineComment / SYMBOL
Runtime/BasicSyntaxPreprocessor.cs: Process
Runtime/InjectionRuntime.cs: Prepare / Load / CallSubrutineValues
Runtime/SemanticScope.cs: Scope
https://learn.microsoft.com/en-us/dotnet/visual-basic/reference/language-specification/introduction (comparison of identifier casing only)
-->
