# UO.PredictedY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit la valeur prévue de la coordonnée Y après les pas déjà en file du joueur.

## Syntaxe exacte

```text
UO.PredictedY() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer Y en cases de carte. 0 peut être une coordonnée réelle ou un joueur absent.

## Comportement

- Uniquement la fonction UO sans argument de la syntaxe. Aucun target, serial, type, destination, distance ou timeout. Le nombre n’est ni Boolean, ID ni enregistrement tile : 1 ne signifie pas arrivée.
- GetEndPosition lit X/Y/Z/direction du dernier Mobile.Step déjà en file. Si la file est vide, lit la position/direction actuelle. Lecture O(1) sans retirer de pas, déplacer, envoyer de paquet, calculer un trajet ou attendre l’arrivée.
- X/Y sont des coordonnées du monde/carte, pas des pixels du gump de conteneur. Z est une hauteur, pas un étage. Renvoie un composant, ni tableau ni destination finale du chemin.
- Prédiction locale, pas arrivée confirmée. Ajout/fin/refus de pas, vidage de file ou téléportation peuvent la changer. Les lectures séparées ne sont pas atomiques ; X égal ne prouve ni Y/Z ni accord serveur.
- Invoke lit dans le thread du jeu ; un thread de travail attend le traitement par le gestionnaire. L’annulation du script interrompt cette attente. Aucun délai ni appel réseau supplémentaire.
- Les IApiBridge externes sans IPredictedMovementBridge gardent la position/direction actuelle en repli. Classic UO implémente l’interface tenant compte de la file.

### Fonctions internes : de l’appel au résultat

Étapes natives réelles. PredictionEquals est une fonction BASIC utilisateur intégralement définie, pas une commande interne ni une procédure de déplacement.

#### 1. ExecuteStealthCompatibility

La fonction native appelle ReadPredictedCoordinate qui sélectionne la propriété IPredictedMovementBridge. Aucun appel de NewMoveXY ou lancement de recherche de chemin.

Uniquement la fonction UO sans argument de la syntaxe. Aucun target, serial, type, destination, distance ou timeout. Le nombre n’est ni Boolean, ID ni enregistrement tile : 1 ne signifie pas arrivée.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 2. ReadPredictedCoordinate

La fonction native appelle ReadPredictedCoordinate qui sélectionne la propriété IPredictedMovementBridge. Aucun appel de NewMoveXY ou lancement de recherche de chemin.

Les IApiBridge externes sans IPredictedMovementBridge gardent la position/direction actuelle en repli. Classic UO implémente l’interface tenant compte de la file.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ReadPredictedCoordinate`.

#### 3. Invoke

Invoke lit dans le thread du jeu ; un thread de travail attend le traitement par le gestionnaire. L’annulation du script interrompt cette attente. Aucun délai ni appel réseau supplémentaire.

Integer Y en cases de carte. 0 peut être une coordonnée réelle ou un joueur absent.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 4. ReadPredictedPosition

ReadPredictedPosition renvoie 0 si Player manque/est détruit ; sinon appelle GetEndPosition et sélectionne un composant.

GetEndPosition lit X/Y/Z/direction du dernier Mobile.Step déjà en file. Si la file est vide, lit la position/direction actuelle. Lecture O(1) sans retirer de pas, déplacer, envoyer de paquet, calculer un trajet ou attendre l’arrivée.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `ReadPredictedPosition`.

#### 5. GetEndPosition

GetEndPosition lit X/Y/Z/direction du dernier Mobile.Step déjà en file. Si la file est vide, lit la position/direction actuelle. Lecture O(1) sans retirer de pas, déplacer, envoyer de paquet, calculer un trajet ou attendre l’arrivée.

X/Y sont des coordonnées du monde/carte, pas des pixels du gump de conteneur. Z est une hauteur, pas un étage. Renvoie un composant, ni tableau ni destination finale du chemin.

Source du projet: `src/ClassicUO.Client/Game/GameObjects/Mobile.cs`; fonction `GetEndPosition`.

#### 6. InjectionValue

Integer Y en cases de carte. 0 peut être une coordonnée réelle ou un joueur absent.

Prédiction locale, pas arrivée confirmée. Ajout/fin/refus de pas, vidage de file ou téléportation peuvent la changer. Les lectures séparées ne sont pas atomiques ; X égal ne prouve ni Y/Z ni accord serveur.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs`; fonction `InjectionValue`.

PredictionEquals(expected) prend une coordonnée/hauteur/direction numérique, rejette un joueur absent puis compare un composant prévu. Renvoie Integer Boolean 1=TRUE ou 0=FALSE. N’attend ni ne garantit l’arrivée.


## Exemples

### Lire un composant

```vb
# Lire un composant
#
# Lit la valeur prévue de la coordonnée Y après les pas déjà en file du joueur.
#
# Integer Y en cases de carte. 0 peut être une coordonnée réelle ou un joueur absent.

SUB Main()
    # predicted stocke un appel sans argument ; CStr formate le nombre pour le journal.

    VAR predicted = UO.PredictedY()
    UO.Print('Predicted: ' + CStr(predicted))
END SUB
```

**Explication des paramètres et du déroulement:**

- predicted stocke un appel sans argument ; CStr formate le nombre pour le journal.

### Observer une variation

```vb
# Observer une variation
#
# Lit la valeur prévue de la coordonnée Y après les pas déjà en file du joueur.
#
# Integer Y en cases de carte. 0 peut être une coordonnée réelle ou un joueur absent.

SUB Main()
    # WAIT(100) suspend cet exemple pendant 100 ms. before/after peuvent être égaux malgré un
    # mouvement intermédiaire ; ces lectures ne lancent aucun mouvement.

    VAR before = UO.PredictedY()
    WAIT(100)
    VAR after = UO.PredictedY()
    IF before <> after THEN
        UO.Print('Prediction changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- WAIT(100) suspend cet exemple pendant 100 ms. before/after peuvent être égaux malgré un mouvement intermédiaire ; ces lectures ne lancent aucun mouvement.

### Fonction de comparaison complète

```vb
# Fonction de comparaison complète
#
# Lit la valeur prévue de la coordonnée Y après les pas déjà en file du joueur.
#
# Integer Y en cases de carte. 0 peut être une coordonnée réelle ou un joueur absent.

SUB Main()
    # expected est une valeur de coordonnée/hauteur/direction de l’exemple, pas un argument natif.
    # PredictionEquals vérifie UO.Self(), lit une fois et renvoie 1=TRUE si égal, sinon 0=FALSE.
    # Définition complète sous Main. Un composant égal ne signifie pas arrivée.

    IF PredictionEquals(1690) = TRUE THEN
        UO.Print('Queued endpoint matches this component')
    ELSE
        UO.Print('Different component or no player')
    END IF
END SUB

SUB PredictionEquals(expected)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR predicted = UO.PredictedY()
    RETURN predicted = expected
END SUB
```

**Explication des paramètres et du déroulement:**

- expected est une valeur de coordonnée/hauteur/direction de l’exemple, pas un argument natif. PredictionEquals vérifie UO.Self(), lit une fois et renvoie 1=TRUE si égal, sinon 0=FALSE. Définition complète sous Main. Un composant égal ne signifie pas arrivée.
