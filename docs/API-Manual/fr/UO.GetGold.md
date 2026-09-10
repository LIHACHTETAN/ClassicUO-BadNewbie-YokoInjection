# UO.GetGold

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit la quantité d’or indiquée dans le status du joueur actuel.

## Syntaxe exacte

```text
UO.GetGold() -> Any
```

## Paramètres

Aucun paramètre.

## Retour

Integer/Decimal — montant positif ou nul, 0..4294967295. Jusqu’à 2147483647 : Integer ; au-delà : Decimal (Double), qui représente exactement tous les entiers UInt32. 0 peut aussi signifier Player absent/détruit ou montant inconnu. Ce n’est ni Boolean, ID, nombre de piles ni inventaire du sac ou de la banque.

## Comportement

- Aucun argument. Lit Player.Gold mis en cache par CharacterStatus (0x11). Le serveur décide de l’or inclus dans ce compteur. Aucun parcours des sacs ni demande du solde bancaire. Player absent/détruit donne 0 ; un fantôme présent peut garder son montant.
- ReadGoldValue lit bridge.Gold une fois. Le bridge C# conserve sa signature Int32 et transporte les bits UInt32. La conversion unchecked restaure le montant non signé : petit montant en Integer, grand en Decimal. Le bit haut ne rend plus le solde négatif. Conversion locale, sans paquet.
- Conserver le résultat numérique pour comparer de grands montants. CInt/CLng convertissent vers un Integer 32 bits. Écrire un grand littéral BASIC avec un point, par exemple 3000000000.0. Le solde peut changer avant l’achat ; CanAfford est un contrôle local, pas une autorisation serveur.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture du compteur et d’élargissement de sa plage non signée. CanAfford est la fonction BASIC utilisateur complète ci-dessous, pas une commande d’achat cachée.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ajoute les fonctions et intrinsèques Gold/GetGold manquants. La branche UO.Gold et son intrinsèque utilisent le même ReadGoldValue. Les noms intrinsèques sont relus sauf si une variable les masque.

Integer/Decimal — montant positif ou nul, 0..4294967295. Jusqu’à 2147483647 : Integer ; au-delà : Decimal (Double), qui représente exactement tous les entiers UInt32. 0 peut aussi signifier Player absent/détruit ou montant inconnu. Ce n’est ni Boolean, ID, nombre de piles ni inventaire du sac ou de la banque.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. ReadGoldValue

ReadGoldValue lit bridge.Gold une fois. Le bridge C# conserve sa signature Int32 et transporte les bits UInt32. La conversion unchecked restaure le montant non signé : petit montant en Integer, grand en Decimal. Le bit haut ne rend plus le solde négatif. Conversion locale, sans paquet.

Conserver le résultat numérique pour comparer de grands montants. CInt/CLng convertissent vers un Integer 32 bits. Écrire un grand littéral BASIC avec un point, par exemple 3000000000.0. Le solde peut changer avant l’achat ; CanAfford est un contrôle local, pas une autorisation serveur.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ReadGoldValue`.

#### 3. Invoke

Aucun argument. Lit Player.Gold mis en cache par CharacterStatus (0x11). Le serveur décide de l’or inclus dans ce compteur. Aucun parcours des sacs ni demande du solde bancaire. Player absent/détruit donne 0 ; un fantôme présent peut garder son montant.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 4. CharacterStatus

Aucun argument. Lit Player.Gold mis en cache par CharacterStatus (0x11). Le serveur décide de l’or inclus dans ce compteur. Aucun parcours des sacs ni demande du solde bancaire. Player absent/détruit donne 0 ; un fantôme présent peut garder son montant.

Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 5. Clear

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.

Integer/Decimal — montant positif ou nul, 0..4294967295. Jusqu’à 2147483647 : Integer ; au-delà : Decimal (Double), qui représente exactement tous les entiers UInt32. 0 peut aussi signifier Player absent/détruit ou montant inconnu. Ce n’est ni Boolean, ID, nombre de piles ni inventaire du sac ou de la banque.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.


## Exemples

### Afficher le montant reçu

```vb
# Afficher le montant reçu
#
# Lit la quantité d’or indiquée dans le status du joueur actuel.
#
# Integer/Decimal — montant positif ou nul, 0..4294967295. Jusqu’à 2147483647 : Integer ;
# au-delà : Decimal (Double), qui représente exactement tous les entiers UInt32. 0 peut aussi
# signifier Player absent/détruit ou montant inconnu. Ce n’est ni Boolean, ID, nombre de piles
# ni inventaire du sac ou de la banque.

