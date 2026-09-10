# UO.GetLuck

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le compteur de status du joueur actuel : points de chance.

## Syntaxe exacte

```text
UO.GetLuck() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — points de chance, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun parcours d’objets ni tableau retourné.

## Comportement

- Aucun argument. Respecter les signatures affichées.
- Lit Player.Luck sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.
- Luck lit les points de chance du serveur, stockés en UInt16 à partir du status type 4. Ni pourcentage, nombre aléatoire ni garantie de butin. Aucun calcul de probabilité ou ajout de bonus d’équipement pendant la lecture.
- CharacterStatus valide son corps fixe avant modification. Weight vient du status propre étendu, les emplacements du type 3, Luck du type 4 et WeightMax serveur du type 5. Un paquet compact/ancien sans compteur optionnel conserve le cache. Un nouveau Player commence à zéro ; la query ne prouve pas un status récent.
- RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture du cache. CanCarry, LuckAtLeast ou CanAddFollower est une fonction BASIC utilisateur complète dans l’exemple, pas une action native cachée. Aucun inventaire ou familier modifié.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.

`Luck GetLuck`.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lit Player.Luck sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. CharacterStatus

CharacterStatus valide son corps fixe avant modification. Weight vient du status propre étendu, les emplacements du type 3, Luck du type 4 et WeightMax serveur du type 5. Un paquet compact/ancien sans compteur optionnel conserve le cache. Un nouveau Player commence à zéro ; la query ne prouve pas un status récent.

Luck lit les points de chance du serveur, stockés en UInt16 à partir du status type 4. Ni pourcentage, nombre aléatoire ni garantie de butin. Aucun calcul de probabilité ou ajout de bonus d’équipement pendant la lecture.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 4. Clear

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.

Integer — points de chance, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun parcours d’objets ni tableau retourné.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.


## Exemples

### Afficher le compteur en cache

```vb
# Afficher le compteur en cache
#
# Lit le compteur de status du joueur actuel : points de chance.
#
# Integer — points de chance, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à Player
# absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun
# parcours d’objets ni tableau retourné.

SUB Main()
    # value conserve une lecture sans argument du joueur ; CStr la formate pour le journal sans
    # changer son sens.

    VAR value = UO.GetLuck()
    UO.Print('Luck: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value conserve une lecture sans argument du joueur ; CStr la formate pour le journal sans changer son sens.

### Observer une variation

```vb
# Observer une variation
#
# Lit le compteur de status du joueur actuel : points de chance.
#
# Integer — points de chance, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à Player
# absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun
# parcours d’objets ni tableau retourné.

SUB Main()
    # WAIT(500) sépare before et after de 500 ms. difference peut être positive, nulle ou négative ;
    # des mises à jour ou changements de personnage peuvent échapper. L’attente appartient à
    # l’exemple.

    VAR before = UO.GetLuck()
    WAIT(500)
    VAR after = UO.GetLuck()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**Explication des paramètres et du déroulement:**

- WAIT(500) sépare before et after de 500 ms. difference peut être positive, nulle ou négative ; des mises à jour ou changements de personnage peuvent échapper. L’attente appartient à l’exemple.

### Fonction de décision complète

```vb
# Fonction de décision complète
#
# Lit le compteur de status du joueur actuel : points de chance.
#
# Integer — points de chance, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à Player
# absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun
# parcours d’objets ni tableau retourné.

SUB Main()
    # LuckAtLeast(minimum) reçoit un seuil numérique ; 1000 est un exemple, ni plafond ni
    # pourcentage. Rejette Player absent, lit une fois puis renvoie Integer Boolean 1=TRUE ou
    # 0=FALSE pour value >= minimum. La chance elle-même n’est pas Boolean. Comparaison du cache,
    # aucune prédiction de butin.

    IF LuckAtLeast(1000) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB LuckAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetLuck()
    RETURN value >= minimum
END SUB
```

**Explication des paramètres et du déroulement:**

- LuckAtLeast(minimum) reçoit un seuil numérique ; 1000 est un exemple, ni plafond ni pourcentage. Rejette Player absent, lit une fois puis renvoie Integer Boolean 1=TRUE ou 0=FALSE pour value >= minimum. La chance elle-même n’est pas Boolean. Comparaison du cache, aucune prédiction de butin.
