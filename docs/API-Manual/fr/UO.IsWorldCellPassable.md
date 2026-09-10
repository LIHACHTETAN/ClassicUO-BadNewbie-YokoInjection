# UO.IsWorldCellPassable

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Vérifie un passage vers une cellule voisine et renvoie la praticabilité avec la hauteur.

## Syntaxe exacte

```text
UO.IsWorldCellPassable(CurrX:Any, CurrY:Any, CurrZ:Any, DestX:Any, DestY:Any, DestZ:Any, WorldNum:Any) -> Array
```

## Paramètres

- `CurrX` — Coordonnée mondiale X obligatoire de la cellule source : entier 0..65535 dans la carte chargée, pas une coordonnée de gump.
- `CurrY` — Coordonnée mondiale Y obligatoire de la cellule source : entier 0..65535 dans la carte chargée, pas une coordonnée de gump.
- `CurrZ` — Hauteur initiale obligatoire −128..127, pas un numéro d’étage. Une hauteur invalide est rejetée, pas tronquée.
- `DestX` — Coordonnée mondiale X obligatoire de la cellule cible : entier 0..65535 dans la carte chargée, pas une coordonnée de gump.
- `DestY` — Coordonnée mondiale Y obligatoire de la cellule cible : entier 0..65535 dans la carte chargée, pas une coordonnée de gump.
- `DestZ` — Z de secours en entrée obligatoire, généralement CurrZ. Ce n’est pas var : la variable reste inchangée et ne fixe pas un étage. Lire la hauteur calculée dans result[1]. Ce bridge fournit toujours sa hauteur ; l’argument conserve la forme Pascal.
- `WorldNum` — Numéro de carte obligatoire : UO.WorldNum(). Seule la carte actuelle aux dimensions connues est vérifiée ; aucune autre carte n’est chargée.

## Retour

Array de deux Integer : [0] — praticabilité, 1 = TRUE, 0 = FALSE ; [1] — Z calculée. Seul le premier élément est logique ; ne comparez pas le tableau à TRUE. Une hauteur nulle/négative est valide ; avec [0]=0, elle ne prouve pas l’accessibilité. Arguments rejetés : [0, CurrZ].

## Comportement

- Aucun déplacement, ouverture de porte, ciblage ou paquet réseau. Lit la géométrie locale disponible ; le serveur peut refuser le pas ultérieur. Les lectures sont des instantanés distincts.
- Voisine : écarts X/Y au plus 1. Cible plus éloignée, dépassement de carte, personnage/carte absent ou IsDestroyed sont rejetés avant les collisions. Pour un trajet complet : GetPathArray ou NewMoveXY.
- Des X/Y identiques et valides donnent [1, CurrZ] sans collision : aucun pas requis. Cela ne vérifie pas la possibilité de quitter la cellule. L’état du personnage et les règles Pathfinder influencent un pas voisin ; une géométrie non chargée peut entraîner un refus.

### Fonctions internes : de l’appel au résultat

Voici les véritables étapes internes C#. IsCellOpen est une fonction auxiliaire entièrement définie dans l’exemple, pas une commande intégrée cachée.

#### 1. ExecuteStealthCompatibility

Lit sept arguments Integer. DestZ sert uniquement si un autre bridge ne fournit pas de hauteur. Renvoie un tableau sans modifier d’argument.

Array de deux Integer : [0] — praticabilité, 1 = TRUE, 0 = FALSE ; [1] — Z calculée. Seul le premier élément est logique ; ne comparez pas le tableau à TRUE. Une hauteur nulle/négative est valide ; avec [0]=0, elle ne prouve pas l’accessibilité. Arguments rejetés : [0, CurrZ].

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 2. CheckWorldStep

Invoke vérifie personnage, carte, dimensions, coordonnées, hauteur et voisinage avant soustraction ; choisit la direction. Exige les X/Y cibles exacts après CanWalkForQuery.

Array de deux Integer : [0] — praticabilité, 1 = TRUE, 0 = FALSE ; [1] — Z calculée. Seul le premier élément est logique ; ne comparez pas le tableau à TRUE. Une hauteur nulle/négative est valide ; avec [0]=0, elle ne prouve pas l’accessibilité. Arguments rejetés : [0, CurrZ].

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `CheckWorldStep`.

#### 3. CanWalkForQuery

Retire temporairement le prédicat de cellules interdites d’un autre trajet, le restaure dans finally, appelle CanWalk sans démarrer de trajet.

Aucun déplacement, ouverture de porte, ciblage ou paquet réseau. Lit la géométrie locale disponible ; le serveur peut refuser le pas ultérieur. Les lectures sont des instantanés distincts.

Source du projet: `src/ClassicUO.Client/Game/Pathfinder.cs`; fonction `CanWalkForQuery`.

#### 4. CanWalk

Vérifie le pas principal et les côtés diagonaux. Renvoie bool et modifie les coordonnées ref seulement pour un pas accepté.

Les fonctions de collision lisent la géométrie chargée et l’état du personnage. Un repli diagonal latéral ne signifie pas que la cellule demandée a été atteinte.

Source du projet: `src/ClassicUO.Client/Game/Pathfinder.cs`; fonction `CanWalk`.

#### 5. CalculateNewZ

Reçoit X/Y cibles, Z initiale par ref et direction. Choisit surface et espace libre selon l’état du personnage ; bool indique le passage, z la hauteur.

