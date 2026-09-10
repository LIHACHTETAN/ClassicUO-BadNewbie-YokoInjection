# UO.LastStatusX

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Renvoie la coordonnée X mémorisée du dernier objet de statut accepté.

## Syntaxe exacte

```text
UO.LastStatusX() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — coordonnée X mémorisée, pas un pixel de fenêtre ni un booléen. 0 avant le premier statut ou après réinitialisation ; zéro est aussi une coordonnée valide. Vérifier UO.LastStatus() pour distinguer une absence.

## Comportement

- Aucun paramètre. La lecture ne transmet rien, n’ouvre aucune fenêtre et n’attend aucune réponse. UO.GetStatus(id), RequestStats et UpdateObject demandent des données ; leur envoi ne modifie pas LastStatus.
- Un paquet 0x11 accepté mémorise ensemble serial et X/Y connus dans World, partagé par les scripts. Un objet inconnu/détruit ou un paquet de base incomplet ne remplace rien. Un statut ultérieur d’un autre objet peut remplacer ces données.
- X/Y sont ceux de Entity à la réception, pas sa position actuelle. Pour un mobile ce sont des cases du monde ; dans un conteneur, un objet peut avoir des coordonnées de contenu. Le paquet de statut ne contient pas X/Y. Déplacement et suppression ultérieurs ne changent pas les valeurs ; World.Clear les efface. GetX/GetY lisent la position actuelle d’un objet présent.
- Les appels séparés ne sont pas atomiques : une mise à jour peut intervenir entre eux. Un serial identique ne prouve pas une réponse récente à votre demande. laststatus sans parenthèses est une valeur intrinsèque dynamique, sauf masquage par une variable ; UO.LastStatus() est la fonction enregistrée.

### Fonctions internes : de l’appel au résultat

Voici les véritables étapes internes C#. ReadSavedStatus est une fonction auxiliaire entièrement définie dans l’exemple, pas une commande intégrée cachée.

#### 1. CharacterStatus

CharacterStatus valide le paquet de base et Entity via World.Get, actualise le statut et conserve serial/X/Y. La position provient de Entity, pas du paquet.

Integer — coordonnée X mémorisée, pas un pixel de fenêtre ni un booléen. 0 avant le premier statut ou après réinitialisation ; zéro est aussi une coordonnée valide. Vérifier UO.LastStatus() pour distinguer une absence.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 2. LastStatusX

ExecuteStealthCompatibility renvoie le serial du bridge comme Integer. LastStatusX/LastStatusY utilisent IStatusSnapshotBridge ; un ancien bridge externe sans cette interface conserve la lecture GetX/GetY.

Integer — coordonnée X mémorisée, pas un pixel de fenêtre ni un booléen. 0 avant le premier statut ou après réinitialisation ; zéro est aussi une coordonnée valide. Vérifier UO.LastStatus() pour distinguer une absence.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `LastStatusX`.

#### 3. Invoke

Invoke lit World sur le fil du jeu avec prise en charge de l’annulation. Il n’attend pas le réseau et ne modifie pas le statut.

Aucun paramètre. La lecture ne transmet rien, n’ouvre aucune fenêtre et n’attend aucune réponse. UO.GetStatus(id), RequestStats et UpdateObject demandent des données ; leur envoi ne modifie pas LastStatus.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 4. Clear

Clear remet le serial et les deux coordonnées à 0, même lorsque les scripts en cours sont préservés.

X/Y sont ceux de Entity à la réception, pas sa position actuelle. Pour un mobile ce sont des cases du monde ; dans un conteneur, un objet peut avoir des coordonnées de contenu. Le paquet de statut ne contient pas X/Y. Déplacement et suppression ultérieurs ne changent pas les valeurs ; World.Clear les efface. GetX/GetY lisent la position actuelle d’un objet présent.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

Les appels séparés ne sont pas atomiques : une mise à jour peut intervenir entre eux. Un serial identique ne prouve pas une réponse récente à votre demande. laststatus sans parenthèses est une valeur intrinsèque dynamique, sauf masquage par une variable ; UO.LastStatus() est la fonction enregistrée.


## Exemples

### Lire la dernière valeur

```vb
# Lire la dernière valeur
#
# Renvoie la coordonnée X mémorisée du dernier objet de statut accepté.
#
# Integer — coordonnée X mémorisée, pas un pixel de fenêtre ni un booléen. 0 avant le premier
# statut ou après réinitialisation ; zéro est aussi une coordonnée valide. Vérifier
# UO.LastStatus() pour distinguer une absence.

SUB Main()
    # Lecture unique. HEX affiche un serial en hexadécimal ; CStr affiche une coordonnée numérique.
    # Aucun objet n’est sélectionné.

    VAR value = UO.LastStatusX()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- Lecture unique. HEX affiche un serial en hexadécimal ; CStr affiche une coordonnée numérique. Aucun objet n’est sélectionné.

### Demander le statut et lire les données connues

```vb
# Demander le statut et lire les données connues
#
# Renvoie la coordonnée X mémorisée du dernier objet de statut accepté.
#
# Integer — coordonnée X mémorisée, pas un pixel de fenêtre ni un booléen. 0 avant le premier
# statut ou après réinitialisation ; zéro est aussi une coordonnée valide. Vérifier
# UO.LastStatus() pour distinguer une absence.

SUB Main()
    # subject est le serial de self. 500 est une attente d’exemple en millisecondes, sans garantie
    # de réponse. Les données affichées peuvent être anciennes ou concerner un autre objet.

    VAR subject = UO.Self()
    IF subject <> 0 THEN
        UO.GetStatus(subject)
        WAIT(500)
        VAR value = UO.LastStatusX()
        UO.Print('Known value: ' + CStr(value))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- subject est le serial de self. 500 est une attente d’exemple en millisecondes, sans garantie de réponse. Les données affichées peuvent être anciennes ou concerner un autre objet.

### Fonction ReadSavedStatus complète

```vb
# Fonction ReadSavedStatus complète
#
# Renvoie la coordonnée X mémorisée du dernier objet de statut accepté.
#
# Integer — coordonnée X mémorisée, pas un pixel de fenêtre ni un booléen. 0 avant le premier
# statut ou après réinitialisation ; zéro est aussi une coordonnée valide. Vérifier
# UO.LastStatus() pour distinguer une absence.

SUB Main()
    # expectedId est le serial mémorisé dans Main. La fonction est entièrement définie ci-dessous ;
    # -1 signifie que l’enregistrement sélectionné a changé, pas un résultat propre à la commande.
    # Les vérifications avant/après limitent le mélange d’objets sans garantir l’atomicité pour un
    # même serial.

    VAR expectedId = UO.LastStatus()
    IF expectedId <> 0 THEN
        VAR value = ReadSavedStatus(expectedId)
        UO.Print('Checked value: ' + CStr(value))
    END IF
END SUB

SUB ReadSavedStatus(expectedId)
    IF expectedId = 0 OR UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    VAR value = UO.LastStatusX()
    IF UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Explication des paramètres et du déroulement:**

- expectedId est le serial mémorisé dans Main. La fonction est entièrement définie ci-dessous ; -1 signifie que l’enregistrement sélectionné a changé, pas un résultat propre à la commande. Les vérifications avant/après limitent le mélange d’objets sans garantir l’atomicité pour un même serial.