SUB Main()
    # amount conserve un appel ; CStr le formate pour le journal. Aucun or n’est recherché, déplacé
    # ou dépensé.

    VAR amount = UO.GetGold()
    UO.Print('Status gold: ' + CStr(amount))
END SUB
```

**Explication des paramètres et du déroulement:**

- amount conserve un appel ; CStr le formate pour le journal. Aucun or n’est recherché, déplacé ou dépensé.

### Fonction CanAfford complète avec grand prix

```vb
# Fonction CanAfford complète avec grand prix
#
# Lit la quantité d’or indiquée dans le status du joueur actuel.
#
# Integer/Decimal — montant positif ou nul, 0..4294967295. Jusqu’à 2147483647 : Integer ;
# au-delà : Decimal (Double), qui représente exactement tous les entiers UInt32. 0 peut aussi
# signifier Player absent/détruit ou montant inconnu. Ce n’est ni Boolean, ID, nombre de piles
# ni inventaire du sac ou de la banque.

SUB Main()
    # price=3000000000.0 est un prix d’exemple. CanAfford(price) rejette un prix négatif ou Player
    # absent, lit une fois puis renvoie Integer Boolean 1=TRUE ou 0=FALSE pour amount >= price. Le
    # montant lui-même n’est pas Boolean. Définition complète ci-dessous.

    VAR price = 3000000000.0
    IF CanAfford(price) = TRUE THEN
        UO.Print('Local balance is sufficient')
    ELSE
        UO.Print('Local check failed')
    END IF
END SUB

SUB CanAfford(price)
    IF price < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR amount = UO.GetGold()
    RETURN amount >= price
END SUB
```

**Explication des paramètres et du déroulement:**

- price=3000000000.0 est un prix d’exemple. CanAfford(price) rejette un prix négatif ou Player absent, lit une fois puis renvoie Integer Boolean 1=TRUE ou 0=FALSE pour amount >= price. Le montant lui-même n’est pas Boolean. Définition complète ci-dessous.

### Observer une variation du solde

```vb
# Observer une variation du solde
#
# Lit la quantité d’or indiquée dans le status du joueur actuel.
#
# Integer/Decimal — montant positif ou nul, 0..4294967295. Jusqu’à 2147483647 : Integer ;
# au-delà : Decimal (Double), qui représente exactement tous les entiers UInt32. 0 peut aussi
# signifier Player absent/détruit ou montant inconnu. Ce n’est ni Boolean, ID, nombre de piles
# ni inventaire du sac ou de la banque.

SUB Main()
    # before/after sont séparés par WAIT(500) millisecondes. difference=after-before peut être
    # négatif si le solde diminue ; ce n’est pas le débordement non signé corrigé. Des mises à jour
    # ou changements de personnage intermédiaires peuvent échapper à la comparaison.

    VAR before = UO.GetGold()
    WAIT(500)
    VAR after = UO.GetGold()
    VAR difference = after - before
    UO.Print('Balance change: ' + CStr(difference))
END SUB
```

**Explication des paramètres et du déroulement:**

- before/after sont séparés par WAIT(500) millisecondes. difference=after-before peut être négatif si le solde diminue ; ce n’est pas le débordement non signé corrigé. Des mises à jour ou changements de personnage intermédiaires peuvent échapper à la comparaison.
