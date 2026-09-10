# UO.HP

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit les points de vie actuels dans le modèle local.

## Syntaxe exacte

```text
UO.HP() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — valeur du champ Hits, pas un pourcentage ni un Boolean. Zéro peut être une valeur réelle ou une donnée absente. Ne divisez jamais par un maximum nul. Les valeurs des autres mobiles peuvent être inconnues. HP/HitsMax peuvent représenter une échelle relative du serveur au lieu de points exacts. HP=0 ne prouve pas la mort ; utilisez Dead/IsDead.

## Comportement

- N’ouvre pas status et ne demande pas de mise à jour au serveur. Contrairement à la demande automatique de HP manquants dans Stealth, ce client lit seulement les données existantes. Aucun changement de caractéristiques ni envoi de paquet.
- Chaque résultat est une lecture distincte. Le monde peut changer entre Exists et l’appel suivant ; plusieurs lectures ne forment pas un instantané atomique.
- Pour un objet, World.Get rejette les entrées absentes ou IsDestroyed et produit 0. HP/HitsMax lisent Entity, y compris les objets possédant ces champs ; Mana/Stamina exigent Mobile. Sans argument, lit self. Un nom sans argument n’a pas forcément de forme avec ID : vérifiez les signatures.
- Les lectures sans argument renvoient aussi 0 si Player est absent ou détruit, y compris les accès directs Mana/Stamina et leurs maximums, pas seulement via World.Get. Un personnage mort encore présent peut conserver des valeurs.

### Fonctions internes : de l’appel au résultat

Voici les véritables étapes internes C#. ReadValue est une fonction auxiliaire entièrement définie dans l’exemple, pas une commande intégrée cachée.

#### 1. RegisterCharacterGetterAliases

À la création du runtime, RegisterCharacterGetterAliases enregistre les noms et les formes. Sans argument, utilise bridge.Self ; avec un argument, son serial. Les enregistrements existants sont conservés.

Integer — valeur du champ Hits, pas un pourcentage ni un Boolean. Zéro peut être une valeur réelle ou une donnée absente. Ne divisez jamais par un maximum nul. Les valeurs des autres mobiles peuvent être inconnues. HP/HitsMax peuvent représenter une échelle relative du serveur au lieu de points exacts. HP=0 ne prouve pas la mort ; utilisez Dead/IsDead.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. Invoke

Invoke lit dans le thread du jeu ; un thread de travail attend le traitement par le gestionnaire. L’annulation du script interrompt cette attente. Aucun délai ni appel réseau supplémentaire.

Chaque résultat est une lecture distincte. Le monde peut changer entre Exists et l’appel suivant ; plusieurs lectures ne forment pas un instantané atomique.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. Get

Pour un objet, World.Get rejette les entrées absentes ou IsDestroyed et produit 0. HP/HitsMax lisent Entity, y compris les objets possédant ces champs ; Mana/Stamina exigent Mobile. Sans argument, lit self. Un nom sans argument n’a pas forcément de forme avec ID : vérifiez les signatures.

Integer — valeur du champ Hits, pas un pourcentage ni un Boolean. Zéro peut être une valeur réelle ou une donnée absente. Ne divisez jamais par un maximum nul. Les valeurs des autres mobiles peuvent être inconnues. HP/HitsMax peuvent représenter une échelle relative du serveur au lieu de points exacts. HP=0 ne prouve pas la mort ; utilisez Dead/IsDead.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Get`.

N’ouvre pas status et ne demande pas de mise à jour au serveur. Contrairement à la demande automatique de HP manquants dans Stealth, ce client lit seulement les données existantes. Aucun changement de caractéristiques ni envoi de paquet.


## Exemples

### Afficher la valeur du personnage

```vb
# Afficher la valeur du personnage
#
# Lit les points de vie actuels dans le modèle local.
#
# Integer — valeur du champ Hits, pas un pourcentage ni un Boolean. Zéro peut être une valeur
# réelle ou une donnée absente. Ne divisez jamais par un maximum nul. Les valeurs des autres
# mobiles peuvent être inconnues. HP/HitsMax peuvent représenter une échelle relative du serveur
# au lieu de points exacts. HP=0 ne prouve pas la mort ; utilisez Dead/IsDead.

SUB Main()
    # L’appel sans argument lit self. value conserve un nombre ; STR le convertit uniquement pour le
    # message.

    VAR value = UO.HP()
    UO.Print('HP: ' + STR(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- L’appel sans argument lit self. value conserve un nombre ; STR le convertit uniquement pour le message.

### Utiliser la valeur dans une condition ou un calcul

```vb
# Utiliser la valeur dans une condition ou un calcul
#
# Lit les points de vie actuels dans le modèle local.
#
# Integer — valeur du champ Hits, pas un pourcentage ni un Boolean. Zéro peut être une valeur
# réelle ou une donnée absente. Ne divisez jamais par un maximum nul. Les valeurs des autres
# mobiles peuvent être inconnues. HP/HitsMax peuvent représenter une échelle relative du serveur
# au lieu de points exacts. HP=0 ne prouve pas la mort ; utilisez Dead/IsDead.

SUB Main()
    # L’exemple applique un seuil ou un calcul propre à ce champ. Les nombres sont des réglages
    # d’exemple, pas des limites du serveur. Le maximum est vérifié positif avant toute division.

    VAR value = UO.HP()
    VAR maximum = UO.GetMaxHP()
    IF maximum > 0 AND value * 100 / maximum < 50 THEN
        UO.Print('Health below half of the known maximum')
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- L’exemple applique un seuil ou un calcul propre à ce champ. Les nombres sont des réglages d’exemple, pas des limites du serveur. Le maximum est vérifié positif avant toute division.

### Fonction ReadValue complète

```vb
# Fonction ReadValue complète
#
# Lit les points de vie actuels dans le modèle local.
#
# Integer — valeur du champ Hits, pas un pourcentage ni un Boolean. Zéro peut être une valeur
# réelle ou une donnée absente. Ne divisez jamais par un maximum nul. Les valeurs des autres
# mobiles peuvent être inconnues. HP/HitsMax peuvent représenter une échelle relative du serveur
# au lieu de points exacts. HP=0 ne prouve pas la mort ; utilisez Dead/IsDead.

SUB Main()
    # Ce nom n’a pas de forme avec ID. ReadValue sans paramètre lit self ; WAIT(1000) sépare deux
    # appels. La comparaison des instantanés peut manquer des changements intermédiaires.

    VAR before = ReadValue()
    WAIT(1000)
    VAR after = ReadValue()
    UO.Print('Before: ' + CStr(before) + '; after: ' + CStr(after))
END SUB

SUB ReadValue()
    RETURN UO.HP()
END SUB
```

**Explication des paramètres et du déroulement:**

- Ce nom n’a pas de forme avec ID. ReadValue sans paramètre lit self ; WAIT(1000) sépare deux appels. La comparaison des instantanés peut manquer des changements intermédiaires.
