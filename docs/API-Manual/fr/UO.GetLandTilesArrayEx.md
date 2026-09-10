# UO.GetLandTilesArrayEx

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Recherche les tuiles de terrain par graphic/type dans un rectangle.

## Syntaxe exacte

```text
UO.GetLandTilesArrayEx(Xmin:Any, Ymin:Any, Xmax:Any, Ymax:Any, WorldNum:Any, TileTypes:Any) -> Any
```

## Paramètres

- `Xmin` — Coordonnées mondiales de deux coins inclus, 0..65535. Les coins inversés sont normalisés. Maximum 1 000 000 de cases ; des limites invalides provoquent une erreur de script avant toute lecture.
- `Ymin` — Coordonnées mondiales de deux coins inclus, 0..65535. Les coins inversés sont normalisés. Maximum 1 000 000 de cases ; des limites invalides provoquent une erreur de script avant toute lecture.
- `Xmax` — Coordonnées mondiales de deux coins inclus, 0..65535. Les coins inversés sont normalisés. Maximum 1 000 000 de cases ; des limites invalides provoquent une erreur de script avant toute lecture.
- `Ymax` — Coordonnées mondiales de deux coins inclus, 0..65535. Les coins inversés sont normalisés. Maximum 1 000 000 de cases ; des limites invalides provoquent une erreur de script avant toute lecture.
- `WorldNum` — Numéro de carte/facette 0..255 ; utilisez UO.WorldNum(). Une autre carte renvoie un Array vide. Un changement de carte entre les tranches annule le résultat partiel.
- `TileTypes` — Array de graphic/type numériques. Les types répétés ne dupliquent pas les enregistrements. Un scalaire est aussi accepté comme type unique. Un Array vide sélectionne tous les types ; un tableau contenant seulement 0 sélectionne uniquement 0.

## Retour

Array de lignes [graphic, X, Y, Z], tous les champs Integer. graphic est le type du terrain, Z sa hauteur de base. Aucun résultat : Array vide. Le nombre de lignes est GetArrayLength(result). Les indices commencent à 0. Ce résultat n’est ni Boolean, ni serial, ni Pascal record ; aucun septième paramètre de sortie.

## Comportement

- Lit les données locales sans modifier FindItem/FindCount, déplacer le personnage, activer une cible ou envoyer une commande au serveur.
- X croissant, puis Y croissant pour chaque X. Les lignes d’une case conservent l’ordre du bridge, pas celui de distance ou de hauteur.
- Jusqu’à 32 cases par tranche, avec un budget souple proche de 1 ms. L’annulation est vérifiée entre les tranches. Une case complexe ou une lecture à froid peut dépasser ce budget. Divisez les grandes zones ; le monde peut changer pendant la lecture.

### Fonctions internes : de l’appel au résultat

Étapes C# réelles, pas de nouvelles commandes UO. La procédure auxiliaire figure intégralement dans les exemples.

#### 1. ExecuteStealthCompatibility

Reçoit six arguments ; la forme simple transmet un type, Ex convertit un Array ou un scalaire en types.

Appelle FindPortableTiles en mode land/static et renvoie directement l’Array de lignes.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 2. FindPortableTiles

Vérifie coordonnées, carte et surface en arithmétique 64 bits, normalise les coins et construit un HashSet de types.

Conserve le curseur X/Y et planifie ScanSlice via ExecutePathQuerySlice. Wait(0) vérifie l’annulation entre tranches ; un changement de carte produit un Array vide.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `FindPortableTiles`.

#### 3. ScanSlice

Traite au plus 32 cases sur le fil du jeu, en conservant le curseur après chaque case.

