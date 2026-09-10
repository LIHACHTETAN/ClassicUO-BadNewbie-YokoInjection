# UO.Followers

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le compteur de status du joueur actuel : emplacements de contrôle occupés.

## Syntaxe exacte

```text
UO.Followers() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — emplacements de contrôle occupés, 0..255 dans le modèle. 0 peut être réel, inconnu ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun parcours d’objets ni tableau retourné.

## Comportement

- Aucun argument. Respecter les signatures affichées.
- Lit Player.Followers sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.
- PetsCurrent/Followers lit les emplacements de contrôle occupés du status propre type >= 3. Un animal peut en occuper plusieurs ; le serveur fixe les règles des créatures invoquées/apprivoisées. Ce n’est ni un nombre de mobiles visibles, ni une liste d’ID, ni un compte d’animaux proches.
- CharacterStatus valide son corps fixe avant modification. Weight vient du status propre étendu, les emplacements du type 3, Luck du type 4 et WeightMax serveur du type 5. Un paquet compact/ancien sans compteur optionnel conserve le cache. Un nouveau Player commence à zéro ; la query ne prouve pas un status récent.
- RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture du cache. CanCarry, LuckAtLeast ou CanAddFollower est une fonction BASIC utilisateur complète dans l’exemple, pas une action native cachée. Aucun inventaire ou familier modifié.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.

`PetsCurrent Followers GetPetsCurrent GetFollowers`.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lit Player.Followers sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. CharacterStatus

CharacterStatus valide son corps fixe avant modification. Weight vient du status propre étendu, les emplacements du type 3, Luck du type 4 et WeightMax serveur du type 5. Un paquet compact/ancien sans compteur optionnel conserve le cache. Un nouveau Player commence à zéro ; la query ne prouve pas un status récent.

PetsCurrent/Followers lit les emplacements de contrôle occupés du status propre type >= 3. Un animal peut en occuper plusieurs ; le serveur fixe les règles des créatures invoquées/apprivoisées. Ce n’est ni un nombre de mobiles visibles, ni une liste d’ID, ni un compte d’animaux proches.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 4. Clear

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.

Integer — emplacements de contrôle occupés, 0..255 dans le modèle. 0 peut être réel, inconnu ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun parcours d’objets ni tableau retourné.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.


## Exemples

### Afficher le compteur en cache

```vb
# Afficher le compteur en cache
#
# Lit le compteur de status du joueur actuel : emplacements de contrôle occupés.
#
# Integer — emplacements de contrôle occupés, 0..255 dans le modèle. 0 peut être réel, inconnu
# ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas
# un succès. Aucun parcours d’objets ni tableau retourné.

SUB Main()
    # value conserve une lecture sans argument du joueur ; CStr la formate pour le journal sans
    # changer son sens.

    VAR value = UO.Followers()
    UO.Print('Followers: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value conserve une lecture sans argument du joueur ; CStr la formate pour le journal sans changer son sens.

### Observer une variation

```vb
# Observer une variation
#
# Lit le compteur de status du joueur actuel : emplacements de contrôle occupés.
#
# Integer — emplacements de contrôle occupés, 0..255 dans le modèle. 0 peut être réel, inconnu
# ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas
# un succès. Aucun parcours d’objets ni tableau retourné.

SUB Main()
    # WAIT(500) sépare before et after de 500 ms. difference peut être positive, nulle ou négative ;
    # des mises à jour ou changements de personnage peuvent échapper. L’attente appartient à
    # l’exemple.

    VAR before = UO.Followers()
    WAIT(500)
    VAR after = UO.Followers()
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
# Lit le compteur de status du joueur actuel : emplacements de contrôle occupés.
#
# Integer — emplacements de contrôle occupés, 0..255 dans le modèle. 0 peut être réel, inconnu
# ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas
# un succès. Aucun parcours d’objets ni tableau retourné.

SUB Main()
    # CanAddFollower(extraSlots) reçoit les emplacements requis ; 2 peut désigner une seule créature
    # occupant deux places. Rejette entrée négative, Player absent ou maximum <= 0, lit
    # occupation/limite puis renvoie Integer Boolean 1=TRUE ou 0=FALSE pour extraSlots <= maximum -
    # current. Pas de débordement d’addition ; dépassement donne false même pour zéro. Ni propriété,
    # compétence de dressage ni accord serveur vérifiés. Mises à jour possibles entre lectures.

    IF CanAddFollower(2) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanAddFollower(extraSlots)
    IF extraSlots < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.Followers()
    VAR maximum = UO.PetsMax()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extraSlots <= maximum - current
END SUB
```

**Explication des paramètres et du déroulement:**

- CanAddFollower(extraSlots) reçoit les emplacements requis ; 2 peut désigner une seule créature occupant deux places. Rejette entrée négative, Player absent ou maximum <= 0, lit occupation/limite puis renvoie Integer Boolean 1=TRUE ou 0=FALSE pour extraSlots <= maximum - current. Pas de débordement d’addition ; dépassement donne false même pour zéro. Ni propriété, compétence de dressage ni accord serveur vérifiés. Mises à jour possibles entre lectures.
