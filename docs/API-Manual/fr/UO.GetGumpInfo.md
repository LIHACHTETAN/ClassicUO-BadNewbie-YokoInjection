# UO.GetGumpInfo

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit un instantané cohérent d’un gump serveur et de ses éléments.

## Syntaxe exacte

```text
UO.GetGumpInfo(GumpIndex:Any) -> Array
```

## Paramètres

- `GumpIndex` — Integer obligatoire : index à partir de 0 jusqu’à GetGumpsCount()-1, et non serial ou GumpID. Un index négatif ou hors liste est invalide. Ouvrir, fermer ou réordonner les fenêtres peut modifier l’index.

## Retour

Array de cinq champs : [0] Integer serial ; [1] Integer GumpID ; [2] Array<String> des textes non vides ; [3] Array<String> des descriptions de boutons ordinaires ; [4] Array<String> de tous les éléments actifs, y compris imbriqués. Un gump invalide, fermé ou ignoré renvoie []. Les ID avec bit de poids fort sont des Integer négatifs ; Hex affiche leurs bits.

## Comportement

- L’ensemble est copié en une requête sur le thread du jeu. Les modifications et fermetures ultérieures ne changent pas les tableaux enregistrés. Seuls les gumps serveur actifs figurent dans la liste ; les fenêtres locales de sac, carte et réglages sont exclues.
- Ce tableau BASIC n’est ni l’enregistrement Pascal TGumpInfo ni le paquet de mise en page original. Les descriptions donnent type, page, ID, X/Y et dimensions ; les boutons ajoutent ButtonID, action, toPage et graphismes ; les sélecteurs ajoutent checked et inactive/active. Le texte peut contenir espaces et =. Les boutons radio sont dans [4], pas [3].
- AddGumpIgnoreByID/BySerial masquent ce résultat pour le script actuel ; ClearGumpsIgnore retire le filtre. GetGumpsCount reste inchangé. Un gump existant peut avoir des tableaux de texte vides. Utiliser GetArrayLength, et non Len, pour leur longueur.

## Exemples

### Lire les deux ID

```vb
# Lire les deux ID
#
# Lit un instantané cohérent d’un gump serveur et de ses éléments.
#
# Array de cinq champs : [0] Integer serial ; [1] Integer GumpID ; [2] Array<String> des textes
# non vides ; [3] Array<String> des descriptions de boutons ordinaires ; [4] Array<String> de
# tous les éléments actifs, y compris imbriqués. Un gump invalide, fermé ou ignoré renvoie [].
# Les ID avec bit de poids fort sont des Integer négatifs ; Hex affiche leurs bits.

SUB Main()
    # 0 sélectionne le premier gump serveur. Vérifier GetArrayLength(info)=5 avant tout accès.
    # info[0] est le serial, info[1] le GumpID du même instantané.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        UO.Print('Serial=' + Hex(info[0]))
        UO.Print('GumpID=' + Hex(info[1]))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- 0 sélectionne le premier gump serveur. Vérifier GetArrayLength(info)=5 avant tout accès. info[0] est le serial, info[1] le GumpID du même instantané.

### Lister les véritables ButtonID

```vb
# Lister les véritables ButtonID
#
# Lit un instantané cohérent d’un gump serveur et de ses éléments.
#
# Array de cinq champs : [0] Integer serial ; [1] Integer GumpID ; [2] Array<String> des textes
# non vides ; [3] Array<String> des descriptions de boutons ordinaires ; [4] Array<String> de
# tous les éléments actifs, y compris imbriqués. Un gump invalide, fermé ou ignoré renvoie [].
# Les ID avec bit de poids fort sont des Integer négatifs ; Hex affiche leurs bits.

SUB Main()
    # info[3] contient les descriptions des boutons. i est un index de ligne ; le champ ButtonID de
    # la description donne l’ID de réponse. Les boutons radio figurent dans la liste complète.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR buttons = info[3]
        VAR i = 0
        WHILE i < GetArrayLength(buttons)
            UO.Print(buttons[i])
            i = i + 1
        WEND
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- info[3] contient les descriptions des boutons. i est un index de ligne ; le champ ButtonID de la description donne l’ID de réponse. Les boutons radio figurent dans la liste complète.

### Conserver le texte avant fermeture

```vb
# Conserver le texte avant fermeture
#
# Lit un instantané cohérent d’un gump serveur et de ses éléments.
#
# Array de cinq champs : [0] Integer serial ; [1] Integer GumpID ; [2] Array<String> des textes
# non vides ; [3] Array<String> des descriptions de boutons ordinaires ; [4] Array<String> de
# tous les éléments actifs, y compris imbriqués. Un gump invalide, fermé ou ignoré renvoie [].
# Les ID avec bit de poids fort sont des Integer négatifs ; Hex affiche leurs bits.

SUB Main()
    # info[2] est une copie du texte. CloseSimpleGump(0) ferme localement si NoClose est absent,
    # sans valeur de retour. Les textes mémorisés restent disponibles ; vérifier leur longueur avant
    # texts[0].

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR texts = info[2]
        UO.CloseSimpleGump(0)
        IF GetArrayLength(texts) > 0 THEN
            UO.Print(texts[0])
        END IF
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- info[2] est une copie du texte. CloseSimpleGump(0) ferme localement si NoClose est absent, sans valeur de retour. Les textes mémorisés restent disponibles ; vérifier leur longueur avant texts[0].