GetLandscapeTile fournit graphic/Z/flags ; GetStaticTiles fournit des triplets graphic/Z/hue. Ajoute les correspondances et rend la main entre tranches.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ScanSlice`.

#### 4. GetChunk2

Reçoit les coordonnées du bloc et le drapeau de chargement ; valide chaque axe avant l’indice linéaire.

Renvoie un Chunk ou null ; un Y hors carte n’utilise jamais la colonne voisine. Réutilise les blocs chargés, lit les autres au besoin.

Source du projet: `src/ClassicUO.Client/Game/Map/Map.cs`; fonction `GetChunk2`.

Lit les données locales sans modifier FindItem/FindCount, déplacer le personnage, activer une cible ou envoyer une commande au serveur.


## Exemples

### Chercher près du personnage

```vb
# Chercher près du personnage
#
# Recherche les tuiles de terrain par graphic/type dans un rectangle.
#
# Array de lignes [graphic, X, Y, Z], tous les champs Integer. graphic est le type du terrain, Z
# sa hauteur de base. Aucun résultat : Array vide. Le nombre de lignes est
# GetArrayLength(result). Les indices commencent à 0. Ce résultat n’est ni Boolean, ni serial,
# ni Pascal record ; aucun septième paramètre de sortie.

SUB Main()
    # x/y désignent self, map la carte actuelle. La zone 3×3 inclut les limites. Ex utilise deux
    # types exemples, la forme simple un seul. Remplacez les graphics selon vos ressources, pas par
    # des ID d’objet.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArrayEx(x, y, x + 2, y + 2, map, types)
    UO.Print("Records: " + CStr(GetArrayLength(rows)))
END SUB
```

**Explication des paramètres et du déroulement:**

- x/y désignent self, map la carte actuelle. La zone 3×3 inclut les limites. Ex utilise deux types exemples, la forme simple un seul. Remplacez les graphics selon vos ressources, pas par des ID d’objet.

### Coins inversés et tous les champs

```vb
# Coins inversés et tous les champs
#
# Recherche les tuiles de terrain par graphic/type dans un rectangle.
#
# Array de lignes [graphic, X, Y, Z], tous les champs Integer. graphic est le type du terrain, Z
# sa hauteur de base. Aucun résultat : Array vide. Le nombre de lignes est
# GetArrayLength(result). Les indices commencent à 0. Ce résultat n’est ni Boolean, ni serial,
# ni Pascal record ; aucun septième paramètre de sortie.

SUB Main()
    # La zone 2×2 utilise des coins décroissants qui sont normalisés. row est une ligne. PrintTile
    # est entièrement définie et affiche seulement des nombres. Pour le terrain, hue=0 est un
    # argument fictif de cette procédure, pas un champ de la ligne.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArrayEx(x + 1, y + 1, x, y, map, types)
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        PrintTile(row[0], row[1], row[2], row[3], 0)
        i = i + 1
    WEND
END SUB

SUB PrintTile(graphic, x, y, z, hue)
    UO.Print("Type=" + CStr(graphic) + " X=" + CStr(x) + " Y=" + CStr(y))
    UO.Print("Z=" + CStr(z) + " hue=" + CStr(hue))
END SUB
```

**Explication des paramètres et du déroulement:**

- La zone 2×2 utilise des coins décroissants qui sont normalisés. row est une ligne. PrintTile est entièrement définie et affiche seulement des nombres. Pour le terrain, hue=0 est un argument fictif de cette procédure, pas un champ de la ligne.

### Répéter avec un nombre limité d’essais

```vb
# Répéter avec un nombre limité d’essais
#
# Recherche les tuiles de terrain par graphic/type dans un rectangle.
#
# Array de lignes [graphic, X, Y, Z], tous les champs Integer. graphic est le type du terrain, Z
# sa hauteur de base. Aucun résultat : Array vide. Le nombre de lignes est
# GetArrayLength(result). Les indices commencent à 0. Ce résultat n’est ni Boolean, ni serial,
# ni Pascal record ; aucun septième paramètre de sortie.

SUB Main()
    # Au plus trois recherches d’une case, avec WAIT(250) entre essais. Chaque appel produit un
    # nouveau résultat. Une longueur nulle signifie aucun résultat actuel, pas une absence
    # permanente sur le serveur.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR attempt = 0
    WHILE attempt < 3
        VAR rows = UO.GetLandTilesArrayEx(x, y, x, y, map, types)
        UO.Print("Records: " + CStr(GetArrayLength(rows)))
        attempt = attempt + 1
        WAIT(250)
    WEND
END SUB
```

**Explication des paramètres et du déroulement:**

- Au plus trois recherches d’une case, avec WAIT(250) entre essais. Chaque appel produit un nouveau résultat. Une longueur nulle signifie aucun résultat actuel, pas une absence permanente sur le serveur.