Les fonctions de collision lisent la géométrie chargée et l’état du personnage. Un repli diagonal latéral ne signifie pas que la cellule demandée a été atteinte.

Source du projet: `src/ClassicUO.Client/Game/Pathfinder.cs`; fonction `CalculateNewZ`.

#### 6. CalculateMinMaxZ

Reçoit nouvelle cellule, Z actuelle, direction et mode. Utilise CreateItemList pour calculer ref minZ/maxZ à partir de la source.

Les fonctions de collision lisent la géométrie chargée et l’état du personnage. Un repli diagonal latéral ne signifie pas que la cellule demandée a été atteinte.

Source du projet: `src/ClassicUO.Client/Game/Pathfinder.cs`; fonction `CalculateMinMaxZ`.

#### 7. CreateItemList

Reçoit liste, X/Y et mode. Collecte objets chargés et règles de collision ; bool indique la géométrie disponible. Map.GetTile utilise load=false sans lire de nouveaux blocs.

Les fonctions de collision lisent la géométrie chargée et l’état du personnage. Un repli diagonal latéral ne signifie pas que la cellule demandée a été atteinte.

Source du projet: `src/ClassicUO.Client/Game/Pathfinder.cs`; fonction `CreateItemList`.

Aucun déplacement, ouverture de porte, ciblage ou paquet réseau. Lit la géométrie locale disponible ; le serveur peut refuser le pas ultérieur. Les lectures sont des instantanés distincts.


## Exemples

### Vérifier la cellule à l’est

```vb
# Vérifier la cellule à l’est
#
# Vérifie un passage vers une cellule voisine et renvoie la praticabilité avec la hauteur.
#
# Array de deux Integer : [0] — praticabilité, 1 = TRUE, 0 = FALSE ; [1] — Z calculée. Seul le
# premier élément est logique ; ne comparez pas le tableau à TRUE. Une hauteur nulle/négative
# est valide ; avec [0]=0, elle ne prouve pas l’accessibilité. Arguments rejetés : [0, CurrZ].

SUB Main()
    # x/y/z sont la source, x+1/y la voisine ; sixième argument z de secours, dernier argument carte
    # actuelle. Vérifier result[0] avant result[1].

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR result = UO.IsWorldCellPassable(x,y,z,x+1,y,z,UO.WorldNum())
    IF result[0] = TRUE THEN
        UO.Print('Passable, Z=' + CStr(result[1]))
    ELSE
        UO.Print('Blocked')
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- x/y/z sont la source, x+1/y la voisine ; sixième argument z de secours, dernier argument carte actuelle. Vérifier result[0] avant result[1].

### Lire Z sans modifier l’argument

```vb
# Lire Z sans modifier l’argument
#
# Vérifie un passage vers une cellule voisine et renvoie la praticabilité avec la hauteur.
#
# Array de deux Integer : [0] — praticabilité, 1 = TRUE, 0 = FALSE ; [1] — Z calculée. Seul le
# premier élément est logique ; ne comparez pas le tableau à TRUE. Une hauteur nulle/négative
# est valide ; avec [0]=0, elle ne prouve pas l’accessibilité. Arguments rejetés : [0, CurrZ].

SUB Main()
    # proposedZ reste 0. targetZ vient de result[1], pas de l’argument. Aucun calcul de hauteur
    # n’est supposé en cas de refus.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR proposedZ = 0
    VAR result = UO.IsWorldCellPassable(x,y,z,x,y+1,proposedZ,UO.WorldNum())
    IF result[0] = 1 THEN
        VAR targetZ = result[1]
        UO.Print('Input=' + CStr(proposedZ) + '; result=' + CStr(targetZ))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- proposedZ reste 0. targetZ vient de result[1], pas de l’argument. Aucun calcul de hauteur n’est supposé en cas de refus.

### Fonction IsCellOpen complète

```vb
# Fonction IsCellOpen complète
#
# Vérifie un passage vers une cellule voisine et renvoie la praticabilité avec la hauteur.
#
# Array de deux Integer : [0] — praticabilité, 1 = TRUE, 0 = FALSE ; [1] — Z calculée. Seul le
# premier élément est logique ; ne comparez pas le tableau à TRUE. Une hauteur nulle/négative
# est valide ; avec [0]=0, elle ne prouve pas l’accessibilité. Arguments rejetés : [0, CurrZ].

SUB Main()
    # La fonction complète après Main prend X/Y/Z source, X/Y cible et carte. Elle fournit le
    # sixième argument et renvoie seulement Integer 1/0, pas un tableau. IsCellOpen peut être
    # comparée à TRUE. Aucun déplacement.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR openCell = IsCellOpen(x,y,UO.GetZ(),x+1,y+1,UO.WorldNum())
    IF openCell = TRUE THEN
        UO.Print('Diagonal cell is locally passable')
    END IF
END SUB

SUB IsCellOpen(x,y,z,toX,toY,map)
    VAR cellResult = UO.IsWorldCellPassable(x,y,z,toX,toY,z,map)
    IF GetArrayLength(cellResult) <> 2 THEN
        RETURN 0
    END IF
    RETURN cellResult[0]
END SUB
```

**Explication des paramètres et du déroulement:**

- La fonction complète après Main prend X/Y/Z source, X/Y cible et carte. Elle fournit le sixième argument et renvoie seulement Integer 1/0, pas un tableau. IsCellOpen peut être comparée à TRUE. Aucun déplacement.
